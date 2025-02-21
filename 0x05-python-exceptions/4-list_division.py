#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = [0] * list_length
    i = 0

    while (i < list_length):
        try:
            new_list[i] = (my_list_1[i] / my_list_2[i])
        except IndexError:
            print("out of range")
            pass
        except (TypeError, ValueError):
            print("wrong type")
            new_list[i] = 0
            pass
        except ZeroDivisionError:
            print("division by 0")
            new_list[i] = 0
            pass
        finally:
            i += 1
    return (new_list)
