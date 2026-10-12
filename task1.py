numbers = [12,5,27,8,14]
def analyser(numbers):
    smallest = numbers[0]
    largest = numbers[0]
    total = 0
    for i in numbers:
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i
        total += i

    average = total /len(numbers)
    return f"Smallest: {smallest}\nLargest: {largest}\nTotal: {total}\nAverage: {average}"
print(analyser(numbers))