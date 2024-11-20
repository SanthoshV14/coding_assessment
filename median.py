import random

def sortAndFindMedian(numbers):
    numbers = sort(numbers)
    n = len(numbers)
    
    if n%2==0:
        return (numbers[(n//2) - 1] + numbers[n//2])//2
    else:
        return numbers[n//2]

def sort(numbers):
    for i in range(len(numbers)-1, 0, -1):
        for j in range(i):
            if numbers[j]>numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

if __name__ == "__main__":
    numbers = []
    cmd_input = input("1. Enter the numbers as comma separated values\n\tor\n2. Just press enter to generate random numbers:\n")
    if cmd_input:
        for num in cmd_input.split(","):
            num = num.strip()
            if num:
                try:
                    numbers.append(int(num))
                except:
                    pass
                
        print(f"\nInput is: {numbers}")
        output = sortAndFindMedian(numbers)
        print(f"median is: {output}")

    else:
        even = [random.randint(0, 100) for i in range(10)]
        odd = [random.randint(0, 100) for i in range(11)]
        
        print(f"\nODD size input: {odd}")
        output = sortAndFindMedian(odd)
        print(f"median is: {output}", end="\n\n")

        print(f"EVEN size input: {even}")
        output = sortAndFindMedian(even)
        print(f"median is: {output}")