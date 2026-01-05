# 🏭 Warehouse Inventory Management API

A specialized Django REST Framework service for calculating raw material requirements based on product specifications and real-time warehouse stock using a virtual FIFO (First In, First Out) logic.

## 📖 Overview

This project solves the "Production-Inventory" problem. It calculates which material batches should be used to manufacture a specific quantity of products, tracking remaining stock across multiple warehouse entries and identifying shortages.

## ✨ Key Features

* **Automated Material Calculation:** Automatically explodes a product into its required components.
* **Virtual FIFO Logic:** Allocates materials starting from the oldest batches (lowest ID) without redundant database writes during calculation.
* **Shortage Detection:** Clearly identifies materials that are out of stock or insufficient for the requested production volume.
* **Service-Oriented Architecture:** Business logic is decoupled from views for better maintainability.

## 🚀 Quick Start

### 1. Installation

```bash
git clone <repo_url>
cd warehouse-production-api

# Setup environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install django djangorestframework

```

### 2. Database Setup

```bash
python manage.py migrate

```

### 3. Running the Service

```bash
python manage.py runserver

```

## 🔌 API Usage

### Calculate Materials

**Endpoint:** `POST /api/v1/calculate/`

**Request Example:**

```json
[
    {
        "product_code": "000001",
        "quantity": 10
    }
]

```

**Response Example:**

```json
{
    "result": [
        {
            "product_name": "T-Shirt",
            "product_qty": 10,
            "product_materials": [
                {
                    "warehouse_id": 1,
                    "material_name": "Cotton",
                    "qty": 15.5,
                    "price": 500
                },
                {
                    "warehouse_id": null,
                    "material_name": "Buttons",
                    "qty": 5.0,
                    "price": null
                }
            ]
        }
    ]
}

```

## 🛠 Tech Stack

* **Python 3.10+**
* **Django 4.2+**
* **Django REST Framework**
* **Database:** SQLite (default) / PostgreSQL compatible

## 📂 Project Structure

* `models.py` — Database schema for Products, Materials, and Warehouse batches.
* `services.py` — Core algorithm for FIFO material allocation and calculations.
* `views.py` — API endpoints and request validation.

## 📄 License

This project is licensed under the MIT License.

---
