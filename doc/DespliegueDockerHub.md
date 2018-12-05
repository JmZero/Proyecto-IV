# Despliegue en Docker

En este apartado veremos con detenimiento como llevar a cabo el despliegue en [Docker Hub](https://hub.docker.com/).

### Proceso
1. **Registrarse en [Docker Hub](https://hub.docker.com/)**

2. **Vincular con GitHub**

  En nuestro caso lo que queremos es que nuestro docker contenga el repositorio del proyecto que estamos diseñando.
  Para ello vincularemos nuestra cuenta de GitHub con Docker Hub.
  En nuestro perfir seleccionaremos la opción **Settings**  y una vez dentro seleccionaremos **Linked Accounts & Services** y vincularemos nuestra cuenta de GitHub.
  ![vinculacion](https://github.com/JmZero/Proyecto-IV/blob/master/img/vinculacion.png)

3. **Despliegue**

  A la hora de realizar el despliegue tendremos que seleccionar la opción **Create** y dentro de esta **Create Automated Build**. En este punto podremos seleccionar el repositorio del cual queremos hacer el despliegue entre todos los que tenemos en GitHub.
  ![create-dockerhub](https://github.com/JmZero/Proyecto-IV/blob/master/img/create-dockerhub.png)

  Una vez realizados estos paso ya tendremos nuestro despliegue en Docker.

  ![resultado-despliegue](https://github.com/JmZero/Proyecto-IV/blob/master/img/resultado-despliegue.png)

### Despliegue en Docker
Una vez configurado Docker procederemos al despliegue [Más información](https://docs.docker.com/get-started/)

Lo primero que tendremos que realizar es la creación de un archivo **Dockerfile** en nuestro repositorio que será el encargado de definir el contenedor.

EL contenido de **Dockerfile** es el siguiente:

```
# Imagen de Python a usar
FROM python:3.6-alpine

# Directorio de alojamiento de la aplicación
WORKDIR /app

# Copiar los contenido del resositorio actucal al de la aplización
COPY . /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Instalar las librerias necesarias de requirements.txt
RUN pip install -r requirements.txt

# Run app.py when the container launches
CMD gunicorn owstatistics-app:app --log-file -
```

**Nota: se ha decidido utilizar la imagen alpine ya que la versión por defecto es demasiado grande. Para más información consulte ![aquí](https://github.com/jfloff/alpine-python#why)**

Vamos a realizar directamente el despliegue del contenedor en Heroku, como ya habiamos realizado anteriormente desde GitHub.

Para ello debemos especificarle a Heroku que lo que vamos a desplegar es un contenedor y para ello crearemos un archivo **heroku.yml** que le indicará a Heroku como ha de construir el contenedor y como ejecutarse desde el Dockerfile.

```
build:
  docker:
    web: Dockerfile
run:
  web: gunicorn owstatistics-app:app --log-file -
```

Tras esto crearemos una nueva app en Heroku para la prueba, en este caso **owstatistics**.

Crearemos un contenedor en local con el mismo nombre de la nueva app para evitar errores, y este a su vez será el que despleguemos.

```
docker build -t owstatistics .
```

Para realizar el despliegue seguiremos los pasos que nos da Heroku:
![proceso-despliegue](https://github.com/JmZero/Proyecto-IV/blob/master/img/proceso-despliegue.png)

Si todo ha ido bien podremos comprobar que la imagen subida corresponde a un despliegue por contenedor.
![desplegar-contenedor](https://github.com/JmZero/Proyecto-IV/blob/master/img/desplegar-contenedor.png)
