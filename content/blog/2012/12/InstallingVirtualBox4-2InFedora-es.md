Title: Instalando VirtualBox 4.2 en Fedora
Date: 2012-12-15 21:00
Category: Fedora
Tags: Fedora, GNU/Linux, Oracle, VirtualBox
Lang: es
Slug: installing-virtualbox-42-fedora
Summary: No soy de usar tanto VirtualBox, ni maquinas virtuales, pero hoy pensé en usar una para hacer unas pruebas y cuando abrí VirtualBox 4.1.\* me informó que existía una versión nueva (4.2.\*).</br></br>No he actualizado mucho la guía de post-instalación de Fedora, y VirtualBox se venía actualizando sin problemas (claro, en su versión 4.1), tengo la teoría de que es conveniente tener siempre el software actualizado, así que no dudé en actualizar VirtualBox a su versión 4.2.\*</br> </br>A continuación explico como hacerlo.

Aclaro, que cuando quise instalar la versión 4.2.\* no me dijo que desinstalaría la versión 4.1.\*, ni que molestaría, ni nada, pero por las dudas, la desinstalé igual con el siguiente comando:  
`$ sudo yum remove VirtualBox-4.1*`  

Si no tuvieses instalado la versión anterior de VirtualBox, deberías instalar los repositorios oficiales, para mantener siempre actualizado (la versión actual, de acuerdo a lo que me pasó a mí). Primero, descargamos el archivo de repositorio ejecutando el siguiente comando en una consola:  
`$ sudo wget http://download.virtualbox.org/virtualbox/rpm/fedora/virtualbox.repo`  

Luego, lo movemos al directorio de los repositorios, lo hacemos con la siguiente linea:  
`$ sudo mv virtualbox.repo /etc/yum.repos.d/`  

Instalamos las cabeceras del kernel, y otros modulos para el kernel:  
`$ sudo yum install gcc kernel-headers dkms kernel-devel`  

Finalmente, ejecutamos la instalación de VirtualBox 4.2:  
`$ sudo yum install VirtualBox-4.2`  

Listo! Tenemos instalado la ultima versión de VirtualBox 4.2, y se actualizará simplemente con un `$ sudo yum update`
