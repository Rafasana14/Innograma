# Descripción del sistema: 

![Django CI](https://github.com/Rafasana14/Innograma/actions/workflows/django.yml/badge.svg)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/314003e444754d15b93e67b8d714de9c)](https://www.codacy.com/gh/Rafasana14/Innograma/dashboard?utm_source=github.com&utm_medium=referral&utm_content=Rafasana14/Innograma&utm_campaign=Badge_Coverage)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/314003e444754d15b93e67b8d714de9c)](https://www.codacy.com/gh/Rafasana14/Innograma/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Rafasana14/Innograma&amp;utm_campaign=Badge_Grade)

Se ha desarrollado una aplicación web para las jornadas Innosoft Days del curso 23/24 y en adelante. El objetivo de esta aplicación es el de aportar a los miembros del comité de programa de Innosoft una plataforma cómoda y accesible con la que gestionar las ponencias, eventos, calendario semanal de las jornadas y ponentes que asistirán a las mismas. La aplicación presenta una página de bienvenida con fotos de jornadas pasadas y una descripción de la propia aplicación. En la parte superior contamos en todo momento con una barra de navegación que ofrece las opciones “Inicio”, “Ponencias”, “Ponentes”, “Eventos”, “Calendario” y “Acceso Administrador”. 


## Cómo ejecutar la aplicación: 

Los usuarios pueden acceder a nuestro sistema siguiendo los siguientes pasos: 

En el caso en el que se quiera acceder desde web sin necesidad de instalar nada tan sólo debe indicar la siguiente URL: [Enlace al despliegue a pythonanywhere](http://ivamorgra.pythonanywhere.com/) 

Por otro lado, si el usuario prefiere tener el sistema instalado en consola, deberá hacer uso de Docker Hub para poder descargar la imagen y lanzarla. Para ello debe hacer lo siguiente: 

    1. Iniciar sesión con una cuenta de Docker 

    2. Descargarse la imagen desde consola mediante el comando docker pull nombre_imagen 

    3. Lanzar la imagen con el comando docker run rafsanesp/innograma:[tag] (El tag por defecto de la última versión es latest)

    4. Acceder a cualquier navegador web e indicar la siguiente url en la barra de navegación: localhost:8000 

Si se quiere hacer build de la imagen del proyecto con Docker Compose

    1. Entrar en la carpeta base del proyecto si se quiere hacer un build del proyecto
    
    2. Ejecutar el siguiente comando:
    
```
docker build -t innograma:prueba . -f .\docker\Dockerfile
    
```
Si se quiere ejecutar el proyecto con Docker Compose:

Entrar en la carpeta docker-compose del proyecto y ejecutar el siguiente comando :
    
```
docker compose up
```
    
o si está situado fuera de la carpeta ejecutar el siguiente comando:
    
```
docker compose -f .\docker-compose\docker-compose.yml up
```

Para ejecutar el proyecto con Vagrant debe situarse dentro de la carpeta vagrant y ejecutar el comando:
```
vagrant up
```
   
## Cómo hacer cambios: 

A continuación, ejemplificaremos el caso de propuesta de cambio siguiente: Queremos añadir una imagen a cada ponencia y evento, para que estas aparezcan en una página nueva que sirva de galería de jornadas de otros años en caso de que se marcaran como destacadas. 

Asumiremos que el miembro encargado de la tarea no tiene descargado el repositorio todavía. Para inicializarlo, entrará en la carpeta donde quiera clonar el repositorio y accederá a la consola de comandos escribiendo “cmd” en la barra de búsqueda y pulsando Enter. Una vez en la consola, escribirá el siguiente comando: 
```
git clone https://github.com/Rafasana14/Innograma.git 
```

Esto le creará una carpeta asociada al repositorio de GitHub. A continuación, entrará a dicha carpeta y abrirá la consola de comandos de nuevo. Aquí escribirá el comando 
```
	git checkout task-037 
```
De esta forma, cambiará a la rama de la tarea 37 que se le ha asignado. A continuación, abrirá su entorno de desarrollo (nosotros hemos usado Visual Studio Code) y abrirá la carpeta del repositorio en él. Tras ello, deberá crear un entorno virtual. Primero deberá instalar virtualenv y virtualenwrapper: 
```
pip install virtualenvwrapper-win 
```
Tras ello, se descargará el instalador de PostgreSQL desde su página y lo instalará, A continuación creará el entorno virtual con el siguiente comando: 
```
	virtualenv Innograma 
```
Y lo activará con 
```
.Innograma\Scripts\activate 
```
Entonces, instalará Django y Psycog2: 
```
	pip install Django 

	pip install psycopg2 
```
Entonces comenzará el proyecto mediante: 
```
	Django-admin startproject innograma. 
```
Tras ello, accederá al al archivo settings.py y lo modificará para que quede asi: 
```
DATABASES = {‘default’:  

{‘ENGINE’: ‘django.db.backends.postgresql_psycopg2’, 

‘NAME’: ‘innograma’, 

‘USER’: ‘admin’,‘ 

PASSWORD’: ‘password’, 

‘HOST’: ‘localhost’, 

‘PORT’: ‘’,}} 
```
Tras ello creará un superuser mediante el comando 
```
	python manage.py createsuperuser 
```
Y finalmente, correrá el sevidor con 
```
	python manage.py runserver 
```
Una vez comprobado que todo ha funcionado correctamente, el entorno vitual estará creado. 

 

Antes de comenzar a programar, el miembro del equipo creará una issue del tipo de nueva funcionalidad (Etiqueta FEAT). En ella se incluirá la siguiente información: 

 
```
Título: [FEAT] Task-037: Imágenes destacadas de eventos y ponencias 

Descripción:  

¿Está funcionalidad está asociada a un problema? Por favor, descríbelo. 

La funcionalidad no está asociada a un problema.  

Describe la solución que te gustaría 

La solución deseada consiste en la inclusión de un campo “url_imagen” en el modelo de eventos y de ponencias, y de un campo booleano “destacado”. Las imágenes de las ponencias y eventos con ese campo verdadero aparecerán en una página destinada a ello, que filtre las imágenes por año. 

Describe alternativas que hayas considerado 

Como alternativa, podría hacerse que esas imágenes destacadas aparezcan en la vista de bienvenida, en lugar de emplear una vista nueva. 

Contenido adicional 

No aplica. 

```

Una vez redactado su contenido, se le asignarán uno o varios responsables, y una etiqueta de prioridad “medium priority” y una de “new”, y se colocará la issue en el tablero del proyecto en la columna “To Do”. Tras esto, el miembro del equipo que haya creado la issue creará una rama de nombre “task-037” para dicha tarea. 

Cuando uno de los responsables decida encargarse de la tarea, cambiará el tag “new” por el tag “accepted”. Y una vez comience a implementarla, moverá la issue a la columna de “In Progress” y cambiará el tag “accepted” por “started”. A partir de aquí comenzaría el proceso de producción, que se explicará en el apartado de Ejercicio de Propuesta de Cambio. 

 

Una vez creado el entorno virtual, se accederá a él mediante los siguientes comandos: 
```
	.Innograma\Scripts\activate 
```
Y se arrancará el servidor mediante los comandos: 
```
	cd innograma 

	python manage.py runserver --settings=Innograma.settings.local    
```
A continuación, se accederá a la aplicación mediante el enlace 
```
	http://127.0.0.1:8000/ 
```
Una vez todo esto haya funcionado correctamente, se comenzará a implementar el cambio en local. 

Tras haber realizado todo el código necesario, el encargado de la tarea subirá los cambios a la rama de la tarea de la siguiente forma: 

Primero verificará que los cambios que va a subir son los correctos con 
```
	git status 
```
Después añadirá los cambios mediante el comando 
```
	git add . 
```
O con 
```
	git add <archivo> 
```
A continuación, podrá revisar de nuevo mediante git status que todo está en orden, y hará el siguiente commit: 
```
	Git commit –m “Code(task-037): Imágenes destacadas de eventos y ponencias” -m “Añade al modelo de eventos y ponencias los atributos Destacado y url_imagen y crea una vista para ver las imágenes de los eventos y ponencias destacados.” 
```
Tras este commit, se subirán los cambios mediante 
```
	git push 
```
A continuación, el encargado deberá entrar al repositorio en el navegador y crear una pull request a develop para su commit. Al crearla indicará que la pull request es a la rama develop, y asignará a uno o varios encagados para su revisión. Por último, cambiará la issue de la tarea a la columna del tablero llamada “In Review”. 


