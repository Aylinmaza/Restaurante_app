# Clase Cliente: representa a un cliente del restaurante
class Cliente:
    def __init__(self, nombre: str, mesa: int):
        self.nombre = nombre
        self.mesa = mesa
        self.pedidos: list[str] = []  # lista de productos pedidos

    def agregar_pedido(self, producto: str):
        self.pedidos.append(producto)

    def __str__(self) -> str:
        pedidos = ', '.join(self.pedidos) if self.pedidos else "Sin pedidos"
        return f"Cliente: {self.nombre}, Mesa: {self.mesa}, Pedidos: {pedidos}"
