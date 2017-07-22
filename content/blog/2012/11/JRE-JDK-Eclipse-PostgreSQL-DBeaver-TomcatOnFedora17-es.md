Title: JRE, JDK, Eclipse, PostgreSQL, DBeaver y Apache Tomcat en Fedora 17
Date: 2012-11-07 23:15
Category: Fedora
Tags: apache, database, db, dbeaver, eclipse, Fedora, GNU/Linux, java, Java Development Kit, Java Runtime Environment, jdk, jre, postgresql, sql, tomcat
Lang: es
Slug: JRE-JDK-Eclipse-PostgreSQL-DBeaver-Tomcat-on-fedora17
Summary: En la catedra “Administración de Base de Datos” de Tecnicatura Superior en Programación usamos PostgreSQL como motor de base de datos, y en la catedra Laboratorio de Computación 4 usamos Eclipse como IDE de desarrollo Java, Apache Tomcat 7 como servidor de aplicaciones web JSP y tambien PostgreSQL como motor de base de datos, aunque también existe la posibilidad de usar Firebird.</br></br>A continuación, una pequeña guía de como instalar en Fedora 17 los programas anteriores y DBeaver, un administrador de base de datos muy bueno, que tiene la capacidad de gestionar diversos motores.

1. **Descargamos [Eclipse IDE](http://www.eclipse.org/downloads/), [DBeaver](http://dbeaver.jkiss.org/download/) y [Apache Tomcat 7](http://tomcat.apache.org/download-70.cgi), [JDK y JRE](http://www.oracle.com/technetwork/java/javase/downloads/index.html) de sus respectivos sitios web**  
  <p>En la facultad, trabajamos con la [version 3.7 (Indigo SR2)](http://www.eclipse.org/indigo/) de Eclipse, aunque existen varias versiones, así que descargamos la versión que queramos, siempre acorde a la arquitectura de nuestro sistema operativo.</p>
  <p>Descargamos tambien [DBeaver](http://dbeaver.jkiss.org/download/), en formato ZIP, correspondiente a la arquitectura de nuestro sistema operativo.</p>
  <p>En el caso de [Tomcat](http://tomcat.apache.org/download-70.cgi), descargamos de “Core” el archivo tar.gz.</p>
  <p>De la página oficial de [Oracle](http://www.oracle.com/technetwork/java/javase/downloads/index.html), descargamos los paquetes RPM de las últimas versiones de JRE y JDK disponibles.</p>
  <p>Mientras se descargan estos paquetes, podemos continuar con los pasos siguientes.</p>

2. **Instalamos PostgreSQL server, y lo configuramos**
    * Para instalarlo, ejecutamos en una consola el siguiente comando:  
      `$ sudo yum install postgresql-server`  

    * Una vez instalado debemos iniciar los servicios, para ello ejecutamos en la consola:  
      `$ sudo service postgresql initdb`  
      `$ sudo service postgresql start`

    * Después, cambiamos la contraseña del usuario postgres, con el siguiente comando en una consola:  
      `$ sudo passwd postgres`  

    * Ahora, iniciamos sesión con el usuario postgres en una consola, usamos el comando “su” (Swich User, permite abrir una sesion con el ID de otro usuario):  
      `$ su postgres`  
      *Debería aparecer un prompt “bash-4.1$”*

    * Ahora entramos a Postgres, escribiendo en ese prompt el comando “psql“:  
      `bash-4.2$ psql`  

    * Procedemos a cambiar la contraseña, realizando la siguiente consulta en postgres=# , donde “CONTRASEÑA” es la misma que pusieron arriba:  
      `postgres=# ALTER USER postgres WITH PASSWORD 'CONTRASEÑA';`  
      *Si todo salió bien debería aparecer “ALTER ROLE”.*  

    * Salimos de Postgres:  
      `\q`  

    * y luego en el prompt “bash-4.1$“:  
      `exit`  

    * Ahora configuramos el puerto de PostgreSQL, ejecutamos en la consola el siguiente comando
      `$ sudo gedit /var/lib/pgsql/data/postgresql.conf`  
      Donde dice `#listen_addresses = ‘localhost'`, lo cambiamos por `listen_addresses = ‘*'`.  
      Y en la línea que dice `#port = 5432`, le quitamos el `#`, debería quedar sólo `port = 5432`.  

    * Ahora procedemos a configurar la configuración de autenticación, editando el archivo pg_hba.conf, ejecutamos en la consola el siguiente comando  
      `$ sudo gedit /var/lib/pgsql/data/pg_hba.conf`  
      Ubicamos la linea que dice `host all all 127.0.0.1/32 ident'`, lo cambiamos por `host all all 127.0.0.1/32 md5`.  
      Con éste cambio le indicamos a PostgreSQL que las conexiones desde el mismo servidor (localhost) deben autenticarse por md5.  

    * Reiniciamos Postgres para que se realicen los cambios.  
      `sudo service postgresql restart`  

3. **Instalamos JRE (Java Runtime Environment)**  
  En una consola, nos dirigimos al directorio donde descargamos el instalador de JRE, y ejecutamos los siguientes comandos:  
  `$ sudo rpm -ivh jre-7u?-linux-*.rpm`  
  `$ sudo /usr/sbin/alternatives --install /usr/bin/java java /usr/java/default/bin/java 20000`  

4. **Instalamos JDK (Java Development Kit)**  
  Nos dirigimos al directorio donde se encuentra el instalador de JDK en una consola, y ejecutamos el comando a continuación:  
  `$ sudo rpm -ivh jdk-7u?-linux-*.rpm`  

5. **Instalamos Apache Tomcat 7**  
    * En una consola, nos dirigimos al directorio donde esta el archivo de Tomcat que descargamos.  

    * Ejecutamos el siguiente comando para extraer los archivos:  
    `$ sudo tar -xvzf apache-tomcat-*.tar.gz`  

    * Después, movemos lo extraido a /usr/share/tomcat, con el comando que sigue, completando “*” con el nombre exacto de la carpeta  
    `$ sudo mv apache-tomcat-* /usr/share/tomcat`  

    * Ahora, creamos el archivo necesario para que se identifique a tomcat como servicio, así podemos iniciarlo, reiniciarlo y detenerlo.  
    `$ sudo gedit /etc/init.d/tomcat`  

    * Dentro de ese archivo...  
    <code>
    \#!/bin/bash  
    \# description: Tomcat Start Stop Restart  
    \# processname: tomcat  
    \# chkconfig: 234 20 80  
    JAVA_HOME=/usr/java/default/  
    export JAVA_HOME  
    PATH=$JAVA_HOME/bin:$PATH  
    export PATH  
    CATALINA_HOME=/usr/share/tomcat  
    case $1 in  
    start)  
    sh $CATALINA_HOME/bin/startup.sh  
    ;;  
    stop)  
    sh $CATALINA_HOME/bin/shutdown.sh  
    ;;  
    restart)  
    sh $CATALINA_HOME/bin/shutdown.sh  
    sh $CATALINA_HOME/bin/startup.sh  
    ;;  
    esac  
    exit 0  
    </code> 
 
        - En donde dice `JAVA_HOME=/usr/java/default/` se debe poner la ruta al programa que proporciona Java, para averiguarlo, en una consola ejecutan el comando:  
        `$ alternatives --config java`  

        - Esto arroja un listado de los programas que aportan Java, y especifica cual es el que está por defecto. En mi caso, me listó lo siguiente:  
        <code>
        Hay 2 programas que proporcionan 'java'.</br>  
        Selección	Comando  
        \-----------------------------------------------  
         \*+ 1		/usr/java/default/bin/java  
         2 /usr/lib/jvm/jre-1.7.0-openjdk.x86_64/bin/java</br>  
        Presione Intro para mantener la selección actual[+], o escriba el número de la selección:
        </code></br>  
        *Fijensé que la ruta que aparece en el archivo no es la absoluta a Java (usr/java/default/bin/java), si no a el directorio home de Java (usr/java/default/)*  

    - Finalmente, ejecutamos los siguientes 3 comandos:  
    <code>$ sudo chmod 755 /etc/init.d/tomcat  
          $ sudo chkconfig --add tomcat  
          $ sudo chkconfig --level 234 tomcat on</code></br>  
y listo, ya podemos iniciar, detener y reiniciar tomcat

6. **Instalamos DBeaver**  
    * Abrimos una consola y nos dirigimos al directorio donde descargamos el archivo zip de DBeaver  
 
    * Extraemos los archivos con este comando:  
    <code>$ sudo unzip dbeaver-*-linux.gtk.*.zip</code>  

    * Después lo movemos a /opt, con el comando a continuación:  
    <code>$ sudo mv dbeaver /opt/dbeaver</code>  

    * Le damos los permisos correspondientes:  
    <code>$ sudo chmod -R +r /opt/dbeaver/</code>  

    * Creamos un ejecutable en el directorio /usr/bin, con los comandos próximos:  
    <code>$ sudo touch /usr/bin/dbeaver  
    $ sudo chmod 755 /usr/bin/dbeaver  
    $ sudo gedit /usr/bin/dbeaver</code>  

    * Y en el archivo copiamos lo que esta a sucesor:  
    <code>xport DBEAVER_HOME="/opt/dbeaver"  
    $DBEAVER_HOME/dbeaver $*</code>  

    * Ahora, creamos el acceso directo en el menú de aplicaciones de GNOME  
    <code>$ sudo gedit /usr/share/applications/dbeaver.desktop</code>  

    * Y copiamos el texto posterior
    <code>[Desktop Entry]  
    Encoding=UTF-8  
    Name=DBeaver  
    Comment=Administrador de base de datos DBeaver  
    Exec=dbeaver  
    Icon=/opt/dbeaver/icon.xpm  
    Terminal=false  
    Type=Application  
    Categories=GNOME;Application;Development;  
    StartupNotify=true</code>  

    Y listo, ya tenemos instalado DBeaver en nuestro sistema  

7. **Instalamos Eclipse IDE**  
    * En una consola, nos dirigimos al directorio donde descargamos el archivo tar.gz de Eclipse.  

    * Extraemos el contenido del archivo en /opt con el siguiente comando:  
      <code>$ sudo tar -xvzf eclipse-*-linux-gtk-*.tar.gz -C /opt</code>  

    * Le damos permiso de lectura a todos los archivos con el comando a continuación:  
      <code>$ sudo chmod -R +r /opt/eclipse</code>  

    * Creamos un ejecutable en el directorio /usr/bin:  
      <code>$ sudo touch /usr/bin/eclipse  
      $ sudo chmod 755 /usr/bin/eclipse  
      $ sudo gedit /usr/bin/eclipse</code>  

    * y en el gedit copiar lo próximo:
      <code>export ECLIPSE_HOME="/opt/eclipse"  
      $ECLIPSE_HOME/eclipse $*</code>  

    * Luego, creamos el archivo para hacer el acceso directo en el menú en GNOME:  
      <code>$ sudo gedit /usr/share/applications/eclipse.desktop</code>  

    * Y en el gedit copiamos el texto consecuente:  
      <code>[Desktop Entry]  
      Encoding=UTF-8  
      Name=Eclipse  
      Comment=Eclipse  
      Exec=eclipse  
      Icon=/opt/eclipse/icon.xpm  
      Terminal=false  
      Type=Application  
      Categories=GNOME;Application;Development;  
      StartupNotify=true
