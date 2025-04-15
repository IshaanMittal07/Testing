import math

def count_sig_figs(number_str):
    number_str = number_str.strip().lower()

    # Handle scientific notation
    if 'e' in number_str:
        coefficient = number_str.split('e')[0]
        return count_sig_figs(coefficient)

    # Remove leading minus sign or plus
    if number_str.startswith(('-', '+')):
        number_str = number_str[1:]

    if '.' in number_str:
        # Decimal numbers
        number_str = number_str.lstrip('0')
        if not number_str:
            return 0
        return len([char for char in number_str if char.isdigit()])
    else:
        # Whole numbers
        number_str = number_str.rstrip('0')
        number_str = number_str.lstrip('0')
        return len(number_str)

def round_sig_figs(num, sig_figs):
    if num == 0:
        return 0
    else:
        return round(num, sig_figs - int(math.floor(math.log10(abs(num)))) - 1)

# Example usage
while True:
    print("\n--- Significant Figures Calculator ---")
    print("1. Count significant figures")
    print("2. Round to significant figures")
    print("3. Exit")
    choice = input("Choose an option (1/2/3): ")

    if choice == '1':
        num_str = input("Enter a number: ")
        sig_figs = count_sig_figs(num_str)
        print(f"Significant figures: {sig_figs}")

    elif choice == '2':
        try:
            num = float(input("Enter a number: "))
            sig = int(input("Round to how many significant figures? "))
            rounded = round_sig_figs(num, sig)
            print(f"Rounded number: {rounded}")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    elif choice == '3':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
