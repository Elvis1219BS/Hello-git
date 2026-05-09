#!/usr/bin/env python3
"""
Simple Calculator Program with GUI
Performs basic arithmetic operations: addition, subtraction, multiplication, and division.
Uses tkinter for graphical interface.
"""

import tkinter as tk
from tkinter import font as tkfont

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

class CalculatorApp:
    """GUI Calculator Application"""
    
    def __init__(self, root):
        """Initialize the calculator GUI"""
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        # Display screen
        self.display_var = tk.StringVar(value="0")
        self.display = tk.Entry(
            root,
            textvar=self.display_var,
            font=tkfont.Font(size=20),
            justify="right",
            state="readonly"
        )
        self.display.pack(fill=tk.BOTH, padx=10, pady=10, ipady=10)
        
        # Variables to store calculation
        self.first_num = None
        self.operator = None
        self.current_input = "0"
        self.operation_display = ""
        
        # Buttons frame
        buttons_frame = tk.Frame(root)
        buttons_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Button layout
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["AC", "DEL"]
        ]
        
        for row in buttons:
            row_frame = tk.Frame(buttons_frame)
            row_frame.pack(fill=tk.BOTH, expand=True, pady=5)
            
            for btn_text in row:
                if btn_text == "AC":
                    btn = tk.Button(
                        row_frame,
                        text=btn_text,
                        font=tkfont.Font(size=14, weight="bold"),
                        command=self.clear,
                        bg="#FF6B6B"
                    )
                    btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
                elif btn_text == "DEL":
                    btn = tk.Button(
                        row_frame,
                        text=btn_text,
                        font=tkfont.Font(size=14, weight="bold"),
                        command=self.delete_last,
                        bg="#FFA500"
                    )
                    btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
                elif btn_text in ["+", "-", "*", "/"]:
                    btn = tk.Button(
                        row_frame,
                        text=btn_text,
                        font=tkfont.Font(size=14, weight="bold"),
                        command=lambda op=btn_text: self.set_operator(op),
                        bg="#FFD93D"
                    )
                    btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
                elif btn_text == "=":
                    btn = tk.Button(
                        row_frame,
                        text=btn_text,
                        font=tkfont.Font(size=14, weight="bold"),
                        command=self.calculate,
                        bg="#6BCF7F"
                    )
                    btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
                else:
                    btn = tk.Button(
                        row_frame,
                        text=btn_text,
                        font=tkfont.Font(size=14),
                        command=lambda num=btn_text: self.append_number(num)
                    )
                    btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
    
    def append_number(self, num):
        """Append number to display"""
        if self.current_input == "0":
            self.current_input = num
        else:
            self.current_input += num
        self.update_display()
    
    def update_display(self):
        """Update the display with operation or current input"""
        if self.operator:
            self.display_var.set(f"{self.first_num} {self.operator} {self.current_input}")
        else:
            self.display_var.set(self.current_input)
    
    def set_operator(self, op):
        """Set operator and store first number"""
        try:
            self.first_num = float(self.current_input)
            self.operator = op
            self.current_input = "0"
            self.update_display()
        except ValueError:
            self.display_var.set("Error")
    
    def calculate(self):
        """Calculate result"""
        try:
            if self.first_num is None or self.operator is None:
                return
            
            second_num = float(self.current_input)
            
            if self.operator == "+":
                result = add(self.first_num, second_num)
            elif self.operator == "-":
                result = subtract(self.first_num, second_num)
            elif self.operator == "*":
                result = multiply(self.first_num, second_num)
            elif self.operator == "/":
                result = divide(self.first_num, second_num)
            
            # Show only the result
            self.current_input = str(result)
            self.display_var.set(self.current_input)
            # Keep the result for chained operations
            self.first_num = result
            self.operator = None
        
        except ValueError:
            self.display_var.set("Error")
        except Exception as e:
            self.display_var.set("Error")
    
    def clear(self):
        """Clear calculator"""
        self.current_input = "0"
        self.display_var.set("0")
        self.first_num = None
        self.operator = None
    
    def delete_last(self):
        """Delete last character"""
        if len(self.current_input) > 1:
            self.current_input = self.current_input[:-1]
        else:
            self.current_input = "0"
        self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
