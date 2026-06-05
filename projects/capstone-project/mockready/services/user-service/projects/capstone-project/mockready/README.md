# MockReady — IT Institute Mock Interview Platform
### Full Project Plan & Step-by-Step Checklist

> **How to use:** Check off `[x]` as you complete each step. Share this file at the start of every session as context.
> **Marking:** `[ ]` Not started · `[~]` In progress · `[x]` Completed

---

## Project Overview

**What we're building:**
An IT training institute platform where students can book mock interview sessions across any campus, get assigned a trainer automatically from an availability pool, upload their resume and artifacts, and use an AI answer coach that generates ideal answers in the student's own voice based on their resume and experience.

**Key business rules:**
- Students can book a cabin at ANY campus (cross-campus booking)
- Trainer is auto-assigned from available trainer pool at the chosen campus
- If trainer declines → silently auto-reassign next available trainer → notify student of new trainer
- Cabin = physical room at a campus; each campus has a fixed number of cabins
- Students upload resume + artifacts (stored on local disk/volume)
- AI answer coach: given interview question + student's resume context → generate ideal answer in human, personalized language (Groq API, free)

---

## Architecture — 5 Microservices

| Service | Responsibility | Primary DB |
|---|---|---|
| `user-service` | Students, trainers, admins, auth, roles | PostgreSQL |
| `booking-service` | Cabin booking, trainer assignment, availability | PostgreSQL + Redis |
| `notification-service` | Email/in-app notifications, event logs | MongoDB |
| `file-service` | Resume + artifact upload, storage, retrieval | PostgreSQL (metadata) + Local disk |
| `ai-service` | Answer coach, resume parsing, prompt building | — (calls Groq API) |

**Supporting infra:**
| Component | Role | Port |
|---|---|---|
| API Gateway (Nginx) | Single entry point, routing, rate limiting | 80 |
| Config Server | Centralised config for all services | 8000 |
| PostgreSQL | Relational data | 5432 |
| MongoDB | Notification/event documents | 27017 |
| Redis | Caching + rate limiting + availability locks | 6379 |
| Kafka | Async event bus between services | 9092 |
| MinIO (optional) | Future file storage upgrade path | 9001 |
| Prometheus | Metrics scraping | 9090 |
| Grafana | Dashboards & alerting | 3000 |
| Elasticsearch | Log storage | 9200 |
| Logstash | Log shipping | 5044 |
| Kibana | Log dashboards | 5601 |
| SonarQube | Code quality gate | 9000 |
| Jenkins | CI/CD pipeline | 8080 |

**Service Ports:**
| Service | Port |
|---|---|
| user-service | 8001 |
| booking-service | 8002 |
| notification-service | 8003 |
| file-service | 8004 |
| ai-service | 8005 |
| config-server | 8000 |

---

## Domain Entities (Big Picture)

```
Campus → has many → Cabins
Campus → has many → Trainers (trainers can be at multiple campuses)
Batch → belongs to → Campus · has many → Students
Student → belongs to → Batch
Trainer → has → Availability slots · Skills · Rating
Booking → links → Student + Cabin + Trainer + TimeSlot
Booking events → fire → Kafka → Notification Service
Resume → belongs to → Student · parsed by → AI Service
InterviewSession → has many → Questions + AI-generated ideal answers
```

---

## Phase 1 — Foundation (Single Service Skeleton)
> Goal: one running FastAPI service, clean structure, students understand the project skeleton before anything is added.

### 1.1 Project Structure
- [ ] Create monorepo layout:
  ```
  mockready/
  ├── services/
  │   ├── user-service/
  │   ├── booking-service/
  │   ├── notification-service/
  │   ├── file-service/
  │   └── ai-service/
  ├── config-server/
  ├── gateway/
  ├── infra/
  │   ├── docker/
  │   ├── prometheus/
  │   ├── grafana/
  │   └── elk/
  ├── docker-compose.yml
  └── README.md
  ```
- [ ] Set up `user-service` first (all others follow same pattern)
- [ ] Inside each service: `app/routers/`, `app/models/`, `app/schemas/`, `app/services/`, `app/core/`, `app/repositories/`
- [ ] Create `requirements.txt` for user-service
- [ ] Create `.env.example` and `core/settings.py` using `pydantic-settings`

### 1.2 First Endpoints
- [ ] `GET /health` → returns `{ service, version, status, timestamp }`
- [ ] `GET /` → returns service info
- [ ] Run with Uvicorn, verify Swagger UI at `/docs`

### 1.3 First Real Router — Campuses
- [ ] Create `Campus` Pydantic schema (`CampusCreate`, `CampusResponse`)
- [ ] `POST /campuses` — create a campus (name, city, address, cabin_count)
- [ ] `GET /campuses` — list all campuses
- [ ] `GET /campuses/{id}` — get single campus
- [ ] `PUT /campuses/{id}` — update campus
- [ ] `DELETE /campuses/{id}` — deactivate campus
- [ ] All using in-memory list for now (no DB yet)

### 1.4 Conventions Lock-in
- [ ] Establish response envelope: `{ "data": ..., "message": "", "success": true }`
- [ ] Establish pagination schema: `{ "data": [], "total": 0, "page": 1, "size": 20 }`
- [ ] Add `README.md` with run instructions

---

## Phase 2 — Database (PostgreSQL + SQLAlchemy + Alembic)
> Goal: real persistence, ORM setup, migrations, repository pattern.

### 2.1 PostgreSQL Setup
- [ ] Add `asyncpg` + `SQLAlchemy` (async) + `alembic`
- [ ] Create `core/database.py` — async engine, session factory, `get_db` dependency
- [ ] Configure via `settings.py` (no hardcoded strings)
- [ ] Add DB startup/shutdown lifecycle events in `main.py`

### 2.2 All Core Models
- [ ] `Campus` (id, name, city, address, cabin_count, is_active, created_at)
- [ ] `Cabin` (id, campus_id, cabin_number, is_active)
- [ ] `User` (id, name, email, hashed_password, role, campus_id, is_active)
  - roles: `student`, `trainer`, `admin`, `super_admin`
- [ ] `Batch` (id, name, campus_id, course, start_date, end_date, is_active)
- [ ] `StudentProfile` (id, user_id, batch_id, enrollment_number, skills)
- [ ] `TrainerProfile` (id, user_id, skills, experience_years, campuses — many-to-many)
- [ ] `TrainerAvailability` (id, trainer_id, date, start_time, end_time, is_booked)
- [ ] `Booking` (id, student_id, trainer_id, cabin_id, campus_id, scheduled_at, status, decline_count)
  - status: `pending`, `confirmed`, `declined`, `reassigned`, `completed`, `cancelled`
- [ ] Run first Alembic migration

### 2.3 Repository Pattern
- [ ] `CampusRepository` — CRUD
- [ ] `UserRepository` — CRUD + find by email
- [ ] `BookingRepository` — CRUD + find available trainers + availability queries
- [ ] Each router calls service layer, service calls repository (never raw queries in routers)

### 2.4 Seed Data Script
- [ ] `scripts/seed.py` — seed 3 campuses, 5 trainers, 10 students, cabins, availability slots
- [ ] Run via `python -m scripts.seed`

---

## Phase 3 — Authentication & Authorization
> Goal: secure all endpoints, teach JWT lifecycle, role-based access, multi-campus permissions.

### 3.1 Password & Token Utilities
- [ ] Add `passlib[bcrypt]` + `python-jose`
- [ ] `core/security.py` — `hash_password`, `verify_password`, `create_access_token`, `create_refresh_token`, `decode_token`
- [ ] Token payload includes: `user_id`, `role`, `campus_id`, `exp`

### 3.2 Auth Endpoints (in user-service)
- [ ] `POST /auth/register` — student self-registration (assigned to campus/batch)
- [ ] `POST /auth/login` — returns access token + refresh token
- [ ] `POST /auth/refresh` — issue new access token
- [ ] `POST /auth/logout` — blacklist token in Redis
- [ ] `GET /auth/me` — current user info

### 3.3 Role-Based Dependencies
- [ ] `get_current_user` dependency — decodes JWT, fetches user
- [ ] `require_role(*roles)` — factory dependency for endpoint protection
- [ ] `require_same_campus` — trainers/admins can only manage their campus (super_admin bypasses)
- [ ] Protect all routes appropriately:
  - Students: book interviews, view own bookings, upload files, use AI coach
  - Trainers: view assigned bookings, accept/decline, set availability
  - Admin: manage campus, batches, trainers, students of their campus
  - Super Admin: full access across all campuses

### 3.4 Token Blacklisting (Redis)
- [ ] On logout, store token `jti` in Redis with TTL = token expiry
- [ ] `get_current_user` checks blacklist before accepting token

---

## Phase 4 — Logging & Exception Handling
> Goal: every request traceable end-to-end, every error consistent and informative.

### 4.1 Structured Logging
- [ ] Add `loguru`
- [ ] JSON log format: `timestamp`, `level`, `service`, `request_id`, `user_id`, `message`
- [ ] `RequestIDMiddleware` — generates UUID per request, attaches to headers + log context
- [ ] Log: method, path, status, response time on every request
- [ ] Log: user_id, campus_id on authenticated requests

### 4.2 Custom Exceptions
- [ ] `NotFoundException` (404) — campus not found, trainer not found, booking not found
- [ ] `UnauthorizedException` (401)
- [ ] `ForbiddenException` (403) — cross-campus access denied
- [ ] `ConflictException` (409) — cabin already booked, slot already taken
- [ ] `TrainerUnavailableException` (409) — no trainers available at campus for slot
- [ ] `ValidationException` (422)
- [ ] `FileUploadException` (400)

### 4.3 Global Exception Handlers
- [ ] Register all custom exceptions in `main.py`
- [ ] Standard error envelope: `{ "success": false, "error": { "code": "", "message": "", "request_id": "" } }`
- [ ] Override Pydantic 422 format to match envelope
- [ ] Handle SQLAlchemy `IntegrityError`, `NoResultFound` cleanly

### 4.4 Audit Logging
- [ ] Log all booking state changes with who triggered them
- [ ] Log all trainer assignment/reassignment events
- [ ] Log all file uploads

---

## Phase 5 — Caching, Rate Limiting & File Service
> Goal: Redis caching patterns, rate limiting with real logic, file upload service.

### 5.1 Redis Setup
- [ ] Add `redis[asyncio]`
- [ ] `core/cache.py` — `RedisClient` wrapper with `get`, `set`, `delete`, `exists`
- [ ] `@cached(ttl, key_fn)` decorator for route-level caching

### 5.2 Caching Strategy
- [ ] Cache `GET /campuses` — TTL 10 min (changes rarely)
- [ ] Cache `GET /campuses/{id}` — TTL 5 min, invalidate on update
- [ ] Cache `GET /trainers/{id}/availability` — TTL 60 sec (changes often)
- [ ] Cache `GET /batches` — TTL 10 min
- [ ] Add cache hit/miss logging

### 5.3 Rate Limiting (Sliding Window, Redis)
- [ ] `RateLimitMiddleware` — sliding window counter per `user_id` (authenticated) or `IP` (anonymous)
- [ ] Configurable limits per route group:
  - Auth endpoints (login/register): 10 req/min (brute force protection)
  - General API: 100 req/min for students, 200 req/min for trainers/admins
  - AI coach endpoint: 20 req/min (LLM is expensive even on free tier)
  - File upload: 10 req/min
- [ ] Response headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`
- [ ] `429 Too Many Requests` with `Retry-After` header
- [ ] Teach concept: sliding window vs fixed window vs token bucket

### 5.4 File Service (file-service)
- [ ] Separate FastAPI service on port 8004
- [ ] `POST /files/resume` — upload resume (PDF only, max 5MB)
- [ ] `POST /files/artifacts` — upload any artifact (PDF, DOCX, PNG, max 10MB)
- [ ] `GET /files/{file_id}` — download file (authenticated, student owns file or admin)
- [ ] `DELETE /files/{file_id}` — soft delete
- [ ] `GET /files/student/{student_id}` — list all files for a student
- [ ] Storage: `volumes/uploads/{student_id}/{uuid}_{filename}`
- [ ] DB: `FileMetadata` table (id, student_id, original_name, stored_path, file_type, size, uploaded_at)
- [ ] Validate file type by magic bytes (not just extension)
- [ ] Virus scan hook (log warning, teachable moment — in prod you'd use ClamAV)

### 5.5 Cabin Availability Lock (Redis)
- [ ] Use Redis distributed lock (`SETNX` with TTL) during booking creation
- [ ] Prevents double-booking same cabin in concurrent requests
- [ ] Teach concept: optimistic vs pessimistic locking

---

## Phase 6 — Booking Service + Trainer Assignment Engine
> Goal: the core business logic — the most interesting and complex service.

### 6.1 Booking Service Setup
- [ ] Separate FastAPI service on port 8002
- [ ] Own PostgreSQL schema (shares same Postgres instance, different schema/tables)

### 6.2 Trainer Assignment Engine
- [ ] `TrainerAssignmentService` — core logic:
  1. Get requested campus + time slot
  2. Query all trainers available at that campus for that slot
  3. Filter out trainers who already have a confirmed booking at that time
  4. Sort by: least bookings this week → highest rating → random tiebreak
  5. Assign top candidate
  6. If no trainers available → raise `TrainerUnavailableException` (student must pick different slot)
- [ ] Assignment is atomic (Redis lock on slot during assignment)

### 6.3 Booking Endpoints
- [ ] `POST /bookings` — student creates booking
  - Input: `campus_id`, `cabin_id`, `date`, `time_slot`, `interview_type` (technical/hr/system_design)
  - Auto-assigns trainer
  - Sets status → `pending` (waiting trainer confirmation)
- [ ] `GET /bookings` — list bookings (filtered by role: student sees own, trainer sees assigned, admin sees campus)
- [ ] `GET /bookings/{id}` — booking detail
- [ ] `PATCH /bookings/{id}/confirm` — trainer confirms (status → `confirmed`)
- [ ] `PATCH /bookings/{id}/decline` — trainer declines → triggers reassignment flow
- [ ] `PATCH /bookings/{id}/cancel` — student cancels (only if >2 hours before slot)
- [ ] `PATCH /bookings/{id}/complete` — admin/trainer marks complete

### 6.4 Trainer Decline & Reassignment Flow
- [ ] On decline:
  1. Increment `booking.decline_count`
  2. Mark current trainer's slot as free again
  3. Re-run `TrainerAssignmentService` excluding all previously declined trainers
  4. If new trainer found → assign, publish `booking.reassigned` Kafka event
  5. If no trainers left → set status `no_trainer_available`, notify student to reschedule
- [ ] Max reassignment attempts: 3 (configurable)

### 6.5 Trainer Availability Management
- [ ] `POST /trainers/availability` — trainer sets available slots (date, start_time, end_time, campus_id)
- [ ] `GET /trainers/availability` — trainer views own availability
- [ ] `GET /campuses/{id}/available-slots` — student views available slots at a campus (date picker)
- [ ] `GET /campuses/{id}/trainers` — list trainers at campus with availability status

### 6.6 Cross-Campus Logic
- [ ] Student can book at any campus (not just their home campus)
- [ ] Trainer is assigned from the TARGET campus's trainer pool
- [ ] Booking always records both `student.home_campus_id` and `booking.campus_id`
- [ ] Super admin can view cross-campus booking analytics

---

## Phase 7 — Notification Service + Kafka Events
> Goal: async event-driven communication between services, MongoDB for document storage.

### 7.1 Kafka Topics Design
| Topic | Producer | Consumer | Trigger |
|---|---|---|---|
| `booking.created` | booking-service | notification-service | Student books slot |
| `booking.confirmed` | booking-service | notification-service | Trainer confirms |
| `booking.declined` | booking-service | booking-service + notification-service | Trainer declines |
| `booking.reassigned` | booking-service | notification-service | New trainer assigned |
| `booking.cancelled` | booking-service | notification-service | Booking cancelled |
| `booking.completed` | booking-service | notification-service | Session done |
| `file.uploaded` | file-service | ai-service | Resume uploaded |
| `ai.analysis.ready` | ai-service | notification-service | AI parsed resume |

### 7.2 Kafka Setup
- [ ] Add `aiokafka`
- [ ] `core/kafka_producer.py` — async producer with retry logic
- [ ] `core/kafka_consumer.py` — async consumer with consumer group
- [ ] Dead Letter Queue (DLQ) topic: `{topic}.dlq` for failed messages
- [ ] Kafka consumer runs as background task on service startup

### 7.3 Notification Service (notification-service)
- [ ] Separate FastAPI service on port 8003
- [ ] MongoDB as primary store (`motor` async driver)
- [ ] `Notification` document schema:
  ```json
  {
    "_id": "uuid",
    "user_id": "uuid",
    "type": "booking_confirmed | booking_reassigned | ...",
    "title": "",
    "message": "",
    "is_read": false,
    "metadata": { "booking_id": "", "trainer_name": "", "campus": "" },
    "created_at": ""
  }
  ```
- [ ] Consume all Kafka booking events → create notification documents
- [ ] `GET /notifications` — list notifications for current user (paginated)
- [ ] `PATCH /notifications/{id}/read` — mark as read
- [ ] `PATCH /notifications/read-all` — mark all read
- [ ] `GET /notifications/unread-count` — for badge count in UI
- [ ] Email stub: log email content (no real SMTP — teachable moment, show how you'd plug in SendGrid/SES)

---

## Phase 8 — AI Service (Answer Coach)
> Goal: real AI integration with Groq, contextual prompt engineering, resume-aware responses.

### 8.1 AI Service Setup
- [ ] Separate FastAPI service on port 8005
- [ ] Add `groq` Python SDK (free API key, Llama 3 / Mixtral)
- [ ] `core/groq_client.py` — async Groq client wrapper
- [ ] Store `GROQ_API_KEY` in config server / `.env`

### 8.2 Resume Parsing
- [ ] `POST /ai/parse-resume` — triggered by `file.uploaded` Kafka event
  - Reads the uploaded PDF via file-service
  - Extracts: skills, experience (years, companies, roles), education, notable projects
  - Stores parsed profile in Redis (TTL 24h) and MongoDB for persistence
- [ ] `GET /ai/student/{id}/profile` — get AI-parsed student profile

### 8.3 Answer Coach — Core Feature
- [ ] `POST /ai/answer-coach` — main endpoint
  - Input: `{ "question": "", "interview_type": "technical|hr|system_design", "booking_id": "" }`
  - Fetches student's parsed resume profile
  - Fetches interview context (what tech stack is this batch learning, what role is being interviewed for)
  - Builds contextual prompt (see below)
  - Streams response from Groq API
  - Returns ideal answer in student's voice

### 8.4 Prompt Engineering (teach this explicitly)
- [ ] System prompt structure:
  ```
  You are an interview coach helping a student prepare for a {interview_type} interview.
  
  Student background:
  - Experience: {years} years, previously worked at {companies}
  - Skills: {skills}
  - Notable projects: {projects}
  - Currently learning: {batch_course}
  
  Respond as if you are the student giving their best possible answer.
  Use natural, human language. Match the vocabulary of someone with {years} years experience.
  Do not use bullet points. Speak in first person. Be specific, reference their actual experience.
  Keep the answer under 3 minutes when spoken aloud (~400 words).
  ```
- [ ] Teach concept: system prompt vs user prompt, temperature settings, token limits
- [ ] Add `POST /ai/generate-questions` — given batch topic + interview type → generate 10 practice questions
- [ ] Add `POST /ai/feedback` — student submits their own answer → AI gives feedback vs ideal answer

### 8.5 Rate Limiting on AI Routes
- [ ] 20 requests/min per student (Redis rate limiter from Phase 5)
- [ ] Daily limit: 50 AI coach calls per student (Redis counter, reset at midnight)
- [ ] Teach why: Groq free tier has token limits

---

## Phase 9 — API Gateway + Config Server + Load Balancing
> Goal: single entry point, centralised config, horizontal scaling.

### 9.1 Config Server
- [ ] FastAPI service on port 8000
- [ ] `GET /config/{service_name}` — returns config for that service
- [ ] Services fetch config on startup, cache locally
- [ ] Manages: DB URLs, Redis URL, Kafka brokers, Groq API key, JWT secret
- [ ] In prod: would be Consul/Vault — teach that context

### 9.2 Nginx API Gateway
- [ ] Route table:
  - `/api/v1/auth/*` → user-service:8001
  - `/api/v1/users/*` → user-service:8001
  - `/api/v1/bookings/*` → booking-service:8002
  - `/api/v1/notifications/*` → notification-service:8003
  - `/api/v1/files/*` → file-service:8004
  - `/api/v1/ai/*` → ai-service:8005
  - `/api/v1/campuses/*` → user-service:8001
- [ ] Rate limiting at gateway level (coarse, per IP)
- [ ] Request timeout config per route
- [ ] Access log format matching request_id for tracing

### 9.3 Load Balancing
- [ ] Run 2 instances of booking-service (highest load expected)
- [ ] Nginx upstream round-robin between instances
- [ ] Teach: sticky sessions not needed because we're stateless (JWT)
- [ ] Health check: Nginx upstream health checks via `/health/ready`

---

## Phase 10 — Observability (Prometheus + Grafana + ELK)
> Goal: full production visibility, teach what to measure and why.

### 10.1 Prometheus Metrics
- [ ] Add `prometheus-fastapi-instrumentator` to all services
- [ ] Expose `GET /metrics` (Prometheus scrape endpoint)
- [ ] Custom metrics to add:
  - `booking_created_total` (counter)
  - `trainer_assignment_attempts_total` (counter, label: success/failed)
  - `trainer_decline_total` (counter)
  - `ai_coach_requests_total` (counter)
  - `groq_response_latency_seconds` (histogram)
  - `cache_hits_total` / `cache_misses_total` (counter)
  - `file_upload_size_bytes` (histogram)

### 10.2 Grafana Dashboards
- [ ] Dashboard 1 — System overview: request rate, error rate, p95 latency per service
- [ ] Dashboard 2 — Booking funnel: created → confirmed → completed → declined rate
- [ ] Dashboard 3 — AI service: request rate, Groq latency, daily usage vs limit
- [ ] Dashboard 4 — Cache: hit rate, Redis memory usage
- [ ] Alert: trainer decline rate > 30% in 10 min (might mean availability problem)
- [ ] Alert: AI service error rate > 10%

### 10.3 ELK Stack
- [ ] Structured JSON logs from all services → Logstash
- [ ] Elasticsearch indices per service
- [ ] Kibana dashboards:
  - All logs with request_id search
  - Error logs with stack traces
  - Booking state change audit trail
  - Cross-campus booking activity

### 10.4 Health Check Endpoints
- [ ] `GET /health/live` — is the process alive? (always 200 if running)
- [ ] `GET /health/ready` — are dependencies ready? (checks DB, Redis, Kafka)
  ```json
  {
    "status": "ready",
    "checks": {
      "postgres": "ok",
      "redis": "ok",
      "kafka": "ok",
      "groq": "ok"
    }
  }
  ```

---

## Phase 11 — Docker + CI/CD (Jenkins + SonarQube)
> Goal: code commit → automated quality gate → deployed containers.

### 11.1 Dockerfiles
- [ ] Multi-stage `Dockerfile` per service:
  - Stage 1 (`builder`): install deps, run tests
  - Stage 2 (`runtime`): copy only what's needed, run as non-root user
- [ ] `.dockerignore` per service
- [ ] Base image: `python:3.12-slim`
- [ ] Labels: service name, version, git SHA

### 11.2 Docker Compose
- [ ] `docker-compose.yml` — full stack:
  - All 5 services + config-server
  - PostgreSQL, MongoDB, Redis, Kafka + Zookeeper
  - Prometheus, Grafana, Elasticsearch, Logstash, Kibana
  - Nginx gateway
- [ ] `docker-compose.dev.yml` — override for local dev (hot reload, exposed ports)
- [ ] Named volumes for Postgres data, MongoDB data, file uploads, Elasticsearch data
- [ ] `depends_on` with health checks (services wait for DB/Redis to be ready)
- [ ] `restart: unless-stopped` on all services

### 11.3 Testing
- [ ] `pytest` + `pytest-asyncio` + `httpx` (async test client)
- [ ] Unit tests: `TrainerAssignmentService` (mock repo), prompt builder, rate limiter logic
- [ ] Integration tests: full booking flow (real DB in Docker)
- [ ] Test: decline → reassign → notify flow end-to-end
- [ ] Test: cross-campus booking (student from campus A books at campus B)
- [ ] Test: rate limit triggers at correct threshold
- [ ] Test: file upload rejects wrong type / over size limit
- [ ] Coverage: minimum 75% (`pytest-cov`)

### 11.4 SonarQube
- [ ] `sonar-project.properties` per service
- [ ] Quality gates:
  - Coverage ≥ 75%
  - Duplications < 3%
  - No critical/blocker code smells
  - No high security hotspots unreviewed
- [ ] Export coverage XML from pytest-cov → SonarQube scanner

### 11.5 Jenkins Pipeline (Jenkinsfile)
```
Pipeline stages per service:
1. Checkout
2. Install dependencies
3. Lint (ruff)
4. Unit tests + coverage
5. SonarQube analysis
6. Quality gate check (fail pipeline if gate fails)
7. Build Docker image (tag: git SHA + branch)
8. Push to local Docker registry
9. Deploy (docker-compose pull + rolling update)
10. Smoke test (hit /health/ready, assert 200)
11. Notify (log success/failure)
```
- [ ] Write `Jenkinsfile` with all stages above
- [ ] Parallel test execution for multiple services
- [ ] Branch strategy: `feature/*` → runs up to stage 6 · `main` → full deploy
- [ ] Keep last 3 Docker image tags (cleanup old images)

### 11.6 Final End-to-End Verification
- [ ] Student registers → logs in → views campuses
- [ ] Student books cabin at a different campus → trainer auto-assigned
- [ ] Trainer declines → silent reassign → student notified of new trainer
- [ ] Student uploads resume → AI parses it
- [ ] Student uses AI coach: asks question → gets personalized answer in their voice
- [ ] Admin views Grafana dashboard, sees booking funnel
- [ ] Kibana shows full request trace by request_id
- [ ] Simulate bad commit → SonarQube blocks pipeline
- [ ] All in Docker, one `docker-compose up`

---

## Key Concepts Taught Per Phase

| Phase | Core Concepts |
|---|---|
| 1 | FastAPI, Pydantic v2, Uvicorn, project structure, response envelopes |
| 2 | SQLAlchemy async, Alembic, repository pattern, connection pooling, seed scripts |
| 3 | JWT (access + refresh), OAuth2, bcrypt, RBAC, token blacklisting with Redis |
| 4 | Structured logging, request tracing (request_id), global exception handling, audit logs |
| 5 | Cache-aside pattern, TTL strategy, cache invalidation, sliding window rate limiting, file validation, distributed locks |
| 6 | Business logic design, trainer assignment algorithm, state machines (booking status), cross-entity transactions |
| 7 | Kafka topics, consumer groups, DLQ, async event-driven architecture, MongoDB document design |
| 8 | Prompt engineering, LLM integration, system vs user prompts, streaming responses, token budgeting |
| 9 | API gateway routing, config server pattern, load balancing, stateless scaling |
| 10 | RED metrics (Rate/Errors/Duration), custom Prometheus metrics, alerting rules, log shipping, distributed tracing |
| 11 | Multi-stage Docker builds, docker-compose orchestration, integration testing, quality gates, CI/CD pipelines |

---

## Session Context Template
> Copy and fill in at the start of each new session.

```
Project: MockReady — IT Institute Mock Interview Platform
Current phase: Phase ___ — ___
Last completed step: ___
Next step to work on: ___
Blockers / questions: ___

Services built so far: [ ] user-service [ ] booking-service [ ] notification-service [ ] file-service [ ] ai-service
Infra running: [ ] Postgres [ ] Redis [ ] MongoDB [ ] Kafka [ ] Nginx

Attach: mockinterview_project_plan.md (this file, with checkboxes updated)
```