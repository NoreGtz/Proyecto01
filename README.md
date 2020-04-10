# Proyecto01

IMPORT.PY
Como su nombre lo indica, se encarga de importar los libros almacenados en el archivo Books.csv

APPLICATION.PY
Aquí se llevan a cabo todas las consultas y modificaciones a las tablas de la base de datos (SELECT, INSERT INTO)
También es donde se maneja la conexión y se establece que hace cada función y a cual ruta pertenece.
Almacena variables que son necesarias en el proyecto.

/
El proyecto se llama Once Upon A Book? (¿Había una vez un libro?)
Al iniciar se puede acceder a dos vistas según sea el caso; la primera opción es que si no se ha iniciado 
se redirige a la página "registrar.html", en caso contrario, es decir si ya se ha iniciado sesión, se 
redirige al "index.html".

REGISTRAR
Dentro de esta página se presenta un formulario que pide que se ingrese un nombre de usuario, el correo 
electronico y la contraseña (2 veces). Cuando se registra al usuario se carga la página del "login.html"
para que aceda. 

Nota: No quise iniciar directamente, deseaba que luciera más natural y por eso decidí que lo mande al 
"login.html" para que tenga más realismo, esto es en base a mi experiencia con diversas páginas web.

En la misma página se aprecia una opción que menciona que si ya está registrado puede ir directamente al 
"login.html"

LOGIN
Se muestra un formulario donde se pide el nombre de usuario y la contraseña para poder ingresar.
Al igual que en el "registrar.html" cuenta con la opción de mandar a registrar si aún no lo estaba.

Nota: la parte de mandar a registrar puede producir error.

INDEX
En el index existe un navbar que comparte con la mayoría de los archivos html a exepción del LOGIN y el REGISTRAR.
Se muestra el usuario que está en sesión (dato obtenido del login)

REVIEWS
Simplemente muestra todos los review que se han hecho. 
Cada review contiene el nombre del usuario (junto a un icono en formato svg), el libro al que se le hizo el review, 
el comentario y la calificación convertida en estrellas.

SEARCH A BOOK
Simplemente es un buscador, donde se puede introducir el isbn, el título o el autor para buscar el libro. Da resultados
aunque se introduzca solamente una letra.

Los resultados de la busqueda muestran el nombre de los libros, el cual es un enlace que lleva a la información de dicho libro.

BOOK
En esta página se presenta la información del libro que fue elegido en SEARCH A BOOK. 
Muestra el título del libro, su isbn, el autor y el año de publicaciónn.

También se puede observar los review que se han hecho respecto a ese libro y permite crear una.
Al crear un review se guarda el nombre de usuario para añadirlo a la información del review, también se almacena el isbn del libro,
el comentario y la calificación, esta ultima es en base a cuantas estrellas se seleccionen (va de 1 a 5 estrellas).

ALLBOOKS
Muestra todos los libros existentes en la base de datos, cada libro es representado por el título y este funciona como enlace al igual
que en SEARCH A BOOK.

ONEBOOK
Está conectado a ALLBOOKS y es el resultado del enlace elegido, presenta la información del libro (título, isbn, autor y año de
publicación) además, cuenta con la opción de hacer un review sobre dicho libro.

PRUEBA
No hay mucho que explicar al respecto ya que, como su nombre lo indica, sólo se usó con el fin de realizar pruebas al proyecto.

LOGO E IMG
El logo fue diseñado por mí en el programa Inkscape, al igual que el icono de los reviews.


STATIC
Dentro de la carpeta static están guardados todos los recursos necesarios (css y svg)



