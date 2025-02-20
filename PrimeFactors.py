from itertools import combinations  # Handles mathematical combination operations
from tabulate import tabulate      # Creates well-formatted, readable tables

def prime_factors(number):
    """Returns a list of prime factors for any given number.
    Note: The factors are returned in ascending order."""
    factors = []
    divisor = 2
    # Search optimization: check factors only up to sqrt(number)
    # This significantly reduces computation time for large numbers
    while divisor ** 2 <= number:
        if number % divisor == 0:
            factors.append(divisor)      # Store each discovered prime factor
            number //= divisor          # Divide out the found prime factor
        else:
            divisor += 1               # Move to next potential factor
    # Include any remaining prime factor greater than 1
    if number > 1:
        factors.append(number)
    return factors

def power_set(numbers):
    """Generates the power set (set of all possible subsets) from a given set.
    Example: Input [1,2] yields [[], [1], [2], [1,2]]"""
    numbers = list(numbers)
    power_set = [set()]  # Initialize with empty set - a fundamental subset
    # Generate subsets of increasing size, from 1 element to full set
    for r in range(1, len(numbers) + 1):
        for combo in combinations(numbers, r):
            power_set.append(set(combo))
    return power_set

def print_power_set_info(p_set, original_set):
    """Displays the complete power set and calculates total number of subsets."""
    print(f"\nPower set P(X) where X = {set(original_set)}:")
    for subset in p_set:
        if len(subset) == 0:
            print("∅", end=", ")  # Empty set representation
        else:
            print(subset, end=", ")
    # Calculate total sets using the power set formula: 2^n
    print(f"\nTotal number of sets: 2^{len(original_set)} = {2 ** len(original_set)}")

def get_set_from_user():
    """Collects and validates user input for a set of numbers.
    Returns a list of integers from space-separated input."""
    while True:
        try:
            numbers = input("Enter a set of numbers separated by spaces: ")
            return [int(x) for x in numbers.split()]
        except ValueError:
            print("Invalid input. Please enter a valid set of numbers.")

def print_factoring_chart(factors, input_number):
    """Creates a formatted table showing all possible factorings and their relationships.
    Displays subsets, factor inclusion, and corresponding factorizations."""
    p_set = power_set(factors)

    # Define table structure
    headers = ["Subset"]
    headers.extend([f"Include {f}" for f in sorted(factors, reverse=True)][::-1])  # Reverse the list after creating it
    headers.append("Factorization")

    # Build table data
    table_data = []
    for subset in sorted(p_set, key=lambda x: (len(x), x)):  # Sort by size, then values
        row = []

        # Format subset representation
        subset_str = "∅" if len(subset) == 0 else str(subset)
        row.append(subset_str)

        # Mark factor inclusion
        for factor in sorted(factors, reverse=True)[::-1]:  # Reverse the list after sorting
            row.append("X" if factor in subset else "")

        # Calculate factorization
        product = 1 if subset else 0
        for factor in subset:
            product *= factor
        other_factor = input_number // product if product != 0 else input_number
        row.append(f"{product} x {other_factor}")

        table_data.append(row)

    # Generate formatted table
    print("\n" + tabulate(table_data, headers=headers, tablefmt="grid", stralign="center"))

def main():
    """Controls program flow through menu-driven interface."""
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

# Program entry point
if __name__ == "__main__":
    main()