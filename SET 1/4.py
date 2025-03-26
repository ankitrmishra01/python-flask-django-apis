def calculate_average(numbers):
    if not numbers:  
        return "The list is empty. Cannot calculate average."
    total = sum(numbers) 
    count = len(numbers)  
    average = total / count  
    return average
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print(f"The average of the list is: {average}")
