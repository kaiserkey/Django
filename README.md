# Django

# Introduccion
Django es un framework de código abierto para el desarrollo de aplicaciones web en el lenguaje de programación **Python**. Proporciona herramientas para el desarrollo de aplicaciones web seguras, estables y escalables. Está diseñado para permitir un **desarrollo ágil** y para facilitar la creación de aplicaciones web complejas con una **cantidad mínima de código**.

Django se basa en el patrón de arquitectura **Modelo-Vista-Controlador (MVC)**, es un patrón de diseño de software ampliamente utilizado en el desarrollo de aplicaciones web. Está compuesto por tres componentes principales: 

Modelo: El modelo es responsable de administrar los datos de la aplicación. Se encarga de acceder a los datos almacenados en la base de datos y presentarlos en un formato adecuado para su uso por parte de la aplicación. 

Vista: La vista es responsable de mostrar los datos al usuario. Esto incluye el diseño de la interfaz de usuario, así como la lógica necesaria para presentar los datos al usuario. 

Controlador: El controlador es responsable de manejar las solicitudes del usuario. Esto incluye la lógica que se ejecuta cuando el usuario interactúa con la aplicación. Esto también incluye el procesamiento de los datos enviados por el usuario y la comunicación con el modelo para recuperar los datos necesarios. 

Django utiliza el patrón MVC para construir sus aplicaciones. Esto significa que los desarrolladores deben dividir su código en los tres componentes principales del patrón. Esto les permite separar la lógica de presentación de la lógica de la aplicación y hacer que el código sea más fácil de mantener. Django ofrece una serie de características especiales, como una interfaz de administración para gestionar los datos de la aplicación, un sistema de plantillas para mejorar la presentación de datos en la aplicación, un sistema de autenticación para gestionar usuarios y contraseñas, así como un sistema de control de acceso a la información para controlar qué usuarios pueden acceder a qué datos.

### Ventajas

1. Facilidad de uso: Django es un marco web fácil de usar e intuitivo, y tiene una curva de aprendizaje muy suave. Está diseñado para ayudar a los desarrolladores a construir aplicaciones web de calidad rápidamente y con menos esfuerzo.

2. Personalizable: Django se puede personalizar fácilmente para satisfacer las necesidades de cualquier proyecto. Esto significa que es fácil de adaptar a las necesidades específicas de un proyecto sin tener que escribir código desde cero.

3. Escalabilidad: Django es un marco web escalable. Esto significa que se puede escalar fácilmente para manejar una gran cantidad de tráfico o datos.

4. Seguridad: Django incorpora una variedad de funciones de seguridad que ayudan a proteger las aplicaciones web de los ataques externos. Esto incluye APIs de autenticación, control de acceso, encriptación de contraseñas y protección contra inyección de código.

5. Comunidad: Django tiene una gran comunidad de desarrolladores que pueden ayudar a responder preguntas y proporcionar consejos útiles. Además, hay una amplia variedad de recursos, tutoriales y documentación disponibles para ayudar a los desarrolladores a aprender Django.

### Historia

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
    
    **pip install virtualenv**<br>
    **viartualenv nombre_entorno_venv**<br>
    
    Esto ayuda a aislar el proyecto y evitar conflictos entre bibliotecas y versiones.
    Un entorno virtual crea una carpeta con todos los archivos y bibliotecas necesarios para el proyecto. Esta carpeta es aislada del sistema y puede tener una versión de Python específica, así como otros paquetes y bibliotecas específicas para el proyecto. Esto significa que el proyecto no se ve afectado por los cambios que se hacen en otros proyectos.


4. Activar el entorno virtual
   Después de crear el entorno virtual, necesita activarlo. Esto se puede hacer ejecutando el siguiente comando en la línea de comandos de Ubuntu:
   **. nombre_del_entorno/bin/activate**
   En caso de no tener permisos: **chmod +x first_django_env/bin/activate**
   PD: para seactivarlo usa el comando **deactivate**

5. Crear una aplicación Django
   Ahora, necesita crear una aplicación Django. Esto se puede hacer ejecutando el siguiente comando en la línea de comandos de Ubuntu:
    **django-admin startproject nombre_de_la_aplicación**<br>
    **django-admin startproject nombre_de_la_aplicación .**<br>
    Esta sintaxis con el punto al final indica que el proyecto Django se creará en el directorio actual. Si no se usa el punto, Django creará un directorio con el nombre especificado y luego creará el proyecto dentro de este directorio.

   Django startapp es una herramienta de la línea de comandos de Django que se usa para crear una nueva aplicación de Django. Esta herramienta genera una estructura de directorios y archivos predeterminada para una aplicación de Django, que le permite comenzar a desarrollar rápidamente. Esta estructura incluye archivos como models.py, views.py, urls.py y forms.py, entre otros. Estos archivos definen la lógica de la aplicación de Django y ayudan a los desarrolladores a ahorrar tiempo y esfuerzo al comenzar un nuevo proyecto.

   **python manage.py startapp nombre_de_la_app**<br>

6. Configurar la aplicación Django
   Una vez creada la aplicación Django, necesita configurarla para que funcione correctamente. Esto se puede hacer ejecutando los siguientes comandos en la línea de comandos de Ubuntu:

   **python manage.py makemigrations nombre_proyecto**<br>
   **python manage.py migrate**<br>
   **python manage.py createsuperuser**<br>

7. Ejecutar la aplicación Django
   Una vez completada la configuración, puede ejecutar su aplicación Django. Esto se puede hacer ejecutando el siguiente comando en la línea de comandos de Ubuntu:

   **python manage.py runserver**<br>
   **python manage.py runserver 3000**
   Elegir el puerto<br>

### EL Administrador de Contenido
El admin de Django es una herramienta de administración de contenido que proporciona una interfaz de usuario web para administrar aplicaciones, bases de datos y contenidos. El admin de Django le permite al usuario realizar tareas tales como crear y modificar objetos, administrar usuarios, trabajar con contenido multimedia, gestionar datos, etc. El admin de Django es una de las características más populares de la plataforma y le permite a los usuarios administrar y controlar contenidos web de una manera mucho más eficiente.

### El ORM de Django
Django ORM es un sistema de mapeo de objetos relacional de Django que proporciona una interfaz de alto nivel para interactuar con la base de datos. Se basa en SQLAlchemy y proporciona una solución de alto nivel para gestionar y consultar bases de datos. El ORM de Django proporciona una forma sencilla y eficiente de realizar operaciones CRUD (crear, leer, actualizar y eliminar) en la base de datos. Esto ayuda a los desarrolladores a ahorrar tiempo y esfuerzo al escribir código SQL complejo. El ORM también le permite crear consultas y relaciones entre tablas, lo que hace que la manipulación de datos sea más fácil y eficiente.


### Administracion de Bases de Datos
Django proporciona su propia herramienta de administración de bases de datos, llamada la Herramienta de administración de bases de datos de Django (Django Database Administration Tool, o DAT). Esta herramienta se incluye con Django y es la herramienta recomendada para administrar la base de datos de tu proyecto Django. Está diseñada para ser fácil de usar y proporciona una interfaz gráfica para la gestión de las bases de datos. Esta herramienta tiene muchas funciones útiles, como la ejecución de consultas SQL, la creación de tablas de la base de datos y la gestión de usuarios de la base de datos.

Puedes acceder a la Herramienta de administración de bases de datos de Django (DAT) desde la línea de comando. Si estás usando la versión estándar de Django, puedes ejecutar el comando:

python manage.py dbshell

Esto abrirá una ventana de la Herramienta de administración de bases de datos de Django. Desde aquí, puedes ejecutar comandos SQL y administrar tu base de datos.

### Templates Django
Jinja2 es un motor de plantillas para Python creado para reemplazar al motor de plantillas de Django llamado Django Template Language (DTL). Está diseñado para ser un motor de plantillas moderno y flexible, con una sintaxis limpia y una gran cantidad de características. Las plantillas de Jinja2 se encuentran entre los motores de plantillas más populares y son ampliamente utilizadas en la comunidad de desarrollo de Django.

Jinja2 se utiliza para generar HTML dinámico en una aplicación de Django. Los desarrolladores pueden utilizar el lenguaje de plantillas de Jinja2 para crear plantillas HTML estáticas o dinámicas. Las plantillas dinámicas pueden contener variables, bucles, condiciones y otros elementos de programación de Python. Esto permite a los desarrolladores crear plantillas HTML dinámicas que se actualizan según los cambios en una aplicación de Django.

El motor de plantillas de Jinja2 también ofrece una gran cantidad de extensiones para facilitar la creación de plantillas HTML. Estas extensiones incluyen filtros, macros, variables, funciones y otros elementos que pueden ayudar a los desarrolladores a crear plantillas HTML más limpias y eficientes. Estas extensiones también permiten a los desarrolladores escribir código HTML más corto y conciso.

En resumen, Jinja2 es un motor de plantillas moderno, flexible y potente que se utiliza para generar HTML dinámico en una aplicación de Django. Ofrece una gran cantidad de características y extensiones que pueden ayudar a los desarrolladores a crear plantillas HTML dinámicas limpias, concisas y eficientes.

Los templates de Django son plantillas de código HTML que se utilizan para crear la interfaz de usuario de una aplicación web. Estas plantillas se pueden completar con lógica y datos proporcionados por el lenguaje de programación Python. Esto permite a los desarrolladores proporcionar una interfaz personalizada para cada usuario.

Los siguientes son algunos de los códigos de Python más comunes que se utilizan en los templates de Django:

- {% if %}: Este código se utiliza para evaluar una condición booleana y realizar una acción si la condición se cumple. Por ejemplo, si se desea mostrar un mensaje si un usuario está conectado, se puede usar el siguiente código: ```{% if user.is_authenticated %} Bienvenido, {{ user.username }}. {% endif %}```

- {% for %}: Esta etiqueta se utiliza para iterar sobre una lista o conjunto de datos. Por ejemplo, si se desea mostrar una lista de usuarios, se puede usar el siguiente código: ```{% for user in users %} <p>{{ user.name }}</p> {% endfor %}```

- {% include %}: Esta etiqueta se utiliza para incluir otro template en el template actual. Esto puede ser útil si se desea reutilizar código en varios templates. Por ejemplo, si se desea incluir una plantilla que contiene un encabezado en todas las páginas, se puede usar el siguiente código: ```{% include 'header.html' %} ```

- {% static %}: Esta etiqueta se utiliza para incluir archivos estáticos en un template. Por ejemplo, si se desea incluir una imagen, se puede usar el siguiente código: ```<img src="{% static 'image.jpg' %}" >```

- {% url %}: Esta etiqueta se utiliza para generar una URL a partir del nombre de una vista. Esto facilita mucho la navegación entre páginas. Por ejemplo, si se desea generar un enlace a una página de inicio, se puede usar el siguiente código: ```<a href="{% url 'home' %}"> Inicio </a>```

- Variables: Las variables se utilizan para almacenar valores. Por ejemplo, para almacenar el nombre de un usuario en una variable:
```{% set user_name = 'John Doe' %}``` 

- Funciones: Las funciones se utilizan para realizar tareas complejas. Por ejemplo, para obtener una lista de elementos únicos de una lista:

```{{ unique_list(names) }}```

- Macros: Las macros se utilizan para crear fragmentos de código reutilizables. Por ejemplo, para crear una macro para mostrar una lista de elementos:

```
    {% macro list_items(items) %}
        <ul>
        {% for item in items %}
            <li>{{ item }}</li>
        {% endfor %}
        </ul>
    {% endmacro %}
```

-  Filtros: Los filtros se utilizan para aplicar transformaciones a datos. Por ejemplo, para convertir una cadena de texto a mayúsculas:

```{{ name | upper }}```

### La estructura de Carpetas Django

```
<nombre_proyecto>/
    manage.py
    <nombre_proyecto>/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    apps/
        <nombre_app_1>/
            __init__.py
            admin.py
            apps.py
            models.py
            tests.py
            views.py
        <nombre_app_2>/
            ...
    static/
        <static_root>
    templates/
        <plantillas_html>
    requirements.txt
```

* **manage.py:** Archivo que contiene código de Python para configurar el entorno de ejecución de la aplicación.

* **nombre_proyecto/__init__.py:** Archivo vacío para marcar este directorio como un módulo de Python.

* **nombre_proyecto/settings.py:** Archivo de configuración que contiene los parámetros para la ejecución de la aplicación.

* **nombre_proyecto/urls.py:** Archivo de configuración de los patrones de URL de la aplicación.

* **nombre_proyecto/wsgi.py:** Archivo que contiene información para el servidor web para el despliegue de la aplicación.

* **apps/:** Directorio que contiene cada una de las apps de la aplicación.

* **static/:** Directorio que contiene los archivos estáticos de la aplicación.

* **templates/:** Directorio que contiene las plantillas HTML de la aplicación.

* **requirements.txt:** Archivo que contiene una lista de las dependencias del proyecto.

### Otras Heramientas de Django

**python3.10 manage.py shell**<br>

El shell de Django se usa para realizar operaciones interactivas en la línea de comandos con el fin de probar y depurar código, interaccionar con el ORM de Django, ejecutar scripts, y ejecutar consultas directamente a la base de datos. Esto facilita la tarea de los desarrolladores cuando trabajan con Django, ya que pueden interactuar con el marco de forma directa desde la línea de comandos.

Los QuerySets de Django son una colección de objetos de modelo que se pueden recuperar de la base de datos. Se usan para buscar, filtrar, modificar y eliminar registros de la base de datos. Los QuerySets se pueden encadenar para aplicar filtros y transformaciones a los datos recuperados. Esto permite una gran flexibilidad para recuperar y manipular datos desde la base de datos.

Los QuerySets de Django se pueden usar para recuperar objetos de modelo desde la base de datos. Esto se hace mediante la API de consultas del modelo. Por ejemplo, si desea recuperar todos los usuarios de la base de datos, puede usar el siguiente código:

users = User.objects.all()

Esto devuelve un QuerySet de objetos User que contiene todos los usuarios en la base de datos. Los QuerySets se pueden encadenar para aplicar filtros y transformaciones a los datos recuperados. Por ejemplo, para recuperar sólo los usuarios con un campo de edad específico:

young_users = User.objects.filter(age=18)

También se pueden usar para crear, actualizar y eliminar registros en la base de datos. Por ejemplo, para crear un nuevo usuario:

new_user = User.objects.create(name="John Doe")

Para actualizar un usuario existente:

User.objects.filter(name="John Doe").update(age=20)

Y para eliminar un usuario:

User.objects.filter(name="John Doe").delete()

Los queryset mas usados de django son:

* all(): Recupera todos los objetos del modelo.
* filter(): Recupera un subconjunto de objetos del modelo basado en una consulta.
* exclude(): Recupera un subconjunto de objetos del modelo excluyendo los que cumplan con ciertos criterios.
* get(): Recupera un objeto único a partir de su ID.
* order_by(): Ordena los resultados de la consulta según uno o más campos.
* distinct(): Devuelve una lista de objetos únicos.
* values(): Devuelve una lista de diccionarios con los valores de los campos especificados.
* values_list(): Devuelve una lista de tuplas con los valores de los campos especificados.
* annotate(): Agrega campos calculados a los resultados de la consulta.
* aggregate(): Agrega resultados de funciones de agregación a una consulta.
* count(): Devuelve el número de objetos en la consulta.
* first(): Devuelve el primer objeto de la consulta.
* last(): Devuelve el último objeto de la consulta.
* exists(): Devuelve si hay o no objetos en la consulta.

