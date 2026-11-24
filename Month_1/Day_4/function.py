

def int_value() :
    while True:
        try:
            return int(input("What`s x? "))
        except:
            print("X should be integer")
        finally:
            print("F***ing end")

