a=int(input("Please A side of the triangle ? "))
b=int(input("Please B side of the triangle ? "))
c=int(input("Please C side of the triangle ? "))


if (a+b < c or a+c < b or c+b < a):

    print ("it is not a triangle")

elif a==b and a == b and a == c:
    print("it is Equilateral")
    

elif a!=b and a != b and a != c and c != b:
    print("It is a scalene")

elif (a == b and a != c) or (a==c and a != b) or (b==c and b != a):
        print ("it is isosceles")
exit()