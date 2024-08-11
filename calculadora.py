# Suma
def suma(a, b):
    return a + b

# Resta
def resta(a, b):
    return a - b

# Multiplicación
def multiplicacion(a, b):
    return a * b

# División
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre cero"
print("Selecciona la operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Ingresa el número de la operación: ")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if opcion == '1':
    print("El resultado es: ", suma(num1, num2))
elif opcion == '2':
    print("El resultado es: ", resta(num1, num2))
elif opcion == '3':
    print("El resultado es: ", multiplicacion(num1, num2))
elif opcion == '4':
    print("El resultado es: ", division(num1, num2))
else:
    print("Opción inválida")

