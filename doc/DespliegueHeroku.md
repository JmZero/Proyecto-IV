# Despliegue en Heroku

En este apartado veremos con detenimiento como llevar a cabo el despliegue en [Heroku](https://www.heroku.com/), que es el PaaS elegido.

### Proceso
1. **Registrarse en [Heroku](https://www.heroku.com/)**

2. **Creación de la aplicación**
  ![newapp](https://github.com/JmZero/Proyecto-IV/blob/master/img/newapp.png)

3. **Despliegue**

  A la hora de realizar el despliegue tendremos que seleccionar la opción de **GitHub** que es donde estamos trabajando y activar la opción del despliegue automático como se muestra en la imagen.
  ![despliegue](https://github.com/JmZero/Proyecto-IV/blob/master/img/despliegue.png)

4. **Crear un archivo Procfile**

  Este archivo será necesario porque será el utilizado por **Heroku** para ejecutar nuestra aplicación.

  ```
  web: gunicorn owstatistics-app:app --log-file -
  ```

5. **Actualizar archivo requirements.txt**

  El archivo deberá de contener las dependencias de nuestra aplicación:

  ```
  Click==7.0
  Flask==1.0.2
  gunicorn==19.9.0
  ```

6. **Comprobar el despliegue de la aplicación**

  Para esto se dan las siguientes opciones:

  - [Principal](https://owstatistics.herokuapp.com/)
  - [Ejemplo Jugador Público](https://owstatistics.herokuapp.com/player/JmZero)
  - [Ejemplo Jugador Privado](https://owstatistics.herokuapp.com/player/Neim)
  - [Ejemplo Error](https://owstatistics.herokuapp.com/player/)
