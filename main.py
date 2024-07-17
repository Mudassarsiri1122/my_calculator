
from addition import addition
from substraction import subtract
from multiplication import Multiply
from division import division

def display_menu():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")


# Main function
def main():
    try:

        display_menu()

        choice = input("Enter choice (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter the first number:"))
            num2 = float(input("Enter the second number:"))


            if choice == '1':
                print(f"{num1} + {num2} = {addition(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {Multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {division(num1, num2)}")
            else:
                print("Invalid input. Please enter 1, 2, 3, or 4.")


    except Exception as e:
        print(f"An error occured: {e}.")

    quit = input("Do you want to quit ? (Y/N):")

    if quit == "N":
        main()

    elif quit == "Y":
        print("Thanks!")

main()