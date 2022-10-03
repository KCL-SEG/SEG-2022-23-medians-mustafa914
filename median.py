while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
        if len(numbers) %2 != 0:
            mid_index = len(numbers)//2
            median_num = (numbers[mid_index])
        else:
            mid_index2 = len(numbers)//2 
            mid_index1 = mid_index2 - 1
            median_num = (numbers[mid_index1] + numbers[mid_index2])/2

    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
print(f'The median is {median_num}')
