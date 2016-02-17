
import math

def smiley(diameter):
    result = ""
    center_x = diameter / 2.0
    center_y = diameter / 2.0

    for y in range(diameter):
        for x in range(diameter):
            distance_x = x - center_x
            distance_y = y - center_y
            distance = math.sqrt(distance_x**2.0 + distance_y**2.0)+1
            diameter_div3 = math.floor(diameter / 3)
            isOoghoogte = y == diameter_div3

            isLinkeroog = x == diameter_div3
            isRechteroog = x == math.floor(diameter_div3 + diameter / 2 - 1)

            isMondhoogte = y == 2 * (diameter_div3)
            isMond = abs(x - center_x) < diameter / 4

            if math.ceil(distance) == math.ceil(diameter/2):  # implicit truncation to int with /2 for a more healthy face
                result += "#"
            else:
                if isOoghoogte and (isLinkeroog or isRechteroog):
                    result += "0"
                elif isMondhoogte and isMond:
                    result += "-"
                else:
                    result += " "
        result += "\n"
    return result

print(smiley(20))

#
# result = ""
# for i in range (0 ,9):
#     for j in range (0,i):
#         result += "*"
#     result += "\n"
# print ( result )