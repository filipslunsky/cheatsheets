# FUNCTIONS
def get_rectangle_area(a, b=10):
    area = a * b
    print(f"area: {area}")
    return area
    

f = 9
g = 7

# get_rectangle_area(4, 5)
# get_rectangle_area(4)
# get_rectangle_area(a=3, b=6)

# get_rectangle_area(b, a)
# get_rectangle_area(b=f, a=g)

def get_multiplication(a:int, b, c=1.0):
    '''this is a very a special function'''
    return a * b * c

result = get_multiplication(2, 3, 4)
print(result)

result = get_multiplication(2, 3)
print(result)



