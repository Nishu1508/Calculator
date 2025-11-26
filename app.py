#!/usr/bin/env python3
import argparse
import sys

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

def main():
    parser = argparse.ArgumentParser(description="Simple Calculator CLI")
    parser.add_argument("op", choices=["add","sub","mul","div"], help="operation")
    parser.add_argument("a", type=float, help="first number")
    parser.add_argument("b", type=float, help="second number")
    args = parser.parse_args()

    try:
        if args.op == "add":
            print(add(args.a, args.b))
        elif args.op == "sub":
            print(sub(args.a, args.b))
        elif args.op == "mul":
            print(mul(args.a, args.b))
        elif args.op == "div":
            print(div(args.a, args.b))
    except Exception as e:
        print("Error:", e, file=sys.stderr)
        sys.exit(2)

if __name__ == "__main__":
    main()
