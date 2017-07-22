Title: A perder el tiempo… HP Compaq Airlife 100
Date: 2014-03-15 22:00
Category: Misc
Tags: Airlife100, Android, GNU/Linux, kernel, MSM8250, project, QSD8250, Qualcomm, Snapdragon
Lang: es
Slug: waste-time-airlife100
adsense: 1
Summary: <img alt="airlife100" src="/images/article/2014/03/airlife100.jpg" class="alignright">Hace unos días terminé la facultad, y si bien tengo bastantes cosas para hacer, he decidido dedicar un poco de tiempo a intentar hacer andar la [HP Compaq Airlife 100](http://www.hp.com/latam/ar/hogar/promociones/airlife/) que compré hace unos años, a ver si puedo sacarle provecho antes de que pase a ser algo totalmente inútil.</br></br>La Airlife 100 es una tablet que tiene un procesador [Qualcomm Snapdragon MSM8250](http://system-on-a-chip.findthebest.com/l/268/Qualcomm-Snapdragon-QSD8250), tiene un formato demasiado bueno como para dejarla tirada, y no voy a dar muchos detalles técnicos, ya que estos abundan en internet, pero les voy a dar mi simple opinión: ¡es hermosa!.. Si, es hermosa, teclado, mouse, pantalla táctil, y tiene un peso ideal, además, la batería dura aproximadamente 13 horas.  

**¿Que es lo que le pasa?**  
Bueno, el problema es que trae Android 1.6 (totalmente privatizado, la tablet es fabricada por HP Compaq y comercializada por Movistar), y un Kernel 2.6.29 (muy, muy antiguo), por lo cual, actualizar Android es algo tedioso, instalarle una distribución GNU/linux también.  

He intentado comenzar con varios proyectos, uno de esos era airlife100.com.ar, el cual era un portal dedicado a la tablet, en la cual fui subiendo aplicaciones que corrían en la versión oficial de la tablet (Angry Birds, Google Maps, una versión vieja de Facebook, entre otras), y tenía como propósito construir una versión nueva de Android para la tablet; Si bien debería continuar con ese proyecto, el ente que proporciona los dominios “.com.ar” ahora cobra el registro y renovación de los dominios (a un precio mayor que el registro de un dominio “.com”), entonces, se me torna complicado soportar económicamente el portal, además, no hubo un mucho “quorum” involucrado en el desarrollo de una actualización.  

Ahora, he decidido ponerme manos a la obra en una actualización para el dispositivo, por empezar, debería hacer un kernel actualizado (estoy pensando en un 2.6.39), y aunque los pronósticos no sean buenos, creo que lo único que tengo para perder es tiempo y, a lo sumo, el funcionamiento de una tablet que no funciona.  

**¿Como voy?**  
¡No sé! Empecé ayer, estoy muy entusiasmado, pero no entiendo nada de kernel, compilarlo quizá sea la tarea más fácil, pero todavía estoy viendo como “prepararlo”.  

Descargué de [kernel.org](https://www.kernel.org/) el kernel 3.13.6 estándar, conseguí la versión oficial del [kernel de la Airlife 100 (kernel 2.6.29)](http://adf.ly/g5QGg) y empecé a compararlos; Encontré cosas que me llamaron la atención (una referencia a arch/n68knommu, y un otra a unos drivers wi-fi Atheros). Después, pensé que capaz había mucha diferencia entre el kernel 2.6.29 y el 3.13.6, entonces descargué el 2.6.39.4 y los empecé a comparar.  

El comando “diff” de GNU/linux, me dio un resultado que quizá también me sirva: en arch/arm/mach-msm/ se encuentran los controladores para el Qualcomm Snapdragon MSM8250 (y en drivers/msm/ deberían estar los drivers del GPU Adreno 200).  

Hay varias distribuciones GNU/Linux preparadas para correr en procesadores con instrucciones basadas en ARMv7, yo, por mi parte, tengo pensado intentar hacer funcionar [Fedora ARM](https://fedoraproject.org/wiki/Architectures/ARM), pero si el kernel queda funcionando, será posible la instalación de varias distribuciones, inclusive, versiones más actualizadas de Android.  

Por ahora es lo único que sé, estoy seguro de que es un trabajo que me va a tomar muchísimo tiempo, pero pienso que hay un montón de gente en España y países de latinoamerica que sufren como yo, quizá alguno pueda ayudarme.  

Veré que pasa con ésto, solo les pido ayuda, si es que saben algo.
