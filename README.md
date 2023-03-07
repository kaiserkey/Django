# Django

# Introduccion
Django es un framework de código abierto para el desarrollo de aplicaciones web en el lenguaje de programación **Python**. Proporciona herramientas para el desarrollo de aplicaciones web seguras, estables y escalables. Está diseñado para permitir un **desarrollo ágil** y para facilitar la creación de aplicaciones web complejas con una **cantidad mínima de código**.

Django se basa en el patrón de arquitectura **Modelo-Vista-Controlador (MVC)**, y ofrece una serie de características especiales, como una interfaz de administración para gestionar los datos de la aplicación, un sistema de plantillas para mejorar la presentación de datos en la aplicación, un sistema de autenticación para gestionar usuarios y contraseñas, así como un sistema de control de acceso a la información para controlar qué usuarios pueden acceder a qué datos.

### Ventajas

1. Facilidad de uso: Django es un marco web fácil de usar e intuitivo, y tiene una curva de aprendizaje muy suave. Está diseñado para ayudar a los desarrolladores a construir aplicaciones web de calidad rápidamente y con menos esfuerzo.

2. Personalizable: Django se puede personalizar fácilmente para satisfacer las necesidades de cualquier proyecto. Esto significa que es fácil de adaptar a las necesidades específicas de un proyecto sin tener que escribir código desde cero.

3. Escalabilidad: Django es un marco web escalable. Esto significa que se puede escalar fácilmente para manejar una gran cantidad de tráfico o datos.

4. Seguridad: Django incorpora una variedad de funciones de seguridad que ayudan a proteger las aplicaciones web de los ataques externos. Esto incluye APIs de autenticación, control de acceso, encriptación de contraseñas y protección contra inyección de código.

5. Comunidad: Django tiene una gran comunidad de desarrolladores que pueden ayudar a responder preguntas y proporcionar consejos útiles. Además, hay una amplia variedad de recursos, tutoriales y documentación disponibles para ayudar a los desarrolladores a aprender Django.

###Historia

Django fue creado en el año 2003 por los programadores de Python **Adrian Holovaty** y **Simon Willison**, como una herramienta para ayudarles a desarrollar aplicaciones web. Holovaty y Willison habían trabajado juntos en el proyecto **World Online**, una red de sitios web conectados, y decidieron construir un marco de trabajo para acelerar el desarrollo de la red.

El nombre **Django** proviene del guitarrista de jazz, **Django Reinhardt**. El equipo de desarrollo lo eligió porque, como Reinhardt, se habían propuesto "abordar la programación web de una forma completamente nueva". El nombre también se aplicó porque los desarrolladores se inspiraron en el lenguaje de programación **Ruby on Rails** para diseñar Django.

El marco de trabajo se liberó de forma abierta al público en julio de 2005. Desde entonces, Django se ha convertido en uno de los frameworks de desarrollo web más populares para aplicaciones web basadas en Python.

### Aplicaciones

Django se utiliza para crear y desarrollar aplicaciones tales como blogs, sitios de medios sociales, plataformas de comercio electrónico, sistemas de gestión de contenido, etc. También se utiliza para crear aplicaciones empresariales y aplicaciones móviles. Algunos ejemplos de aplicaciones Django incluyen Instagram, Pinterest, The Washington Post, Disqus, NASA, etc.


### Instalacion y Configuracion

1. Instalar Python
   Primero, necesita instalar la versión de Python que desea utilizar. Esto se puede hacer ejecutando el siguiente comando en la línea de comandos de Ubuntu:
   **sudo apt-get install python3**

2. Instalar Django
   Ahora, necesita instalar Django. Esto se puede hacer ejecutando el siguiente comando en la línea de comandos de Ubuntu:
   **pip install django**
   **django-admin --version**
   Version LTS:**pip install Django==3.2** 

3. Crear un entorno virtual
   Después de instalar Django, necesita crear un entorno virtual para su proyecto. Esto se puede hacer ejecutando el siguiente comando en la línea de comandos de Ubuntu:

   **python3.10 -m venv nombre_del_entorno**
    
    Esto ayuda a aislar el proyecto y evitar conflictos entre bibliotecas y versiones.
    Un entorno virtual crea una carpeta con todos los archivos y bibliotecas necesarios para el proyecto. Esta carpeta es aislada del sistema y puede tener una versión de Python específica, así como otros paquetes y bibliotecas específicas para el proyecto. Esto significa que el proyecto no se ve afectado por los cambios que se hacen en otros proyectos.


4. Activar el entorno virtual
   Después de crear el entorno virtual, necesita activarlo. Esto se puede hacer ejecutando el siguiente comando en la línea de comandos de Ubuntu:
   **. nombre_del_entorno/bin/activate**
   En caso de no tener permisos: **chmod +x first_django_env/bin/activate**
   PD: para seactivarlo usa el comando **deactivate**

5. Crear una aplicación Django
   Ahora, necesita crear una aplicación Django. Esto se puede hacer ejecutando el siguiente comando en la línea de comandos de Ubuntu:
   
   **django-admin startproject nombre_de_la_aplicación**

6. Configurar la aplicación Django
   Una vez creada la aplicación Django, necesita configurarla para que funcione correctamente. Esto se puede hacer ejecutando los siguientes comandos en la línea de comandos de Ubuntu:

   **python manage.py makemigrations**
   **python manage.py migrate**
   **python manage.py createsuperuser**

7. Ejecutar la aplicación Django
   Una vez completada la configuración, puede ejecutar su aplicación Django. Esto se puede hacer ejecutando el siguiente comando en la línea de comandos de Ubuntu:

   **python manage.py runserver**
