Title: AndSec 2016 [Reporte]
Date: 2016-06-13 14:00
Category: Fedora
Tags: Fedora, SELinux, CABA, event, AndSec
Lang: es
Slug: andsec-2016-report
Summary: <a href="http://www.andsec.org" target="_blank"><img alt="andsec" src="/images/article/2016/06/logo-andsec.png" class="alignright"></a>El 4 y 5 de junio, con <a href="https://fedoraproject.org/wiki/User:Villadalmine" target="_blank">Rino Rondan</a>, estuvimos en <a href="http://www.andsec.org" target="_blank">AndSec (Angels and Deamons Security Conference)</a> representando a la comunidad Fedora y dando un taller muy completo de SELinux.</br>Ésta es la 4ta edición del evento, y <a href="www.fedoraproject.org" target="_blank">Fedora Project</a> era una supporting community.  

El evento tuvo lugar en Auditorio Buenos Aires, en el salón del edificio Buenos Aires Design, ocupó 3 ambientes, uno para las charlas primarias, otra para charlas secundarias o workshops, y otro ambiente donde había talleres de armado de antenas, supervivencias, opentalks… y barra libre!  
Los organizadores del evento se preocuparon realmente por todo, el hotel en donde nos alojamos estaba bastante cerca del lugar del evento, y gestionaron de manera fabulosa las reuniones post-evento. Me agradó mucho reencontrarme con gente con la que compartí eventos previos.

Nunca pensé que un workshop de SELinux iba a tener tanta audiencia, y nos sentimos muy bien cuando la gente empezó a hacer preguntas.  

El sábado 4 dimos una parte más teórica, explicando de donde salió, que es, que no es, el funcionamiento y los términos importantes.
Cabe aclarar que, por cuestiones de tiempo, y la falta de internet en mi casa, no pudimos terminar del todo la presentación, pero dimos un workshop que cubrió todo, inclusive (por arriba) MLS, usando presentaciones que dimos en otros eventos.  

El domingo 5 decidimos dar la parte práctica, preparando buenos ejemplos para mostrar como SELinux protege el sistema (No sin antes repasar la teoría para refrescar las cabezas o para ayudar a los que no habían ido el día anterior).  
Algunos ejemplos ejemplos fueron: 
 
* **con Samba:** creando archivo con root en /root y moviéndolo a un path compartido vía smb.
* **con Apache:** Leandro Poli, del LUG Paraná, nos preparó un script php que listaba /dev y /etc, y así mostramos que puede prevenir SELinux.  

Con los ejemplos, mostramos la solución de problemas de etiquetas, mostramos booleans, y mostramos lectura de logs.  

Personalmente, quedé muy conforme con las asistencias al workshop, con las preguntas, con los ejemplos en vivo, y no puedo negar que aprendí muchísimo SELinux cuando preparábamos la práctica.  

Quiero agradecer:  

* a **Fedora Project**, a los **organizadores de AndSec** por permitirnos y ayudarnos a asistir y por darnos lugar para el workshop.  
* a mi amigazo **Rino Rondan**, que siempre me acompaña y me ayuda con todo. Un groso!  
* a **Leandro Poli**, que viajó desde Paraná conmigo, por el aguante, por el script php, y por darnos una mano en lo que pudiera. 


Realmente <a href="http://www.andsec.org" target="_blank">AndSec</a> es un evento para aprovechar, los talleres de antena y supervivencia estuvieron muy buenos, al igual que el simulador de drones (y la barra libre :-P), para la próxima edición, si podes, anda, no la vas a pasar mal.

Próximamente publicaremos el Workshop de SELinux, tanto la presentación como los scripts y pasos para la práctica. 

###<a href="/images/galleries/2016/AndSec2016" target="_blank">Galería de fotos</a>
