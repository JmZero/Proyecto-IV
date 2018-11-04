# Proyecto-IV
Proyecto de la asignatura Infraestructura Virtual de 4º, Grado Ingeniería Informática de la Universidad de Granada.

## Descripción
Este proyecto pretende ofrecer un servicio de consulta de las estadísticas de jugadores de Overwatch.
Mediante el uso del BattleTag (o identificador de usuario) de un jugador podrás tener acceso a sus estadísticas, personajes más jugados, nº de victorias, etc. (Todo esto está condicionado a que el perfil del jugador sea público.)

## Licencia
[![AGPL](https://camo.githubusercontent.com/cb1d26ec555a33e9f09fe279b5edc49996a3bb3b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4147504c25323076332d626c75652e737667)](https://www.gnu.org/licenses/agpl.html)

[![Build Status](https://travis-ci.org/JmZero/Proyecto-IV.svg?branch=master)](https://travis-ci.org/JmZero/Proyecto-IV)

## Herramientas
* El lenguaje que utilizaremos para implementar el proyecto será [Python](https://www.python.org/). Se ha escogido este lenguaje dado que está en auge y últimamente es muy requerido su conocimiento.
* Como framework se utilizará [Hug](http://www.hug.rest). Esto está sustentado por una recomendación del profesor de la asignatura, JJMerelo.
* La base de datos que usaré para almacenar todos los datos se llevará a cabo usando [MySQL](https://www.mysql.com/) o [MariaDB](https://mariadb.org/)
* Como editor de texto se usará [Atom](https://atom.io/)
* Para realizar el testeo utilizaremos la biblioteca **unittest**.
* En este punto del proyecto los datos estarán almacenados de manera estática, por lo que utilizaremos ficheros *JSON*.
* Los test se harán haciendo uso de [Travis-CI](https://travis-ci.com/).

##Integración Continua
La integración continua consiste en la integración de los cambios hechos en el proyecto en el momento en el que estén y estos hayan pasado los test.
Como ya se ha mencionado antes usaremos Travis-CI para realizar la integración.
Se va a testear la clase [infojugador.py](https://github.com/JmZero/Proyecto-IV/blob/master/src/infojugador.py) que contiene una información básica sobre el perfil de jugador, su nombre y su tipo de perfil, así como funciones para consultar si el jugador existe, si el perfil es público o no y para añadir una nueva cuenta de usuario.
Para realizar los test tendremos que ejecutar el fichero [test.py](https://github.com/JmZero/Proyecto-IV/blob/master/src/test.py)
Para mas información de como implementar la integración continua click [aquí](https://github.com/JmZero/Proyecto-IV/blob/master/doc/InteracionContinua.md)
