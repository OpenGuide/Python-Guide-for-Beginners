p = 0
g = 0
q = 0
r = 0
p = int(input("Enter the larger number."))
g = int(input("Enter the smaller number."))

while 1:
    q = p//g
    r = p % g
    # print(p,",",g,",",q,",",r)

    if r == 0:
        break
    p = g
    g = r

print("H.C.F = ", g)
# print(p,",",g,",",q,",",r)
