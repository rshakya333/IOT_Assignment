#Write a Python Program find an area of a rectangle and perimeter of the rectangle.

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
lang = input("Area or Perimeter: ")

match lang.lower():  # Convert input to lowercase for case-insensitive matching
    case "area":
        def area_rectangle(length: float, width: float):
            return length * width
        print(f"Area of the rectangle is: {area_rectangle(length, width)}")

    case "perimeter":
        def perimeter_rectangle(length: float, width: float) -> float:
            return 2 * (length + width)
        print(f"Perimeter of the rectangle is: {perimeter_rectangle(length, width)}")

    case _:
        print("Not a valid choice")

