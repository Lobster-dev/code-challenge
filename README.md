# Accounts API

Implementation of the **EBANX Software Engineer Take-home assignment**.  
This API supports deposits, withdrawals, transfers, and balance queries, keeping state in memory (no persistence required).

---

## 🚀 Tech Stack

- [Python 3.11+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/) — web framework
- [Uvicorn](https://www.uvicorn.org/) — ASGI server
- [Pydantic](https://docs.pydantic.dev/) — data validation

---
## 📂 Project Structure

```plaintext
accounts_api/
├─ app/
│  ├─ __init__.py
│  ├─ main.py                # Application entrypoint
│  ├─ api/
│  │  ├─ __init__.py
│  │  └─ endpoints.py        # API endpoints
│  ├─ domain/
│  │  ├─ __init__.py
│  │  ├─ models.py           # Pydantic models (I/O schemas)
│  │  └─ services.py         # Business logic (deposit, withdraw, transfer)
│  ├─ infra/
│  │  ├─ __init__.py
│  │  └─ storage.py          # In-memory store (thread-safe)
├─ requirements.txt
└─ README.md
```


## ▶️ Running the project

### 1. Clone the repository
```bash
git clone https://github.com/your-username/accounts_api.git
cd accounts_api
```

### 2. Create a virtual environment
```shell
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```shell
pip install -r requirements.txt
```

### 4. Start the server
```shell
uvicorn app.main:app --reload  # Uvicorn
fastapi dev .\app\main.py      # FastApi CLI 
```