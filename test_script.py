def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr



numbers = [64, 34, 25, 12, 22, 11, 90]

print("Неотсортированный массив")
print(numbers)

sorted_numbers = bubble_sort(numbers)

print("Отсортированный массив")
print(sorted_numbers)
input("Нажмите Enter для выхода...")

