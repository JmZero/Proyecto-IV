# Imagen de Python a usar
FROM python:3.6

# Directorio de alojamiento de la aplicación
WORKDIR /app

# Copiar los contenido del resositorio actucal al de la aplización
COPY . /app

# Instalar las librerias necesarias de requirements.txt
RUN pip install -r requirements.txt

# Establece el puerto 80 por defecto
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "owstatistics-app.py"]
