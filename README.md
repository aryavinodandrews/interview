# Automation Interview

This project contains automated tests for given scenarios in question.

## Setup

### Prerequisites

- Python 3.x installed on your system ([Download Python](https://www.python.org/downloads/))

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/aryavinodandrews/interview.git
   cd interview
   ```

2. **Setup virtual environment:**

   It's recommended to use a virtual environment to manage dependencies locally.

   ```bash
   # On Windows
   python -m venv venv

   # On macOS/Linux
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**

   ```bash
   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

To run the tests, use pytest:

```bash
pytest
```

To run them individually:

```bash
pytest tests/test_login.py
```

## Notes

- Chrome engine is used in these tests, So ensure chrome is installed.
- Update `requirements.txt` with any additional dependencies as needed.
- Ensure your WebDriver is compatible with your browser version.
