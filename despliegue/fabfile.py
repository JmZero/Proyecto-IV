from fabric.api import *

#Se indica el host al que se va a conectar
env.hosts = ['owstatistics.westeurope.cloudapp.azure.com']
#Se define el nombre de usuario para conectarse a la MV
env.user = 'vagrant'

#Actualización de la versión del proyecto
def Actualizar():

    # Eliminamos la version anterior de la aplicación
    run('sudo rm -rf Proyecto-IV')

    # Actualizar a la nueva versión
    run('git clone https://github.com/JmZero/Proyecto-IV.git')

    # Instalar requirements
    run('pip3 install -r Proyecto-IV/requirements.txt')


def Iniciar():

     # Iniciar el servicio web
     with cd("Proyecto-IV/"):
         sudo('gunicorn owstatistics-app:app -b 0.0.0.0:80')
