class Deudor:
    def __init__(self, nombre,telefono,direccion,deuda):
        self.nombre = nombre
        self.deuda = deuda
        self.telefono = telefono
        self.direccion = direccion

    def cobrar_deuda(self, cantidad):
        if cantidad <= self.deuda:
            self.deuda -= cantidad
            print(f"Se han cobrado {cantidad} unidades. Deuda actual: {self.deuda}")
        else:
            print("La cantidad a cobrar supera la deuda actual.")

deudores = []

def agregar_deudor():
    nombre = input("Nombre del deudor: ")
    deuda = float(input("Cantidad de deuda: "))
    direccion = input("Dirección del deudor")
    telefono= int(input("Ingresa el número de telefono si tiene"))
    deudor = Deudor(nombre, deuda, direccion,telefono)
    deudores.append(deudor)
    print("Deudor añadido exitosamente.")

def mostrar_deudores():
    for deudor in deudores:
        print(f"Nombre: {deudor.nombre} | Deuda: {deudor.deuda} | Dirección: {deudor.direccion} | Telefono: {deudor.telefono}")
    print()

def cobrar_deudas():
    mostrar_deudores()
    nombre = input("Nombre del deudor a cobrar: ")
    cantidad = float(input("Cantidad a cobrar: "))
    for deudor in deudores:
        if deudor.nombre == nombre:
            deudor.cobrar_deuda(cantidad)
            break
    else:
        print("No se encontró al deudor en la lista.")
