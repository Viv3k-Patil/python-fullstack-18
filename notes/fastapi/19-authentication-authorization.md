# Authentication & Authorization

## Overview

| Concept | Question Answered | Example |
|---|---|---|
| **Authentication** | *Who are you?* | Logging in with username + password |
| **Authorization** | *What are you allowed to do?* | Admin can delete users; viewer cannot |

These two concepts are distinct but work together. Authentication always comes first.

---

## Authentication

### What It Is
The process of verifying the identity of a user, service, or system.

### Common Methods

**1. Password-Based**
- User provides credentials (username + password)
- Server compares against stored (hashed) password
- Vulnerable to brute force, phishing, credential stuffing

**2. Multi-Factor Authentication (MFA)**
- Something you **know** (password)
- Something you **have** (OTP device, phone)
- Something you **are** (biometrics)
- Significantly reduces account takeover risk

**3. Token-Based**
- After login, server issues a signed token
- Client sends token on every subsequent request
- Server validates the token (no session lookup needed)
- Common formats: JWT (JSON Web Token)

**4. Session-Based**
- Server creates a session after login and stores it server-side
- Client holds only a session ID (usually in a cookie)
- Server looks up the session on each request

**5. OAuth 2.0 / Social Login**
- Delegate authentication to a trusted third party (Google, GitHub, etc.)
- Your app never sees the user's password
- Returns an access token scoped to specific permissions

**6. API Keys**
- Long-lived secret strings for machine-to-machine communication
- Should be rotated regularly and scoped to minimum permissions

**7. Certificate-Based (mTLS)**
- Both client and server present cryptographic certificates
- Common in service-to-service communication

---

### JWT Deep Dive

A JWT has three Base64URL-encoded parts separated by dots:

```
header.payload.signature
```

- **Header** — algorithm used (e.g., `HS256`, `RS256`)
- **Payload** — claims: user ID, roles, expiry (`exp`), issued-at (`iat`)
- **Signature** — cryptographic proof the token hasn't been tampered with

**Key rules:**
- Never store sensitive data in the payload (it's encoded, not encrypted)
- Always validate `exp` and `iss` (issuer)
- Use short expiry + refresh tokens rather than long-lived access tokens

---

### Session vs. Token

| | Session-Based | Token-Based (JWT) |
|---|---|---|
| State | Stored server-side | Stateless (client holds it) |
| Scalability | Harder (sticky sessions or shared store) | Easier (any server can verify) |
| Revocation | Easy (delete session) | Hard (need a blocklist) |
| Size | Small (just a session ID) | Larger (full payload) |

---

### Password Storage Best Practices
- **Never** store plaintext passwords
- **Never** use MD5 or SHA-1 alone
- Use a slow, salted hashing algorithm: **bcrypt**, **Argon2**, or **scrypt**
- Salt is added per-user to prevent rainbow table attacks

---

## Authorization

### What It Is
Determining what an authenticated identity is permitted to do.

### Models

**1. Role-Based Access Control (RBAC)**
- Users are assigned roles (`admin`, `editor`, `viewer`)
- Permissions are attached to roles, not individual users
- Simple and widely used
- Can become unwieldy with many fine-grained roles

**2. Attribute-Based Access Control (ABAC)**
- Access decisions based on attributes of the user, resource, and environment
- Example: "Allow if `user.department == resource.department AND time < 18:00`"
- Very flexible; more complex to implement and audit

**3. Policy-Based Access Control (PBAC)**
- Policies are written as explicit rules (often in a policy language like OPA/Rego)
- Centralized policy engine evaluates requests
- Good for microservices and decoupled systems

**4. Discretionary Access Control (DAC)**
- Resource owner controls who can access it
- Example: file system permissions (owner/group/others)

**5. Mandatory Access Control (MAC)**
- System enforces access based on classifications (Top Secret, Confidential)
- Users cannot override — common in government/military systems

---

### RBAC Example

```
Roles:       admin, editor, viewer
Permissions: read, write, delete

admin  → read, write, delete
editor → read, write
viewer → read
```

---

### Principle of Least Privilege
> Grant only the minimum permissions needed to perform a task.

- Reduces blast radius of compromised accounts
- Apply to users, services, and API keys alike
- Review and revoke unused permissions regularly

---

### Common Authorization Patterns

**Resource-Level Authorization**
Check not just *can this user write posts*, but *can this user write THIS post* (ownership).

**Scope-Based (OAuth)**
Access tokens carry scopes (e.g., `read:profile`, `write:files`). The server checks the token's scope before allowing an action.

**Guard / Middleware Pattern**
Authorization logic sits in a middleware layer before the route handler executes. Keeps business logic clean.

---

## Common Vulnerabilities

| Vulnerability | Description | Mitigation |
|---|---|---|
| Broken Authentication | Weak passwords, no MFA, session fixation | Enforce strong auth, MFA, secure session handling |
| Broken Access Control | User accesses another user's data (IDOR) | Server-side ownership checks on every request |
| JWT Algorithm Confusion | Accepting `alg: none` or RS256 → HS256 swap | Whitelist allowed algorithms; validate strictly |
| Privilege Escalation | User gains higher permissions than granted | Enforce authorization at every layer |
| Insecure Direct Object Reference (IDOR) | Guessing IDs to access other users' resources | Use unpredictable IDs + ownership checks |
| Session Hijacking | Stolen session cookie | Use `HttpOnly`, `Secure`, `SameSite` cookie flags |
| CSRF | Forged requests from another site | CSRF tokens or `SameSite=Strict` cookies |

---

## Token Storage (Client Side)

| Location | XSS Risk | CSRF Risk | Notes |
|---|---|---|---|
| `localStorage` | High | Low | Accessible by JS — avoid for sensitive tokens |
| `sessionStorage` | High | Low | Same as localStorage, clears on tab close |
| `HttpOnly` Cookie | Low | Higher | Invisible to JS; pair with `SameSite` and CSRF token |

**Recommendation:** Store access tokens in memory (JS variable) and use `HttpOnly` cookies for refresh tokens.

---

## Refresh Token Flow

```
1. User logs in → Server issues:
     access_token  (short-lived, e.g., 15 min)
     refresh_token (long-lived, e.g., 7 days, stored securely)

2. Client uses access_token for API calls.

3. access_token expires → Client sends refresh_token to /refresh endpoint.

4. Server validates refresh_token → Issues new access_token (and optionally rotates refresh_token).

5. If refresh_token is invalid/expired → Force re-login.
```

---

## Quick Reference Checklist

### Authentication
- [ ] Passwords hashed with bcrypt / Argon2
- [ ] MFA available (especially for privileged accounts)
- [ ] Account lockout after N failed attempts
- [ ] Secure password reset flow (time-limited tokens)
- [ ] HTTPS enforced everywhere
- [ ] Tokens have short expiry + refresh strategy

### Authorization
- [ ] Authorization checked server-side on every request
- [ ] Ownership validated for resource-level operations
- [ ] Principle of least privilege applied
- [ ] Roles and permissions documented and audited
- [ ] No authorization logic leaking to the client only

---

## Glossary

| Term | Meaning |
|---|---|
| **AuthN** | Authentication |
| **AuthZ** | Authorization |
| **JWT** | JSON Web Token |
| **OAuth 2.0** | Authorization framework (delegated access) |
| **OIDC** | OpenID Connect — identity layer on top of OAuth 2.0 |
| **MFA / 2FA** | Multi-Factor / Two-Factor Authentication |
| **RBAC** | Role-Based Access Control |
| **ABAC** | Attribute-Based Access Control |
| **IDOR** | Insecure Direct Object Reference |
| **CSRF** | Cross-Site Request Forgery |
| **XSS** | Cross-Site Scripting |
| **mTLS** | Mutual TLS — both sides present certificates |
| **Scope** | A permission attached to an OAuth access token |
| **Claim** | A key-value assertion inside a JWT payload |