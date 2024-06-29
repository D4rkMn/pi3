Se necesita definir el archivo `WiFiCredentials.h`, donde se encontrarán las credenciales necesarias para la conexión del ESP32 Master tanto con el internet como con el webSocket.

El archivo deberá tener el siguiente formato:

```c++
// WiFi Credentials
#define WIFI_SSID "(el SSID de tu internet)"
#define WIFI_PASSWORD "(la contraseña de tu internet)"

// WebSockets info
#define HOST_IP "(ip local del host de websockets)"
#define HOST_PORT 8080 // tiene que ser un número
```

Además, para subir el archivo correctamente a la placa, se necesita instalar las librerías externas mediante el Arduino IDE:

- Janelia Arduino's Vector

- Markus Sattler's WebSockets

- WebServer

Me parece que eso es todo lo que se necesita para hacer el setup previo. 