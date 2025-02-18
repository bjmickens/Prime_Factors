from itertools import combinations
from tabulate import tabulate

def prime_factors(number):
    factors = []
    i = 2
    while i * i <= number:
        if number % i == 0:
            factors.append(i)
            number //= i
        else:
            i += 1
    if number > 1:
        factors.append(number)
    return factors


def power_set(numbers):
    numbers = list(numbers)
    power_set = [set()]
    for r in range(1, len(numbers) + 1):
        for combo in combinations(numbers, r):
            power_set.append(set(combo))
    return power_set


def print_power_set_info(p_set, original_set):
    print(f"\nPower set P(X) where X = {set(original_set)}:")
    for subset in p_set:
        if len(subset) == 0:
            print("∅", end=", ")
        else:
            print(subset, end=", ")
    print(f"\nTotal number of sets: 2^{len(original_set)} = {2 ** len(original_set)}")


def get_set_from_user():
    while True:
        try:
            numbers = input("Enter a set of numbers separated by spaces: ")
            return [int(x) for x in numbers.split()]
        except ValueError:
            print("Invalid input. Please enter a valid set of numbers.")


def print_factoring_chart(factors, input_number):
    p_set = power_set(factors)

    # Prepare headers
    headers = ["Subset"]
    headers.extend([f"Include {f}" for f in sorted(factors, reverse=True)])
    headers.append("Factorization")

    # Prepare table rows
    table_data = []
    for subset in sorted(p_set, key=lambda x: (len(x), x)):
        row = []

        # Add subset representation
        subset_str = "∅" if len(subset) == 0 else str(subset)
        row.append(subset_str)

        # Add X markers for included factors
        for factor in sorted(factors, reverse=True):
            row.append("X" if factor in subset else "")

        # Calculate and add factorization
        product = 1 if subset else 0
        for factor in subset:
            product *= factor
        other_factor = input_number // product if product != 0 else input_number
        row.append(f"{product} × {other_factor}")

        table_data.append(row)

    # Print the table
    print("\n" + tabulate(table_data, headers=headers, tablefmt="grid", stralign="center"))


def main():
    while True:
        print("\nMenu:")
        print("1. Find Prime Factors")
        print("2. Find Power Set")
        print("3. List All Factorings and Subsets")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            number = int(input("Enter a number: "))
            factors = prime_factors(number)
            print(f"Prime factors of {number}: {factors}")
        elif choice == "2":
            numbers = get_set_from_user()
            p_set = power_set(numbers)
            print_power_set_info(p_set, numbers)
        elif choice == "3":
            num = int(input("Enter a number: "))
            factors = prime_factors(num)
            print(f"Prime factors of {num}: {factors}")
            print_factoring_chart(factors, num)
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()