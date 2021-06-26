Pais = {
    "Guatemala": 16896000,
    "Honduras": 8795000,
    "Nicaragua": 6361000,
    "El Salvador": 6551000,
    "Costa Rica": 4949000,
    "Panamá": 3842000,
    "Belice": 382000,
}

try:
    print ("Poblacion de Los paises de Centro America")
    Pais2 = input("Ingrese Nombre de Un Pais de Centro America: ")
    print("La poblacion de {} es de {} habitantes.".format(Pais2, format(Pais[Pais2], ",d")))
except KeyError:
    print("El Pais no existe")