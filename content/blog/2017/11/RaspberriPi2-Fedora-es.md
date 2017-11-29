Title: Instalando Fedora en Raspberry Pi 2
Date: 2017-11-28 22:15
Category: Fedora
Tags: Fedora, Raspberry, RPi, ARM
Lang: es
Slug: installing-fedora-on-raspberry-pi-2-b
Summary: <a href="https://www.raspberrypi.org" target="_blank"><img alt="Raspberry Pi" src="/images/static/RaspberryPi-150.png" class="alignright"></a> Hace un buen par de años conocí las [Raspberry](https://www.raspberrypi.org), y desde entonces quise tener una. El tiempo pasó, y salió la Raspberry Pi 2, y salió la Raspbery Pi 3, y salió la Raspberry Pi Zero, y yo sin mi Raspbery... Después de unos 3 años, ¡me compré una!.. Tengo una [Raspberry Pi 2 Model B](https://www.raspberrypi.org/products/raspberry-pi-2-model-b/) hace unas 2 semanas , y, por cuestiones de tiempo, no he podido usarla, ni siquiera prepararla. Así que ahora, que voy a ponerme manos a la obra, voy a hacer una pequeña guía de como instalar Fedora en la Raspberry, usando [Fedora Workstation](https://getfedora.org/en/workstation/). *Más adelante publicaré una guía de como hacerlo por consola*  

[![RaspberryPi2B](/images/article/2017/11/RaspberryPi2.jpg)](/images/article/2017/11/RaspberryPi2.jpg)  
## ¿Qué es Raspberry Pi?
Se podría decir que es **una micro-computadora, como para resumir**, pero si queremos extender un poco la explicación, podemos decir que es un "ordenador de placa reducida" (en realidad, single-board computer, o SBC), es decir, una computadora completa montada en una sola placa.  
Todas las Raspberry Pi tienen un tamaño aproximado al de una tarjeta de crédito (a excepción de la [Zero](https://www.raspberrypi.org/products/raspberry-pi-zero/) que tiene la mitad de tamaño), lo que hace que sea usada para muchos proyectos IoT (Internet of Things, o Internet de las cosas); También, tienen salida HDMI, USB, y conexión ethernet, inclusive, la versión 3, tiene WiFi incluido.  
La alimentación es vía microUSB (el peor invento en los últimos años :-P), siempre con 5V, pero varía el amperaje de acuerdo a la versión. Por último, no tiene ningún almacenamiento, tiene un slot microSD, en donde debe ir una tarjeta con el sistema operativo que se vaya a utilizar.  

En éste caso vamos a hacer una instalación mínima de Fedora en una **Raspberry Pi 2 Model B**, prepararemos todo desde una PC con Fedora instalado.  

## ¿Que vamos a necesitar?
  *  **Raspberry Pi (2 o 3):**  
    Obviamente, vamos a necesitar una Raspbery. ¿Por qué 2 o 3? Porque para éste caso, vamos a usar Fedora Media Writer, el cual, entre sus opciones, solo es compatible con esas versiones.  
  *  **Fuente de alimentación:**  
    De acuerdo a la versión de Raspberry que utilicemos, vamos a necesitar una fuente de alimentación distinta, por el consumo de la placa. Una fuente de 5V 2,5 amperes es suficiente para cualquiera de las 2 versiones, mientras que la Raspberry Pi 2 puede funcionar correctamente con una fuente de 5V 2 amperes.  
  *  **Memoria MicroSD:**  
    Como expliqué anteriormente, la Raspberry bootea el sistema operativo desde la MicroSD, por lo tanto, es necesario una tarjeta microSD de por lo menos 8GB de capacidad. Recomiendo, además, que sea Clase 10 o superior. Para éste ejemplo vamos a usar una memoria de 16GB clase 10.  
  *  **Cable HDMI (y display, obvio):**  
    Si bien las Raspberry tienen una salida analógica de audio y video, es más seguro que tengas un display (monitor o TV) con HDMI, para usarlo necesitamos, obviamente, un cable HDMI.  
  *  **Teclado USB:**  
    Vamos a necesitar un teclado para poder controlar la Raspberry antes de poder tener algún acceso para control remoto. Necesitamos que sea USB. Depende de la finalidad que tenga la Raspberry, puede ser que también quieran un mouse.
  *  **Dungle WiFi USB:**  
    En el caso de no tener posibilidad de hacer una conexión por red cableada, podemos usar una placa WiFi USB para conectarnos a alguna red.  
  *  **Imágen de Fedora para ARM:**  
    Al ser Raspberry un dispositivo con procesador ARM, vamos a tener que descargar una [imágen de Fedora para ARM](https://fedoraproject.org/wiki/Architectures/ARM/Raspberry_Pi?rd=Raspberry_Pi#Downloading_the_Fedora_ARM_image), en éste caso, como aclaré antes, vamos a usar la [versión "mínimal"](https://download.fedoraproject.org/pub/fedora/linux/releases/26/Spins/armhfp/images/Fedora-Minimal-armhfp-26-1.5-sda.raw.xz), por la capacidad de la memoria.  
  *  **Fedora Media Writer:**  
    [Fedora Media Writer](https://fedoraproject.org/wiki/How_to_create_and_use_Live_USB) es un software diseñado para crear dispositivos USB y tarjetas de memorias booteables, lo vamos a usar justamente para eso, crear la imágen de arranque de Fedora en la tarjeta microSD.  
    En Fedora, la instalación se puede hacer desde el centro de Software, o con el comando:  
  
    ` # dnf install mediawriter `  
  
  *  **GParted:**  
    [GParted](http://gparted.sourceforge.net/) es un editor de particiones compatible con GNOME, lo vamos a usar para modificar la partición que crea Fedora Media Writer.  
    La instalación en Fedora también puede hacerse desde el centro de Software, sino, con el comando:  
  
    ` # dnf install gparted `  
  
  
---

# ¡Manos a la obra!
**NOTA:** *Los screenshots fueron tomados hace unas semanas, cuando todavía no estaba disponible Fedora 27.*
## Paso 0: Descargar todo lo necesario
Instalaremos Fedora Media Writer y GParted, podemos hacerlo desde el Centro de Software o vía CLI con el comando:  
  
` # dnf -y install mediawriter gparted `  
  
También, deberemos descargar la imágen ARM de la versión de Fedora que queramos instalar, podemos ver las opciones en:  
[https://fedoraproject.org/wiki/Architectures/ARM/Raspberry_Pi?rd=Raspberry_Pi#Downloading_the_Fedora_ARM_image](https://fedoraproject.org/wiki/Architectures/ARM/Raspberry_Pi?rd=Raspberry_Pi#Downloading_the_Fedora_ARM_image)  

## Paso 1: Crear microSD con Fedora
1. Iniciamos Fedora Media Writer  
    ![mediawriter-0](/images/article/2017/11/mediawriter-0.png)
2. Vamos a "Mostrar sabores adicionales de Fedora" en la parte inferior de la lista de opciones.
    ![mediawriter-1](/images/article/2017/11/mediawriter-1.png)
3. En la lista que apareció en la parte superior, seleccionamos ARMv7.
    ![mediawriter-2](/images/article/2017/11/mediawriter-2.png)
4. Elegimos "Imágen personalizada" en la lista principal, y seleccionamos la imágen que descargamos.
    ![mediawriter-3](/images/article/2017/11/mediawriter-3.png)
5. En la ventana que  nos apareció, seleccionamos la versión de Raspberry que vamos a usar (y la tarjeta que vamos a escribir, si es necesario), y luego "Escribir al disco".
    ![mediawriter-4](/images/article/2017/11/mediawriter-4.png)
6. Escribimos la contraseña de root, para poder escribir la tarjeta de memoria.
    ![mediawriter-5](/images/article/2017/11/mediawriter-5.png)
7. Esperamos...
    ![mediawriter-6](/images/article/2017/11/mediawriter-6.png)
8. Listo.
    ![mediawriter-7](/images/article/2017/11/mediawriter-7.png)

## Paso 2: Modificar la partición root ("/")
Para hacer la imágen descargable lo más pequeña posible, se redujo a un mínimo el tamaño de la partición raíz o root ("/"), que es, básicamente, donde se guarda todo el sistema operativo y los que usaremos, tenemos ahora la posibilidad de crear particiones adicionales y/o agrandar la partición principal. En éste caso, vamos sólo a agrandar la partición root.  
  
1. Iniciamos GParted  
    **Nota:** Si tienen problema para ejecutarlo, es un **[problema de Wayland](http://gparted-forum.surf4.info/viewtopic.php?id=17446)**, habitual y no solucionado hasta la fecha. La solución es ejecutar (no es necesario usar root o sudo) el comando  
  
    `$ xhost +SI:localuser:root`  
  
    ![gparted-0](/images/article/2017/11/gparted-0.png)
2. Seleccionamos, en la lista de dispositivos de la parte superior, la que corresponda a la memoria microSD
    ![gparted-1](/images/article/2017/11/gparted-1.png)
3. Ahora podemos cómo ver está particionada la tarjeta microSD. En la imágen a continuación, está seleccionada la partición "/", pero, si prestan atención, está montada (tiene una llave a la izquierda), lo cual no va a permitir que la modifiquemos. Hay que desmontarla.
    ![gparted-2](/images/article/2017/11/gparted-2.png)
4. Desmontarlo es tan sencillo como apretarle botón derecho a la partición y luego "Desmontar", y esperar a que termine de desmontarse (apenas unos segundos).
    ![gparted-3](/images/article/2017/11/gparted-3.png)
5. Ahora podemos redimensionar la partición, para ésto, en el menú que se despliega desde la partición cuando usamos el botón derecho, seleccionamos "Redimensionar/mover"  
    ![gparted-4](/images/article/2017/11/gparted-4.png)
6. En la ventana que nos aparece, estiramos la partición al máximo posible (o a lo que pretendan). Lo que estamos haciendo es usar el espacio que esta sin asignar.
    ![gparted-5](/images/article/2017/11/gparted-5.png)
7. Después de aceptar las modificaciones a la partición, nos aparecerán dichas modificaciones en una cola de trabajos, si estamos de acuerdo con los cambios, le damos clic a "Aplicar todas las operaciones".
    ![gparted-6](/images/article/2017/11/gparted-6.png)  
8. A continuación, nos aclara que la operación puede causar la perdida de datos. Si estamos seguros de lo que vamos a hacer, "Aplicar". 
    ![gparted-7](/images/article/2017/11/gparted-7.png)  
9. Esperamos a que termine...
    ![gparted-8](/images/article/2017/11/gparted-8.png)  
    ![gparted-9](/images/article/2017/11/gparted-9.png)  
    ![gparted-10](/images/article/2017/11/gparted-10.png)  
10. Vemos los cambios y comprobamos que todo haya salido bien.
    ![gparted-11](/images/article/2017/11/gparted-11.png)  
    Si todo salió bien, ya podemos continuar con la memoria en la Raspberry.

## Paso 3: Arrancando la Raspberry Pi
[![Raspberry-Cables](/images/article/2017/11/Raspberry-Cables.jpg)](/images/article/2017/11/Raspberry-Cables.jpg)  
  
1. Colocamos la memoria microSD en la Raspberry Pi.
2. Conectamos todo lo que sea necesario (cable HDMI, cable de red, teclado y/o mouse, demás dispositivos USB)
3. (por último, **¡siempre!**) Conectamos la fuente de alimentación a la Raspberry.

## Paso 4: Configurando Fedora
Al finalizar el arranque, Fedora inicia un asistente de configuración; Disculpen la foto (en el celular se veía mejor).  
[![Raspberry-Fedora-Wizard](/images/article/2017/11/Raspberry-Fedora-Wizard.jpg)](/images/article/2017/11/Raspberry-Fedora-Wizard.jpg)  
  
Éste asistente, tiene 5 opciones, con subopciones.  
A continuación, muestro en profundidad las opciones del menú:  

1. **Idioma**  
   Ésto mostrará la lista de idiomas disponibles para instalación. **21** es español.  
2. **Timezone**  
   Hay que configurar la zona horaria. A veces lo detecta automáticamente, si no, se puede modificar después.  
3. **Configuración de red**  
     1. **Set host name**  
     Usamos ésta opción para darle un nombre al host (hostname.domain) (Ej: raspberrypi.micasa)  
     2. **Configurar red**  
     Si necesitáramos una configuración especifica de red (IP, DNS, etc), ésta es la opción. Usualmente, los routers otorgan configuración automáticamente via DHCP.  
4. **set root password**  
    Es **necesario** configurar una contraseña para "root", ya que es el superusuario del sistema.  
5. **Crear usuario**  
    Es cómodo crear un usuario durante el wizard, aunque puede hacerse después con la "root".  

Cuando terminamos de configurar lo que queramos/necesitemos, apretamos **c "continue"**, y listo. La Raspberry se reiniciará tomando la configuración  

## Paso 5: Actualizar
Una vez que arrancó, deberíamos actualizar el sistema. Ésto puede complicarse de acuerdo al tamaño de la memoria microSD, y de la versión de Fedora que usemos, ya que puede ocurrir que no alcance el espacio para descargar todas las actualizaciones. Si tienen ese problema, pueden ir instalando de manera selectiva las actualizaciones, para ir sobrescribiendo archivos con las actualizaciones, y así dejando espacio para otras.  
Para actualizar **todo** el sistema, debemos ejecutar el comando:  
  
` # dnf update `  
  
E "y" o "s" cuando pregunte si queremos proceder.  
Si caemos en el problema de la falta de capacidad de la memoria, podemos hojear las cosas que se van a actualizar en la lista actualizaciones que arrojaría el comando anterior, y ejecutarlo de forma selectiva para un paquete específico, por ejemplo:  
  
` # dnf update curl`  
  
O podemos hacerlo con varios paquetes específicos, por ejemplo:  
  
` # dnf update curl libcurl`  
  

## Paso 6: Ahora les toca a ustedes
Esto fue una pequeña guía para instalar Fedora Minimal, es decir, es hasta ahora, solo la linea de comandos.  
Pueden probar con otras versiones de Fedora, o instalar en Fedora Minimal un entorno de escritorio de su preferencia; Yo, por mi parte, voy a instalarle sway o i3wm, y empezar a armarlo con lo que necesite.  
  
Próximamente subo una **guía sobre como instalar i3** a partir de éstos pasos.
