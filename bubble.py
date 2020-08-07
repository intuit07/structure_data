

# test_list = [115, 1, 33, 5, 10, 5558, 87, 5435, 987]
#
#
#
def sort(income_list):
    last_element = len(income_list) - 1
    for element in range(last_element):
        for el in range(last_element-element):
            if income_list[el] > income_list[el+1]:
                income_list[el], income_list[el+1] = income_list[el+1], income_list[el]
    return income_list
#
#
# print("1-->\n", test_list)
# new_list = sort(test_list).copy()
# print("2-->\n", new_list)



def summa(x):
    if x == 0:
        return  0
    elif x == 1:
        return 1
    else:
        return x+summa(x-1)

print("summa(5)--->\n", summa(5))



def factor(x):
    if x == 1:
        return 1
    else:
        return x * factor(x-1)

print("summa(5)--->\n", factor(5))


def fibonach(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        print("fibonach(x-1)--->\n", fibonach(x-1))
        print("fibonach(x-2)--->\n", fibonach(x-2))
        return fibonach(x-1)+fibonach(x-2)


print("summa(5)--->\n", fibonach(5))