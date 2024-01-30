print("Learn your squares and cubes!")
print()


def print_table(num):
    print(f"\n{'Number':<10}{'Square':<10}{'Cube':<10}")
    print("=" * 30)
    for i in range(1, num + 1):
        square = i ** 2
        cube = i ** 3
        print(f"{i:<10}{square:<10}{cube:<10}")

def main():
    while True:
        try:
            user_input = int(input("Enter an integer: "))
            print_table(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        print("Would you like to continue y/n? ")
        y_n = input(" > ")
        if y_n == "n":
            print("Thank you for playing! Have a nice day!")
            break
    print()



