Title: Actualizar Sony Ericsson Xperia Neo V con Ice Cream Sandwich OFICIAL
Date: 2012-11-17 23:00
Category: Smartphones
Tags: Android, firmware, flashtool, Gingerbread, Ice Cream Sandwich, ICS, Neo V, Sony Ericsson, Xperia
Lang: es
Slug: update-SE-NeoV-ICS-oficial 
adsense: 1
Summary: Hace un par de días, tras la ruptura de mi Motorola Milestone, decidí comprarme un teléfono nuevo. Un amigo me había mostrado el Sony Ericsson Xperia Neo V, el cual parecía tener muy buenas prestaciones en relación a su costo; Apenas conseguí la plata me lo compré. Como este post no está dedicado a cubrir lo que es el celular, voy directamente al tema.</br></br>El celular trajo Android Gingerbread 2.3.4, anda bien, pero yo estaba acostumbrado al CyanogenMod que tenía en mi Milestone, con Android Gingerbread 2.3.7; Entonces, me puse a averiguar como actualizar a una versión más moderna y funcional de Android.</br></br>Con los pasos que describo a continuación, conseguí instalarle un firmware OFICIAL DE SONY con Android Ice Cream Sandwich 4.0.4.

![NeoVAndroid404](/images/article/2012/11/NeoVLogoyAndroid404.jpg)


**ADVERTENCIA: SE BORRAN TODOS LOS DATOS QUE HAY EN EL TELÉFONO, DEJA EL TELÉFONO COMO NUEVO. Lo unico que no borra son los datos de la tarjeta MicroSD.**  

1. **Descargamos lo necesario para realizar la actualización.**  
    * Firmware 4.1.B.0.587 (Tenémos que descargar la versión acorde a nuestra ubicación)  
    a = american | i = international
        * [MT11a 4.1.B.0.587 US, CDF-1254-9468i](http://adf.ly/deDZU)  
        * [MT11i 4.1.B.0.587 NCB, Nordic, CDF-1255-1755, SI-1254-9263](http://adf.ly/deDZU)  
        * [MT11i 4.1.B.0.587 India CDF-1254-8478, SI-1254-8966](http://adf.ly/deDch)  
        * [MT11i 4.1.B.0.587 Central Europe 1, CDF-1254-9708](http://adf.ly/deDeF)  
        * [MT15i 4.1.B.0.587 NCB, Nordic, CDF-1247-0875](http://adf.ly/deDft)  

    *  Flashtool (ultima versión disponible)  
        * [Flashtool — Xperia devices flashing](http://adf.ly/uUJeV)  

2. **Instalamos Flashtool y los drivers correspondientes**  
    * Instalamos Flashtool, corriendo el ejecutable y siguiendo los pasos de instalación.  
    * Una vez finalizada la instalación, nos dirigimos a la carpeta donde se instaló Flashtool (Por ejemplo: “C:\Flashtool”).  
    * Dentro de la carpeta de Flashtool, acccedemos a la carpeta “drivers”, y ejecutamos el *.exe que se encuentre en ese directorio (“Flashtool-drivers.exe”, en este caso).  
    * En la lista de controladores, elegimos los siguientes:  
        * Sony Ericsson Xperia arc, Xperia Neo, Xperia PLAY, Xperia acro IS11S, Xperia acro SO-2C drivers  
        * Flashmode Drivers  
        * Fastboot Drivers  

    ... y finalizamos la instalación.

3. **Copiamos** el archivo *.tft (firmware) al directorio “firmwares” dentro del directorio de instalación de Flashtool.  

4. **Ejecutamos Flashtool**, y hacemos click en el trueno, seleccionamos “Flashmode” y le damos OK.  
    ![flash-tool](/images/article/2012/11/flashtool-flashmode.png)
5. En la lista de Firmwares que apareció, **seleccionamos** la que corresponde (MT11i, por ejemplo), y le damos OK.  

6. Nos aparece un cartel que dice que **desconectemos y apaguemos el teléfono**, que apretemos y mantengamos apretado el botón “volver” (la flechita para atras) y conectemos el cable. **NO SOLTAR LA TECLA HASTA QUE TERMINE EL PROCESO**.  

7. **Comienza la instalación de los drivers**, puede ser que además de los drivers que instalamos, Windows necesite descargar algunos (automáticamente) de internet.  

8. Una vez finalizada la instalación de los drivers, Flashtool comienza a hacer su trabajo, tenemos que **esperar a que termine**, y dice que prendamos el dispositivo.  

9. **Prendemos el dispositivo**, y listo, ya está actualizado el firmware.
