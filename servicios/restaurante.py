# Clase Restaurante: servicio principal que administra menú y clientes
from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.menu: list[Producto] = []
        self.clientes: list[Cliente] = []

    def agregar_producto(self, producto: Producto):
        self.menu.append(producto)

    def registrar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def mostrar_menu(self):
        print(f"\n--- Menú de {self.nombre} ---")
        for producto in self.menu:
            print(producto)

    def mostrar_clientes(self):
        print(f"\n--- Clientes en {self.nombre} ---")
        for cliente in self.clientes:
            print(cliente)
