

import string
import secrets


def generate_password(length, use_lower, use_upper, use_digits, use_symbols):

    characters = ""
    password = []

    if use_lower:
        characters += string.ascii_lowercase
        password.append(secrets.choice(string.ascii_lowercase))

    if use_upper:
        characters += string.ascii_uppercase
        password.append(secrets.choice(string.ascii_uppercase))

    if use_digits:
        characters += string.digits
        password.append(secrets.choice(string.digits))

    if use_symbols:
        characters += string.punctuation
        password.append(secrets.choice(string.punctuation))

    for i in range(length - len(password)):
        password.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password)

    return "".join(password)


def main():

    print("\n========== PASSWORD GENERATOR ==========")

    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("Password length must be greater than zero.")
            return

        print("\nSelect password complexity:")
        print("1. Lowercase letters")
        print("2. Uppercase letters")
        print("3. Numbers")
        print("4. Special characters")

        lower = input("Include lowercase letters? (y/n): ").lower()
        upper = input("Include uppercase letters? (y/n): ").lower()
        digits = input("Include numbers? (y/n): ").lower()
        symbols = input("Include special characters? (y/n): ").lower()

        choices = [lower, upper, digits, symbols]

        if any(choice not in ["y", "n"] for choice in choices):
            print("Invalid input! Please enter y or n.")
            return

        use_lower = lower == "y"
        use_upper = upper == "y"
        use_digits = digits == "y"
        use_symbols = symbols == "y"

        selected = sum([use_lower, use_upper, use_digits, use_symbols])

        if selected == 0:
            print("Please select at least one character type.")
            return

        if length < selected:
            print("Password length must be at least", selected)
            print("to include all selected character types.")
            return

        password = generate_password(
            length, use_lower, use_upper, use_digits, use_symbols
        )

        print("\nGenerated Password:", password)
        print("Password length:", len(password))

    except ValueError:
        print("Invalid input! Please enter a valid whole number.")


if __name__ == "__main__":
    main()

