# Mini User & Project Management API

A small REST API built with FastAPI, SQLModel, and PostgreSQL.

## Run

Docker and Docker Compose are required. Start the API and database with:

```bash
docker-compose up
```

The API is available at http://localhost:8000. Interactive OpenAPI documentation is at http://localhost:8000/docs.

## Endpoint Examples

### Users

- `POST /users` creates a user.
- `GET /users/{id}` retrieves a user.
- `GET /users?limit=50&offset=0` lists users.
- `DELETE /users/{id}` deletes a user and its projects.

Create a user:

```bash
curl -X POST http://localhost:8000/users \
  -H 'Content-Type: application/json' \
  --data '{"name":"Ada Lovelace","email":"ada@example.com"}'
```

### Projects

- `POST /projects` creates a project for an existing user.
- `GET /projects/{id}` retrieves a project.
- `GET /users/{id}/projects` lists a user's projects.

Create a project:

```bash
curl -X POST http://localhost:8000/projects \
  -H 'Content-Type: application/json' \
  --data '{"name":"API design","description":"Initial API design","owner_id":1}'
```

## Assumptions

- A user has a required name and a unique, valid email address.
- A project has a required name, an optional description, and exactly one owner.
- Project creation requires an existing owner; otherwise the API returns `404 Not Found`.
- User pagination defaults to `limit=50` and `offset=0`; `limit` can be at most 100.
- Deleting a user removes all projects owned by that user through a database cascade.
- The database schema is created automatically when the API container starts.
