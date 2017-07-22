Title: Eclipse en Fedora 21
Date: 2015-01-14 13:58:52
Category: Fedora
Tags: apache, C/C++, c++, cpp, Eclipse, Fedora, 21, Fedora21, GNU/Linux, java, Java EE, JavaEE, JBoss, Php, Python
Lang: es
Summary: <a href="http://www.eclipse.org" target="_blank"><img alt="eclipse" src="/images/article/2015/01/eclipse.png" class="alignright"></a></br>Hace 1 mes, [Fedora](http://www.fedoraproject.org) lanzó su versión 21, la cual viene en 3 versiones (sin contar los [spins](https://spins.fedoraproject.org/)): [Workstation](https://getfedora.org/workstation/), [Server](https://getfedora.org/server/) y [Cloud](https://getfedora.org/cloud/).</br></br>La versión [Workstation de Fedora, está apuntada a desarrolladores](http://fedoraproject.org/wiki/Workstation), y lo primero que me llamó la atención fue la aplicación [DevAssistant](http://devassistant.org/), de la cual no voy a hablar en éste post.</br></br>Hace un tiempo publiqué un articulo que explicaba [como tener varias versiones de eclipse en el mismo sistema operativo](/blog/2014/abr/multiple-installations-eclipse-same-system-es.html); Ésto era, porque Eclipse se tornaba lento a medida que le iba añadiendo extensiones, pero esta vez, quise probar el [Eclipse de Fedora](http://fedoraproject.org/wiki/Eclipse), y la verdad, me convenció. Le instalé de todo un poco y la velocidad no se vió afectada.  

* **Eclipse for Java Developers**<a href="https://www.eclipse.org/downloads/packages/eclipse-ide-java-developers/lunasr1a" target="_blank"><img alt="eclipse-java" src="/images/article/2015/01/eclipse-java.png" class="alignright"></a>  
  Para instalar Eclipse Java, tan solo tenemos que ejecutar el comando:  
  <code>su -c 'dnf install eclipse'</code></br>  
   Ésto instalará Eclipse, OpenJDK-Devel, y todo lo demás necesario para desarrollar código Java.  

* **Eclipse for Java EE Developers**<a href="https://www.eclipse.org/downloads/packages/eclipse-ide-java-ee-developers/lunasr1a" target="_blank"><img alt="eclipse-jee" src="/images/article/2015/01/eclipse-javaee.png" class="alignright"></a>  
  Para poder desarrollar Java Enterprise Edition con Eclipse, necesitamos instalar Eclipse for Java EE Developers ejecutando:  
  <code>su -c 'dnf install eclipse-webtools-javaee'</code></br>  
  Con ésto instalamos los paquetes necesarios para desarrollar Java EE en Eclipse, como servidores Tomcat, y demás. Tambien pueden instalar JBoss para Eclipse, ejecutando el comando:  
  <code>su -c 'dnf install eclipse-jbosstools'</code></br>  
  Éste último, instalará, además de servidores JBoss, paquetes como Hibernate.  

* **Eclipse for PHP Developers**<a href="https://www.eclipse.org/downloads/packages/eclipse-php-developers/lunasr1a" target="_blank"><img alt="eclipse-php" src="/images/article/2015/01/eclipse-php.png" class="alignright"></a>  
  No existe forma de evitar que Eclipse traiga lo necesario para desarrollar Java, por lo cual, siempre se instalará OpenJDK-Devel y demás, pero, para instalar el Eclipse PHP, basta con ejecutar el comando:  
  <code>su -c 'dnf install eclipse-pdt'</code></br>  
  Ésto instalará Eclipse Java, y Eclipse PHP, tambien instalará en el sistema Apache (httpd), PHP y demás paquetes necesarios para poder desarrollar PHP en nuestro sistema.  

* **Eclipse for C/C++ Developers**<a href="https://www.eclipse.org/downloads/packages/eclipse-ide-cc-developers/lunasr1a" target="_blank"><img alt="eclipse-cdt" src="/images/article/2015/01/eclipse-cdt.png" class="alignright"></a>  
  Si bien no es lo más usado en la actualidad, C y C++ nunca desaparecieron. Instalar Eclipse for C/C++ Developers en Fedora es tan sencillo como ejecutar:  
  <code>su -c 'dnf install eclipse-cdt'</code></br>  

* **Eclipse for Python Developers** (si, para Python)<a href="http://pydev.org/" target="_blank"><img alt="eclipse-pydev" src="/images/article/2015/01/eclipse-pydev.png" class="alignright"></a>  
  No sabía de que Eclipse tambien tenía un IDE para Python, no es (todavía) oficial, pero que es útil, lo es… Se instala ejecutando el comando:  
  <code>su -c 'dnf install eclipse-pydev'</code></br>  
  Y con ésto podemos desarrollar código Python, también usar Django.
