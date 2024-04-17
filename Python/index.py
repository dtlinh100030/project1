print("Hello world")

x = 5
y ="Hello world"
print(x)
print(y)

#Diện tích HCN
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    :param length: The length of the rectangle.
    :param width: The width of the rectangle.
    :return: The area of the rectangle.
    """
    area = length * width
    return area

# Example usage
length = 10
width = 5
area = calculate_area(length, width)
print(f"The area of the rectangle is {area}.")