# Define the calculate_mean function
def calculate_mean(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)