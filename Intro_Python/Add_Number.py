def main():
    print("Simple Calculator (+, -)")

    num1 = int(input("Enter first number: "))
    operator = input("Enter operation (+, - or *): ")
    num2 = int(input("Enter second number: "))

    if operator == '+':
        total = num1 + num2
        print(f"The sum is {total}")
    elif operator == '-':
        total = num1 - num2
        print(f"The difference is {total}")
    elif operator == '*':
        total = num1 * num2
        print(f"The product is {total}")
    else:
        print("Invalid operator. Please use + or -")

if __name__ == "__main__":
    main()
