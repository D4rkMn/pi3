# Que necesitamos hacer:

Primero obten tu dirección IP local
La vas a necesitar, porque vas a utilizarla para los archivos "script.js" de Frontend, para hacer que la página pueda hacer requests correctamente al Backend.

En la carpeta Backend, hay un archivo websocketServer.py. Este es el que habilita el Backend de la página, y manejará toda la comunicación entre Arduino y el programa. De momento, allí se encuentra un archivo que, si bien no esta tan bien estructurado como el resto del proyecto (aun), se puede utilizar como base para lo demás que vamos a hacer.

De momento, si quieres ampliar la funcionalidad pues podrías buscar una forma de comunicar el Frontend con el resto de funciones del Backend. Se me ocurre que podrias hacer que, primero el Frontend le diga al usuario que elijas entre las opciones (Pdf o imagen), elija el idioma (acuerdate que es necesario para ciertas cosas), y luego que elija enviar las imagenes.

Luego que se haga todo el proceso de conversión, traducción, y esa mierda, y que luego de todo eso, antes del paso final (el OutputGenerator), se envie una señal específica al python websocket del Backend, la cual al ser recibida, luego este tendra que ahora esperar a que exista conexion con el Arduino.

Si se detecta un mensaje recibido del Arduino (el cual lo deberias definir como cierto formato que me deberas indicar para utilizar en el codigo del Arduino), se sabrá que existe una conexión y se podrá continuar al envio del output al Python, y eso seria basicamente todo me parece.

Si vas a hacer que la pagina sea mas bonita o algo, normal, solo no rompas la funcionalidad basica. Otra cosa, si quieres probar que tu codigo funciona (a pesar de no tener arduino), lo que podrias hacer seria hacer una segunda pagina web cuyo unico proposito sea actuar como un cliente mas del websocket, porque recuerda que lo unico que hace el websocket es comunicar señales entre "clientes" del websocket (por ejemplo la pagina web, y el Arduino), por lo que podrias hacer que el Arduino sea reemplazado por otro cliente que envie y reciba señales, osea otra pagina que tome su rol de forma momentanea. Si logras hacer eso, me parece que ya sería todo.