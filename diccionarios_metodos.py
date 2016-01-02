from time import sleep

diccionario = {
	"redes_sociales": ["Twitter","Facebook","LinkedIn"],
	3: "Tres",
	"Hola": "Mundo"
}

print diccionario.has_key(3)

sleep(2)

print ""
print diccionario.items()
print ""

sleep(2)

print diccionario.keys()
print ""

sleep(2)

print diccionario.values()
print ""

sleep(2)

print diccionario.pop(2)