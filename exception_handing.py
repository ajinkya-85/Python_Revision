#try-except-else-finally

try:
    a=int(input("enter any no."))
    b=a+68
except InterruptedError as error:
    print(error)
    print("its except")
else:
    print("its else")
finally:
    print("Its finally")