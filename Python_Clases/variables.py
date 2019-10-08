nombre = "Slavik"   # Literal cadena
edad = 20           # Literal int
pi = 3.1415         # Literal float

llevoGafas = False  # Literal Booleano
# No se puede dejar una variable sin declarar
# Se puede dejar una variable vacia
contadorVacio = None

print("Hola " + nombre)

x = y = z = 1

print(x, y, z)
# Tipado Dinamico

print(type(contadorVacio))

contadorVacio = 0

print(type(contadorVacio))

# Listas en Python

caracteres = ['a', 'b', 'c']
print(caracteres)
# Los elementos pueden accederse con indices
# Con los indices negativos empezamos por el final a contar
print(caracteres[-1])

# Arrays Anidados
personas = [
    ["Hector", 20],
    ["Juan", "Costa"],
    ["Diego", "Perez"]
]
print(personas[1][1])

# Diccionarios Python
colores = {
    "rojo": "red",
    "azul": "blue",
    "negro": "black"
}
# Asignación en el momento a Un diccionario
colores["gris"] = "gray"
print(colores["gris"])
