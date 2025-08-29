try:
    div=4//0
    print(div)
except ZeroDivisionError:
    print("Attempting to divide by zero")
finally:
    print("This is code of finaly clause")        
