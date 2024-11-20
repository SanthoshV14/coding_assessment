import random

# Function finds and returns the median
def sortAndFindMedian(numbers):
    numbers = sort(numbers)
    n = len(numbers)
    
    if n%2==0:
        return (numbers[(n//2) - 1] + numbers[n//2])/2
    else:
        return numbers[n//2]

# Function to sort the list of numbers.
# Bubble sort algorithm used.
def sort(numbers):
    for i in range(len(numbers)-1, 0, -1):
        for j in range(i):
            if numbers[j]>numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


if __name__ == "__main__":
    numbers = []
    
    # prompt user for input
    cmd_input = input("1. Enter the numbers as comma separated values\n\tor\n2. Just press enter to generate random numbers:\n")

    # If user gives a command
    if cmd_input:
        for num in cmd_input.split(","): # split the input to form the list of numbers
            num = num.strip()   # removing extra empty spaces on the front and back
            if num:
                try:
                    numbers.append(int(num))    # convert the string to int if possible else move on to the next element
                except:
                    pass
        
        if len(numbers)==0:
            print("Invalid inputs provided.")
        else:
            print(f"\nInput is: {numbers}")
            output = sortAndFindMedian(numbers)
            print(f"median is: {output}")
    
    # If user does not give a command
    else:
        even = [random.randint(0, 100) for i in range(10)]
        odd = [random.randint(0, 100) for i in range(11)]
        
        print(f"\nODD size 11 input: {odd}")
        output = sortAndFindMedian(odd)
        print(f"median is: {output}", end="\n\n")

        print(f"EVEN size 10 input: {even}")
        output = sortAndFindMedian(even)
        print(f"median is: {output}")