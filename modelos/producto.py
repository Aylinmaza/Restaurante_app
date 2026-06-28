class Producto:
    def __init__(self, nombre: str, cantidad: int, precio: float, disponible: bool):
        self.nombre = nombre         
        self.cantidad = cantidad      
        self.precio = precio          
        self.disponible = disponible  

    def __str__(self) -> str:
        estado = "Disponible" if self.disponible else "No disponible"
        return f"{self.nombre} - Cantidad: {self.cantidad}, Precio: ${self.precio:.2f} ({estado})"
