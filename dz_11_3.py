class MyOwnErr(Exception):
    pass


in_data = input("Enter a number: ")
try:
    in_data = int(in_data)
    if type(in_data) is not int:
        raise MyOwnErr("Only number")
except (ValueError, MyOwnErr) as err:
    print(err)
else:
    print(in_data)
finally:
    print("The end")
