# FIT1056 Code Venture 2.0

## Description

CodeVenture is a backend project for FIT1056 that provides simple data models and CRUD operations for learning content, quizzes, tutorials, and users. It includes test coverage for core modules and is intended as an educational codebase.

👥 Team Members
- Chee Min Hao
- Christine Chiong
- Ong Kai Yun
- Ashley Yow

🎮 What This Project Does
- Implements data models and CRUD-like operations for tutorials, quizzes, learning modules, and users.
- Provides a small test suite under the `testing/` folder to validate module behaviour.
- Includes a `main.py` entry point for manual runs and quick exploration.

🛠️ Tech Stack
- Python 3.x
- pytest for tests
- Plain file-based modules under the `database/` package

📋 Prerequisites
1. Python 3.8+ installed
2. Create and activate a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

🚀 Usage

- Run the app (quick manual run):

```bash
python3 main.py
```

- Run the full test suite:

```bash
pytest testing
```

- Run a single test module:

```bash
pytest testing/test_user.py
```

For development, ensure your virtual environment is active and dependencies are installed before running the commands above.