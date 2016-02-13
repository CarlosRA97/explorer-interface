''' Database conection '''
import porc
import hashlib

client = porc.Client("38c54a74-cfc1-4936-8a74-9dec1bd61a40")


def register(name, pw):
    passwd = hashlib.sha256(pw).hexdigest()
    response = client.put(
        'users',
        name,
        {
            "name": name.lower(),
            "lastname": lastname.lower(),
            "passwd": passwd
        }
    )
    # make sure the request succeeded
    response.raise_for_status()


def check(name, pw):
    pawd = hashlib.sha256(pw).hexdigest()
    search = client.get('users', name)

    if search['name'] == name.lower():
        if search['passwd'] == pawd:
            print "Hola, %s. Has iniciado correctamente" % name.title()
        else:
            print "Fuera de aqui bicho"
    else:
        print "No estas registrado"
        ask = raw_input("Quieres registrarte?: ( si | no )")
        if ask == 'si':
            n = raw_input("Cual es su nombre?: ").lower()
            p = raw_input("Introduzca su contrasena: ").lower()
            register(n, p)
        elif ask == 'no':
            pass


# 	batman = client.get('users', 'batman')

# 	batman.raise_for_status() # make sure the request succeeded

# 	print batman.json # prints fields and values as a dict

# 	print batman['Name'] # prints 'Bruce Wayne'

def login():
    pass


n = raw_input("Cual es su nombre?: ").lower()
p = raw_input("Introduzca su contrasena: ").lower()

print ""
