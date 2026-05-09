#!/usr/bin/env python3
"""
Simple Calculator Program
Performs basic arithmetic operations: addition, subtraction, multiplication, and division.
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def calculator():
    """Main calculator program"""
    print("=== Simple Calculator ===")
    print("Operations: +, -, *, /")
    print("Type 'quit' to exit\n")
    
    while True:
        try:
            user_input = input("Enter calculation (e.g., 5 + 3): ").strip()
            
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
            
            # Parse input
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid format. Please use: number operator number\n")
                continue
            
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])
            
            # Perform calculation
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print(f"Unknown operator: {operator}\n")
                continue
            
            print(f"Result: {result}\n")
        
        except ValueError:
            print("Error: Please enter valid numbers\n")
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    calculator()
