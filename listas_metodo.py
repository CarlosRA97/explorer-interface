lista = [1,"dos",3,5,2,6,8,7]

buscar = input("Introduce un numero del 1 al 10: ")

if buscar in lista:
	print "Se encuentra en la posicion",lista.index(buscar)+1,"de la lista"
else:
	print "No esta en la lista"
	lista.append(buscar)
	print "El elemento a buscar se agrego a la lista"

