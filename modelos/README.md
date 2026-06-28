*Nombre : Aylin Maribel Maza Guaman Descripcion del programa desarrollado = Este proyecto implementa un sistema modular en Python para la gestión de un restaurante.
Permite registrar productos del menú, clientes y sus pedidos, mostrando la información organizada en consola Estructura del Proyecto restaurante_app/ │ ├── main.py # Punto de entrada del programa ├── modelos/ │ ├── producto.py # Clase Producto │ └── cliente.py # Clase Cliente └── servicios/ └── restaurante.py # Clase Restaurante (servicio principal)

Tipos de datos utilizados En las clases se emplean los siguientes tipos de datos:

str → texto (ejemplo: nombre del producto, nombre del cliente).
int → números enteros (ejemplo: cantidad de productos, número de mesa).
float → números decimales (ejemplo: precio de un producto).
bool → valores lógicos (ejemplo: producto disponible o no).
list → listas para almacenar múltiples objetos (ejemplo: menú de productos, lista de clientes, pedidos de cada cliente).
Reflexión El uso de identificadores descriptivos facilita la comprensión del código y evita confusiones.
La aplicación de tipos de datos adecuados asegura que cada atributo represente correctamente la información que maneja.
El empleo de listas permite gestionar múltiples objetos de manera ordenada y flexible.
En conjunto, estas prácticas fortalecen la modularidad del proyecto y hacen que el sistema sea más claro, mantenible y escalable.
*
