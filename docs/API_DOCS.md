# API Documentation - Roadmap AI Tools

## Base URL

- **Development:** `http://localhost:5000`
- **Production:** `https://api.roadmapaitools.com`

## Authentication

All protected endpoints require JWT token:

```
Authorization: Bearer <token>
```

## Response Format

```json
{
  "status": "success",
  "data": {},
  "message": "Operation successful"
}
```

---

## Authentication Endpoints

### Register User

**POST** `/api/auth/register`

**Request:**
```json
{
  "email": "user@example.com",
  "password": "password123",
  "username": "username",
  "full_name": "John Doe"
}
```

### Login

**POST** `/api/auth/login`

**Request:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

### Google OAuth

**POST** `/api/auth/google`

**Request:**
```json
{
  "token": "google_id_token"
}
```

### Refresh Token

**POST** `/api/auth/refresh`

Requires: Authorization header

---

## Tools Endpoints

### Get All Tools

**GET** `/api/tools?page=1&limit=20&category=writing`

**Query Parameters:**
- `page` (int): Page number (default: 1)
- `limit` (int): Items per page (default: 20)
- `category` (string): Filter by category
- `search` (string): Search query

### Get Tool by ID

**GET** `/api/tools/:id`

### Get Tools by Category

**GET** `/api/tools/category/:category`

### Create Tool (Admin)

**POST** `/api/tools`

Requires: Admin authorization

### Update Tool (Admin)

**PUT** `/api/tools/:id`

Requires: Admin authorization

### Delete Tool (Admin)

**DELETE** `/api/tools/:id`

Requires: Admin authorization

---

## Blog Endpoints

### Get All Blog Posts

**GET** `/api/blog?page=1&limit=10`

### Get Blog Post

**GET** `/api/blog/:slug`

### Create Blog Post (Admin)

**POST** `/api/blog`

Requires: Admin authorization

### Update Blog Post (Admin)

**PUT** `/api/blog/:id`

Requires: Admin authorization

### Delete Blog Post (Admin)

**DELETE** `/api/blog/:id`

Requires: Admin authorization

---

## File Conversion Endpoints

### Convert PDF to Word

**POST** `/api/convert/pdf-to-word`

Form Data: `file` (PDF file)

### Convert Word to PDF

**POST** `/api/convert/word-to-pdf`

### Convert JPG to PNG

**POST** `/api/convert/jpg-to-png`

### Convert PNG to JPG

**POST** `/api/convert/png-to-jpg`

### Compress Image

**POST** `/api/convert/compress-image`

### Compress PDF

**POST** `/api/convert/compress-pdf`

### Merge PDF

**POST** `/api/convert/merge-pdf`

### Split PDF

**POST** `/api/convert/split-pdf`

### Extract Text (OCR)

**POST** `/api/convert/extract-text`

---

## User Dashboard Endpoints

### Get User Profile

**GET** `/api/user/profile`

Requires: Authorization

### Update User Profile

**PUT** `/api/user/profile`

Requires: Authorization

### Get Conversion History

**GET** `/api/user/history?page=1&limit=20`

Requires: Authorization

### Get Favorite Tools

**GET** `/api/user/favorites`

Requires: Authorization

### Add Favorite Tool

**POST** `/api/user/favorites/:tool_id`

Requires: Authorization

### Remove Favorite Tool

**DELETE** `/api/user/favorites/:tool_id`

Requires: Authorization

---

## Admin Endpoints

### Get Analytics

**GET** `/api/admin/analytics`

Requires: Admin authorization

### Get All Users

**GET** `/api/admin/users?page=1&limit=50`

Requires: Admin authorization

### Get All Uploads

**GET** `/api/admin/uploads?page=1&limit=50`

Requires: Admin authorization

---

## Error Responses

### 400 Bad Request
```json
{
  "status": "error",
  "message": "Invalid input"
}
```

### 401 Unauthorized
```json
{
  "status": "error",
  "message": "Unauthorized access"
}
```

### 404 Not Found
```json
{
  "status": "error",
  "message": "Resource not found"
}
```

### 500 Server Error
```json
{
  "status": "error",
  "message": "Internal server error"
}
```

---

## Rate Limiting

- **Default:** 100 requests per hour per IP
- **API:** 1000 requests per hour per API key

Limits returned in headers:
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1609459200
```

---

## Pagination

**Query Parameters:**
- `page` (int): Page number (default: 1)
- `limit` (int): Items per page (default: 20, max: 100)
