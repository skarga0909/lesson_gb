class MyOwnErr(Exception):
    pass


in_data = input("Enter a number: ")
try:
    in_data = int(in_data)
    res = in_data / 0
    in_data = int(in_data)
except ZeroDivisionError as err:
    print(err)
else:
    print(res)
finally:
    print("The end")
