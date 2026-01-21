# 💰 LedgerFlow — Expense Tracker Backend

A **production-grade Django REST backend** for personal expense tracking with secure JWT authentication, structured categorization, and analytics-ready design.

Built with **clean service-layer architecture** and designed for future AI and automation integrations.

---

## 🚀 Key Features

### 🔐 Authentication & Security
- JWT-based authentication (access & refresh tokens)
- Stateless API design
- User-scoped data access (no cross-user leakage)
- Object-level permission checks enforced in service layer

---

### 🗂 Hybrid Category System
- System-defined **base categories** (FOOD, TRANSPORT, BILLS, etc.)
- Seeded via **data migrations** (environment-safe)
- User-defined subcategories mapped to base categories
- Stable **category-code based design** (analytics & AI friendly)

---

### 💰 Expense Management
- Create, update, delete, and list expenses
- Strict business validation:
  - Positive amounts only
  - Active base categories
  - User ownership checks
- Optional user categories
- Date-based expense tracking

---

### 🧠 Service-Layer Architecture
- No business logic in views or models
- Centralized reusable services for:
  - Expense creation
  - Updates & deletion
  - Querying & filtering
- Enables reuse across APIs, analytics, AI ingestion, and automation

---

### 📊 Analytics & Reporting
- Built using **Pandas + NumPy**
- Provides:
  - Total spending
  - Category-wise aggregation
  - Average & largest transaction
  - Spending standard deviation
- User-scoped, graph-ready JSON output
- Designed for easy extension (monthly trends, exports)

---

## 🛠️ Tech Stack
- **Backend:** Django, Django REST Framework
- **Auth:** SimpleJWT
- **Database:** PostgreSQL
- **Analytics:** Pandas, NumPy
- **Version Control:** Git, GitHub

---

## 🔗 API Endpoints
- /api/auth/
- /api/categories/
- /api/expenses/
- /api/analytics/

All endpoints are **JWT-protected by default**.

---

## ⚙️ Setup

- git clone https://github.com/<your-username>/ledgerflow-backend.git
- cd ledgerflow-backend

- python -m venv venv
- venv\Scripts\activate

- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver
