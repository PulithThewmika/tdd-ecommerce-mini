# 🧪 TDD E-Commerce Mini System

Welcome to the **TDD E-Commerce Mini System**, a practical demonstration of Test-Driven Development (TDD) principles applied to building a robust, fully-tested e-commerce backend in Python.

This project was built step-by-step using the classic **Red → Green → Refactor** cycle, emphasizing not just basic unit testing, but advanced testing techniques to ensure real-world system reliability.

## 🚀 Key Features
- **Product & Catalog Management**: Centralized catalog referencing for item pricing and validation.
- **Shopping Cart**: Fully encapsulated cart logic (add/remove items, gross totals, inventory bounds checking).
- **Discount Engine**: A scalable rules engine capable of applying tiered discounts (e.g., 10% off bulk items, 5% off large orders).
- **Concurrency-Safe Inventory**: Thread-safe inventory reservation utilizing Python locks, preventing race conditions from simultaneous buyers.
- **Checkout & Payment Processing**: Facade integration with payment gateways, handling success/failure states seamlessly.
- **Order Persistence**: Order history system using the Repository pattern, backed by SQLite.

## 🛠️ Tech Stack & Methodologies
- **Python 3.13+**
- **Pytest**: The core testing framework used for all test running and assertions.
- **Hypothesis**: Used for **Property-Based Testing** (e.g., ensuring cart totals are always mathematically sound regardless of randomized inputs).
- **Integration Tests**: End-to-end flows validating system cohesion using an in-memory SQLite database (`:memory:`).
- **Concurrency Testing**: Specifically simulating thousands of multi-threaded requests battling for limited inventory to guarantee thread safety.
- **CI/CD**: Fully automated testing set up via **GitHub Actions** to prevent regressions on pull requests.

## 📁 Project Structure
```text
tdd-ecommerce-mini/
├── .github/workflows/       # CI/CD Pipelines
├── src/                     # Core Business Logic
│   ├── cart.py              # Shopping cart and validations
│   ├── catalog.py           # Product catalog definitions
│   ├── checkout.py          # Payment processing and order creation
│   ├── discount.py          # Discount engine and extensible rules
│   ├── inventory.py         # Thread-safe inventory management
│   ├── order_repository.py  # SQLite database implementation
│   └── order.py             # Order models
├── tests/                   # Pytest Test Suite
│   ├── test_cart.py
│   ├── test_cart_properties.py    # Hypothesis property tests
│   ├── test_checkout.py           
│   ├── test_discount.py
│   ├── test_integration.py        # SQLite E2E tests
│   ├── test_inventory.py
│   ├── test_inventory_concurrency.py # Multi-threaded tests
│   └── test_order_history.py
```

## 🏁 Getting Started

### 1. Setup the Environment
Create and activate a virtual environment, then install dependencies:
```bash
python -m venv .venv

# On Windows:
.\.venv\Scripts\Activate.ps1
# On macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

### 2. Run the Test Suite
Because the test files live outside the `src` directory, you should execute pytest as a module. This ensures the environment paths load correctly:
```bash
python -m pytest
```

To see detailed outputs and standard prints, run:
```bash
python -m pytest -v
```

## 🛡️ TDD Philosophy
Every feature in this repository was built using the following methodology:
1. **RED**: Write a failing test expecting a specific capability or checking an edge case.
2. **GREEN**: Write the minimal amount of code necessary to make the test pass.
3. **REFACTOR**: Improve the structure, encapsulation, and design of the code without breaking the tests.
