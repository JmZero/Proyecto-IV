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
