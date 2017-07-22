Title: Rooteando Sony Ericsson Xperia Neo V con Firmware 4.1.B.0.587
Date: 2013-03-19 16:00
Category: Smartphones
Tags: Android, flashtool, Ice Cream Sandwich, ICS, MT11i, Neo V, root, Sony Ericsson, Xperia
Lang: es
Slug: rooting-SE-NeoV-firmware-41B0587
adsense: 1
Summary: Android está basado en Linux, por lo cual, rootear un celular nos permitirá obtener privilegios que nos permitiran realizar algunos cambios en el celular que de otra manera no podríamos.</br></br>En un [post anterior](/blog/2012/nov/update-SE-NeoV-ICS-oficial-es.html) expliqué como actualizar la versión oficial del Sony Ericsson Neo V a Ice Cream Sandwich, a continuación explico los pasos para rootear el Neo V con esta versión.

Para llevar a cabo el rooteo necesitamos la misma aplicación que usamos para actualizar el equipo, y además necesitamos descargar:  
  * [MT11i_4.1.A.0.562_kernel.ftf](http://adf.ly/deCwy)  
  * [DooMLoRD_v1_Xperia-2011-ICS-ROOT-emu-busybox-su.zip](http://adf.ly/deD0A)  


1. Nos vamos, en el celular, a “Ajustes” > “Opciones de desarrollo” y activamos “Depuración de USB” y “Permitir ubic. de prueba”.  

2. En “Ajustes”, nos vamos a “Xperia ™” > “Conectividad” > “Modo de conexión USB” y elegimos “MSC”.  

3. Copiamos el archivo que descargamos (MT11i_4.1.A.0.562_kernel.ftf) a la carpeta “firmwares” de Flashtool  

4. Ejecutamos Flashtool y hacemos clic en el rayo y luego en flashmode, como cuando actualizamos el telefono (se explica en el post citado anteriormente).  

5. En la lista, seleccionamos la versión ***.0.562 y le damos OK, nos aparece la ventana diciendo que desconectemos y apaguemos el teléfono; Luego apretamos y mantenemos apretado el botón “volver” y conectamos el cable USB. Flashtool empieza a flashear el dispositivo, solo hay que esperar a que termine.  

6. Extraemos los archivos de “DooMLoRD_v1_Xperia-2011-ICS-ROOT-emu-busybox-su.zip” y ejecutamos “runme.bat” de los archivos generados.  

7. Con el equipo prendido, conectamos el cable USB y omitimos “PC Companion Software”. El teléfono se reiniciara algunas veces, y cuando el programa diga que está listo, podemos continuar.  

8. Ahora, solo queda volver a actualizar el Kernel; Para eso, abrimos nuevamente Flashtool, el rayo y luego flashmode, pero ahora excluímos todo menos Kernel, como se muestra en la imágen, le damos “OK” y flasheamos nuevamente.  
[![flashtool-onlykernel2](/images/article//2013/03/flashtool-onlykernel2.png)](/images/article//2013/03/flashtool-onlykernel2.png)  


Y con estos simples pasos, ¡listo! Nuestro Sony Ericsson Neo V ahora tiene Ice Cream Sandwich y está rooteado.  

Espero les sirva. Saludos!
