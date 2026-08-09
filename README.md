# Python Utilities
A collection of small Python utilities created to practice core Python concepts and solve practical programming tasks.

## Projects

### 1. Days From Today
Calculates the number of days between a given date and the current date. The program accepts dates in YYYY-MM-DD format (ISO 8601), supports both past and future dates, and handles invalid input.

**Concepts used:** `datetime`, functions, type hints, exception handling, date parsing, input validation

### 2. Lottery Number Generator
Generates a sorted list of unique random numbers within a specified range. The program validates input parameters, prevents duplicate numbers, and handles invalid input.

**Concepts used:** `sample()`, functions, type hints, exception handling, input validation, conditional logic, lists, sorting

### 3. Phone Number Normalizer
Developed as a programming task to normalize Ukrainian phone numbers entered in different formats. The program removes unnecessary characters, handles different number prefixes, and converts numbers to a consistent international format beginning with `+380`. The normalization logic can be adapted to support phone number formats from other countries.

**Concepts used:** `re` module (regular expressions), functions, type hints, string processing, conditional logic, input normalization, list comprehensions

## Technologies & Skills
- **Language:** Python
- **Standard Library:** `datetime`, `random`, `re`
- **Core Python:** functions, type hints, conditional logic, lists, list comprehensions
- **Validation & Error Handling:** exception handling, input validation
- **Data Processing:** string processing, date parsing, data normalization
- **Additional Techniques:** regular expressions, random sampling, sorting

## How to Run

Make sure Python 3 is installed on your system.

### Option 1: Download a single script

If you only want to use one program, open the corresponding `.py` file on GitHub and download the file.

### Option 2: Clone the entire repository

Make sure Git is installed on your system.

Open a terminal (Terminal on macOS, PowerShell or Command Prompt on Windows) and clone the repository:

```bash
git clone https://github.com/DariaTelehina/python-utilities.git
```

Navigate to the project directory:

```bash
cd python-utilities
```

Choose one of the scripts to run:

**Days From Today**
```bash
python days_from_today.py
```

**Lottery Number Generator**
```bash
python lottery_number_generator.py
```

**Phone Number Normalizer**
```bash
python phone_number_normalizer.py
```

> **Note:** On some systems, you may need to use `python3` instead of `python`.

No external dependencies are required. All scripts use Python's standard library.

## Project Structure

```text
python-utilities/
├── days_from_today.py
├── lottery_number_generator.py
├── phone_number_normalizer.py
└── README.md

