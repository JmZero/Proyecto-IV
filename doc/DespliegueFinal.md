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
Para mas información consultar [aquí](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html).

Se creará un archivo **playbook.yml**. En el describiremos la política que se debe aplicar a nuestra máquina virtual, como se ha dicho antes, para el correcto funcionamiento de la aplicación.
El archivo tendrá el siguiente contenido:
```
- hosts: all          #Especifico la validez del archivo (en este caso para todos los host)
  become: yes           #Se permite el uso de sudo
  remote_user: jmzero #Especifico el usuaro de la máquina

  tasks:
    #Se añade un repositorio con la version 3.6 de python, indicando donde encontrarlo.
  - name: Añadir repositorio de python 3.6
    become: true
    apt_repository: repo=ppa:deadsnakes/ppa state=present

    #Se actualiza el sistema por el comando update
  - name: Actualizar sistema
    become: true
    command: sudo apt-get update

    #Se instala python3.6 en caso de no estar instalado
  - name: Instalar Python 3.6
    become: true
    apt: pkg=python3.6 state=present

    #Se instala pip3
  - name: Instalacion de pip3
    become: true
    command: sudo apt-get -y install python3-pip

    #Se instala git para poder hacer uso del repositorio de GitHub en caso de no estar instalado
  - name: Instalar GitHub
    become: true
    command: sudo apt-get install -y git

    #Se clona el repositorio de GitHub
  - name: Clonar repositorio de GitHub
    git: repo=https://github.com/JmZero/Proyecto-IV.git dest=owstatistics/ force=yes

    #Se instalan las dependencias necesarias para el proyecto
  - name: Instalar Requerimientos
    command: pip3 install -r owstatistics/requirements.txt
```

En primer lugar se definirá un item que en este caso se realizará para todos los host, y bajo este item se definirán las diferentes tareas a realizar, como son la instalación del lenguaje de python que necesitaremos, la instalación de GitHub o el clonado del repositorio.

Para más información de como realizar el archivo hacer uso de la guia propuesta por **Ansible** en el siguiente [enlace](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html)

## 2. Creación de la máquina virtual
Tras el provisionamiento, se procederá a crear y configurar la máquina virtual que alojaremos en [Azure](https://azure.microsoft.com/es-es/). En este caso se hará uso de Vagrant para la creación de la máquina virtual.

### 2.1. **Instalacion de Azure CLI y login en Azure**

En primer lugar se deberá instalar Azure CLI. Para ello se ha seguido los pasos que nos proporciona la web de Azure y que se puede encontrar [aquí](https://docs.microsoft.com/es-es/cli/azure/install-azure-cli-apt?view=azure-cli-latest). En mi caso me dio algunos problemas al instalarlo y [aquí](https://docs.microsoft.com/es-es/cli/azure/install-azure-cli-linux?view=azure-cli-latest) conseguí solucionarlo.
Una vez instalado tendremos que tener una cuenta en Azure y por tanto, estar registrados. Una vez registrados se procederá a ejecutar el comando `az login` en la terminal, el cual nos redirigirá para acceder a la cuenta de Azure que hemos creado.

![login_azure](https://github.com/JmZero/Proyecto-IV/blob/master/img/login_azure.png)

Se puede ver que los datos mostrados corresponden a la suscripción actual de Azure, en este caso una suscripción para estudiantes.

### 2.2. **Creación de una Azure Active Directory**

Mediante el comando `az ad sp create-for-rbac` se creará un Azure Active Directory con acceso a Azure Resource Manager para la suscripción actual.

![aad_azure](https://github.com/JmZero/Proyecto-IV/blob/master/img/aad_azure.png)

### 2.3. **Exportación de variables de entorno**

Es recomendable, previa creación del archivo Vagrantfile, la exportacion de ciertas variables de entorno asociadas a Azure, estas serán las siguientes:
* AZURE_TENANT_ID = campo "tenant" del apartado anterior
* AZURE_CLIENT_ID = campo "appID" del apartado anterior
* AZURE_CLIENT_SECRET = campo "password" del apartado anterior
* AZURE_SUBSCRIPTION_ID = obtenido al ejecutar el comando `az account list --query "[?isDefault].id" -o tsv`

![variables_azure](https://github.com/JmZero/Proyecto-IV/blob/master/img/variables_azure.png)

Este paso y el anterior se realizan con el fin de no colocar en el archivo `Vagrantfile` que crearemos en el siguiente punto los valores de las variables directamente en él.

### 2.4. **Creación del archivo Vagrantfile**

LLegados a este punto se creará un archivo Vagrantfile, el cual tendrá la funcionalidad de construir y provisionar junto con el archivo `playbook.yml` la máquina virtual.
El archivo tendrá el siguiente contenido:
```
#Se usara la version 2 del plugin azure-vagrant
Vagrant.configure('2') do |config|
  config.vm.box = 'azure' #Especificaremos este parametro para evitar errores en vagrant up y será la base para el funcionamiento.
  #Se usa la imagen especificada en urn en el apartado azure provider

  #Configuracion de la conexion a traves de ssh
  config.ssh.private_key_path = '~/.ssh/id_rsa'
  config.vm.provider :azure do |owstatistics, override| #Se crea una nueva variable owstatistics para darle información al proveedor de las variables
                                                        #necesarias para la creación de la máquina virtual

    #Exportación de las variables encargadas de identificar la cuenta de azure
    owstatistics.tenant_id = ENV['AZURE_TENANT_ID']
    owstatistics.client_id = ENV['AZURE_CLIENT_ID']
    owstatistics.client_secret = ENV['AZURE_CLIENT_SECRET']
    owstatistics.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']

    #Parametros adicionales de la máquina virtual
    owstatistics.vm_name = "owstatistics"    #Se da un nombre a la MV
    owstatistics.vm_size = "Standard_D2_v2"  #Se establece el tamaño a usar
    owstatistics.tcp_endpoints = 80          #Se establece el puerto el puerto 80 para la máquina
    owstatistics.location = "westeurope"     #Se establece la locacización de la MV
    owstatistics.admin_username = "jmzero"   #Se establece el nombre para el root de la máquina

  end

  #Se realiza el provisionamiento de la máquina
  config.vm.provision :ansible do |provision|
      provision.playbook = "provision/playbook.yml" #Provision de la MV
  end

end
```

En primer lugar tendremos que asignar las diferentes variables de entorno que creamos en el apartado anterior.
Tras esto se colocarán las variables relacionadas con la máquina, como son el nombre, el puerto, su tamaño(en este caso de proposito general), etc.
Por último se escribirá una función la cual tendrá como proposito el uso del archivo de provisionamiento que se habrá creado en el primer punto haciendo uso de **Ansible**.

### 2.5. **Instalación Vagrant-Azure**
Para poder desplegar la máquina virtual será necesario hacer uso de `vagrant-azure`, el cual se utiliza para desplegar una máquina virtual creada por Vagrant en Azure. Para su instalación ejecutaremos el comando `vagrant plugin install vagrant-azure` (En mi caso surgió un problema debido a la versión de Vagrant, por lo que es recomendable descargar e instalar la última versión disponible).

### 2.6. **Despliegue**
Para llevar a cabo el despliegue ejecutaremos el comando `vagrant up --provider=azure` en la carpeta donde se tenga el proyecto.
Para la creación de la máquina se hará uso del archivo Vagrantfile creado con anterioridad, de  tal forma que también se realizará el provisionamiento.

![vagrant_azure](https://github.com/JmZero/Proyecto-IV/blob/master/img/vagrant_azure.png)

Como se ve el proceso se ha realizado de forma correcta, aunque también podremos verificarlo en la cuenta de Azure.

![cuenta_azure](https://github.com/JmZero/Proyecto-IV/blob/master/img/cuenta_azure.png)

Para realizar este proceso se han seguido los pasos explicados por la cuenta de **Azure** de GitHub, para mas informaciación click [aquí](https://github.com/Azure/vagrant-azure). Se explica detalladamente en cada línea del vagrantfile lo que hace gracias a la documentación mencionada antes y a cieta información propuesta por el profesor de la asignatura como la [siguiente](https://stackoverflow.com/questions/7065421/could-implicit-topics-be-implemented-cleanly-in-a-language/7066007#7066007).

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
     run('sudo gunicorn owstatistics-app:app -b 0.0.0.0:80')
```

Como se puede ver, se han definido dos funciones, una que se encargará de actualizar el repositorio, borrando el repositorio actual, conandolo desde GitHub e instalando todo lo requerido y la otra encargada de iniciar la aplicación mediante gunicorn.

Para poder ejecutar alguna función tendrá que usarse el comando `fab -f ./despliegue/fabfile.py -H vagrant@owstatistics.westeurope.cloudapp.azure.com "funcion"`

Para mas información a cerca de usar **Fabric** consulte [aquí](https://www.digitalocean.com/community/tutorials/how-to-use-fabric-to-automate-administration-tasks-and-deployments) o [aquí](http://docs.fabfile.org/en/1.14/tutorial.html). Para ver también como realizar un fabfile ademas he consultado a un compañero que cursó la asignatura con anteridad para averiguar la estructura que debería seguir el archivo. Adjunto el GitHub del compañero [JaoChaos](https://github.com/JaoChaos).

En estos ejemplos se muetra el funcionamiento de ambas funciones:

![fabfile1](https://github.com/JmZero/Proyecto-IV/blob/master/img/fabfile1.png)
![fabfile2](https://github.com/JmZero/Proyecto-IV/blob/master/img/fabfile2.png)

**NOTA: En caso de producirse algun error al ejecutar los comandos anteriores se recomienda cambiar la version de python a la 2.7**

Como resultado del proceso se podrá ver el funcionamiento de la aplicación mirando el DNS `http://owstatistics.westeurope.cloudapp.azure.com`

![dns_azure1](https://github.com/JmZero/Proyecto-IV/blob/master/img/dns_azure1.png)
![dns_azure2](https://github.com/JmZero/Proyecto-IV/blob/master/img/dns_azure2.png)
