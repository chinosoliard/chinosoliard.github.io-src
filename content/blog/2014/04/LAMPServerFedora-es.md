Title: Servidor LAMP en Fedora
Date: 2014-04-03 18:00
Category: Fedora
Tags: apache, Fedora, GNU/Linux, httpd, LAMP, MariaDB, mod_php, MySQL, Perl, php, python, sql, systemctl, web
Lang: es
Slug: LAMP-server-Fedora
Summary: <a href="http://www.gugler.com.ar" target="_blank"><img alt="gugler" src="/images/static/gugler-150.png" class="alignright"></a>La semana pasada empecé (por 3ra vez) el curso de PHP nivel 1 en [GUGLER](http://www.gugler.com.ar), entonces, tengo que montar un servidor php en mis equipos para poder llevar a cabo las practicas.</br></br>Si bien [**XAMPP**](https://www.apachefriends.org/es/index.html) (X=Windows/Linux/Mac, A=Apache, M=MySQL, P=PHP, P=Perl) tiene disponible una versión para sistemas GNU/Linux, considero que es mejor instalar el software de los repositorios.</br></br><a href="http://www.fedoraproject.org" target="_blank"><img alt="fedora" src="/images/static/fedora-150.png" class="alignleft"></a>[**LAMP**](http://es.wikipedia.org/wiki/LAMP) era la sigla de “Linux, Apache, MySQL and PHP”, pero, en la actualidad, LAMP tiene variantes en cuanto a la “P”, que puede ser tanto PHP, como Perl o Python, mismo caso para la “M”, que puede ser MySQL o MariaDB.</br></br>A continuación, los pasos a llevar a cabo para montar un servidor LAMP en nuestro Fedora  

1. **Instalación**  
    1. **Apache Web Server**  
      [Apache](http://www.apache.org/) es una fundación, pero el nombre Apache hace (directamente) referencia al servidor web HTTPd (Apache HyperText Transfer Protocol daemon). Instalarlo en Fedora no es para nada dificil, basta con ejecutar el siguiente comando en la consola:  
      `# yum install httpd`  

    2. **MariaDB**  
      En el caso de Fedora, MySQL fue reemplazado por MariaDB, tras la compra de MySQL por parte de Oracle, lo cual lo convirtió en un software de codigo abierto, en vez de software libre, como antes era. Al igual que al servidor web Apache, instalarlo es tan sencillo como ejecutar el siguiente comando:  
      `# yum install mariadb-server`  

    3. **PHP (mod_php)**  
      El servidor web Apache es modular, por lo que se pueden instalar los módulos que necesitemos (mod_python, mod_perl, mos_php, mod_ssl, etc.). En mi caso, que voy a trabajar con PHP, voy a instalar mod_php, con el comando siguiente:  
      `# yum install php`  

    Con estos tres simples pasos, tenemos instalado el software  necesario

2. **Inicialización de los servicios**
    1. **Apache Web Server**  
      Para iniciar el servidor web apache, hacemos:  
      `# systemctl start httpd.service`  

    2. **MariaDB**  
      En el caso de MariaDB, ejecutamos:  
      `# systemctl start mariadb.service`  

3. **Configuración de los servicios y el sistema**  
    1. **Instalación segura de MariaDB**  
      Este proceso:  
        * Establece (Cambia) la contraseña de root (de MariaDB).  
        * Elimina usuarios anónimos.  
        * Deshabilita el login de root de forma remota.  
        * Elimina la base de datos “test” y el acceso a ésta.  
        * Carga nuevamente la tabla de privilegios.  

        Para ejecutar “MariaDB Secure Installation” corremos el comando:  
        `# /usr/bin/mysql_secure_installation`  

    2. **Permisos del directorio de Apache**  
      Al instala HTTPd, se crea el directorio <code>/var/www/html</code>, el cual contendrá el/los archivos del servidor web, con esto me refiero a que si ingresamos a <code>http://localhost/index.php</code> estaremos ingresando a <code>/var/www/html/index.php</code>.  
      Si queremos añadir un archivo o editar alguno, necesitaremos permisos para ello, y apache también necesita acceso para poder “servir” los archivos; Entonces, debemos hacer que el directorio “/var/www/html” pertenezca al grupo “apache”, y a nuestro usuario, ésto se configura mediante los siguientes comandos:  
        `# chown -R usuario /var/www/html/`  

        `# chgrp -R apache /var/www/html/`  

        `# chmod -R 750 /var/www/html/`  

        `# chmod g+s /var/www/`  

        Si Apache va a tener que escribir archivos en el directorio (por ejemplo: subir archivos), también tendremos que darle permisos de escritura a Apache, usando el siguiente comando, le daremos permiso a Apache para escribir en un directorio llamado “media” dentro de /var/www/html/  
        `#chmod g+w /var/www/html/media`  

      Con esto ya estaríamos listo para trabajar.  

4. **Configurando el inicio automático de los servicios**  
  En el caso de que queramos que nuestro sistema funcione como servidor, resultaría tedioso iniciar los servicios manualmente cada vez que el equipo se apague, se corte la luz, o lo-que-sea, podemos hacer que los servicios se ejecuten automáticamente haciendo uso de los comandos:  
  <code># systemctl enable mariadb.service</code></br>  
  <code># systemctl enable httpd.service</code></br>    
   Estos últimos 2 (dos) comandos hacen que inicien automáticamente al inicio del sistema MariaDB y Apache HTTP Server (respectivamente).  

Apache tiene muchísimas configuraciones, permite host virtuales, múltiples usuarios, y muchísimas cosas más; Acá solo muestro como hacer de nuestra pc una plataforma de desarrollo web, o, a lo sumo, un servidor muy simple.  
  
Si buscan en internet pueden encontrar como hacer para alojar varios sitios en un solo equipo, o permitir que varios usuarios puedan editar diferentes sitios, es solo cuestión de buscar.  

Espero les haya servido, saludos!
