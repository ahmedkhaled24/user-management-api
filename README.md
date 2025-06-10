
# 🧑‍💻 User Management API

A simple FastAPI-based RESTful API for managing users with MongoDB as the backend database.

---

## 🚀 Features

- Create new users
- Retrieve all users
- Retrieve a user by ID
- Retrieve users by name
- Update user data
- Delete user by ID

---

## 🛠️ Technologies Used

- **FastAPI** 🚀 - Python web framework for building APIs quickly
- **MongoDB** 🍃 - NoSQL database
- **Motor** 🔌 - Async MongoDB driver for Python
- **Pydantic** ✅ - Data validation
- **Uvicorn** ⚡ - ASGI server

---

## 📂 Project Structure

```
user_api/
├── main.py            # FastAPI app setup
├── database.py        # MongoDB connection
├── models.py          # Pydantic models
├── routes/
│   └── user_router.py # API endpoints
├── requirements.txt
└── README.md
```

---

## ⚙️ How to Run Locally

### 1. 🐍 Create virtual environment and activate it

```bash
python -m venv venv
# For Linux/macOS
source venv/bin/activate
# For Windows
venv\Scripts\activate
```

### 2. 📦 Install dependencies

```bash
pip install -r requirements.txt
```

### 3. 🔧 Set up MongoDB

Make sure MongoDB is running locally on:  
`mongodb://localhost:27017`

You can change the URI by using a `.env` file (optional).

### 4. 🚀 Start the server

```bash
uvicorn main:app --reload
```

---

## 📬 API Endpoints

| Method | Endpoint               | Description         |
|--------|------------------------|---------------------|
| POST   | /user                  | Create a new user   |
| GET    | /users                 | Get all users       |
| GET    | /user/{id}             | Get user by ID      |
| GET    | /userByName/{name}     | Get users by name   |
| PUT    | /user/{id}             | Update user         |
| DELETE | /user/{id}             | Delete user by ID   |

---

## 📘 Example JSON for User

```json
{
  "name": "Ahmed Khaled",
  "email": "ahmed@example.com",
  "age": 25
}
```

---

## 🔒 Note

Do not push sensitive information (like MongoDB URI with credentials) to GitHub. Use `.env` and add it to `.gitignore`.

---

## 🤝 Contributing

Feel free to fork, raise issues, or submit pull requests.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🧑‍💻 Developed by

Ahmed Khaled
