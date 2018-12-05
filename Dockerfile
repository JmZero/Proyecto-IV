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
CMD gunicorn owstatistics-app:app
