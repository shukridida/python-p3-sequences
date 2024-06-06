#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = []
    
    if length <= 0:
        print("[]")
    elif length == 1:
        print("[0]")
    elif length == 2:
        print("[0, 1]")
    else:
        fibonacci_sequence = [0, 1]
        for i in range(2, length):
            next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_term)
            
        print (fibonacci_sequence)


print_fibonacci(10) 