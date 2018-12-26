# Despliegue de la aplicación en la nube

En este apartado se verá con detenimiento cómo llevar a cabo el despliegue en la nube. Para facilitarlo lo dividiremos en tres puntos:
* Provisionamiento
* Creación de la maquina virtual
* Despliegue

## 1. Provisionamiento
Para llevar a cabo el provisionamiento se hará uso de **Ansible**, una herramienta que tratará la configuración de la máquina virtual que crearemos para que esta cumpla los requisitos necesarios para el correcto funcionamiento de la aplicación.
En primer lugar se instalará **Ansible** en la máquina host y se configurará el archivo `/etc/ansible/hosts` para especificar qué host va a utilizar el archivo de provisionamiento. En el se deberá detallar una IP o un dominio de la siguiente manera:
```
[owstatistics]
owstatistics.westeurope.cloudapp.azure.com
```
Se creará un archivo **playbook.yml**. En el describiremos la política que se debe aplicar a nuestra máquina virtual, como se ha dicho antes, para el correcto funcionamiento de la aplicación.
El archivo tendrá el siguiente contenido:
```
- hosts: all
  sudo: yes
  remote_user: jmzero

  tasks:
  - name: Añadir repositorio de python 3.6
    become: true
    apt_repository: repo=ppa:deadsnakes/ppa state=present

  - name: Actualizar sistema
    become: true
    command: sudo apt-get update

  - name: Instalar Python 3.6
    become: true
    apt: pkg=python3.6 state=present

  - name: Instalar pip3
    become: true
    command: sudo apt-get -y install python3-pip

  - name: Instalar GitHub
    become: true
    command: sudo apt-get install -y git

  - name: Clonar repositorio de GitHub
    git: repo=https://github.com/JmZero/Proyecto-IV.git dest=owstatistics/ force=yes

  - name: Instalar Requerimientos
    command: pip3 install -r owstatistics/requirements.txt
```

En primer lugar se definirá un item que en este caso se realizará para todos los host, y bajo este item se definirán las diferentes tareas a realizar, como son la instalación del lenguaje de python que necesitaremos, la instalación de GitHub o el clonado del repositorio.

## 2. Creación de la máquina virtual
Tras el provisionamiento, se procederá a crear y configurar la máquina virtual que alojaremos en [Azure](https://azure.microsoft.com/es-es/). En este caso se hará uso de Vagrant para la creación de la máquina virtual.

2.1. **Instalacion de Azure CLI y login en Azure**
En primer lugar se deberá instalar Azure CLI. Para ello se ha seguido los pasos que nos proporciona la web de Azure y que se puede encontrar [aquí](https://docs.microsoft.com/es-es/cli/azure/install-azure-cli-apt?view=azure-cli-latest). En mi caso me dio algunos problemas al instalarlo y [aquí](https://docs.microsoft.com/es-es/cli/azure/install-azure-cli-linux?view=azure-cli-latest) conseguí solucionarlo.
Una vez instalado tendremos que tener una cuenta en Azure y por tanto, estar registrados. Una vez registrados se procederá a ejecutar el comando `az login` en la terminal, el cual nos redirigirá para acceder a la cuenta de Azure que hemos creado.

![login_azure](https://github.com/JmZero/Proyecto-IV/blob/master/img/login_azure.png)

Se puede ver que los datos mostrados corresponden a la suscripción actual de Azure, en este caso una suscripción para estudiantes.

2.2. **Creación de Azure Active Directory con acceso a Azure Resource Manage**
Mediante el comando `az ad sp create-for-rbac` se creará un Azure Active Directory con acceso a Azure Resource Manager para la suscripción actual.

![aad_azure](https://github.com/JmZero/Proyecto-IV/blob/master/img/aad_azure.png)

2.3. **Exportación de variables de entorno**
Es recomendable, previa creación del archivo Vagrantfile, la exportacion de ciertas variables de entorno asociadas a Azure, estas serán las siguientes:
* AZURE_TENANT_ID = campo "tenant" del apartado anterior
* AZURE_CLIENT_ID = campo "appID" del apartado anterior
* AZURE_CLIENT_SECRET = campo "password" del apartado anterior
* AZURE_SUBSCRIPTION_ID = obtenido al ejecutar el comando `az account list --query "[?isDefault].id" -o tsv`

![variables_azure](https://github.com/JmZero/Proyecto-IV/blob/master/img/variables_azure.png)

Este paso y el anterior se realizan con el fin de no colocar en el archivo `Vagrantfile` que crearemos en el siguiente punto los valores de las variables directamente en él.

2.4. **Creación del archivo Vagrantfile**
LLegados a este punto se creará un archivo Vagrantfile, el cual tendrá la funcionalidad de construir y provisionar junto con el archivo `playbook.yml` la máquina virtual.
El archivo tendrá el siguiente contenido:
```
Vagrant.configure('2') do |config|
  config.vm.box = 'azure'

  config.ssh.private_key_path = '~/.ssh/id_rsa'
  config.vm.provider :azure do |azure, override|

    azure.tenant_id = ENV['AZURE_TENANT_ID']
    azure.client_id = ENV['AZURE_CLIENT_ID']
    azure.client_secret = ENV['AZURE_CLIENT_SECRET']
    azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']

    azure.vm_name = "owstatistics"
    azure.vm_size = "Standard_D2_v2"
    azure.tcp_endpoints = "80"
    azure.location = "westeurope"
    azure.admin_username = "jmzero"

  end

  config.vm.provision :ansible do |ansible|
      ansible.playbook = "provision/playbook.yml"
  end

end
```

En primer lugar tendremos que asignar las diferentes variables de entorno que creamos en el apartado anterior.
Tras esto se colocarán las variables relacionadas con la máquina, como son el nombre, el puerto, su tamaño(en este caso de proposito general), etc.
Por último se escribirá una función la cual tendrá como proposito el uso del archivo de provisionamiento que se habrá creado en el primer punto haciendo uso de **Ansible**.

2.5. **Instalación Vagrant-Azure**
Para poder desplegar la máquina virtual será necesario hacer uso de `vagrant-azure`, el cual se utiliza para desplegar una máquina virtual creada por Vagrant en Azure. Para su instalación ejecutaremos el comando `vagrant plugin install vagrant-azure` (En mi caso surgió un problema debido a la versión de Vagrant, por lo que es recomendable descargar e instalar la última versión disponible).

2.6. **Despliegue**
Para llevar a cabo el despliegue ejecutaremos el comando `vagrant up --provider=azure` en la carpeta donde se tenga el proyecto.
Para la creación de la máquina se hará uso del archivo Vagrantfile creado con anterioridad, de  tal forma que también se realizará el provisionamiento.

![vagrant_azure](https://github.com/JmZero/Proyecto-IV/blob/master/img/vagrant_azure.png)

Como se ve el proceso se ha realizado de forma correcta, aunque también podremos verificarlo en la cuenta de Azure.

![cuenta_azure](https://github.com/JmZero/Proyecto-IV/blob/master/img/cuenta_azure.png)

## 3. Automatización del Despliegue
Será de gran utilidad poder realizar todo el proceso de despliegue de forma automática. Para ello se hará uso de **Fabric**. Mediante el archivo `fabfile.py` se podran ejecutar una serie de ordenes que estarán definidas en este archivo y ejecutarán las ordenes correspondientes para la automatización.

El archivo tendrá el siguiente contenido:
```
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
```

Como se puede ver, se han definido dos funciones, una que se encargará de actualizar el repositorio, borrando el repositorio actual, conandolo desde GitHub e instalando todo lo requerido y la otra encargada de iniciar la aplicación mediante gunicorn.

Para poder ejecutar alguna función tendrá que usarse el comando `fab -f ./despliegue/fabfile.py -H vagrant@owstatistics.westeurope.cloudapp.azure.com "funcion"`

En estos ejemplos se muetra el funcionamiento de ambas funciones:

![fabfile1](https://github.com/JmZero/Proyecto-IV/blob/master/img/fabfile1.png)
![fabfile2](https://github.com/JmZero/Proyecto-IV/blob/master/img/fabfile2.png)

**NOTA: En caso de producirse algun error al ejecutar los comandos anteriores se recomienda cambiar la version de python a la 2.7**

Como resultado del proceso se podrá ver el funcionamiento de la aplicación mirando el DNS `http://owstatistics.westeurope.cloudapp.azure.com`

![dns_azure1](https://github.com/JmZero/Proyecto-IV/blob/master/img/dns_azure1.png)
![dns_azure2](https://github.com/JmZero/Proyecto-IV/blob/master/img/dns_azure2.png)
