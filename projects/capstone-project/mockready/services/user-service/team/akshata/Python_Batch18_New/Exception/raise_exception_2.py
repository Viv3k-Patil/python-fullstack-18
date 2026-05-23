

try:
    #a=1/0
    #int("abc")
    raise Exception("I dont know")
except ValueError:
    print("This is value error")

except ZeroDivisionError:
    print("This is zero division error")

except Exception:
    print("something want wrong")











