# Archivo principal: crea objetos y ejecuta el sistema
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def main():
    restaurante = Restaurante("Delicias Margarita")

    # Crear productos (mínimo 2)
    pizza = Producto("Pizza Pepperoni", 8, 8.50, True)
    hamburguesa = Producto("Hamburguesa Clásica", 10, 6.00, True)
    jugo = Producto("Jugo Natural", 15, 2.50, True)

    # Crear clientes (mínimo 2)
    cliente1 = Cliente("Aylin", 5)
    cliente2 = Cliente("Carlos", 3)

    # Registrar productos y clientes en el servicio
    restaurante.agregar_producto(pizza)
    restaurante.agregar_producto(hamburguesa)
    restaurante.agregar_producto(jugo)
    restaurante.registrar_cliente(cliente1)
    restaurante.registrar_cliente(cliente2)

    # Agregar pedidos a los clientes
    cliente1.agregar_pedido("Pizza Pepperoni")
    cliente1.agregar_pedido("Jugo Natural")
    cliente2.agregar_pedido("Hamburguesa Clásica")

    # Mostrar información organizada en consola
    restaurante.mostrar_menu()
    restaurante.mostrar_clientes()

if __name__ == "__main__":
    main()

