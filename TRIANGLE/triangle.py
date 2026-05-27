def classifyTriangle(a, b, c):

    if (not isinstance(a, int) or
        not isinstance(b, int) or
        not isinstance(c, int)):
        return "Invalid input"

    if (a < 1 or b < 1 or c < 1):
        return "Invalid input"

    if (a > 100 or b > 100 or c > 100):
        return "Invalid input"

    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"

    if a == b == c:
        return "Equilateral triangle"

    elif (a == b or b == c or a == c):
        return "Isosceles triangle"

    else:
        return "Scalene triangle"