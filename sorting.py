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

def main():
    my_data = read_data("numbers.csv")
    # print(my_data)
    pass


if __name__ == '__main__':
    main()
