p = input("first value : ")
q = input("second value : ")
j = 0
k = int(input("rows you want? : "))
while k >= 1:
    print(" "*j + (k-1)*(p+q) +p+ " "*j)
    k = k-1
    j=j+1
