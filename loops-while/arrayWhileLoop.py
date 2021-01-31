# add square of numbers from 1 to num to the list named arr and return list
def insert_squares(arr, num):
     i = 1
    while i <= num:
        arr.append(i * i)
        i += 1
    return arr
    