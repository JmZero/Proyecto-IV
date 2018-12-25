from fabric.api import *

def Actualizar():

    # Eliminamos la version anterior de la aplicación
    run('sudo rm -rf Proyecto-IV')

    # Actualizar a la nueva versión
    run('git clone https://github.com/JmZero/Proyecto-IV.git')

    # Instalar requirements
    run('pip3 install -r Proyecto-IV/requirements.txt')


def Iniciar():

     # Iniciar el servicio web
     run('cd Proyecto-IV/ && sudo gunicorn owstatistics-app:app -b 0.0.0.0:80')
