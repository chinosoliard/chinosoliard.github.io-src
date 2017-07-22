Title: Impresoras Samsung en Fedora
Date: 2012-10-21 19:00
Category: Fedora
Tags: CLP-315, CUPS, Fedora, GNU/Linux, printer, ML-1640, samsung, Samsung Unified Linux Drivers, SPLIX
Lang: es
Slug: samsung-printer-on-fedora
Summary: Hace más de 2 años que tengo 2 impresoras láser marca Samsung, una [ML-1640](http://www.samsung.com/es/consumer/pc-peripherals-printer/printers/laser-monocrome-printers/ML-1640/SEE) y una [CLP-315](http://www.samsung.com/es/business/printer/productos-y-soluciones/impresoras-y-faxes/impresoras-l%C3%A1ser-color/clp-310-/impresora-l%C3%A1ser-color-clp-315/feature.prt?printerCode=CLP-315/SEE). Sinceramente, nunca me dediqué mucho a hacerlas funcionar en GNU/Linux, cuando intenté hacerlo simplemente con [CUPS](http://www.cups.org/) no lo conseguí. Ahora que uso [Fedora](http://www.fedoraproject.org/es/) el 99,9% del tiempo en que estoy sentado frente a un equipo, tuve que buscar la forma de que funcionen. Luego de publicar una pregunta en [ask.fedoraproject.org](http://ask.fedoraproject.org), recibí 2 respuestas, de las cuales una funcionó.

La primera y no funcional, era instalar los drivers oficiales de [Samsung Unified Linux Drivers](http://downloadcenter.samsung.com/content/DR/200911/20091118145015140/UnifiedLinuxDriver_1.01.tar.gz), lo ejecuté con “$ sudo”, y comencé la instalación. Durante la instalación ya se pueden instalar impresoras, conecté la ML-1640, y parecía ir todo muy bien. Cuando terminé con toda la instalación, voy a CUPS ([http://localhost:631](http://localhost:631/)) y la impresora aparecía. Entre muchos detalles que ya no recuerdo, lo único que sé es que la impresora NUNCA FUNCIONÓ, busqué en internet y resultó que el paquete era muy problemático entonces proseguí a desinstalar el maldecido paquete, para esto, en una consola ejecutamos $ sudo /opt/Samsung/mfp/uninstall/guiuninstall, esto iniciará la desinstalación. Después de unos pasos, el programa no dejó rastros (o eso pareciera).

La segunda, funcional, y mucho más sencilla, es instalar SPLIX, un conjunto de drivers para CUPS que manejan SPL (Samsung Printer Language). A continuación, explico como lo hice.

1. Ahora está empaquetado para Fedora, entonces, lo único que hay que hacer para instalar el paquete es ejecutar en una consola:  
  `$ sudo yum install splix`

2. Después de instalar SPLIX, solo basta con conectar la impresora (aparecen ventanas para instalar drivers, pero cancelen) e ir a CUPS (http://localhost:631), una vez en CUPS, nos vamos a Administración, y ahí a “Añadir impresora”.

3. En la lista de impresoras locales nos aparece la impresora conectada, la seleccionamos y le damos a “siguiente”.
[![samsung-printer-on-fedora-1](/images/article/2012/10/samsung-printer-on-fedora-1.png)](/images/article/2012/10/samsung-printer-on-fedora-1.png)

4. Luego aparecen las configuraciones para nombre de la impresora, descripción, ubicación, y la opción de compartirla, le damos siguiente (después de configurar a gusto los campos).
[![samsung-printer-on-fedora-2](/images/article/2012/10/samsung-printer-on-fedora-2.png)](/images/article/2012/10/samsung-printer-on-fedora-2.png)

5. Llegamos a la parte donde definimos el controlador, en la lista “Modelo” seleccionamos el modelo que estamos instalando, después “Añadir impresora”.
[![samsung-printer-on-fedora-3](/images/article/2012/10/samsung-printer-on-fedora-3.png)](/images/article/2012/10/samsung-printer-on-fedora-3.png)

6. Finalmente, se nos pide que establezcamos las opciones predeterminadas de la impresora.
[![samsung-printer-on-fedora-4](/images/article/2012/10/samsung-printer-on-fedora-4.png)](/images/article/2012/10/samsung-printer-on-fedora-4.png)

7. Una vez que estemos en la parte de la impresora, dentro de CUPS, podemos probar la impresora seleccionando “Imprimir página de prueba” en la lista “Mantenimiento”.
[![samsung-printer-on-fedora-5](/images/article/2012/10/samsung-printer-on-fedora-5.png)](/images/article/2012/10/samsung-printer-on-fedora-5.png)


La impresora ya está funcionando, pero, a mi personalmente, me quedaron 4 impresoras instaladas en la lista de impresoras de CUPS, por lo que eliminé las que yo no instalé (las detecté por el nombre).

[![samsung-printer-on-fedora-6](/images/article/2012/10/samsung-printer-on-fedora-6.png)](/images/article/2012/10/samsung-printer-on-fedora-6.png)

Bueno, así de sencillo fue instalar las impresoras, espero les haya sido útil.
