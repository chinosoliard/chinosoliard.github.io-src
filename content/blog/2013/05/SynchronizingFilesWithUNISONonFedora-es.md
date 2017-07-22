Title: Sincronizando archivos con UNISON en Fedora
Date: 2013-05-22 14:00
Category: Fedora
Tags: Fedora, GNU/Linux, Local, maintenance, SSH, Sync, Synchronization, UNISON
Lang: es
Slug: synchronizing-files-unison-fedora 
Summary: <img alt="unison-logo" src="/images/article/2013/05/unison-logo.png" class="alignright">Yo almacenaba casi todos mis archivos en mi computadora de escritorio, otros archivos los tenía en mi notebook, que tenía menos espacio, y otros los sincronizaba automáticamente con Dropbox; Esto se terminó cuando cambie la notebook, y ahora ésta tiene más espacio que la computadora de escritorio, pero almacenar todo en la notebook es algo peligroso e inseguro, por lo cual, solo quiero que los datos estén en las 2 pc.</br>Hay diversas alternativas para realizar sincronizaciones automáticas (la mayoría pagas), en mi caso, decidí usar [UNISON](http://www.cis.upenn.edu/~bcpierce/unison/), una aplicación multiplataforma que permite realizar las sincronizaciones entre 2 anfitriones, o tambien entre 2 directorios locales.</br></br>Sincronizar, según la [Real Academia Española](http://buscon.rae.es/drae/srv/search?id=EizugCEyTDXX2pMts9vl), significa “Hacer que coincidan en el tiempo dos o más movimientos o fenómenos.”, por lo tanto, eso es exactamente lo que hace Unison, los cambios son propagados de forma bidireccional, es decir, archivos que estan en el host a y no estan en el host b, se copian, y viceversa; Además, compara las fechas de los archivos para detectar, obviamente, cual es más reciente.</br></br>Unison, como comenté anteriormente, permite hacer sincronizaciones entre directorios locales, y entre diferentes anfitriones utilizando [SSH (Secure Shell)](http://es.wikipedia.org/wiki/Secure_Shell), [RSH (Remote Shell)](http://es.wikipedia.org/wiki/Rsh) y [TCP (por Socket)](http://es.wikipedia.org/wiki/Socket_de_Internet). Al ser SSH el metodo más seguro, es el que elegí para operar, y el que usaremos en esta sencilla guía.  

1. **Instalamos UNISON**  
  Unison se encuentra en los repositorios de Fedora, así que lo instalamos sencillamente con el siguiente comando:  
  `su -c ‘yum install unison’`  

2. **Creamos el/los perfiles de sincronización**  
  Unison trabaja por perfiles, los cuales configuramos para especificar cuales son los directorios a sincronizar.  
    1. Lo ejecutamos, y, ahora no recuerdo bien si la primera vez fue así, pero creo que automáticamente se ejecutaba el asistente para agregar un perfil, si no es así, apretamos “Añadir” para iniciar el asistente de creación.  

    2. En la primer pantalla, que es solo una introducción, apretamos “Adelante”.  
    [![unison-1](/images/article/2013/05/unison-1.png)](/images/article/2013/05/unison-1.png)  

    3. A continuación, nos pide que completemos el nombre del perfil y una descripción del mismo. Completamos y le damos siguiente.  
    [![unison-2](/images/article/2013/05/unison-2.png)](/images/article/2013/05/unison-2.png)  

    4. Después, nos pide que seleccionemos el tipo de conexión, en donde podemos elegir Local, SSH, RSH y por conexión TCP.  

        * **Perfiles de sincronización en forma Local**  
            1. Seguimos los pasos que enumeramos anteriormente, seleccionamos “Local” de la lista de tipos de conexión y le damos “adelante”  
            [![unison-3](/images/article/2013/05/unison-3.png)](/images/article/2013/05/unison-3.png)  

            2. A continuación, deberemos detallar los directorios involucrados en la sincronización, lo hacemos y le damos a “Adelante”  
            [![unison-4](/images/article/2013/05/unison-4.png)](/images/article/2013/05/unison-4.png)  

            3. En mi caso, estoy por sincronizar directorios que estan en particiones NTFS, por lo tanto, activo el checkbox que configura el perfil para que trabaje sin utilizar los permisos que usa GNU/Linux  
            [![unison-5](/images/article/2013/05/unison-5.png)](/images/article/2013/05/unison-5.png)  

            4. Finalmente, Unison nos informa que terminamos de configurar el perfíl, y que apretemos “Aplicar” para crearlo.  
            [![unison-6](/images/article/2013/05/unison-6.png)](/images/article/2013/05/unison-6.png)  


        * **Perfiles de sincronización en forma remota con SSH**  
            1. Seguimos los pasos que enumeramos anteriormente, seleccionamos “SSH” de la lista de tipos de conexión, el contenido de la ventana se extenderá, y ahora solicitará que le introduzcamos el host, que puede ser el nombre o la dirección IP del equipo al cual nos queremos conectar, y el nombre de usuario con el cual nos identificaremos en dicho equipo.  
               Tambien, podemos activar un checkbox para que Unison comprima los archivos que se envían, como dice el software, es bueno para conexiones lentas, pero hace más lentas las conexiones rápidas.  
               Luego de configurar esto, avanzamos  
            [![unison-7](/images/article/2013/05/unison-7.png)](/images/article/2013/05/unison-7.png)  

            2. A continuación, deberemos configurar los directorios que sincronizaremos. El local lo seleccionamos, el remoto debemos escribirlo, por lo cual, es necesario saber previamente el nombre del directorio. Pueden corroborarlo haciendo una conexión SSH por consola.  
Después de esto, seguimos  
            [![unison-8](/images/article/2013/05/unison-8.png)](/images/article/2013/05/unison-8.png)  

            3. Al igual que en ejemplo anterior, en el que hacemos una sincronización de forma local, debemos configurar el perfil para trabajar con particiones NTFS o FAT, o mejor dicho, para que excluya el tratamiento de permisos de archivos que GNU/Linux utiliza. En mi caso, utilizo particiones NTFS en la sincronización, así que lo activo.  
            [![unison-9](/images/article/2013/05/unison-9.png)](/images/article/2013/05/unison-9.png)  

            4. A continuación, basta con apretar “Aplicar” y listo, ya terminamos de configurar el perfil para sincronizar directorios por SSH.  
            [![unison-10](/images/article/2013/05/unison-10.png)](/images/article/2013/05/unison-10.png)  

3. **Realizamos una sincronización.**  
    1. Ejecutamos un perfil de sincronización, seleccionándolo de la lista y haciendo clic en “Abrir”.  
    [![unison-11](/images/article/2013/05/unison-11.png)](/images/article/2013/05/unison-11.png)  
    *Al abrir uno de los perfiles creados para sincronizar por SSH, se nos pedirá una contraseña para iniciar la sesión.*  
    [![unison-12](/images/article/2013/05/unison-12.png)](/images/article/2013/05/unison-12.png)  

    2. Cuando realizamos la sincronización por primera vez, se muestra una ventana como la siguiente, que explica que no existen archivos historicos de sincronizaciones, y que eso se debe a que, o no se han realizado sincronizaciones aún, o se actualizó la version de Unison y esta no reconoce los archivos historicos; Por lo cual, Unison asume que el archivo historico está completamente vacio.  
    [![unison-13](/images/article/2013/05/unison-13.png)](/images/article/2013/05/unison-13.png)  
    *La primera vez que se realizan sincronizaciones, este proceso demora mucho.*  

    3. Finalizada la comparación, se muestra una lista, la cual ajustó automáticamente los cambios a realizar, los cuales podemos modificar.  
      Revisamos bien los cambios que se van a realizar, podemos saltar cambios (“skip”, que pasa por alto la fila, no realiza cambios), y elegir el reemplazo y copiado en ambas direcciones.  
    [![unison-14](/images/article/2013/05/unison-14.png)](/images/article/2013/05/unison-14.png)  

    4. Una vez que controlamos los cambios a realizar, apretamos el botón “Go”, y comienza la sincronización.  

    5. Después de terminar de copiar los archivos, nos aparecerá una ventana informando que la sincronización finalizó, y un pequeño sumario, el cual podemos extender.  
    [![unison-15](/images/article/2013/05/unison-15.png)](/images/article/2013/05/unison-15.png)  


Así de simple es utilizar Unison, luego de haber ejecutado por primera vez un perfil el punto 3.2 finaliza más rápido.  
Un punto importante a tener en cuenta es que Unison debe estar instalado en ambos equipos, si es que se realiza la sincronización en forma remota.  
En esta guía trabajamos con Unison GUI, es decir, con entorno gráfico, pero tambien se puede utilizar por consola (Estoy considerando utilizar Unison por linea de comandos en conjunto “cron”, para automátizar sincronizaciones y backups).  
  

Espero les haya servido.  
  

Saludos
