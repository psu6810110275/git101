def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        min_ix = i
        for j in range(i+1,n):
            if numbers[j] < numbers[min_ix]:
                min_ix = j
        numbers[i] , numbers[min_ix] = numbers[min_ix] , numbers[i]
    return numbers
if __name__ == "__main__":
    numbers = list(map(int, input("Enter integer number with space: ").split()))
    sorted_numbers = selection_sort(numbers)
    print("Sorted number is", sorted_numbers)
