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
    
    return sum(map(int, numbers))

