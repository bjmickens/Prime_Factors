from itertools import combinations


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

    print("\nElement of power set", " " * 25, end="")
    for factor in sorted(factors, reverse=True):
        print(f"include {factor}", " " * 15, end="")
    print("resulting factoring")

    for subset in sorted(p_set, key=lambda x: (len(x), x)):
        if len(subset) == 0:
            print("∅", " " * 45, end="")
        else:
            subset_str = str(subset)
            print(f"{subset_str}", " " * (47 - len(subset_str)), end="")

        for factor in sorted(factors, reverse=True):
            if factor in subset:
                print("x", " " * 25, end="")
            else:
                print(" " * 26, end="")

        product = 1
        for factor in subset:
            product *= factor
        other_factor = input_number // product if product != 0 else input_number
        print(f"{product} x {other_factor}")


def main():
    while True:
        print("\nMenu:")
        print("1. Find prime factors")
        print("2. Find power set")
        print("3. List all factorings and subsets")
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