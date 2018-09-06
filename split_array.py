array = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX', 'YZA']

def split_array(array,*dividers):
    current_array = []
    for element in array:
        if element not in dividers:
            current_array.append(element)
        else:
            yield current_array
            current_array = []

    yield current_array
    
desired_result = [[ 'ABC', 'DEF', 'GHI'],   ['MNO', 'PQR'], ['VWX', 'YZA']]
result = split_array(array,'JKL', 'STU')

print("\nResult: ")
print(list(result))

print("\nDesired result: ")
print(desired_result)
