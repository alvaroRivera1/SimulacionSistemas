def congruencia_lineal(a,c,m,xo):
    xn=xo
    xa=0
    sen=True
    i=0
    while(sen):
        xa=(xn*a+c)%m
        if(xa==xo):
            sen=False    
        xn=xa
        i=i+1
        print("x"+str(i)+"="+str(xn))

a=int(input("Ingrese a:"))
c=int(input("Ingrese c:"))
m=int(input("Ingrese m:"))
x0=int(input("Ingrese x0:"))
congruencia_lineal(a,c,m,x0)