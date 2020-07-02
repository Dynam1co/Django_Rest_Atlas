# Atlas API
Con esta API Rest eliminamos las consultas a la base de datos Postgre por código haciendo uso del ORM de Django en los bots de Telegram. Las peticiones a la base de datos las hacemos mediante llamadas a esta API que se ha construido usando Django Rest Framework.

## Creación de la base de datos
En este repositorio explico cómo montar un servidor Postgre dockerizado:
[Repositorio GitHub](https://github.com/Dynam1co/Docker_container_postgresql_12)

### Creación del usuario
Una vez montado el contenedor, creamos el usuario:

```
CREATE USER username WITH SUPERUSER PASSWORD 'my_pass';
```

### Creación de la base de datos
Y la base de datos. El propietario será el usuario que acabamos de crear:

```
CREATE DATABASE db_name WITH OWNER username;
```

## Datos por defecto
La aplicación necesita unos datos por defecto para funcionar, dentro de la carpeta fixtures, hay un fichero json llamado **initial_data.json** que contiene esos datos por defecto.

Para insertar los datos, con el entorno virtual activado ejecutamos:

```
$ python manage.py loaddata initial_data.json
```

# Configuración
Tendremos que crear un archivo llamado **settings.py** dentro de la carpeta **atlas** hay uno de ejemplo que puede renombrarse. [Settings ejemplo](atlas/settings_example.py)

## Configuración de Django
Abrimos el fichero **settings.py** y cambiamos la base de datos por defecto poniendo la siguiente:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'USER': 'username',
        'PASSWORD': 'my_pass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## drf_yasg Swagger generator
Swagger dejó de dar soporte y no funciona en Django 3, así que usamos [esta librería](https://github.com/axnsan12/drf-yasg) para la generación automática de los esquemas de Django Rest Framework. 

La librería se instala automáticamente cuando instalamos el **Requirements.txt** pero hay que configurarla. Si usamos el [fichero de configuración de ejemplo](atlas/settings_example.py) no es necesario hacer nada.