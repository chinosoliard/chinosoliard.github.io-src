Title: Multiples instalaciones de Eclipse IDE en el mismo sistema
Date: 2014-04-05 18:00
Category: Fedora
Tags: c++, cpp, development, eclipse, IDE, Fedora, GNU/Linux,jee, Php
Lang: es
Slug: multiple-installations-eclipse-same-system 
Summary: <a href="http://www.eclipse.org" target="_blank"><img alt="eclipse" src="/images/article/2014/04/eclipse.png" class="alignright"></a>Creo que no soy el único que piensa que [Eclipse IDE](http://eclipse.org/) se torna pesado a medida que le agregamos plugins y demás, y, si bien tiene la facilidad de cambiar entre áreas de trabajo (Workspaces), personalmente prefiero separarlos del todo.</br></br>En mi caso en particular, trabajo con Java, veo algunas cosas en C y estoy haciendo un curso de PHP, entonces, decidí tener 3 Eclipse distintos en mis equipos (obviamente, uno para cada lenguaje), pero puede usarse con distintos fines, por ejemplo, uno para Java y SWING y otro para Java EE, etc.  

Antes que nada aclaro que estos pasos me sirvieron en [Fedora](http://fedoraproject.org/), y son compatibles con todos los sistemas GNU/Linux, desconozco si existe alguna forma de hacerlo en Windows.  

Eclipse necesita de un entorno de ejecución Java, por lo que, basta con tener OpenJDK o instalar el Java Runtime Environment oficial (Oracle JRE) para poder iniciar eclipse. En el caso de necesitar el JDK oficial (muchos desarrolladores Java no quieren arriesgarse con OpenJDK), pueden instalar Java Development Kit Oficial (Oracle JDK) el cual trae incluido JRE.  

**Instalación de JRE/JDK**  

1. Descargar JRE o JDK en versión RPM. [(desde acá)](http://www.oracle.com/technetwork/es/java/javasebusiness/downloads/index.html)  
2. Ejecutamos los siguientes comandos en una consola o terminal:  
  <code># rpm -ivh jre-8u*-linux-*.rpm`</code></br>
  <code># alternatives –install /usr/bin/java java /usr/java/default/bin/java 20000</code>  

**Instalación de Eclipse IDE**  
Instalar Eclipse en Fedora es tan sencillo como ejecutar “<code>yum install eclipse</code>“, pero nos vemos apegado a configuraciones de Fedora, actualizaciones de Fedora y, nos limitamos a no poder hacer lo que sería el fin de este post.  
De todos modos, instalar Eclipse de forma manual, no trae complicaciones, y tampoco es tan dificil.  
Lo primero que tenemos que hacer es descargar la versión (o las versiones) que queremos instalar en formato ; Como dije, en mi caso, Eclipse JEE, Eclipse C/C++ y Eclipse PHP (éste último en su versión Helios SP1).  

Una vez que los descargamos, hay que hacer las instalaciones **DE A UNA**; Tomamos como ejemplo Eclipse JEE, y realizamos los siguientes pasos:  

1. Extraemos la versión de Eclipse (en este caso JEE) que descargamos con el siguiente comando:  
  `# tar -xvzf eclipse-jee-linux-gtk-*.tar.gz` 
   
    Donde “jee” hay que reemplazarlo por lo que corresponda según la versión de eclipse.  
    Donde “*” es un comodín para la arquitectura de Eclipse (32 bits o 64 bits).  

2. Esto va a crear un directorio “eclipse“, el cual vamos a mover a /opt, pero, con un nombre especifico, en el caso de JEE, le cambiamos el nombre a “eclipsejee“, ésto lo hacemos ejecutando:  
  `# mv eclipse /opt/eclipsejee`  
  En éste caso, lo movemos a “eclipsejee” porque tomamos como ejemplo Eclipse JEE, puede ser “eclipsephp” o lo que corresponda.  

3. Ahora, tenemos que darle los permisos de lectura a los archivos del directorio, con el comando:  
  `# chmod -R +r /opt/eclipsejee`  

4. Después, creamos el ejecutable, haciendo:  
  `# touch /usr/bin/eclipsejee`  
  `# chmod 755 /usr/bin/eclipsejee`  

    Editamos este archivo que creamos, en este caso, con “gedit”  
  `# gedit /usr/bin/eclipsejee`  

    En el archivo, copiamos lo siguiente:  
  <code>export ECLIPSEJEE_HOME=”/opt/eclipsejee”</br>
  $ECLIPSEJEE_HOME/eclipse $*</code>  

    Donde “eclipsejee” (o “ECLIPSEJEE”), puede ser “eclipsephp” o lo que corresponda.  
    Con ésto, lo que hacemos es que ahora, desde una consola, usemos el comando “$ eclipsejee” para ejecutar Eclipse JEE.

5. Finalmente, creamos el acceso por el menú de GNOME, esto lo hacemos (con gedit) haciendo:  
  `# gedit /usr/share/applications/eclipsejee.desktop`  

    Y copiando lo siguiente en el archivo:  
  <code>
[Desktop Entry]  
Encoding=UTF-8  
Name=Eclipse JEE  
Comment=Eclipse JEE  
Exec=eclipsejee  
Icon=/opt/eclipse/icon.xpm  
Terminal=false  
Type=Application  
Categories=GNOME;Application;Development;  
StartupNotify=true  
</code>  

    Ésto creara un icono en el menú de aplicaciones de GNOME, que ejecutará “eclipsejee“.  

**Un paso adicional**, es hacer que cada eclipse tenga un icono adecuado, así sería más facil identificarlo (y además más “estético” :-P); Busqué un rato hasta que encontré unos iconos como la gente, y resultaron:

<center>[![eclipsejee](/images/article/2014/04/iconjee.png)](/images/article/2014/04/EclipseIcons/iconjee.xpm)</center>  

<center>[![eclipsephp](/images/article/2014/04/iconphp.png)](/images/article/2014/04/EclipseIcons/iconphp.xpm)</center>  

<center>[![eclipsecpp](/images/article/2014/04/iconcpp.png)](/images/article/2014/04/EclipseIcons/iconcpp.xpm)</center>  


Una vez descargados, basta moverlos (reemplazar) a icon.xpm en (siguiendo el ejemplo) /opt/eclipsejee/icon.xpm, con el comando:  
`# mv /iconjee.xpm /opt/eclipsejee/icon.xpm`  


Espero les ayude.  

Saludos!
