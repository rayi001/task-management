# TaskSphere API Documentation

## Authentication Endpoints

### POST /api/auth/register/
**Description**: Register a new user account

**Request Body**:
```json
{
    "username": "testuser",
    "email": "test@example.com",
    "password": "securepassword123",
    "password_confirm": "securepassword123"
}
```

**Response (201 Created)**:
```json
{
    "user": {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com",
        "first_name": "",
        "last_name": ""
    },
    "tokens": {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
    }
}
```

**Error Response (400 Bad Request)**:
```json
{
    "password": ["Passwords don't match"]
}
```

---

### POST /api/auth/login/
**Description**: Login and get JWT tokens

**Request Body**:
```json
{
    "username": "testuser",
    "password": "securepassword123"
}
```

**Response (200 OK)**:
```json
{
    "user": {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com",
        "first_name": "",
        "last_name": ""
    },
    "tokens": {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
    }
}
```

**Error Response (400 Bad Request)**:
```json
{
    "non_field_errors": ["Invalid credentials"]
}
```

---

### GET /api/auth/profile/
**Description**: Get current user profile (requires authentication)

**Headers**: `Authorization: Bearer <access_token>`

**Response (200 OK)**:
```json
{
    "id": 1,
    "username": "testuser",
    "email": "test@example.com",
    "first_name": "",
    "last_name": ""
}
```

**Error Response (401 Unauthorized)**:
```json
{
    "detail": "Authentication credentials were not provided."
}
```

---

### POST /api/auth/refresh/
**Description**: Refresh JWT access token

**Request Body**:
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

**Response (200 OK)**:
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

---

## Usage Examples

### Register a new user:
```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "newuser",
    "email": "newuser@example.com",
    "password": "password123",
    "password_confirm": "password123"
  }'
```

### Login:
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "newuser",
    "password": "password123"
  }'
```

### Get profile (with token):
```bash
curl -X GET http://localhost:8000/api/auth/profile/ \
  -H "Authorization: Bearer <your_access_token>"
```

---

## Notes

- All timestamps are in UTC
- Access tokens expire after 60 minutes
- Refresh tokens expire after 7 days
- Passwords must be at least 8 characters long
- Username and email must be unique
