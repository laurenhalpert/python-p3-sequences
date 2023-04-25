#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = []
    if length >0:
        fibonacci.append(0)
        if length >1:
            fibonacci.append(1)
            if length >2:
                for i in range(2, length):
                    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    print(fibonacci)
    pass