Title: CyanogenMod 7.2.2 en Motorola Milestone
Date: 2012-09-26 21:00
Category: Smartphones
Tags: Android, CyanogenMod, Gingerbread, Milestone, Motorola
Lang: es
Slug: motorola-milestone-cyanogenmod-722
adsense: 1 
Summary: Acabo de instalar la versión final de **Cyanogenmod** (7.2.2) en mi **Motorola Milestone**, anteriormente había instalado la Release Candidate 2 de la versión 7.0.2 y el gran problema que el encontré fue que no podía bloquear la pantalla.</br>A continuación explico los pasos a seguir para concretar la instalación (los cuales fueron extraídos en su mayoría de [aquí](http://www.mrmuh.com/2012/01/update-a-motorola-milestone-from-motorola-firmware-to-cyanogenmod-7 "").  

Para empezar, aclaro que hay que tener cuidado a la hora de hacer este tipo de trabajos, y siempre hay que tener la **batería cargada**. Tambien, el celular debe estar en con la versión oficial  de Android 2.2 de Motorola.  

Listo los archivos que se van a necesitar, así los descargas de antemano y no hay contratiempos:  

* [OpenRecovery 1.46](http://adf.ly/deE4L "OpenRecovery 1.46").
* [Vulnerable Recovery para Milestone](http://adf.ly/deE5G "Vulnerable Recovery for Milestone").
* Drivers Motorola ([32-bits](http://adf.ly/deE6O) o [64-bits](http://adf.ly/deE7R), dependiendo de tu sistema operativo).
* [RSDLite 5.7.](http://adf.ly/deE8f "RDSLite 5.7").
* [La última versión de CyanogenMod disponible](http://adf.ly/deEAA "") (Actualmente 7.2.2).
* [Google Apps](http://adf.ly/deEBE) (Ultima versión 2011-12-16). (Podés fijarte [acá](http://android.doshska.net/cm7) si hay una nueva versión).

Ahora, vamos a lo nuestro...

1. **Preparar OpenRecovery**  
  OpenRecovery son herramientas para la gestión del equipo y del sistema operativo, el cual vas a usar para restaurar el celular a fabrica, actualizarlo y, básicamente, todos los pasos a seguir.
    1. Descarga [OpenRecovery 1.46](http://adf.ly/deE4L ""), y lo descomprimís en el directorio raíz  de la tarjeta MicroSD del equipo. (Esta es la ultima versión del OR hasta la fecha, y tiene anidados modulos y librerías, para el manejo de la tarjeta MicroSD, disposición del teclado, bandas de funcionamiento, etc).

    2. Ahora deberías tener una carpeta “OpenRecovery” y un archivo “update.zip” en tu tarjeta MicroSD.


2. **Instalar el “Vulnerable Recovery”**  
  El “Vulnerable Recovery” no cambia nada en el sistema del dispositivo, solo flashea la partición de recuperación original, permitiendo que se ejecute el OpenRecovery desde la MicroSD.
    1. Descarga “Vulnerable Recovery”, los drivers (depende si tu sistema operativo es 32-bits o 64-bits) y RSDLite. Instala primero los drivers y luego RSDLite.

    2. Apaga el teléfono, y lo encendes en modo Bootloader, para esto, lo apagas y apretás la tecla de arriba (del teclado qwerty, no la de volumen) mientras presionas la tecla de encendido.

    3. Conectás el Milestone a la computadora y esperas que Windows instale los drivers.

    4. Ejecutá RSDLite, y el dispositivo debería estar aparecer en la lista (S Flash OMAP3430) como “conected”.

    5. Elegí el archivo sbf del vulnerable recovery haciendo clic en el botón “…” que aparece arriba.

    6. **IMPORTANTE:** Cuando el teléfono se reinicie luego de empezar el proceso de flasheo, es MUY recomendable que no llegue a iniciar android, e inicie Open Recovery. Para esto hay que mantener el botón de la cámara presionado mientras el equipo se reinicia, hasta que aparezca un triangulo.  
Haz clic en el botón “start” y espera a que el teléfono reinicie. Acordate de mantener el botón de la cámara precionado cuando esto pase.

    7. Cuando el dispositivo haya iniciado Open Recovery, RSDLite no va a haber terminado (y nunca lo va a hacer), ignora cualquier cartel de advertencia y cerralo, ya está listo.


3. **Instalar OpenRecovery**  
  NOTA:Todas las veces que quieras inicar el equipo en modo recovery debes mantener el botón de la cámara junto con el de encendido.
    1. Cuando el triangulo aparezca, mantené presionado el botón de subir el volumen y apretás el botón de la cámara. Con esto, accedes al recovery actual, es decir, el que trae Motorola Milestone.

    2. Para terminar de instalar OpenRecovery, tenés que seleccionar “apply sdcard:update.zip”. (La navegación por el menú es con las direcciones del teclado qwerty y el botón del medio actúa como ENTER).

    3. Después de un rato, verás que el menú cambió. Ahora, inclusive, puedes moverte con las teclas de volumen, y el botón de la cámara hace de ENTER.  
Debería verse algo como la siguiente imagen:  
<center>![OpenRecovery](http://2.bp.blogspot.com/_8HmrfJJQrGw/TSMoFnnO3ZI/AAAAAAAAA8M/9agds36If-U/s1600/xt720%2Bopenrecovery.png "OpenRecovery")</center>  

    4. En el punto 2.6, dije que no convenía que el teléfono iniciara Android, la razón es porque Motorola instala un script que instala el recovery original, este se ejecuta cada vez que se inicia Android.  
Para eliminarlo:
        1. Ejecutamos la consola (“console”) de OpenRecovery
        2. Ejecutamos el comando “rm -f /system/etc/install-recovery.sh”
        3. Ahora ejecutamos “exit” para salir, y listo.

4. **Particion para Aplicaciones (Opcional)**  
  A pesar de ser un paso opcional, es recomandado hacerlo, aumenta el espacio para instalar aplicaciones de tu teléfono.  
  >**NOTA:** Siempre que quieras cambiar la disposición de teclado de OpenRecovery, tenés que ir a “settings/Keyboard Layout” y cambiarlo.

    Para hacer esto, necesitas: 
 
    * Más de 1GB, ya que la particion que vamos a hacer es de 1GB, y necesitas para los demás datos.
    * Conocimientos básicos sobre Linux y particiones.
    * Un backup de los datos de la SD (por si no se cumple muy bien el punto anterior).

    Dentro del menú de OpenRecovery, nos vamos a la consola (“console”). Ahí:

    1. Desmontamos la tarjeta con el comando “umount /sdcard”.
    2. Iniciamos el editor de particiones parted con el comando “parted /dev/block/mmcblk0”.  
**IMPORTANTE:** Dentro de parted la tecla borrar NO FUNCIONA, así que tené mucho cuidado con lo que escribes.  
    3. Listá la tabla de particiones de tu MicroSD con el comando “print”  
Deberías ver algo como la imagen siguiente:  
Es importante que anotes el tamaño exacto de la tarjeta. Verás “Disk /dev/block/mmcblk0: XXXXMB”, esos XXXXMB son el tamaño exacto de la tarjeta.
    4. Redimensiona la partición FAT32 para dejar 1GB libre (1024MB). En el caso de la imagen, la partición sería 7969MB – 1024MB = 6945MB.  
Para hacerlo, ejecuta el comando “resize 1 0MB 6945MB”, donde:
        * 1 es el número de partición.
        * 0MB es donde comenzaría la partición.
        * 6945MB es donde terminaría la partición.
    5. Creá la particion ext2 usando los 1024MB que quedaron libres al final de la partición en el paso anterior.
Usa el comando “mkpartfs primary ext2 6945MB 7969MB”, donde:
        * “primary” es el tipo de partición.
        * “ext2” es el sistema de archivos.
        * 6945MB es donde comenzaría la partición.
        * 7969MB es donde terminaría la partición.
    6. Listá nuevamente las particiones, para corroborar que todo haya salido bien, esto con el comando “print”.  
       Debería verse algo parecido a la imagen siguiente.
    7. Si todo salió bien, con el comando “quit” salimos de parted.
    8. Convertimos la particion ext2 a ext3, usando el comando “tune2fs -j /dev/block/mmcblk0p2”.
    9. Todo listo, salimos de la consola con el comando “exit”.
  >**NOTA:** Durante el uso del teléfono, no se podrá admirar el espacio, pero cuando instalas aplicaciones, veras que no disminuye el espacio ocupado por esta.

5. **Instalar CyanogenMod**  
  El último paso es instalar CyanogenMod. Una vez que tengás [la última versión descargada](http://adf.ly/deEAA) y las [Google Apps](http://adf.ly/deEBE),los pasos a seguir son:  
    1. Iniciar el equipo en OpenRecovery.
    2. Elige “Wipe Dalvik cache”.
    3. Luego, elige “Wipe data / Factory Reset” (te apareceran como 9 “no” y 1 “yes”, esto es por seguridad, dale al “yes”, obvio).
    4. Ahora selecciona “Wipe cache partition”.
    5. Te vas a “Apply update” y seleccionas el archivo de Cyanogen que descargaste. (Existen otros test-*, que son solo pruebas y muestras, si te molestan los borras).
    6. Después seleccionas las Google Apps, tambien en el menu de “Apply update”.
    7. Volvés al menú principal de OpenRecovery, seleccionas “Reboot System” y listo.
    8. Lo dejás iniciar CyanogenMod, la primera vez demora un poco más de lo normal.

6. **Actualizar CyanogenMod**
  Es recomendable mantener CyanogenMod actualizado, de vez en cuando fijate si hay una versión nueva, y para actualizar, los pasos son:
    1. Iniciar el teléfono en OpenRecovery.
    2. Selecciona “Wipe Cache partition”.
    3. Selecciona “Wipe Dalvik cache”.
    4. Instala la actualización desde “Apply Update”.
    5. Reinicia el equipo, y estará iniciando la nueva versión de Cyanogen (Toma más tiempo de lo normal).



**Espero les haya servido**
