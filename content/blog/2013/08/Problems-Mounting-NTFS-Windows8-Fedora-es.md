Title: Problemas montando particiones NTFS de Windows 8 en Fedora
Date: 2013-08-17 19:00
Category: Fedora
Tags: Fedora, GNU/Linux, issue, NTFS, partition, power, problem, Windows, Windows-8
Lang: es
Slug: problems-mounting-ntfs-windows8-fedora
Summary: Tengo mis equipos configurados para montar automáticamente al inicio particiones NTFS, en donde comparto archivos entre Windows y Fedora.</br></br>Hace poco actualicé a Windows 8, y después de conocerlo, quise nuevamente iniciar Fedora, y me daba un error queriendo levantar la partición.</br></br>A continuación, explico que es lo que pasa y como resolverlo.  

Windows 8, trae activado por defecto “Inicio Rápido”, esta caracteristica sirve para que Windows inicie en una velocidad relativamente corta (se nota mucho en comparación con otras versiones de Windows), y funciona haciendo que el sistema no se apague por completo, si no que es un estado “parcial” de hibernación, es decir, guarda el estado del sistema en un archivo en el disco, y cuando inicia el sistema nuevamente, carga el contenido del archivo, dejando el sistema de la misma forma que cuando se apagó.  

El problema surge cuando, en mi caso para este ejemplo, quiero iniciar GNU/Linux el cual tiene una configuración en /etc/fstab para montar automáticamente la unidad que uso para los datos de los 2 sistemas operativos; Fedora me indica que encuentra problemas al montar dicha partición.
La solución es muy sencilla, desactivar esa caracteristica de Windows, para hacer esto…  

1. Iniciamos Windows 8  

2. En el inicio, escribimos “administración de energía”, o “power management” en su caso.  

3. En el menú lateral derecho, vamos a la pestaña “Configuración”.  

4. Ahí, seleccionamos del menu izquierdo “Cambiar las acciones de los botones de inicio/apagado”.  
  [![nfts-1](/images/article/2013/08/ntfs-1.png)](/images/article/2013/08/ntfs-1.png)  

5. Se abre una ventana de “Configurar el sistema” con algunas opciones bloqueadas; Apretamos “Cambiar la configuración actualmente no disponible”, esto hará que podamos modificar los ajustes bloqueados.  
  [![nfts-2](/images/article/2013/08/ntfs-2.png)](/images/article/2013/08/ntfs-2.png)  

6. Ahora, simplemente desactivamos la casilla “Activar inicio rápido (recomendado)” y guardamos los cambios.  
  [![nfts-3](/images/article/2013/08/ntfs-3.png)](/images/article/2013/08/ntfs-3.png)  

Eso es todo, ahora no habrá problemas para montar unidades NTFS de Windows 8 en GNU/Linux.  
