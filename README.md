# Proyecto-IV
Proyecto de la asignatura Infraestructura Virtual de 4º, Grado Ingeniería Informática de la Universidad de Granada.

## Descripción
Este proyecto pretende ofrecer un servicio de consulta de las estadísticas de jugadores de Overwatch.
Mediante el uso del BattleTag (o identificador de usuario) de un jugador podrás tener acceso a sus estadísticas, personajes más jugados, nº de victorias, etc. (Todo esto está condicionado a que el perfil del jugador sea público.)

## Licencia
[![AGPL](https://camo.githubusercontent.com/cb1d26ec555a33e9f09fe279b5edc49996a3bb3b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4147504c25323076332d626c75652e737667)](https://www.gnu.org/licenses/agpl.html)

## Instalación
- Clonar el repositorio:
```
git clone git@github.com:JmZero/Proyecto-IV.git
```

- Instalar todo lo requerido:
```
pip3 install -r requirements.txt
```

- Comprobar que pasa los test:
```
python3 test/test.py
```
- Ejecutar la aplicación:
```
python3 owstatistics-app.py
```
## Integración Continua
Para llevar a cabo la Integración Continua usaremos [Travis-CI](https://travis-ci.com/) como podemos ver en las herramientas. Esta estará vinculada a nuestro repositorio del proyecto.

### Travis [![Build Status](https://travis-ci.org/JmZero/Proyecto-IV.svg?branch=master)](https://travis-ci.org/JmZero/Proyecto-IV)

Se va a testear la clase [infojugador.py](https://github.com/JmZero/Proyecto-IV/blob/master/src/infojugador.py) que contiene una información básica sobre el perfil de jugador, su nombre y su tipo de perfil, así como funciones para consultar si el jugador existe, si el perfil es público o no y para añadir una nueva cuenta de usuario.

Para realizar los test tendremos que ejecutar el fichero [test.py](https://github.com/JmZero/Proyecto-IV/blob/master/test/test.py)
Para más información de cómo implementar la integración continua click [aquí](https://github.com/JmZero/Proyecto-IV/blob/master/doc/InteracionContinua.md)

### Depliegue por medio de Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

Una vez registrados en [Heroku](https://www.heroku.com/) y realizado el despliegue de nuestra aplicación podemos ver el resultado del mismo:
- [Despliegue](https://owstatistics-app.herokuapp.com/)

Para ver el proceso de despliegue click [aquí](https://github.com/JmZero/Proyecto-IV/blob/master/doc/DespliegueHeroku.md).

### Despliegue en Docker Hub

- Enlace al despliegue en Docker Hub: [Despliegue Docker Hub](https://hub.docker.com/r/jmzerox/proyecto-iv/)

- Enlace al despliegue en Heroku (con el contenedor): [Despliegue Heroku](https://owstatistics.herokuapp.com/)

Para ver el proceso de despliegue click [aquí](https://github.com/JmZero/Proyecto-IV/blob/master/doc/DespliegueDockerHub.md).
