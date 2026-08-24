# 🎮 Nova Play

**Nova Play** es una tienda web de videojuegos desarrollada con **Django**. La aplicación permite explorar un catálogo de videojuegos, consultar información detallada de cada producto, realizar búsquedas, crear cuentas de usuario, iniciar sesión y gestionar un carrito de compras.

El proyecto está organizado en diferentes aplicaciones de Django, separando cada funcionalidad principal para mantener una estructura modular, ordenada y fácil de mantener.

---

## 🚀 Tecnologías utilizadas

* **Python**
* **Django 6**
* **HTML5**
* **CSS3**
* **JavaScript**
* **Bootstrap 5**
* **Font Awesome**
* **SQLite**
* **Git**
* **GitHub**

---

## ✨ Funcionalidades

### 🏠 Página principal

Nova Play dispone de una página principal desde la que el usuario puede acceder a las diferentes secciones de la tienda.

También cuenta con una página de contacto.

### 🎮 Catálogo de videojuegos

El catálogo permite:

* Visualizar los videojuegos disponibles.
* Mostrar 6 videojuegos por página.
* Navegar entre diferentes páginas del catálogo.
* Consultar la información individual de cada videojuego.
* Visualizar nombre, precio, plataforma e imagen.

### 🔍 Buscador

Nova Play incluye un sistema de búsqueda que permite encontrar videojuegos utilizando:

* Nombre del videojuego.
* Plataforma.

Los resultados también se muestran mediante paginación de 6 videojuegos por página.

### 👤 Sistema de usuarios

La aplicación utiliza un modelo de usuario personalizado basado en el sistema de autenticación de Django.

Permite:

* Registrar nuevos usuarios.
* Utilizar un correo electrónico único.
* Iniciar sesión.
* Cerrar sesión.
* Acceder a un perfil de usuario.
* Iniciar sesión automáticamente después del registro.
* Proteger determinadas páginas para usuarios autenticados.

### 🛒 Carrito de compras

Cada usuario registrado dispone de su propio carrito.

El sistema permite:

* Añadir videojuegos al carrito.
* Incrementar automáticamente la cantidad de un videojuego si ya existe.
* Eliminar productos.
* Vaciar completamente el carrito.
* Mostrar la cantidad de productos.
* Calcular el subtotal de cada producto.
* Calcular el precio total del carrito.
* Mostrar el número de productos del carrito en la barra de navegación.

### 🔔 Sistema de mensajes

Nova Play utiliza el sistema de mensajes de Django para mostrar notificaciones al usuario después de determinadas acciones.

Por ejemplo:

* Registro completado.
* Inicio de sesión correcto.
* Producto añadido al carrito.
* Producto eliminado.
* Carrito vaciado.
* Errores de autenticación.

Los mensajes se muestran mediante notificaciones tipo **toast**.

### 🌗 Interfaz

La interfaz incluye:

* Diseño responsive.
* Bootstrap 5.
* Font Awesome.
* Tema oscuro.
* Cambio de tema mediante JavaScript.
* Barra de navegación adaptable a dispositivos móviles.
* Buscador integrado.
* Menú de usuario.
* Indicador de productos del carrito.

---

# 📁 Estructura del proyecto

```text
tienda_videojuegos/
│
├── .gitignore
├── inicio_env.bat
│
└── tienda_videojuegos/
    │
    ├── manage.py
    ├── reparar_admin.py
    │
    ├── buscador/
    │   ├── migrations/
    │   ├── templates/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    │
    ├── carrito/
    │   ├── migrations/
    │   ├── templates/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── context_processors.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    │
    ├── catalogo/
    │   ├── migrations/
    │   ├── templates/
    │   │   └── catalogo/
    │   │       ├── detalle_juego.html
    │   │       └── lista_juegos.html
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    │
    ├── home/
    │   ├── migrations/
    │   ├── templates/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    │
    ├── usuarios/
    │   ├── migrations/
    │   ├── templates/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    │
    ├── static/
    │   ├── css/
    │   ├── img/
    │   └── js/
    │
    ├── templates/
    │   └── base.html
    │
    └── tienda_videojuegos/
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

---

# 🧩 Aplicaciones de Django

## 🏠 `home`

Gestiona las páginas generales de Nova Play.

Incluye:

* Página principal.
* Página de contacto.

Rutas principales:

```text
/
/contacto/
```

---

## 🎮 `catalogo`

Gestiona los videojuegos disponibles en Nova Play.

El modelo principal es `Juego`.

### Modelo Juego

Cada videojuego almacena:

```text
nombre
precio
plataforma
imagen
```

El modelo utiliza:

* `nombre`: nombre del videojuego.
* `precio`: precio del producto.
* `plataforma`: plataforma o plataformas disponibles.
* `imagen`: nombre o ruta de la imagen correspondiente.

### Funcionalidades

* Mostrar todos los videojuegos.
* Paginación de 6 productos.
* Página individual para cada videojuego.
* Obtención del producto mediante su ID.

Rutas:

```text
/catalogo/
/catalogo/<id>/
```

---

## 🔍 `buscador`

Gestiona las búsquedas dentro del catálogo.

La búsqueda se realiza sobre el modelo `Juego`.

Permite buscar coincidencias por:

```text
nombre
plataforma
```

La búsqueda no distingue entre mayúsculas y minúsculas.

Los resultados también cuentan con paginación.

Ruta:

```text
/buscador/?q=termino
```

Ejemplo:

```text
/buscador/?q=playstation
```

---

## 👤 `usuarios`

Gestiona la autenticación de los usuarios.

Nova Play utiliza un modelo propio llamado:

```python
Usuario
```

Este modelo hereda de:

```python
AbstractUser
```

y modifica el correo electrónico para que sea único.

### Registro

El formulario de registro solicita:

```text
Nombre de usuario
Correo electrónico
Contraseña
Confirmación de contraseña
```

Cuando el registro se completa correctamente, el usuario inicia sesión automáticamente.

### Inicio de sesión

Los usuarios pueden autenticarse utilizando el sistema de autenticación integrado de Django.

### Perfil

La página de perfil está protegida mediante:

```python
@login_required
```

por lo que solo los usuarios autenticados pueden acceder.

### Rutas

```text
/usuarios/registro/
/usuarios/login/
/usuarios/logout/
/usuarios/perfil/
```

---

# 🛒 Carrito de compras

El carrito está asociado directamente a cada usuario de Nova Play.

El sistema utiliza dos modelos:

```text
Carrito
ItemCarrito
```

## `Carrito`

Cada usuario dispone de un único carrito mediante una relación:

```python
OneToOneField
```

El carrito almacena además:

* Fecha de creación.
* Fecha de actualización.

También dispone de métodos para calcular:

```text
Cantidad total de productos
Precio total del carrito
```

## `ItemCarrito`

Representa un producto dentro del carrito.

Contiene:

```text
carrito
juego
cantidad
```

Cada combinación de carrito y videojuego es única.

Si un videojuego ya está en el carrito y el usuario vuelve a añadirlo, su cantidad aumenta.

### Operaciones disponibles

#### Añadir un producto

```text
/carrito/agregar/<juego_id>/
```

#### Ver carrito

```text
/carrito/
```

#### Eliminar un producto

```text
/carrito/eliminar/<juego_id>/
```

#### Vaciar carrito

```text
/carrito/limpiar/
```

Las operaciones del carrito requieren que el usuario haya iniciado sesión.

---

# 🌐 Rutas principales

| Ruta                      | Descripción              |
| ------------------------- | ------------------------ |
| `/`                       | Página principal         |
| `/contacto/`              | Página de contacto       |
| `/catalogo/`              | Catálogo de videojuegos  |
| `/catalogo/<id>/`         | Detalle de un videojuego |
| `/buscador/`              | Buscador                 |
| `/usuarios/registro/`     | Registro de usuario      |
| `/usuarios/login/`        | Inicio de sesión         |
| `/usuarios/logout/`       | Cierre de sesión         |
| `/usuarios/perfil/`       | Perfil del usuario       |
| `/carrito/`               | Carrito de compras       |
| `/carrito/agregar/<id>/`  | Añadir producto          |
| `/carrito/eliminar/<id>/` | Eliminar producto        |
| `/carrito/limpiar/`       | Vaciar carrito           |
| `/admin/`                 | Administración de Django |

---

# ⚙️ Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/MiguelMesa1/tienda_videojuegos.git
```

Entrar en el repositorio:

```bash
cd tienda_videojuegos
```

Después acceder a la carpeta donde se encuentra `manage.py`:

```bash
cd tienda_videojuegos
```

---

## 2. Crear un entorno virtual

### Windows

```bash
python -m venv venv
```

Activar el entorno:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activarlo:

```bash
source venv/bin/activate
```

---

## 3. Instalar Django

Actualmente el repositorio no incluye un archivo `requirements.txt`, por lo que Django puede instalarse directamente:

```bash
pip install django
```

El proyecto fue creado utilizando **Django 6**.

Puedes comprobar la versión instalada mediante:

```bash
python -m django --version
```

---

## 4. Aplicar las migraciones

```bash
python manage.py migrate
```

Si se realizan cambios en los modelos:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 5. Crear un superusuario

Para acceder al panel administrativo:

```bash
python manage.py createsuperuser
```

Introduce los datos solicitados.

---

## 6. Ejecutar el servidor

```bash
python manage.py runserver
```

La aplicación estará disponible normalmente en:

```text
http://127.0.0.1:8000/
```

---

# 🔐 Panel de administración

Django proporciona un panel desde el que se pueden gestionar diferentes datos de la aplicación.

Acceso:

```text
http://127.0.0.1:8000/admin/
```

Se debe iniciar sesión utilizando una cuenta con permisos administrativos.

---

# 🗄️ Base de datos

Nova Play utiliza actualmente:

```text
SQLite
```

La configuración utiliza la base de datos integrada de Django:

```text
db.sqlite3
```

Esto facilita el desarrollo y las pruebas locales sin necesidad de configurar un servidor externo de bases de datos.

---

# 🏗️ Arquitectura

Nova Play sigue la arquitectura **MVT (Model - View - Template)** utilizada por Django.

```text
Usuario
   │
   ▼
URL
   │
   ▼
View
   │
   ├────► Model ────► SQLite
   │
   ▼
Template
   │
   ▼
Navegador
```

Además, las funcionalidades se encuentran divididas en aplicaciones independientes:

```text
Nova Play
│
├── home
├── catalogo
├── buscador
├── usuarios
└── carrito
```

Esto permite mantener separada la lógica de cada parte del sistema.

---

# 🎨 Frontend

Nova Play dispone de una plantilla global:

```text
templates/base.html
```

Las diferentes páginas pueden heredar de esta plantilla para mantener elementos comunes como:

* Header.
* Barra de navegación.
* Buscador.
* Carrito.
* Menú del usuario.
* Mensajes.
* Footer.

La interfaz utiliza:

```text
Bootstrap 5
Font Awesome
CSS personalizado
JavaScript personalizado
```

También incluye soporte para una interfaz adaptable a dispositivos móviles.

---

# 🔐 Autenticación

En `settings.py` se utiliza un modelo personalizado:

```python
AUTH_USER_MODEL = 'usuarios.Usuario'
```

Las páginas que requieren autenticación utilizan el sistema de protección proporcionado por Django.

Cuando un usuario no autenticado intenta acceder a una vista protegida, se utiliza la página de inicio de sesión configurada.

---

# 📦 Modelo de datos simplificado

```text
Usuario
   │
   │ 1
   │
   │ 1
   ▼
Carrito
   │
   │ 1
   │
   │ N
   ▼
ItemCarrito
   │
   │ N
   │
   │ 1
   ▼
Juego
```

Un usuario tiene un carrito.

Un carrito puede contener varios elementos.

Cada elemento está asociado a un videojuego y posee una cantidad.

---

# 🔮 Posibles mejoras

Algunas funcionalidades que podrían añadirse en futuras versiones son:

* [ ] Sistema de noticias.
* [ ] Proceso completo de compra.
* [ ] Gestión de pedidos.
* [ ] Historial de compras.
* [ ] Integración de una pasarela de pago.
* [ ] Sistema de favoritos.
* [ ] Valoraciones y reseñas.
* [ ] Filtrado avanzado por plataforma.
* [ ] Filtrado por precio.
* [ ] Gestión de stock.
* [ ] Categorías o géneros de videojuegos.
* [ ] Recuperación de contraseña.
* [ ] Edición de datos del perfil.
* [ ] API REST.
* [ ] Uso de PostgreSQL en producción.
* [ ] Despliegue de la aplicación.

---

# ⚠️ Configuración para producción

La configuración actual está orientada al desarrollo.

Antes de desplegar Nova Play en producción se recomienda:

* Desactivar `DEBUG`.
* Configurar correctamente `ALLOWED_HOSTS`.
* Utilizar variables de entorno.
* No almacenar la `SECRET_KEY` directamente en el repositorio.
* Configurar correctamente los archivos estáticos.
* Utilizar una base de datos adecuada para producción.
* Revisar la configuración de seguridad de Django.

Por ejemplo, la clave secreta debería cargarse desde una variable de entorno en lugar de escribirse directamente en `settings.py`.

---

# 🎯 Objetivo del proyecto

El objetivo de **Nova Play** es desarrollar una tienda web de videojuegos utilizando Django y aplicar conceptos como:

* Arquitectura MVT.
* Modelos y relaciones.
* Sistema de autenticación.
* Formularios.
* Sesiones.
* Templates.
* Herencia de plantillas.
* URLs.
* Vistas.
* Paginación.
* Consultas con el ORM de Django.
* Búsqueda mediante filtros.
* Context processors.
* Sistema de mensajes.
* Carrito de compras.
* Panel administrativo.
* Archivos estáticos.
* Diseño responsive.

---

# 👨‍💻 Autor

**Miguel Mesa**

* GitHub: `MiguelMesa1`
* Correo: `miguelangelmesagarzon@gmail.com`
* Repositorio: `MiguelMesa1/tienda_videojuegos`

---

# 📄 Licencia

Proyecto desarrollado con fines educativos y de aprendizaje.

---

## 🌌 Nova Play

### Tu próxima aventura comienza aquí. 🎮
