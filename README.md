# Student Management System API

A FastAPI-based REST API for managing student classes with proper project structure following FastAPI best practices.

## 🚀 Features

- **Classroom Management**: Create, read, update, and delete classrooms
- **RESTful API**: Follows REST conventions with proper HTTP status codes
- **Data Validation**: Pydantic schemas for request/response validation
- **Database Integration**: PostgreSQL with SQLAlchemy ORM
- **Auto Documentation**: Interactive API docs with Swagger UI
- **Error Handling**: Comprehensive error handling with proper HTTP exceptions
- **Project Structure**: Organized code following FastAPI best practices

## 📁 Project Structure

```
student/
├── config.py          # Centralized configuration management
├── database.py        # Database connection and session management
├── main.py           # FastAPI application and global endpoints
├── models.py         # SQLAlchemy database models
├── schemas.py        # Pydantic schemas for data validation
├── routers/          # API route organization
│   ├── __init__.py
│   └── classrooms.py # Classroom-related API endpoints
├── requirements.txt  # Python dependencies
└── README.md        # Project documentation
```

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- PostgreSQL database

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd student
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the root directory:
   ```env
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=student_db
   DB_USER=postgres
   DB_PASSWORD=your_password
   ```

5. **Database Setup**
   - Create a PostgreSQL database named `student_db`
   - The application will automatically create tables on first run

## 🏃‍♂️ Running the Application

### Development Mode
```bash
uvicorn main:app --reload
```

### Production Mode
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

The API will be available at:
- **API Base URL**: `http://localhost:8000`
- **Interactive Docs**: `http://localhost:8000/docs`
- **ReDoc Documentation**: `http://localhost:8000/redoc`

## 📚 API Endpoints

### Classroom Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/classrooms/` | Get all classrooms (with pagination) |
| `GET` | `/api/v1/classrooms/{id}` | Get specific classroom by ID |
| `POST` | `/api/v1/classrooms/` | Create a new classroom |
| `PUT` | `/api/v1/classrooms/{id}` | Update a classroom |
| `DELETE` | `/api/v1/classrooms/{id}` | Delete a classroom |

### Health Check
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Check API and database connectivity |

## 📝 API Usage Examples

### Create a Classroom
```bash
curl -X POST "http://localhost:8000/api/v1/classrooms/" \
     -H "Content-Type: application/json" \
     -d '{
       "class_name": "Mathematics 101",
       "class_teacher": "Dr. Smith"
     }'
```

### Get All Classrooms
```bash
curl -X GET "http://localhost:8000/api/v1/classrooms/"
```

### Get Specific Classroom
```bash
curl -X GET "http://localhost:8000/api/v1/classrooms/1"
```

### Update a Classroom
```bash
curl -X PUT "http://localhost:8000/api/v1/classrooms/1" \
     -H "Content-Type: application/json" \
     -d '{
       "class_name": "Advanced Mathematics 101",
       "class_teacher": "Dr. Johnson"
     }'
```

### Delete a Classroom
```bash
curl -X DELETE "http://localhost:8000/api/v1/classrooms/1"
```

## 🗄️ Database Schema

### Classrooms Table
| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | Integer | Primary Key, Auto-increment | Unique classroom identifier |
| `class_name` | String | Not Null, Indexed | Name of the classroom |
| `class_teacher` | String | Not Null | Teacher assigned to the classroom |

## 🔧 Configuration

The application uses a centralized configuration system in `config.py`:

- **Database Settings**: Connection parameters from environment variables
- **API Settings**: API versioning and project metadata
- **Environment Variables**: Secure configuration management

## 🧪 Testing

### Health Check
```bash
curl -X GET "http://localhost:8000/health"
```

Expected response:
```json
{
  "status": "healthy",
  "database": "connected",
  "message": "Database connection successful"
}
```

## 📋 Request/Response Schemas

### Classroom Creation Schema
```json
{
  "class_name": "string",
  "class_teacher": "string"
}
```

### Classroom Response Schema
```json
{
  "id": 1,
  "class_name": "string",
  "class_teacher": "string"
}
```

## 🚨 Error Handling

The API returns appropriate HTTP status codes:

- `200 OK`: Successful GET/PUT requests
- `201 Created`: Successful POST requests
- `204 No Content`: Successful DELETE requests
- `400 Bad Request`: Invalid request data
- `404 Not Found`: Resource not found
- `422 Unprocessable Entity`: Validation errors

## 🛡️ Best Practices Implemented

- **Separation of Concerns**: Models, schemas, and routes are properly separated
- **Dependency Injection**: Database sessions are properly managed
- **Data Validation**: Pydantic schemas ensure data integrity
- **Error Handling**: Comprehensive error responses
- **API Documentation**: Auto-generated interactive documentation
- **Configuration Management**: Environment-based configuration
- **Database Best Practices**: Proper ORM usage with SQLAlchemy

## 🔄 Development Workflow

1. **Add new models** in `models.py`
2. **Create schemas** in `schemas.py` for validation
3. **Implement routes** in `routers/` directory
4. **Update main.py** to include new routers
5. **Test endpoints** using the interactive docs at `/docs`

## 📦 Dependencies

- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **Pydantic**: Data validation using Python type annotations
- **PostgreSQL**: Relational database
- **Uvicorn**: ASGI server for running FastAPI applications

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.