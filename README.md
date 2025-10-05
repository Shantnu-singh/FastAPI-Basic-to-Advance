 ⚡ FastAPI — Basic to Advance

This repository is a **complete FastAPI learning series**, designed to take you from **building simple APIs** to **integrating ML models and deploying with Docker**.
Each file demonstrates a focused concept in FastAPI — from HTTP methods to path/query parameters, data validation, and model deployment.

---

## Table of Contents

| Lesson | Title                                                      | Description                                                   | Why This Is Important                                                                  |
| :----: | :--------------------------------------------------------- | :------------------------------------------------------------ | :------------------------------------------------------------------------------------- |
|  **1** | [hello_world_api.py](hello_world_api.py)                   | Your first FastAPI app — simple “Hello World” endpoint.       | Introduces the FastAPI syntax and basic server setup — the foundation for all APIs.    |
|  **2** | [GET_HTTP_Method.py](GET_HTTP_Method.py)                   | Demonstrates GET method usage for data retrieval.             | GET is the most common HTTP method — crucial for fetching data safely and efficiently. |
|  **3** | [POST_HTTP_Method.py](POST_HTTP_Method.py)                 | Shows how to use POST for sending data to the API.            | Enables creating and submitting data — core for building interactive web apps.         |
|  **4** | [PUT_DELETE_HTTP_Method.py](PUT_DELETE_HTTP_Method.py)     | Covers PUT (update) and DELETE (remove) methods.              | Essential for building full CRUD (Create, Read, Update, Delete) APIs.                  |
|  **5** | [Path_Parametrs.py](Path_Parametrs.py)                     | Demonstrates path parameters in API routes.                   | Dynamic routes make APIs flexible — key for identifying resources via URLs.            |
|  **6** | [Query_Parameters.py](Query_Parameters.py)                 | Explains query parameters and filtering data.                 | Query params allow flexible client requests and advanced search capabilities.          |
|  **7** | [Pydentic_Data_Validation.py](Pydentic_Data_Validation.py) | Data validation using Pydantic models.                        | Ensures data integrity and error handling — one of FastAPI’s strongest features.       |
|  **8** | [ML_Model_API.py](ML_Model_API.py)                         | Shows how to integrate a Machine Learning model with FastAPI. | Bridges ML and web — deploy your AI models as real-world APIs.                         |
|  **9** | [app.py](app.py)                                           | Main app combining endpoints and ML integration.              | Centralizes your FastAPI app — demonstrates a complete production-ready structure.     |
| **10** | [docker_basics.md](docker_basics.md)                       | Introduction to Docker and containerizing FastAPI apps.       | Deployment skill — Docker ensures consistent environments across systems.              |

---

## 🚀 How to Run the Project

### 🧩 1. Clone the Repository

```bash
git clone https://github.com/Shantnu-singh/FastAPI-Basic-to-Advance.git
cd fastapi-basic-to-advance
```

### ⚙️ 2. Install Dependencies

```bash
pip install -r requirements.txt
```


### ▶️ 3. Run Any Script

Example:

```bash
uvicorn hello_world_api:app --reload
```


Then visit: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 🧠 What You’ll Learn

* Fundamentals of FastAPI and RESTful design
* CRUD operations with HTTP methods (GET, POST, PUT, DELETE)
* Path and query parameter handling
* Data validation with **Pydantic models**
* Building and deploying **Machine Learning APIs**
* **Docker** for API containerization and deployment

---

## 💡 Author & Credits

**Author:** [Shantnu Singh](https://github.com/shantnu-singh)
**Repository:** [FastAPI Basic to Advance](https://github.com/Shantnu-singh/FastAPI-Basic-to-Advance)

If this project helped you, please ⭐ **star the repo** and share it with other FastAPI learners!
