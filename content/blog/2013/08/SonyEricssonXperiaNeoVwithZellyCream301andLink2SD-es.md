Title: Sony Ericsson Xperia Neo V con Zelly Cream 3.0.1 + Link2SD
Date: 2013-08-24
Category: Smartphones
Tags: Android, Apps2SD, CWM, Recovery, Ice Cream Sandwich, ICS, Link2SD, Neo V, Recovery, Sony Ericsson, Xperia, Zelly Cream
Lang: es
Slug: sony-ericsson-xperia-neo-v-zelly-cream-301-link2sd
adsense: 1
Summary: Después de un buen tiempo de sufrir con mi Xperia Neo V funcionando mal, me dí cuenta de que el problema era que no tenía espacio en la memoria interna; Decidí entonces, volver a probar con Link2SD, una aplicación que la última vez que lo instalé me trajo problemas, pero esta vez los pasos fueron distintos.</br></br>En conclusión, mi Xperia Neo V ahora tiene Zelly Cream 3.0.1, y un listado amplio de aplicaciones.</br></br>A continuación una guía para instalar Zelly Cream 3.0.1 y Link2SD para poder tener más rendimiento.  

Por empezar, hago una lista de lo que necesitamos para llevar a cabo el proceso:  

1. Tener el celular actualizado al Firmware 4.1.B.0.587 y rooteado.  
    * [Actualizar Sony Ericsson Xperia Neo V con Ice Cream Sandwich OFICIAL](../../2012/nov/update-SE-NeoV-ICS-oficial-es.html)  

    * [Rooteando Sony Ericsson Xperia Neo V con Firmware 4.1.B.0.587](../mar/rooting-SE-NeoV-firmware-41B0587-es.html)  

2. [ClockWorkMod Recovery](http://adf.ly/deDCD) [1]  

3. Alguna utilidad para particionar la tarjeta microSD, existen varias alterntivas para Windows, yo recomiendo [PartitionWizard](http://adf.ly/deDEF).  

4. [Zelly Cream 3.0.1 Full ROM](http://adf.ly/deDG6) [2]  
  [Otro Link](http://adf.ly/deDJU)  
  [Otro Link](http://adf.ly/deDKi)  

**Recomiendo, ir bajando todo mientras se prosigue con el post, para ir ahorrando tiempo.**  

*Si ya tenés instalado ClockWorkMod Recovery puedes saltearte este paso*  

1. **Instalamos ClockWorkMod Recovery**  
  Lo primero que hacemos es instalar ClockWorkMod Recovery, es un programa que puede ejecutarse antes de que se carge el sistema operativo, permite hacer limpiezas, actualizar el sistema, realizar backups, entre otras cosas.  

    1. Extraemos el contenido del archivo [1].  

    2. En el celular nos vamos a “Ajustes” > “Opciones de desarrollo” y activamos “Depuración de USB”.  

    3. Ejecutamos “install-cwm1.bat” (de los archivos extraídos, obvio) y conectamos el dispositivo y seguimos las instrucciones.  
      Nota: El software dice que prendas la pantalla y aceptes los permisos de superusuario, a mi, personalmente, no me saltó ningun cartel, pero me fijé en los registros de la aplicación Superuser y aparecía una actividad por consola.  

    4. Finalmente, ClockWorkMod está instalado, para ejecutarlo apagamos el equipo y cuando lo prendemos, apenas vibra empezamos a apretar repetidamente el botón de bajar volumen.  
      **Si no funcionase, intentar nuevamente hasta que lo haga.**  

2. **Particionamos la memoria microSD**  
  Particionamos la tarjeta de memoria para que queden 2 partes, una para los datos y otra para que las aplicaciones se instalen ahí en vez de en la memoria interna del celular.  
  **Este proceso depende mucho del software que utilicen para hacer las particiones**, por eso no voy a dar un detalle de como realizarlo; Lo que si, voy a resaltar puntos importantes:  

    1. **RESPALDAR LOS DATOS**  
      Si no queres perder datos, reespaldalos siempre que trabajes con particiones. “Es un antes y un después”.  

    2. La partición para las aplicaciones debe:  
        * Quedar segunda, es decir, la partición de datos (FAT32) debe quedar a la izquierda, la partición para aplicaciones debe quedar a lo ultimo de la tarjeta.  
        * Ser de formato **EXT2**.  
        * En mi caso la hice de 1 GB (1GB = 1024MB), pero puede ser menor o mayor, aunque no creo que necesite ser mayor de 1G.  

    3. En la imagen a continuación se muestra más o menos como quedaría, no le presten atención a la 3ra partición, esa la hice para otro experimento.  
      [![gparted](/images/article/2013/08/gparted.png)](/images/article/2013/08/gparted.png)  

3. **Instalamos Zelly Cream 3.0.1**  
  Zelly Cream es una ROM de Android 4.1.1 NO OFICIAL, que ha sido votada como la “mejor ROM  Ice Cream Sandwich” por sus usuarios.  
  Personalmente no me ha defraudado, tiene muchas opciones y está bien optimizada.  
  Pueden obtener más información en el thread oficial: [http://forum.xda-developers.com/showthread.php?t=2151648](http://forum.xda-developers.com/showthread.php?t=2151648)

    1. Copiamos Zelly Cream v3.0.1 Full ROM [2] a la partición de datos en la tarjeta microSD del celular (a la **de datos**, no a la de las aplicaciones).  

    2. Iniciamos ClockWorkMod Recovery. (Prendemos el celular y cuando vibre empezamos a apretar reiteradas veces la tecla de bajar volumen).  

    3. Una vez en CWM Recovery, seleccionamos “wipe data/factory reset” con la tecla “home” (la casita) y luego seleccionamos “Yes”. (La navegación se realiza con las teclas de volumen).  

    4. Después, seleccionamos “wipe cache partition” y luego “Yes”.  

    5. Nos dirigimos a  “advanced” y ahí hacemos “Wipe Dalvik Cache”.  

    6. Tambien en “advanced”, le damos a “Wipe Battery Stats”.  

    7. Luego nos vamos a “mounts and storage” del menú principal y seleccionamos “format /data”, “format /system” y “format /cache”.  

    8. Ahora, nos dirigimos a “install zip from sdcard” en el menú principal, dentro de este, seleccionamos “choose zip from sd card” y elegimos el archivo “Zelly Cream v3.0.1 by gagan.u20.zip”.  

    9. Se ejecuta el instalador, en el cual seguimos las instrucciones; Hay algunas cosas que se pueden personalizar, yo solamente elegí la versión de mi dispositivo, y no instalé ninguna de las aplicaciones que propone, pero eso va en cada uno.  

    10. Cuando termina la instalación, desactivamos la opción “Reboot device”, y le damos “Finish”.  

    11. Una vez en CWM Recovery, seleccionamos “Reboot system now”.  
  
    ¡Listo! Ya está instalado Zelly Cream 3.0.1 en nuestro Neo V, ahora solo hay que esperar a que se termine de preparar todo y el sistema cargue, luego solo seguir el asistente.  
  **Si pensas instalar Link2SD, te recomendaría hacerlo automáticamente después de sincronizar la cuenta de Google.**  

4. **Instalamos y configuramos Link2SD**  
  Link2SD es una aplicación que utiliza una fortaleza que tiene GNU/Linux, los enlaces, que son como los accesos directos de Windows, pero su trabajo es bastante más desarrollado.  
  Link2SD, al instalarse una aplicación en la memoria interna del telefono, la mueve a la partición que hicimos para las aplicaciones, y crea un enlace duro, haciendo que en la memoria interna solo queden enlaces a las aplicaciones, y estas en realidad están en la tarjeta de memoria.  
  Hay que tener en cuenta que cuando saquemos la tarjeta y/o conectemos el celular a una computadora las aplicaciones NO ESTARAN DISPONIBLES, por lo que es mejor, a veces, apagar el telefono, quitar la tarjeta y conectarla de alguna otra forma a la computadora.  

    1. Instalado Zelly Cream 3.0.1, y ya sincronizada nuestra cuenta de Google, nos dirigimos al Play Store, Buscamos e instalamos Link2SD, y lo ejecutamos.  

    2. Nos va a aparecer una ventana que nos pregunta si le damos permiso de superusuario o no, obviamente, le damos a Link2SD permisos de Superusuario.  

    3. Luego, nos aparece el asistente para configuración, en donde nos pregunta el formato de la segunda partición de la tarjeta SD, seleccionamos, obviamente, EXT2.  

    4. Link2SD crea un script que se ejecuta cuando inicia Android, este script se encarga de montar la partición como parte del sistema cada vez que Android inicie. Luego de crear el script, nos dice que tiene que reiniciar el sistema; Reiniciamos.  

    5. Después de que reinicia, y ejecutamos nuevamente Link2SD, y pasamos una ventana introductoria, nos muestra una lista de las aplicaciones instaladas, apretamos la tecla “menu” del Xperia, y nos vamos a “Ajustes”, ahí checkeamos que esten activas las opciones “Enlace Automático”, las 3 opciones que aparecen en “Ajustes de enlace automático”. Tambien, en “Ubicación de la instalación” seleccionamos “Externo”, esto es para que las aplicaciones que se puedan instalar en la tarjeta SD, lo hagan. (es decir, las que sin Link2SD se pudieran mover a la tarjeta SD).  
      Más de eso, no hay que configurar para que la aplicación funcione.  

    6. En el menú principal tambien tenemos para seleccionar “Información de almacenamiento”, que muestra más detalles de almacenamiento.  

    7. Una vez configurado Link2SD, ya pueden instalar aplicaciones, este automáticamente.  

    8. Algunas consideraciones:  

        * Ciertas aplicaciones, por ejemplo: WhatsApp, y otras que es mejor que tengan más performance, **conviene dejarlas en la memoria interna del celular, estas se van a ejecutar con más velocidad que las que estén en la tarjeta SD**.  

        * En “Ajustes” > “Almacenamiento” no se va a mostrar la memoria extendida generada por Link2SD, si no que se veran numeros incoherentes, como los de la imagen que muestra que la memoria interna tiene 420MB, tengo instalado 428MB en aplicaciones y casi 100 disponibles.  
[![links2sd-1](/images/article/2013/08/links2sd-1.png)](/images/article/2013/08/links2sd-1.png)  
[![links2sd-2](/images/article/2013/08/links2sd-2.png)](/images/article/2013/08/links2sd-2.png)  
  

Yo lo tengo hace más de 24 horas y anda muy bien. Tengo instalado:  
Adobe Reader, Androidify, Barcode Scanner, Brujula, Google Calendar, ConnectBot, Cymera, Google Drive, Dropbox, ES File Explorer, Facebook, Flash Player, Foursquare, Google Goggles, Google+, Hangouts, Instagram, Level, Linkedin, Maps, Facebook Messenger, My Tracks, Pinterest, Shazam, Google Sky Map, Android Terminal Emulator, Google Translator, Tumblr, Twitter, WakeOnLan, WhatsApp y YouTube Remote, y el equipo sigue funcionando excelente.  
  

Espero les sea útil el articulo. Saludos!
