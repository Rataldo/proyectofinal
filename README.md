# proyecto final
###  de el curso de Python en Coder House comision 40450

Buenas, soy Rene Aranzaez esta es mi entrega de el proyecto final para el curso de Python hecho en el framework Django.
aqui dejo el link al video explicativo sobre el funcionamiento de mi pagina: https://www.youtube.com/watch?v=_G5fTPTYdMc

**debo mencionar que el link se encuentra oculto por lo que solo se puede acceder por medio de el link, no asi buscando el video directamente en youtube.**

## Pasos para trabajar con estre proyecto:

1. Primero tenemos que crear una carpeta para probar este repositorio en nuestro computador. hecho esto, ejecutamos en la terminal de nuestro editor lo siguiente:

```Python

pip install pipenv

```
con esto creamos el entorno virtual. luego ejecutamos:

```Python
pipenv shell
```

2. Una vez creado el entorno virutal tenemos que instalar DJANGO:
   vamos a la terminal y ejecutamos:
```Python
pip install django
```

3. Ahora tenemos que traer este repositorio a nuestro sistema:
   para traer el repo ejecutamos en la terminal:

  ***git clone https://github.com/Rataldo/proyectofinal.git***

4. Con esto tenemos que seleccionar la carpeta en la cual esta el proyecto:
```Python
cd proyectofinal
```

5. Una vez selecionada podemos correr el proyecto con el siguiente comando:

```Python
python manage.py runserver
```
una vez esta corriendo el servidor clickeamos en el link con la url que aparece o copiamos y pegamos la direccion
la cual en mi caso local es http://127.0.0.1:8000/

6. Cuando queramos terminar la ejecurcion del servidor solo debemos apretar CTRL+C estando en la terminal. asi terminaremos la ejecucion del servidor.



## Usuarios para pruebas en el servidor:

**Usuario admin:**

usuario: rene

contraseña: 123


**Usuario 1:**

usuario: Rataldo

contaseña: panconqueso123


**Usuario 2:**

usuario: Rataldo

contraseña: telefono2


**Usuario 3:**

usuario: prueba1

contraseña: testeando1


**Usuario 4:**

usuario: coderhouse

contraseña: rataldo20



# CASOS DE PRUEBA

## 1. Primer caso

### Un usuario recien registrado quiere agregar un Meme a la pagina:

- el usuario recien registrado debe clickear en la barra superior donde dice "Agregar Memes"
- al clickear aca sera redirigido a la pagina para agregar memes. solo debe llenar lo solicitado,
  colocar un Nombre al meme, subir la imagen y una pequeña descripcion.
- Una vez este subida la imagen el podra revisarlo en la ventana "Ver memes" o tambien
  puede confirmarlo en la ventana "Mis Memes" donde vera todos los que ha subido ademas de poder
  borrarlos o editarlos.



## 2. Segundo caso

### Usuario se equivoco a la hora de escribir nombre o descripcion de un meme y lo subio con este error:

- El usuario para poder corregir su error debe clickear en la barra superior donde dice: "Mis memes"
- una vez dentro de esta vista debe buscar entre sus memes el que tiene el error y clickear donde dice: "Editar meme"
- dentro de "Editar meme" podra cambiar el nombre y descripcion de este, si desea cambiar la imagen debera directamente
  borrar el meme y volver a subirlo.
- Una vez el haya corregido su error debera clickear en "Guardar cambios" y podra ver su correccion reflejada en
  "Mis memes" o tambien en "Ver memes"

## 3. Tercer Caso

PROXIMAMENTE














 
