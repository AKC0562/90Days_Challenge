def convert(frac):
    x,y = map(int,frac.split("/"))
    if x>y:
        raise ValueError
    return round(x/y*100)

def fuel_gause(perC):
    if perC<=1:
        return "E"
    elif perC>=99:
        return "F"
    else:
        return f"{perC}%"

def main():
    while True:
        try:
            print (fuel_gause(convert(input("Enter your fraction: "))))
        except (ValueError, ZeroDivisionError):
            print("An error occured.")
        else:
            break

main()