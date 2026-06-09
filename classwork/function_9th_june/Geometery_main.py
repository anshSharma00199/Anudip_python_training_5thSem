from Geometery import *
while True:
    print("\n-----2D FIGURES-----")
    print("1. Circle")
    print("2. Triangle")
    print("3. Square")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        r = float(input("Enter radius: "))

        while True:
            print("\n1. Area")
            print("2. Perimeter")
            print("3. Exit")

            op = int(input("Enter choice: "))

            if op == 1:
                print("Area =", area_circle(r))
            elif op == 2:
                print("Perimeter =", perimeter_circle(r))
            elif op == 3:
                break
            else:
                print("Invalid Choice")

    elif ch == 2:
        while True:
            print("\n1. Area")
            print("2. Perimeter")
            print("3. Exit")

            op = int(input("Enter choice: "))

            if op == 1:
                b = float(input("Enter base: "))
                h = float(input("Enter height: "))
                print("Area =", area_triangle(b, h))

            elif op == 2:
                a = float(input("Enter side 1: "))
                b = float(input("Enter side 2: "))
                c = float(input("Enter side 3: "))
                print("Perimeter =", perimeter_triangle(a, b, c))

            elif op == 3:
                break

            else:
                print("Invalid Choice")

    elif ch == 3:
        s = float(input("Enter side: "))

        while True:
            print("\n1. Area")
            print("2. Perimeter")
            print("3. Exit")

            op = int(input("Enter choice: "))

            if op == 1:
                print("Area =", area_square(s))
            elif op == 2:
                print("Perimeter =", perimeter_square(s))
            elif op == 3:
                break
            else:
                print("Invalid Choice")

    elif ch == 4:
        print("Program Ended...👍")
        break

    else:
        print("Invalid Choice")