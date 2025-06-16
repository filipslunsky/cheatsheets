# FUNCTIONS

# a = 15
# b = 10
# plocha = a * b

# print(f"plocha je {plocha}.")

def get_rectangle_area(a, b):
    plocha = a * b    
    print(plocha) # lokální proměnná
    return plocha



rectangle_area_1 = get_rectangle_area(15, 10) # globální proměnná
rectangle_area_2 = get_rectangle_area(5, 100) # globální proměnná

# print(rectangle_area_1)
# print(rectangle_area_2)