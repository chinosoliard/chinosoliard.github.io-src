Title: ROM Zelly Cream v2.0 en Xperia Neo V con Firmware 4.1.B.0.587
Date: 2013-03-19 23:30
Category: Smartphones
Tags: Android, ClockWorkMod, Recovery, CWM, Gingerbread, Ice Cream Sandwich, ICS, Neo V, Sony Ericsson, Xperia, Zelly Cream
Lang: es
Slug: zelly-cream-20-xperia-neov-firmware-41B0587
adsense: 1
Summary: Las ROMS originales traen restricciones y aplicaciones de más (entre otras cosas que quizá no nos agraden). Cambiarle la ROM al celular nos permite sacarle mas fruto al celular, aunque, puede ser que las ROMS tengan problemas, por eso siempre hay que asesorarse bien.</br></br>Zelly Cream 2.0 es una de las ultimas ROMs diseñadas para Xperia Neo V, los comentarios que he leído son muy buenos, y ahora que lo estoy probando estoy convencido de que es una muy buena alternativa (y quizá, por ahora, la mejor).</br></br>A continuación, una pequeña “guía” de instalación de Zelly Cream 2.0 en el Xperia Neo V.  

**Para realizar la instalación, el celular debe estar [actualizado](/blog/2012/nov/update-SE-NeoV-ICS-oficial-es.html) y [rooteado](/blog/2013/mar/rooting-SE-NeoV-firmware-41B0587-es.html). Si no fuera así debes hacerlo antes de continuar.**  

Los archivos que vamos a necesitar son:  

* [ClockWorkMod Recovery](http://adf.ly/deDCD) [1]  

* [Zelly Cream v1.2.0 – FULL ROM](http://adf.ly/deDuS) [2]  

* [Zelly Cream v2.0 – Update ROM](http://adf.ly/deDvB) [3]  

* [Zelly Cream hot update [4]](http://adf.ly/deDwq) [Opcional]  

Lo primero que hacemos es instalar ClockWorkMod Recovery, es un programa que puede ejecutarse antes de que se carge el sistema operativo, permite hacer limpiezas, actualizar el sistema, realizar backups, entre otras cosas. Para hacerlo:  

1. Extraemos el contenido del archivo [1].  

2. En el celular nos vamos a “Ajustes” > “Opciones de desarrollo” y activamos “Depuración de USB”.  

3. Ejecutamos “install-cwm1.bat” (de los archivos extraídos, obvio) y conectamos el dispositivo y seguimos las instrucciones.  
  **Nota:** *El software dice que prendas la pantalla y aceptes los permisos de superusuario, a mi, personalmente, no me saltó ningun cartel, pero me fijé en los registros de la aplicación Superuser y aparecía una actividad por consola.*  

4. Finalmente, ClockWorkMod está instalado, para ejecutarlo apagamos el equipo y cuando lo prendemos, apenas vibra empezamos a apretar repetidamente el botón de bajar volumen.  

**ClockWorkMod nos sirve para instalar esta ROM entre otras que hay dando vueltas por la web, yo probé otra que no me terminó de convencer, y ahora voy a proba esta. Si quieren pueden probar otra, pero recuerden que los pasos no siempre son los mismos.**  


Procedemos a la instalación de Zelly Cream, **recuerden tener la batería del celular con una carga considerable**.  

1. Copiamos los archivos restantes [2][3][4] a la tarjeta microSD del celular.  

2. Iniciamos ClockWorkMod Recovery.  

3. Seleccionamos “wipe data/factory reset” con la tecla “home” (la casita) y luego seleccionamos “Yes”. (La navegación se realiza con las teclas de volumen)  

4. Seleccionamos “wipe cache partition” y luego “Yes”.  

5. Nos dirigimos a  “advanced” y ahí hacemos “Wipe Dalvik Cache”.  

6. Tambien en “advanced” le damos a “Wipe Battery Stats”.  

7. Luego nos vamos a “mounts and storage” del menú principal y seleccionamos “format /data”, “format /system” y “format /cache”.  

8. Ahora, nos dirigimos a “install zip from sdcard” en el menú principal, dentro de este, seleccionamos “choose zip from sd card” y elegimos el archivo “Zelly Cream 1.2.0 by gagan.u20.zip” ([2]).  

9. Se ejecuta el instalador, en el cual seguimos las instrucciones; Hay algunas cosas que se pueden personalizar, yo solamente elegí la versión de mi dispositivo.  

10. Desactivamos la opción “Reboot device” cuando termina de instalar, así vuelve al ClockWorkMod Recovery, y le damos “Finish”.  

11. En ClockWorkMod Recovery, hacemos lo mismo que en el paso 8, pero esta vez elejimos “Zelly Cream v2.0 by gagan.u20.zip” [3].  

12. Seguimos los pasos de instalación, nuevamente podemos personalizarla, yo, otra vez, elegí mi dispositivo y nada más. Termina la instalación y volvemos a hacer el paso 10.  

13. Ahora, hacemos el paso 8, pero elegimos el último archivo, “Zelly Cream App Updates.zip”[4]. Este es mucho más rápido y sencillo, en unos segundos ya está listo.  

14. Volvemos al menú principal de ClockWorkMod Recovery y seleccionamos “reboot phone”.  

¡Listo! Ya está instalado Zelly Cream en nuestro Neo V, ahora solo hay que esperar a que se termine de preparar todo y el sistema cargue, luego solo seguir el asistente.
