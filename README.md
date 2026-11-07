# Password Generator

A simple command-line password generator written in Python. It builds a random password from letters, digits, and special symbols using Python's `secrets` module, which is designed for security-sensitive randomness.

## Features

- Cryptographically secure randomness (`secrets`, not `random`)
- Minimum password length of 16 characters
- Uses uppercase, lowercase, digits, and symbols
- Custom exception (`PasswordError`) for passwords that are too short
- Handles invalid input (for example, typing letters instead of a number)

## Requirements

- Python 3.6 or higher (the `secrets` module was added in 3.6)
- No external libraries needed

## How to Run

```bash
python Password_generator.py
```

Then enter the length you want when prompted.

## Example

```
Enter length of password: 20
Password is: k7#Pq2Zr!mW9xT_vB4aL
```

Short lengths and invalid input show an error:

```
Enter length of password: 5
Error: Password length must be at least 16

Enter length of password: abc
Error: please enter a number
```

## How It Works

1. The program asks for a password length.
2. It raises `PasswordError` if the length is below 16.
3. It picks one random character from the pool (`a-z`, `A-Z`, `0-9`, and `!@#$%&*()_-=+`) for each position using `secrets.choice()`.
4. It joins the characters and prints the password.

## Concepts Used

- `secrets` and `string` modules
- Custom exceptions
- `try` / `except` error handling
- Generator expressions with `str.join()`

## Possible Improvements

- Guarantee at least one character from each type (lowercase, uppercase, digit, symbol)
- Accept the length from the command line using `argparse`
- Add unit tests with `pytest`
- Copy the password to the clipboard

## License

This project is open source and available under the [MIT License](LICENSE).
