listaUsuarios = [["alex", "123", "admin"],["freddy", "1234", "user"],["pedro","perro","admin"]]
def login():
    user = input("Ingresa tu usuario: ")
    i = 0
    y = 0
    while i < len(listaUsuarios):
        while y < len(listaUsuarios[i]):
            if y == 0 and listaUsuarios[i][y] == user:
                contrasena = input("ingrese su contrasena: ")
                if listaUsuarios[i][y+1] == contrasena:
                    if listaUsuarios[i][y+2] == "admin":
                        print("es admin")
                        return
                    else:
                        print("es user")
                        return
            y+=1
        i+=1
        y = 0
    print("error!")

def registro():
    print("***")

while True:
    opcionPrincipal = int(input("Bienvenido!\nQue desea hacer:\n1)Iniciar Sesion\n2)Registrarse\n3)Salir"))
    if opcionPrincipal == 1:
        login()
    elif opcionPrincipal == 2:
        registro()
    elif opcionPrincipal == 3:
        exit()