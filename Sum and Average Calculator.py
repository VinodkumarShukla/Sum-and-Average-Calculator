def calculate_sum_and_average(numbers):
    # Calculate the sum of numbers
    total_sum = sum(numbers)

    # Calculate the average
    average = total_sum / len(numbers) if len(numbers) > 0 else 0

    return total_sum, average

# Example usage:
numbers_str = input("Enter a list of numbers separated by spaces: ")

# Convert the input string to a list of floats
numbers = [float(num) for num in numbers_str.split()]

# Calculate sum and average
sum_numbers, average_numbers = calculate_sum_and_average(numbers)

# Display the result
print(f"The sum of numbers is: {sum_numbers}")
print(f"The average of numbers is: {average_numbers:.2f}")
