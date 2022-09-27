#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(0, list_length):
        val = 0
        try:
            val = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            continue
        except ZeroDivisionError:
            print("division by 0")
            continue
        except IndexError:
            print("out of range")
            continue
        finally:
            res.append(val)
    return res
