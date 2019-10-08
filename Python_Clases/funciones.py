# Funciones en Python
def saludar(nombre, apellido=None):  # Se le puede pasar por defecto una referencia
    print("Hola desde función Saludar a", nombre, apellido)

# Funciones con Return


def doblar(numero):
    return numero*2


saludar("Slavik")
saludar("Hector")

print("El 7 doblado es :", doblar(7))
