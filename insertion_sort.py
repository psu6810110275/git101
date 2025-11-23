def insertion_sort(numbers):
    for i in range(1,len(numbers)):
        j = i 
        while numbers[j-1] > numbers[j] and j > 0 :
            numbers[j-1] , numbers[j] = numbers[j] , numbers[j-1]
            j -= 1
    return numbers
if __name__ == "__main__":
    numbers = list(map(int, input("Enter integer number with space: ").split()))
    sorted_numbers = insertion_sort(numbers)
    print("Sorted number is", sorted_numbers)