# CodeVenture Backend

## Description
CodeVenture is a software developed to teach young kids how to code Python by providing multiple types learning content such as quizzes and tutorials, a progress checker, and gamification elements. This repository houses the backend of the system, developed using Flask and Firebase.

Developed as part of an assignment from FIT1056: Collaborative Engineering for Web Applications in Monash University.

## 👥 Team Members
- Chee Min Hao
- Christine Chiong
- Ong Kai Yun
- Ashley Yow

## 🎮 What This Project Does
- Implements data models and CRUD-like operations for tutorials, quizzes, learning modules, and users.
- Provides a small test suite under the `testing/` folder to validate module behaviour.
- Includes a `main.py` entry point for manual runs and quick exploration.

## 🛠️ Tech Stack
- Python 3.x
- pytest for tests
- Plain file-based modules under the `database/` package

## 📋 Prerequisites
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