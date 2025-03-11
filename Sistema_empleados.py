class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
    
    def calcular_salario(self):
        return self.salario
    
    def __str__(self):
        return f"{self.nombre} ({self.edad} años) - Salario: {self.calcular_salario():.2f}"

class Gerente(Empleado):
    def calcular_salario(self):
        return self.salario * 1.2

class Desarrollador(Empleado):
    def __init__(self, nombre, edad, salario, proyectos):
        super().__init__(nombre, edad, salario)
        self.proyectos = proyectos

    def calcular_salario(self):
        bono = self.proyectos * 50 + 500
        return self.salario + bono

class Practicante(Empleado):
    pass


print("\nBienvenido a la Gestion de Empleados")
empleados = []

while True:

    print("\nSeleccione el tipo de empleado")
    print("1. Gerente")
    print("2. Desarrollador")
    print("3. Practicante")

    opcion = input("\nIngresa una opciones (1-3): ")

    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    salario = float(input("Salario: "))

    if opcion == '1':
        empleado = Gerente(nombre, edad, salario)
    elif opcion == '2':
        proyectos = int(input("Cantidad de proyectos: "))
        empleado = Desarrollador(nombre, edad, salario, proyectos)
    else:
        empleado = Practicante(nombre, edad, salario)

    
    empleados.append(empleado)
    print(f"\nEmpleado registrado: {empleado}")

    continuar = input("Quieres agregar otro empleado? (s/n)").lower()
    if continuar != 's':
        break

print("\nLista de empleados registrados:")
for emp in empleados:
    print(emp)