# FastAPI Database Integration

> Covers SQLAlchemy 2.x async patterns, repository pattern, session management, scalar/scalars, query methods, migrations, and production-grade architecture.

---

## Table of Contents

1. [Stack Overview](#1-stack-overview)
2. [Engine & Session Setup](#2-engine--session-setup)
3. [Models & Base Declaration](#3-models--base-declaration)
4. [Session Dependency Injection](#4-session-dependency-injection)
5. [`scalar` vs `scalars` — Deep Dive](#5-scalar-vs-scalars--deep-dive)
6. [Core Query Methods](#6-core-query-methods)
7. [Repository Pattern](#7-repository-pattern)
8. [Generic Base Repository](#8-generic-base-repository)
9. [Unit of Work Pattern](#9-unit-of-work-pattern)
10. [Relationships & Eager Loading](#10-relationships--eager-loading)
11. [Transactions & Savepoints](#11-transactions--savepoints)
12. [Migrations with Alembic](#12-migrations-with-alembic)
13. [Connection Pooling](#13-connection-pooling)
14. [Testing with Database](#14-testing-with-database)
15. [Common Pitfalls](#15-common-pitfalls)

---

## 1. Stack Overview

```
FastAPI  →  SQLAlchemy 2.x (async)  →  asyncpg (driver)  →  PostgreSQL
                    ↓
             Alembic (migrations)
```

Key libraries:

```txt
fastapi
sqlalchemy[asyncio]>=2.0
asyncpg           # async postgres driver
alembic
pydantic>=2.0
```

SQLAlchemy 2.x introduced a **unified API** — the old `Query` object is gone. Everything is now `select()`, `insert()`, `update()`, `delete()` statements executed via `session.execute()`.

---

## 2. Engine & Session Setup

```python
# app/database.py
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

DATABASE_URL = "postgresql+asyncpg://user:pass@localhost:5432/mydb"

engine: AsyncEngine = create_async_engine(
    DATABASE_URL,
    echo=False,          # set True in dev to log SQL
    pool_size=10,        # persistent connections kept open
    max_overflow=20,     # extra connections allowed beyond pool_size
    pool_pre_ping=True,  # test connection health before using from pool
    pool_recycle=3600,   # recycle connections older than 1 hour
)

# async_sessionmaker is the 2.x replacement for sessionmaker
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,  # IMPORTANT: prevents lazy-load errors after commit
    autocommit=False,
    autoflush=False,
)
```

**Why `expire_on_commit=False`?**
By default SQLAlchemy expires all attributes after `commit()`. In async code, accessing an expired attribute triggers a lazy load — which is not supported in async. Setting this to `False` keeps attribute values in memory post-commit.

---

## 3. Models & Base Declaration

```python
# app/models/base.py
from sqlalchemy import DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import uuid

class Base(DeclarativeBase):
    pass


# app/models/user.py
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base
import uuid

class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=uuid.uuid4
    )
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(100))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # Relationship
    posts: Mapped[list["Post"]] = relationship(
        back_populates="author", lazy="selectin"
    )
```

**`Mapped[T]`** — SQLAlchemy 2.x typed annotation. Replaces `Column(...)`. The type hint IS the column type definition. Much cleaner than 1.x.

---

## 4. Session Dependency Injection

```python
# app/dependencies.py
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import AsyncSessionLocal

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise

# In router:
from fastapi import Depends

@router.get("/users/{user_id}")
async def get_user(
    user_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
):
    ...
```

The `async with AsyncSessionLocal() as session` block handles `session.close()` automatically. Commit/rollback is managed in the dependency, so your service layer doesn't need to.

---

## 5. `scalar` vs `scalars` — Deep Dive

This is one of the most misunderstood parts of SQLAlchemy 2.x.

### The result chain

```
session.execute(stmt)  →  CursorResult  →  .scalars()  →  ScalarResult  →  .all() / .first() / .one()
                                        →  .scalar()   →  single value or None
                                        →  .scalar_one() → single value or raises
```

### `session.execute()` returns rows

When you `SELECT` a model, `execute()` returns `Row` objects — tuples wrapped in a special class. You need to unwrap them.

```python
result = await session.execute(select(User).where(User.id == user_id))
# result is CursorResult
# result.all()  →  [(User(...),), (User(...),)]  ← tuples!
# result.fetchone()  →  (User(...),)             ← still a tuple
```

### `.scalars()` — unwrap the first column

`.scalars()` returns a `ScalarResult` that extracts the first element from each row tuple.

```python
result = await session.execute(select(User))
users = result.scalars().all()
# users → [User(...), User(...)]  ← clean model instances
```

### `.scalar()` — get exactly one value or None

Combines `.scalars().first()`. Returns the first column of the first row, or `None`.

```python
result = await session.execute(
    select(User).where(User.email == email)
)
user = result.scalar()
# user → User(...) or None
```

Use for: lookups where you expect 0 or 1 results.

### `.scalar_one()` — get exactly one or raise

```python
user = result.scalar_one()
# Raises NoResultFound if 0 rows
# Raises MultipleResultsFound if >1 rows
```

Use for: cases where the data MUST exist (e.g., fetching by primary key after INSERT).

### `.scalar_one_or_none()`

```python
user = result.scalar_one_or_none()
# Returns None if 0 rows
# Raises MultipleResultsFound if >1 rows
```

### Shorthand methods on session

SQLAlchemy 2.x also has session-level shortcuts:

```python
# Equivalent to session.execute(stmt).scalar_one_or_none()
user = await session.scalar(select(User).where(User.id == id))

# Equivalent to session.execute(stmt).scalars()
users = await session.scalars(select(User))
users_list = users.all()
```

### Summary table

| Method | Returns | Raises if >1 | Use when |
|---|---|---|---|
| `.scalar()` | first value or `None` | No (silently ignores) | Optional single result |
| `.scalar_one()` | first value | Yes | Must exist, must be unique |
| `.scalar_one_or_none()` | value or `None` | Yes | Optional but must be unique |
| `.scalars().all()` | `list[Model]` | No | Fetch multiple records |
| `.scalars().first()` | first or `None` | No | Top result only |

---

## 6. Core Query Methods

### SELECT

```python
from sqlalchemy import select, and_, or_, desc, asc, func

# All users
stmt = select(User)
result = await session.execute(stmt)
users = result.scalars().all()

# With WHERE
stmt = select(User).where(User.is_active == True)

# Multiple conditions
stmt = select(User).where(
    and_(User.is_active == True, User.name.ilike("%john%"))
)

# OR condition
stmt = select(User).where(
    or_(User.email == "a@b.com", User.email == "c@d.com")
)

# ORDER, LIMIT, OFFSET (pagination)
stmt = (
    select(User)
    .where(User.is_active == True)
    .order_by(desc(User.created_at))
    .limit(10)
    .offset(20)
)

# Specific columns (returns Row tuples, not models)
stmt = select(User.id, User.email)
result = await session.execute(stmt)
rows = result.all()  # [(uuid, "a@b.com"), ...]
```

### INSERT

```python
# Method 1: ORM style (preferred for single records)
user = User(email="test@example.com", name="Test")
session.add(user)
await session.flush()  # sends SQL, gets auto-generated ID back
# session.commit() happens in dependency

# Method 2: Bulk insert (fast, bypasses ORM events)
from sqlalchemy import insert

stmt = insert(User).values([
    {"email": "a@example.com", "name": "A"},
    {"email": "b@example.com", "name": "B"},
])
await session.execute(stmt)

# Method 3: Insert and return
stmt = (
    insert(User)
    .values(email="c@example.com", name="C")
    .returning(User)
)
result = await session.execute(stmt)
new_user = result.scalar_one()
```

### UPDATE

```python
from sqlalchemy import update

# ORM style (fetches record first)
user = await session.get(User, user_id)
user.name = "New Name"
# flush/commit will detect the change (dirty tracking)

# Core style (single SQL UPDATE, no fetch)
stmt = (
    update(User)
    .where(User.id == user_id)
    .values(name="New Name", is_active=False)
    .returning(User)
)
result = await session.execute(stmt)
updated_user = result.scalar_one_or_none()
```

### DELETE

```python
from sqlalchemy import delete

# ORM style
user = await session.get(User, user_id)
await session.delete(user)

# Core style (no fetch required)
stmt = delete(User).where(User.id == user_id)
await session.execute(stmt)
```

### COUNT & Aggregates

```python
from sqlalchemy import func, select

# Count
stmt = select(func.count()).select_from(User).where(User.is_active == True)
count = await session.scalar(stmt)

# Group by with count
stmt = (
    select(User.is_active, func.count(User.id).label("total"))
    .group_by(User.is_active)
)
result = await session.execute(stmt)
rows = result.all()
# [Row(is_active=True, total=42), Row(is_active=False, total=7)]
```

### `session.get()` — fetch by PK

```python
# Fastest way to fetch by primary key
# Checks identity map (cache) first, only hits DB if not found
user = await session.get(User, user_id)
# Returns None if not found
```

---

## 7. Repository Pattern

The repository pattern abstracts database access behind a clean interface. Your route handlers and services call methods like `user_repo.get_by_email(email)` — they never write raw SQL.

**Why it matters at senior level:**

- Decouples business logic from persistence layer
- Makes unit testing trivial (mock the repo, not the DB)
- Centralizes query logic — one place to optimize
- Easy to swap ORMs or add caching later

### Without Repository (anti-pattern)

```python
# router.py — DON'T do this
@router.get("/users/{id}")
async def get_user(id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.id == id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(404)
    return user
```

Your routes now know about SQLAlchemy internals. Changing the ORM means touching every router.

### With Repository (correct pattern)

```python
# app/repositories/user_repository.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User
import uuid

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, user_id: uuid.UUID) -> User | None:
        return await self.session.get(User, user_id)

    async def get_by_email(self, email: str) -> User | None:
        result = await self.session.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()

    async def get_all_active(self, limit: int = 100, offset: int = 0) -> list[User]:
        result = await self.session.execute(
            select(User)
            .where(User.is_active == True)
            .order_by(User.created_at.desc())
            .limit(limit)
            .offset(offset)
        )
        return result.scalars().all()

    async def create(self, email: str, name: str) -> User:
        user = User(email=email, name=name)
        self.session.add(user)
        await self.session.flush()
        return user

    async def update(self, user: User, **kwargs) -> User:
        for key, value in kwargs.items():
            setattr(user, key, value)
        await self.session.flush()
        return user

    async def delete(self, user: User) -> None:
        await self.session.delete(user)
        await self.session.flush()

    async def exists_by_email(self, email: str) -> bool:
        result = await self.session.execute(
            select(func.count()).select_from(User).where(User.email == email)
        )
        return result.scalar() > 0
```

### Wiring repo into routes via Depends

```python
# app/dependencies.py
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repository import UserRepository

def get_user_repo(db: AsyncSession = Depends(get_db)) -> UserRepository:
    return UserRepository(db)

# router.py
@router.get("/users/{user_id}")
async def get_user(
    user_id: uuid.UUID,
    repo: UserRepository = Depends(get_user_repo),
):
    user = await repo.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```

---

## 8. Generic Base Repository

DRY pattern — one base class that handles common CRUD, extended per model.

```python
# app/repositories/base.py
from typing import Generic, TypeVar, Type, Any
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.base import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], session: AsyncSession):
        self.model = model
        self.session = session

    async def get(self, id: Any) -> ModelType | None:
        return await self.session.get(self.model, id)

    async def get_or_raise(self, id: Any) -> ModelType:
        obj = await self.get(id)
        if obj is None:
            raise ValueError(f"{self.model.__name__} with id={id} not found")
        return obj

    async def list(
        self,
        *filters,
        limit: int = 100,
        offset: int = 0,
        order_by=None,
    ) -> list[ModelType]:
        stmt = select(self.model)
        if filters:
            stmt = stmt.where(*filters)
        if order_by is not None:
            stmt = stmt.order_by(order_by)
        stmt = stmt.limit(limit).offset(offset)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def count(self, *filters) -> int:
        stmt = select(func.count()).select_from(self.model)
        if filters:
            stmt = stmt.where(*filters)
        return await self.session.scalar(stmt) or 0

    async def create(self, **kwargs) -> ModelType:
        obj = self.model(**kwargs)
        self.session.add(obj)
        await self.session.flush()
        await self.session.refresh(obj)
        return obj

    async def update(self, obj: ModelType, **kwargs) -> ModelType:
        for key, value in kwargs.items():
            setattr(obj, key, value)
        await self.session.flush()
        return obj

    async def delete(self, obj: ModelType) -> None:
        await self.session.delete(obj)
        await self.session.flush()

    async def bulk_create(self, items: list[dict]) -> None:
        objects = [self.model(**item) for item in items]
        self.session.add_all(objects)
        await self.session.flush()


# Extending the base
class UserRepository(BaseRepository[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(User, session)

    async def get_by_email(self, email: str) -> User | None:
        result = await self.session.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()

    async def get_active_users(self) -> list[User]:
        return await self.list(User.is_active == True)
```

---

## 9. Unit of Work Pattern

When a single business operation spans multiple repositories, you need them to share the same session (same transaction). Unit of Work encapsulates this.

```python
# app/uow.py
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repository import UserRepository
from app.repositories.post_repository import PostRepository

class UnitOfWork:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.users = UserRepository(session)
        self.posts = PostRepository(session)

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()


# Dependency
def get_uow(db: AsyncSession = Depends(get_db)) -> UnitOfWork:
    return UnitOfWork(db)


# Service using UoW
class UserService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def register_with_welcome_post(self, email: str, name: str) -> User:
        user = await self.uow.users.create(email=email, name=name)
        await self.uow.posts.create(
            author_id=user.id,
            title="Welcome!",
            content="Your first post."
        )
        # Both operations are in the same transaction
        # commit happens in dependency or explicitly here
        return user
```

---

## 10. Relationships & Eager Loading

Lazy loading doesn't work in async SQLAlchemy. You must always explicitly load relationships.

### Loading strategies

```python
from sqlalchemy.orm import selectinload, joinedload, subqueryload

# selectinload — separate SELECT IN query (best for 1:many)
stmt = select(User).options(selectinload(User.posts))
result = await session.execute(stmt)
users = result.scalars().all()
# Now user.posts is already loaded, no extra query needed

# joinedload — single JOIN query (best for many:1 / optional single related)
stmt = select(Post).options(joinedload(Post.author))
result = await session.execute(stmt)
posts = result.scalars().unique().all()  # .unique() required with joinedload

# Nested eager loading
stmt = (
    select(User)
    .options(
        selectinload(User.posts)
        .selectinload(Post.comments)
    )
)
```

### Why `.unique()` with joinedload?

JOINs duplicate the left-side rows. If a user has 3 posts, a joined query returns 3 rows for that user. `.unique()` deduplicates by identity map.

### Lazy="selectin" on model (auto-load)

```python
class User(Base):
    posts: Mapped[list["Post"]] = relationship(
        back_populates="author",
        lazy="selectin"  # always loads, no explicit .options() needed
    )
```

This is convenient but can be wasteful if you always fetch users but rarely need posts.

---

## 11. Transactions & Savepoints

### Default behavior

Every `AsyncSession` is a transaction boundary. `session.commit()` commits everything done since the last commit.

```python
async with AsyncSessionLocal() as session:
    session.add(User(email="a@b.com"))
    session.add(Post(title="Hi"))
    await session.commit()  # both written atomically
```

### Savepoints (nested transactions)

```python
async with AsyncSessionLocal() as session:
    async with session.begin():
        session.add(user)

        # Savepoint — rollback just this nested block on error
        async with session.begin_nested():
            try:
                session.add(risky_record)
                await session.flush()
            except IntegrityError:
                # Rolls back only the savepoint, outer tx survives
                await session.rollback()

        # This still commits
        session.add(safe_record)
```

### Manual transaction management (when you need full control)

```python
async with AsyncSessionLocal() as session:
    try:
        async with session.begin():
            # All your operations
            result = await session.execute(stmt)
    except Exception:
        # session.begin() rolls back automatically on __aexit__ exception
        raise
```

---

## 12. Migrations with Alembic

```bash
pip install alembic
alembic init alembic
```

### `alembic/env.py` — async setup

```python
from sqlalchemy.ext.asyncio import create_async_engine
from app.models.base import Base
from app.database import DATABASE_URL

target_metadata = Base.metadata

def run_migrations_online():
    connectable = create_async_engine(DATABASE_URL)

    async def do_run():
        async with connectable.connect() as connection:
            await connection.run_sync(do_migrations)

    asyncio.run(do_run())

def do_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()
```

### Common commands

```bash
# Auto-generate migration from model changes
alembic revision --autogenerate -m "add users table"

# Apply all pending migrations
alembic upgrade head

# Rollback one step
alembic downgrade -1

# Show current revision
alembic current

# Show migration history
alembic history
```

### Sample migration file

```python
# alembic/versions/001_add_users.py
def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("email", sa.String(255), nullable=False),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default="true"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_index("ix_users_email", "users", ["email"])

def downgrade() -> None:
    op.drop_index("ix_users_email", "users")
    op.drop_table("users")
```

---

## 13. Connection Pooling

Production pool configuration:

```python
engine = create_async_engine(
    DATABASE_URL,
    pool_size=10,          # base connections kept alive
    max_overflow=20,       # burst connections (total max = pool_size + max_overflow)
    pool_timeout=30,       # wait up to 30s for a connection before raising
    pool_recycle=3600,     # close & replace connections older than 1 hour (avoids stale)
    pool_pre_ping=True,    # "SELECT 1" before using pooled conn (detects dropped conns)
)
```

### Closing the engine on shutdown

```python
# main.py
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await engine.dispose()  # closes all pooled connections on shutdown

app = FastAPI(lifespan=lifespan)
```

### Monitoring the pool

```python
# How many connections are checked out right now
engine.pool.checkedout()
engine.pool.size()
engine.pool.overflow()
```

---

## 14. Testing with Database

### Approach: rollback after each test

```python
# tests/conftest.py
import pytest_asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.models.base import Base

TEST_DATABASE_URL = "postgresql+asyncpg://user:pass@localhost:5432/test_db"

@pytest_asyncio.fixture(scope="session")
async def engine():
    engine = create_async_engine(TEST_DATABASE_URL)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()

@pytest_asyncio.fixture
async def session(engine):
    async with engine.connect() as conn:
        await conn.begin()
        session = AsyncSession(bind=conn, expire_on_commit=False)
        yield session
        await session.close()
        await conn.rollback()  # ← rolls back ALL changes after each test

@pytest_asyncio.fixture
async def user_repo(session):
    return UserRepository(session)
```

### Test example

```python
@pytest.mark.asyncio
async def test_create_user(user_repo: UserRepository):
    user = await user_repo.create(email="test@example.com", name="Test")
    assert user.id is not None
    assert user.email == "test@example.com"

    fetched = await user_repo.get_by_email("test@example.com")
    assert fetched.id == user.id
```

---

## 15. Common Pitfalls

### 1. Lazy loading in async context

```python
# BAD — triggers lazy load which crashes in async
user = await session.get(User, user_id)
posts = user.posts  # MissingGreenlet error!

# GOOD — eagerly load relationships
result = await session.execute(
    select(User).where(User.id == user_id).options(selectinload(User.posts))
)
user = result.scalar_one_or_none()
posts = user.posts  # already loaded ✓
```

### 2. Forgetting `.unique()` with joinedload

```python
# BAD — duplicate model instances
users = result.scalars().all()

# GOOD — deduplicate after joinedload
users = result.scalars().unique().all()
```

### 3. Using `session.execute().fetchall()` instead of `.scalars().all()`

```python
# Returns Row tuples, not model instances
users = result.fetchall()  # [(User(...),), (User(...),)]

# Returns model instances
users = result.scalars().all()  # [User(...), User(...)]
```

### 4. Not flushing before accessing generated fields

```python
user = User(email="a@b.com")
session.add(user)
# user.id is None here — DB hasn't run the INSERT yet
await session.flush()
# Now user.id is populated (identity map refreshed)
print(user.id)  # uuid ✓
```

### 5. Committing inside repository methods

Repositories should only flush, never commit. Commit is the caller's responsibility (service layer or dependency).

```python
# BAD — commits inside repo, breaks UoW pattern
async def create(self, **kwargs):
    obj = self.model(**kwargs)
    self.session.add(obj)
    await self.session.commit()  # ← don't do this in repo

# GOOD — flush only
async def create(self, **kwargs):
    obj = self.model(**kwargs)
    self.session.add(obj)
    await self.session.flush()
    return obj
```

### 6. N+1 query problem

```python
# BAD — hits DB once per user to load their posts
users = result.scalars().all()
for user in users:
    print(user.posts)  # each access = new query

# GOOD — load all posts in one extra query
stmt = select(User).options(selectinload(User.posts))
```

### 7. Using strings instead of model columns in filters

```python
# BAD — typo-prone, not refactor-safe
stmt = select(User).where(text("is_active = true"))

# GOOD — type-safe, IDE-friendly
stmt = select(User).where(User.is_active == True)
```

---

## Quick Reference Cheatsheet

```python
# Single record, may not exist
user = await session.scalar(select(User).where(User.email == email))

# Single record, must exist and be unique
user = (await session.execute(stmt)).scalar_one()

# Single record, unique or None
user = (await session.execute(stmt)).scalar_one_or_none()

# Multiple records
users = (await session.execute(stmt)).scalars().all()

# Count
count = await session.scalar(select(func.count()).select_from(User))

# Fetch by PK (uses identity map cache)
user = await session.get(User, user_id)

# Bulk insert
await session.execute(insert(User), [{"email": "a"}, {"email": "b"}])

# Update returning
result = await session.execute(
    update(User).where(User.id == id).values(name="X").returning(User)
)
updated = result.scalar_one()
```
