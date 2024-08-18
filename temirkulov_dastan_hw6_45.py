numbers = [64, 34, 25, 12, 22, 11, 90]


def bubble_sort(numbers):
    n = len(numbers)
    for i in numbers:
        for m in range(0, n-m-1):
            if numbers[m] > numbers[m + 1]:
                numbers[m], numbers[m + 1] = numbers[m + 1], numbers[m]

print("Исходный состав чисел:", numbers)

bubble_sort(numbers)

print("Отсортированный состав чисел:", numbers)

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            print(f"Элемент {target} найден на позиции {mid}.")
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    print(f"Элемент {target} не найден.")
    return -1

arr = [27, 31, 49, 10, 40, 50, 80]
target = 10

binary_search(arr, target)


