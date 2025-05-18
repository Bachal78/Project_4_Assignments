
def main():
    fahrenheit_Value:float= float(input("Enter the temperature in Fahrenheit:"))
    celsius: float = (fahrenheit_Value - 32) * 5.0/9.0
    print(f"the Fahrenet temperature {fahrenheit_Value} in celsius is {celsius:}C")

if __name__ == "__main__":
    main()