# Pizzas App API

### Descripción

Proyecto backend de una Pizzería desarrollado en Python con Django, Django REST Framework, Postgresql y Docker.

En el proyecto he creado endpoints para la autenticación básica de REST Framework, así también autenticación por JWT(JSONWebToken), utilizando código limpio siguiendo los estándares PEP-8 de Python así también el orden de las importaciones de Django.

La API está contenerizada con Docker, utilizando la base de datos Postgresql

### Construcción 🛠️
* **Lenguaje:** Python 3
* **Framework:** Django, Django REST Framework

## Requisitos
- Docker instalado.

## Instalación y ejecución:

- Clone o descargue el proyecto.

Ejecute el comando ```docker-compose``` dentro de la carpeta raíz.

* Construir los contenedores: ```docker-compose build```

* Inicializar los servicios: ```docker-compose up -d```

* Detener los servicios: ```docker-compose stop```

De forma predeterminada, la API se ejecutará en el puerto 8000.

#### Nota:
La aplicación probablemente lanzará una excepción la primera vez, porque intentará conectarse al servicio de la base de datos que aún se está inicializando por primera vez; en este caso, espere a que se inicialice por completo y luego ejecute el comando: 
`docker-compose restart app` en otra terminal para reiniciar los servicios bloqueados.
Luego de reiniciar debería de continuar con las respectivas migraciones y posterior ejecución del servidor.

### Probar la aplicación:
Para probar los endpoints basta con abrir el archivo de colección de Postman, contenida dentro de la carpeta raiz.

### Endpoints creados:
- CRUD de usuarios.
- CRUD de las Categorías de los ingredientes.
- CRUD de los Ingredientes.
- CRUD de las Pizzas.

### Protección de Endpoints
Todos los endpoints están protegidos excepto los de creación de usuarios.

### Crear Super Usuario
Para crear un superusuario deberá ejecutar en otra terminal el comando: ```docker-compose run --rm app sh -c "python manage.py createsuperuser"```

### Desactivar un objeto Pizza
Para desactivar un objeto Pizza basta con entrar al administrador de django con el superusuario creado y desactivarlo desde ahí.

### Observaciones:
1. Si desea borrar un ingrediente, pero este está asociado a alguna Pizza, no se podrá borrar.
2. El Endpoint para listar las pizzas solo muestra las pizzas 'activas', pero si el usuario es un superusuario mostrará todas.
3. En el endpoint para borrar un ingrediente de una pizza, hay que ingresar en el los id's correspondientes a la pizza y al ingrediente en cuestión. Luego se borra utilizando el método remove(), me pareció una manera sencilla de hacerlo de esa forma.

### Testing ⚙️
Me pareció súper importante agregar test por lo menos para la aplicación de usuarios.
Para ejecutar los test debe ejecutar en otra terminal el comando ```docker-compose run --rm app sh -c "python manage.py test"```

