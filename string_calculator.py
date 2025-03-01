import re

def add(numbers: str) -> int:
    
    if not numbers:
        return 0
    
    delimeter = ","
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimeter = parts[0][2:]
        numbers = parts[1]
    
    numbers = re.split(f"[{delimeter}\n]", numbers)
    numbers = list(map(int,numbers))

    negatives = [num for num in numbers if num < 0]

    if negatives:
        raise ValueError(f"Negative numbers not allowed: {', '.join(map(str,negatives))}")
    
    return sum(numbers)

