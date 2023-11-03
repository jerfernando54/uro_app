# URO APP

Herramienta Móvil de Apoyo a la Toma de Decisiones en el Tratamiento del Cáncer de Vejiga basada en Inteligencia Artificial

## Pasos para levantar la aplicación
## Requerimientos
Para levantar la aplicación es necesario tener instaladas las siguientes aplicaciones:
#### Lenguaje de programacion
- [Python 3](https://www.python.org/downloads/)
#### Entorno virvtual de python (virtualenv)
- `pip install virtualenv` | `pip3 install virtualenv`
#### Servidor de base de datos (puede ser cualquiera de los que se listan a continuación)
- [wamp](https://www.wampserver.com/en/download-wampserver-64bits/)
- [xampp](https://www.apachefriends.org/es/download.html)

#### Plataforma API para probar los endpoints que hemos desarrollado (cualquiera de las que se listan a continuación)
- [Postman](https://www.postman.com/downloads/)
- [Insomnia](https://insomnia.rest/download)

Una vez instalados los requerimientos arriba mencionados, procedemos con la creación de una base de datos en nuestro gestor de base de datos MySql.
- La base de datos debe llamarse: *`uro_bd_v1`*
- El siguiente paso es configurar la conexión de la base de datos en la aplicación. Para ello, nos dirigimos al directorio *`uro_api/backend/backend`*, abrimos el fichero *settings.py* y en `DATABASES`, configuramos las variables con nuestros credenciales para acceder a nuestra base de datos local que hemos creado previamente.\
por ejemplo:\
DATABASES = {\
    'default': {\
        'ENGINE': 'django.db.backends.mysql',\
        'NAME': 'uro_bd_v1',\
        'USER': 'nombre de usuario para acceder a la base de datos',\
        'PASSWORD': 'password para acceder a la base de datos',\
        'HOST': 'localhost',\
        'PORT': el puerto donde está correindo el servidor de la base de datos.,\
        'OPTIONS': {
            'charset': 'utf8',
        },\
    }
}
### Instalación de los módulos y librerías de Python
El siguiente paso corresponde a la instalción de todos los módulos y librerías utilizados en el proyecto.\
Primero debemos crear y activar el entorno virtual donde levantaremos nuestra aplicación. Este paso es sumamente importante para evitar conflitos, en caso de que tengamos otras aplicaciones de python en nuestra máquina.

Abrimos la terminal y, nos dirigimos a la carpeta donde se encuentra nuestro proyecto y ejecutamos los siguientes comandos:
- *virtualenv venv* -> creamos el entorno virtual
-  *source venv/Scripts/activate* -> activamos el entorno virtual

Para instalar las liobrerias, desde la terminal de comandos nos dirigimos al directorio *uro_api/backend* y ejecutamos el siguiente comando:
- pip install -r requirements.txt

Haste este punto si todo ha ido bien ya tenemos todo listo para levantar la aplicación. Pero todavía nos quedas unos pasos más.
Desde el mismo diroctório donde nos encontramos, ejecutamos los siguientes comandos para crear las migraciones y luego migrar estos cambios a la base de datos.
- *python manage.py makemigrations* -> creamos las migracions
- *python manage.py migrate* -> migramos los cambios a la base de datos

Es posible que se genere un error relacionado con el tamaño de los campos que hemos asignados al crear nuestro modelo de datos para las tablas *user*, *bladdercancer* y *bladdercancerprediction*. Para solucionar el error ejecutamos el siguiente comando a cada una de las tablas desde nuestro servidor local:\
*ALTER DATABASE `databasename` CHARACTER SET utf8;* 

Hecho esto, ya estamos en condiciones de hacer el `makemigrations ` y el `migrate`.\
Una vez hecha las migraciones, procedemos con la importacion de los datos iniciales a la tabla `bladdercancerprediction`. El script se encuentra adjuntado en la misma carpeta donde el proyecto\
Ahora sí, ya estamos en condiciones de levantar nuesta aplicación, para ello ejecutamos el siguiente comando:
- python manage.py runserver.

## Endpoints
Para conocer los endpoints disponibles en nuetra alicación, desde un navegador accedemos a las siguientes rutas:
- http://localhost:8000/docs
- http://localhost:8000/redocs

Las dos rutas nos mustran la documentación en swagger de nuestros endpoints, es decir, muestran:\
- `el endpoint`
- `el/los parametros `
- `y la repuesta`

Empezamos a probar los distintos endpoints, pero primero hay que darse de alta como medico en la aplicación, a traves del endpoint:\
- http://localhost:8000/auth/register/
se trata de una petición de tipo POST, por tanto enviamos los datos como se muestra en la imagen a continuación:






