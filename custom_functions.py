# This custom function creates a frequency table from a specified column in a specified dataset.
# it has two parameters (a parameter is the variable you put into a function). When the function is
# called, it passes the parameters to the function as arguments. The two parameters in this function
# are the variable in place for the dataset and the index of the column you have chosen.


from csv import *
file_path = '/Users/chiggy/PycharmProjects/dataquest/AppleStore.csv'
opened_file = open(file_path)
read_file = reader(opened_file)
apps_data = list(read_file)

def freq_table(data_set, index):
    result = {}
    for row in data_set[1:]:
        value = row[index]
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result

ratings_ft = freq_table(apps_data, 7)

print(ratings_ft)

# Here's another function mean() which used other functions in the function body:

def extract(data_set, index):
    column = []
    for row in data_set[1:]:
        value = row[index]
        column.append(value)
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    values = extract(data_set, index)
    sum_values = find_sum(values)
    len_values = find_length(values)
    return sum_values / len_values

avg_price = mean(apps_data, 4)
print(avg_price)
