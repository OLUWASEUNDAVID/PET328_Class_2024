######### Assignment 2  ##################
poro = float(input("What is the reservoir porosity: "))
area = float(input("What is the acreage of the reservoir: "))
h = float(input("What is the thickness of the reservoir: "))
sw = float(input("What is the water saturation of the reservoir: "))
boi = float(input("What is formation volume factor of the reservoir fluid: "))

N = (7758 * area * h * poro * (1 - sw)) / boi

print('The amount of oil initially in place is', N)
