# Simple Python Calculator

First homework from the Academy: a command-line calculator written in Python, kept here as a record of learning progress.

## Versions

| File | What it is |
|---|---|
| `Georgi's calculator.py` | The original homework. Four operations (add, subtract, divide, multiply), menu text transliterated to Latin letters. |
| `Calculator_functionality_upgrade.py` | The improved version. Separate functions with docstrings, plus square root and power. |

## Features of the upgraded version

- Addition, subtraction, multiplication, division (division by zero returns a message instead of crashing)
- Square root and power
- Menu-driven input, with an `__main__` guard so the functions can be imported

**Not finished:** option 7 (solving linear systems) is a placeholder. `solve_linear_system` is a stub and the menu only prints a message.

## Run

Requires Python 3.8 or newer. No dependencies.

```bash
python Calculator_functionality_upgrade.py
```

Example session:

```text
Enter first number: 12
Enter second number: 4
Select operation:
1. Add
...
Enter choice (1/2/3/4/5/6/7): 4
Result: 3.0
```

## Known limitations

- Non-numeric input raises a `ValueError`; there is no input validation yet.
- Square root of a negative number raises a `ValueError`.
- The original script divides without a zero check.

## Possible next steps

- Validate input with `try`/`except`
- Implement `solve_linear_system` (Gaussian elimination)
- Add unit tests for the functions

## License

No license file yet. Add one (for example MIT) before reusing the code.
