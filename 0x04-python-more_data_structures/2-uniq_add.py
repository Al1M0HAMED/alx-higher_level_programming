#!/usr/bin/python3
def uniq_add(my_list=[]):
    not_uniq, sum = {}, 0
    for element in my_list:
        if element is not_uniq.get(str(element)):
            continue
        else:
            sum += int(element)
            not_uniq[str(element)] = int(element)
    return (sum)
