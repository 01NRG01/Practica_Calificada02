N = [1,2,3],[4,5,6],[7,8,9]
S = 0

if len(N)%2==1 or len(N)==2:
    for i in range(len(N)):
        S = S + N[i][i]
    print(S)

    if S%2==0:
        print("La suma es un número par.")

    else:
        print("La suma es un número impar.")

else:
    print("La matriz tiene que ser de tipo cuadrada (A x A) y además A debe ser impar exceptuando el número 2")

J = [2,2,3,5,7],[4,8,6,89,13],[10,31,9,14,15],[4,13,19,45,30],[0,3,6,1,4]
S1 = 0
if len(J)%2==1 or len(J)==2:
    for i in range(len(J)):
        S1 = S1 + J[i][i]
    print(S1)

    if S1%2==0:
        print("La suma es un número par.")

    else:
        print("La suma es un número impar.")

else:
    print("La matriz tiene que ser de tipo cuadrada (A x A) y además A debe ser impar exceptuando el número 2")

H = [1,5,3],[4,5,6],[7,14,9]
S2 = 0
if len(H)%2==1 or len(H)==2:
    for i in range(len(H)):
        S2 = S2 + H[i][i]
    print(S2)

    if S2%2==0:
        print("La suma es un número par.")

    else:
        print("La suma es un número impar.")

else:
    print("La matriz tiene que ser de tipo cuadrada (A x A) y además A debe ser impar exceptuando el número 2")


T = [1,0,3],[4,15,6],[7,43,9]
S3 = 0
if len(T)%2==1 or len(T)==2:
    for v in range(len(T)):
        S3 = S3 + T[v][v]
    print(S3)

    if S3%2==0:
        print("La suma es un número par.")

    else:
        print("La suma es un número impar.")

else:
    print("La matriz tiene que ser de tipo cuadrada (A x A) y además A debe ser impar exceptuando el número 2")