def safe_divide(numerator, denominator):
    # Handle non-numeric inputs
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    # Handle division by zero
    try:
        result = num / den
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
