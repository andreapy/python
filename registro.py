##funcion incremento
def incremento(x):
	if x[0]<8:
		x=x[0]+1,x[1]
	else:
		if x[1]==8:
			x=1,1
		else:
			x=1,x[1]+1
	return x
##funcion ataque
def ataque(a,b):
	if a[0]==b[0] or a[1]==b[1] or a[0]+a[1]==b[0]+b[1] or a[0]-a[1]==b[0]-b[1]:
		return True
	else:
		return False
##consecutivo
def consecutivo(a):
    if a==8:
        return 1
    else:
        a=a+1
        return a

##funcion registro
def registro(h,i,j,k,l,m,n,o,p):
	while ataque (h[i],h[j])==True:
		h[j]=incremento(h[j])
		if h[j][1]==consecutivo(consecutivo(h[i][1])):
			print "no solucion"
			return 0
		##print "j",h
	while ataque (h[j],h[k])==True or ataque (h[i],h[k])==True:
		h[k]=incremento(h[k])
		if h[k][1]==consecutivo(consecutivo(h[j][1])):
		    h[k]=h[j]
		    h[j]=incremento(h[j])
		    registro(h,i,j,k,l,m,n,o,p)
		##print "k",h
	while ataque(h[i],h[l])==True or ataque(h[j],h[l]) or ataque(h[k],h[l]):
		h[l]=incremento(h[l])
		if h[l][1]==consecutivo(consecutivo(h[k][1])):
		    h[l]=h[k]
		    h[k]=incremento(h[k])
		    registro(h,i,j,k,l,m,n,o,p)
		##print "l",h
	while ataque(h[m],h[i])==True or ataque(h[m],h[j])==True or ataque(h[m],h[k])==True or ataque(h[l],h[m])==True:
		h[m]=incremento(h[m])
		if h[m][1]==consecutivo(consecutivo(h[l][1])):
		    h[m]=h[l]
		    h[l]=incremento(h[l])
		    registro(h,i,j,k,l,m,n,o,p)
		##print "m",h
	while ataque(h[n],h[i])==True or ataque(h[n],h[j])==True or ataque(h[n],h[k])==True or ataque(h[n],h[l])==True or ataque(h[n],h[m])==True:
		h[n]=incremento(h[n])
		if h[n][1]==consecutivo(consecutivo(h[m][1])):
		    h[n]=h[m]
		    h[m]=incremento(h[m])
		    registro(h,i,j,k,l,m,n,o,p)
		##print "n",h
	while ataque(h[o],h[i])==True or ataque(h[o],h[j])==True or ataque(h[o],h[k])==True or ataque(h[o],h[l])==True or ataque(h[o],h[m])==True or ataque(h[o],h[n])==True:
		h[o]=incremento(h[o])
		if h[o][1]==consecutivo(consecutivo(h[n][1])):
		    h[o]=h[n]
		    h[n]=incremento(h[n])
		    registro(h,i,j,k,l,m,n,o,p)
		##print "o",h
	while ataque(h[p],h[i])==True or ataque(h[p],h[j])==True or ataque(h[p],h[k])==True or ataque(h[p],h[l])==True or ataque(h[p],h[m])==True or ataque(h[p],h[n])==True or ataque(h[p],h[o])==True:
		h[p]=incremento(h[p])
		if h[p][1]==consecutivo(consecutivo(h[o][1])):
		    h[p]=h[o]
		    h[o]=incremento(h[o])
		    registro(h,i,j,k,l,m,n,o,p)
		##print "p",h

	return h
##funcion "ordenar"
def ordenar(h):
    t=0,0
    i=0
    j=0
    while i<=7:
        j=i
        while j<=7:
            if h[j][1] < h[i][1]:
                t=h[i]
                h[i]=h[j]
                h[j]=t
            j=j+1
        i=i+1
    return h
##funcion "tablero"
def tablero(h):
    i=0
    j=0
    print "- - - - - - - - - - - - - - - - -"
    while i<=7:
        while j<=7:
            print "|",
            if j==h[i][0]-1:
                print "*",
            else:
                print " ",
            if j==7:
                print "|"
            j=j+1
        print "- - - - - - - - - - - - - - - - -"
        j=0
        i=i+1
##Parte principal del programa
print "este programa ubicar? 8 reinas en un tablero de ajedrez de tal modo que no se ataquen entre ellas a partir de la coordenada de una reina fijada por el usuario"
print "debe ingresar la coordenada de la primera reina indicando dos numeros: fila y columna, estos numeros deben estar entre 1 y 8 "
a=input("ingrese la fila")
b=input("ingrese la columna")
c1=a,b
h=[c1,c1,c1,c1,c1,c1,c1,c1]##tupla que almacenara la solucion
##print h
h=registro(h,0,1,2,3,4,5,6,7)
##print h
h=ordenar(h)##ordena la tupla para facilitar la impresion
print "su solucion es:"
tablero(h)
