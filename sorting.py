import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.
    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        data = {}
        for row in reader:
            for head, value in row.items():
                if head not in data:
                    data[head] = [int(value)]
                else:
                    data[head].append(int(value))
    return data

def selection_sort(array, direction):
    for ind in range(len(array)):
        min_index = ind

        for j in range(ind + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[ind], array[min_index] = array[min_index], array[ind]
    if direction == "asc":
        return array
    elif direction == "desc":
        return array[::-1]
    else:
        return "Error in direction"

def bubble_sort(arr):
    swapped = False
    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return arr
    return arr

def insertion_sort(arr):
    if (n := len(arr)) <= 1:
        return
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def main():
    my_data = read_data("numbers.csv")
    print(my_data["series_1"], "Původné dáta")
    sorted_data = selection_sort(my_data["series_1"].copy(), "asc")
    print(sorted_data, "Selection sort")
    bubble_sorted_data = bubble_sort(my_data["series_1"].copy())
    print(bubble_sorted_data, "Bubble sort")
    insertion_sort_data = insertion_sort(my_data["series_1"].copy())
    print(insertion_sort_data, "Insertion sort")
    pass


if __name__ == '__main__':
    main()
