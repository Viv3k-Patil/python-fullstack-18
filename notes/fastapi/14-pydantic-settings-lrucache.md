# Pydantic Settings, BaseSettings, and lru_cache

## Intuition First: What Problem Are We Solving?

Imagine you're building a microservice (like `user-service`). Your app needs configuration:
- App name, version, environment
- Database host, port
- API keys, secrets
- Debug mode, feature flags

Where do you store this? Hardcoding is bad. Parsing environment variables manually is error-prone. You need:
1. **Type validation** (ensure port is an int, not a string)
2. **Default values** (fallback if env var is missing)
3. **Centralized access** (one place to get all settings)
4. **Caching** (don't re-read env vars on every request)

Pydantic's `BaseSettings` + `lru_cache` solves this elegantly.

***

## 1. Pydantic Settings – Intuition

### What Is BaseSettings?

`BaseSettings` is a special Pydantic class that:
- Reads configuration from **environment variables** automatically
- Validates types automatically
- Provides default values if env vars are missing
- Lets you organize settings in a clean class

### Intuition

Think of `BaseSettings` as a **configuration reader** that maps environment variables to class attributes.

```
Environment Variables → BaseSettings → Python Object with Typed Attributes
```

***

## 2. Building Settings Class Step by Step

### Step 1: Basic Settings Without Customization

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    db_host: str
    db_port: int
```

**What happens?**
- Pydantic looks for environment variables: `APP_NAME`, `DB_HOST`, `DB_PORT`
- It validates types (converts string "8001" to int 8001)
- It raises an error if any required field is missing

**Usage:**
```python
import os
os.environ["APP_NAME"] = "user-service"
os.environ["DB_HOST"] = "localhost"
os.environ["DB_PORT"] = "5432"

settings = Settings()
print(settings.app_name)  # "user-service"
print(settings.db_port)   # 5432 (int, not string)
```

### Step 2: Adding Default Values

```python
class Settings(BaseSettings):
    app_name: str = "user-service"  # default if env var missing
    app_version: str = "0.1.0"
    app_env: str = "development"
    debug: bool = True
```

**What happens?**
- If `APP_NAME` env var exists, use it
- If not, use default `"user-service"`
- Same for other fields

**Usage:**
```python
# No environment variables set
settings = Settings()
print(settings.app_name)   # "user-service" (default)
print(settings.debug)      # True (default)
```

### Step 3: Grouping Related Settings (Optional Organization)

```python
class Settings(BaseSettings):
    # ── App ──────────────────────────────────────────────
    app_name: str = "user-service"
    app_version: str = "0.1.0"
    app_env: str = "development"
    debug: bool = True

    # ── Server ───────────────────────────────────────────
    host: str = "0.0.0.0"
    port: int = 8001
```

**Why group?**
- Comments help organize logically
- Makes it easier to scan
- Groups related configuration together

**Note:** The comments (`# ── App ───`) are just visual organization. Pydantic doesn't enforce groups.

***

## 3. model_config – Customizing Settings Behavior

### What Is model_config?

`model_config` is a Pydantic configuration dictionary that controls how settings behave.

### Full Example with SettingsConfigDict

```python
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "user-service"
    app_version: str = "0.1.0"
    app_env: str = "development"
    debug: bool = True

    host: str = "0.0.0.0"
    port: int = 8001

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )
```

### Breaking Down Each Option

| Option | What It Does | Example |
|---|---|---|
| `env_file=".env"` | Reads from `.env` file instead of (or in addition to) env vars | Loads `APP_NAME=user-service` from `.env` |
| `env_file_encoding="utf-8"` | File encoding for `.env` | Prevents encoding errors on Windows/Linux |
| `case_sensitive=False` | Ignores case when matching env vars | `app_name`, `APP_NAME`, `App_Name` all work |
| `extra="ignore"` | Ignores extra env vars not in class | `RANDOM_VAR` won't cause an error |

### Detailed Explanation of Each Option

#### `env_file=".env"`

**Without this:**
```python
# Only reads from environment variables
import os
os.environ["APP_NAME"] = "user-service"
settings = Settings()  # Works
```

**With this:**
```python
# Reads from .env file automatically
# .env file contains:
# APP_NAME=user-service
# DB_HOST=localhost
# DB_PORT=5432

settings = Settings()  # Automatically loads from .env
```

**Priority order:**
1. Environment variables (highest priority)
2. `.env` file
3. Default values in class (lowest priority)

#### `case_sensitive=False`

**Without this (`case_sensitive=True` by default):**
```python
# EXACT case match required
os.environ["APP_NAME"] = "user-service"
settings = Settings()  # ✅ Works

os.environ["app_name"] = "user-service"
settings = Settings()  # ❌ Error: field not found
```

**With this (`case_sensitive=False`):**
```python
os.environ["APP_NAME"] = "user-service"
settings = Settings()  # ✅ Works

os.environ["app_name"] = "user-service"
settings = Settings()  # ✅ Also works (case ignored)

os.environ["App_Name"] = "user-service"
settings = Settings()  # ✅ Also works
```

**Why use this?**
- Environment variables are often uppercase (`APP_NAME`)
- Python attributes are lowercase (`app_name`)
- Setting `case_sensitive=False` makes matching more flexible

#### `extra="ignore"`

**Without this (`extra="forbid"` by default):**
```python
# .env contains:
# APP_NAME=user-service
# DB_HOST=localhost
# RANDOM_VAR=should-error

settings = Settings()  # ❌ Error: extra fields detected
```

**With this (`extra="ignore"`):**
```python
# .env contains:
# APP_NAME=user-service
# DB_HOST=localhost
# RANDOM_VAR=ignored

settings = Settings()  # ✅ Works, RANDOM_VAR is ignored
```

**Other options:**
- `extra="forbid"` → raise error on extra fields (default)
- `extra="allow"` → add extra fields as attributes (rarely used)

**Why use `extra="ignore"`?**
- `.env` files often contain extra vars for other services
- You don't want your app to crash because of unrelated env vars
- Example: `.env` has `REDIS_URL` but your settings class doesn't need it

***

## 4. Properties – Computed Values from Settings

### What Is a Property?

A `@property` is a method that behaves like an attribute. It's computed on-the-fly based on other attributes.

### Example

```python
class Settings(BaseSettings):
    app_env: str = "development"

    @property
    def is_production(self) -> bool:
        return self.app_env == "production"

    @property
    def is_development(self) -> bool:
        return self.app_env == "development"
```

### Usage

```python
settings = Settings()
print(settings.app_env)       # "development"
print(settings.is_production) # False (computed)
print(settings.is_development) # True (computed)
```

### Why Use Properties?

1. **Cleaner code** → `settings.is_production` instead of `settings.app_env == "production"`
2. **Centralized logic** → Change the condition once, all code using it updates
3. **Type hints** → `-> bool` makes it clear this returns a boolean

### Real-World Example

```python
# Without property
if settings.app_env == "production":
    use_prod_database()

# With property (cleaner)
if settings.is_production:
    use_prod_database()
```

***

## 5. lru_cache – Caching the Settings Object

### What Is lru_cache?

`@lru_cache` is a Python decorator that caches function return values. If you call the function again with the same arguments, it returns the cached value instead of re-running the function.

**lru** = **Least Recently Used** (eviction policy when cache is full)

### Why Cache Settings?

Creating a `Settings` object reads environment variables and `.env` file. This is **expensive** if done repeatedly.

**Without caching:**
```python
# Called on every request
def handle_request():
    settings = Settings()  # Reads .env every time ❌ SLOW
    use_database(settings.db_host)
```

**With caching:**
```python
@lru_cache
def get_settings() -> Settings:
    return Settings()

# Called on every request
def handle_request():
    settings = get_settings()  # First call reads .env, later calls use cache ✅ FAST
    use_database(settings.db_host)
```

### Full Example

```python
from functools import lru_cache
from pydantic_settings import BaseSettings

@lru_cache
def get_settings() -> Settings:
    return Settings()
```

### How It Works

**First call:**
```python
settings1 = get_settings()
# Reads .env file
# Creates Settings object
# Caches the result
```

**Second call:**
```python
settings2 = get_settings()
# Returns cached object (no file reading)
# settings1 is settings2 (same object in memory)
print(settings1 is settings2)  # True
```

### Why This Pattern?

1. **Singleton pattern** → Only one `Settings` object exists in the app
2. **Performance** → Don't re-read `.env` on every request
3. **Consistency** → All parts of the app use the same settings object

### lru_cache Parameters

```python
@lru_cache(maxsize=128)  # default maxsize=128
def get_settings() -> Settings:
    return Settings()
```

- `maxsize=128` → cache up to 128 most recent calls
- For `get_settings()`, we only need 1 cache entry (no arguments), so default is fine

### Clearing the Cache (Rarely Needed)

```python
get_settings.cache_clear()  # Clears the cache
```

Use this in tests if you need to reload settings between test cases.

***

## 6. Complete Working Example

```python
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # ── App ──────────────────────────────────────────────
    app_name: str = "user-service"
    app_version: str = "0.1.0"
    app_env: str = "development"
    debug: bool = True

    # ── Server ───────────────────────────────────────────
    host: str = "0.0.0.0"
    port: int = 8001

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @property
    def is_production(self) -> bool:
        return self.app_env == "production"

    @property
    def is_development(self) -> bool:
        return self.app_env == "development"


@lru_cache
def get_settings() -> Settings:
    return Settings()


# ─── Usage ───────────────────────────────────────────────

# Load settings
settings = get_settings()

# Access attributes
print(settings.app_name)     # "user-service"
print(settings.port)         # 8001 (int)
print(settings.debug)        # True

# Access properties
print(settings.is_production)    # False
print(settings.is_development)   # True

# Conditional logic using properties
if settings.is_production:
    print("Connecting to production database...")
else:
    print("Connecting to development database...")
```

***

## 7. Environment Variables Flow (Step by Step)

```
┌────────────────────────────────────────────────────────┐
│ 1. Environment Variables (highest priority)            │
│    export APP_NAME="api-service"                       │
│    export PORT=9000                                    │
└────────────────────┬───────────────────────────────────┘
                     │
                     ▼
┌────────────────────────────────────────────────────────┐
│ 2. .env file (if env var not set)                      │
│    APP_NAME=user-service                               │
│    DB_HOST=localhost                                   │
└────────────────────┬───────────────────────────────────┘
                     │
                     ▼
┌────────────────────────────────────────────────────────┐
│ 3. Default values in class (lowest priority)           │
│    app_name: str = "user-service"                      │
│    debug: bool = True                                  │
└────────────────────┬───────────────────────────────────┘
                     │
                     ▼
┌────────────────────────────────────────────────────────┐
│ 4. Settings object created                             │
│    settings = Settings()                               │
└────────────────────┬───────────────────────────────────┘
                     │
                     ▼
┌────────────────────────────────────────────────────────┐
│ 5. Cached by @lru_cache                                │
│    get_settings() returns same object forever          │
└────────────────────────────────────────────────────────┘
```

***

## 8. Common Mistakes

### Mistake 1: Forgetting `@lru_cache`

```python
# ❌ WRONG: Creates new Settings on every call
def get_settings() -> Settings:
    return Settings()

# Called 1000 times = reads .env 1000 times
```

**Fix:**
```python
# ✅ CORRECT: Cache the result
@lru_cache
def get_settings() -> Settings:
    return Settings()
```

### Mistake 2: Using `extra="forbid"` with .env

```python
model_config = SettingsConfigDict(
    extra="forbid",  # ❌ Will error if .env has extra vars
)
```

**Fix:**
```python
model_config = SettingsConfigDict(
    extra="ignore",  # ✅ Gracefully ignores extra vars
)
```

### Mistake 3: Not Setting `case_sensitive=False`

```python
model_config = SettingsConfigDict(
    case_sensitive=True,  # Default
)

# .env has: APP_NAME=user-service
# Class has: app_name: str
# ❌ Error: field not found (case mismatch)
```

**Fix:**
```python
model_config = SettingsConfigDict(
    case_sensitive=False,  # ✅ Matches APP_NAME to app_name
)
```

### Mistake 4: Missing `__init__.py` in Package

```python
# ❌ If importing from package, missing __init__.py
from myapp.settings import get_settings  # ImportError
```

**Fix:**
```python
# ✅ Ensure __init__.py exists
# myapp/
#   __init__.py
#   settings.py
```

***

## 9. Side-by-Side Comparison

| Concept | Purpose | When to Use |
|---|---|---|
| `BaseSettings` | Read config from env vars | Any app needing configuration |
| `model_config` | Customize settings behavior | When you need `.env`, case-insensitive, etc. |
| `SettingsConfigDict` | Type-safe config for `model_config` | Always use instead of plain dict |
| `@property` | Computed attributes | When you need derived values (e.g., `is_production`) |
| `@lru_cache` | Cache function results | For singleton patterns, expensive operations |
| `get_settings()` | Singleton settings accessor | Always use this instead of `Settings()` directly |

***

## 10. Summary (Cheat Sheet)

| Code Pattern | What It Does |
|---|---|
| `app_name: str = "user-service"` | Field with default value |
| `app_env: str` | Required field (must be in env or .env) |
| `model_config = SettingsConfigDict(...)` | Configure settings behavior |
| `env_file=".env"` | Read from `.env` file |
| `case_sensitive=False` | Match `APP_NAME` to `app_name` |
| `extra="ignore"` | Ignore extra env vars |
| `@property` | Computed attribute (e.g., `is_production`) |
| `@lru_cache` | Cache function result (singleton pattern) |
| `get_settings()` | Get cached settings object |

**Final flow:**
```
Vault → Environment Variables → .env file → Settings defaults → get_settings() → App
```