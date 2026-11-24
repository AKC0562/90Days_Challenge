def convert(frac) :
    x,y = map(int, frac.split("/"))
    if x>y:
        raise ValueError("The numerator is greator than denominator.")
    return round(x/y *100)

def gause(percentage):
    if percentage<=1:
        return "E"
    elif percentage>=99:
        return "F"
    else:
        return f"{percentage}%"

def main():
    while True:
        try:
            print(gause(convert(input("Fraction: "))))
        except (ValueError, ZeroDivisionError):
            print("An error occured!!")
        else:
            break



main()