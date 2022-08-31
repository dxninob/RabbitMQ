# Info de la materia: ST0263 - Tópicos especiales en telemática
#
# Estudiante(s): Daniela Ximena Niño Barbosa (dxninob@eafit.edu.co), Samuel Ceballos Posada (sceballosp@eafit.edu.co)
#
# Profesor: Edwin Nelson Montoya Munera (emontoya@eafit.edu.co)
#
# Laboratorio 2
#
# 1. Breve descripción de la actividad
#
RabbitMQ es middleware de código abierto que funciona como un intermediario entre aplicaciones que pueden ser independientes entre si. De esta forma, RabbitMQ se constituye en una capa software que le permitirá la comunicación entre ellas. Una de las grandes ventajas que da el considerar este tipo de soluciones, es que la arquitectura final del sistema se convierte en una solución débilmente acoplada.  El objetivo de este laboratorio es entender cómo funciona RabbitMQ y realizar un proyecto de IoT con este MOM.

Para este laboratorio, se realizó un código de Productor y Consumidor en Pyhton.  El productor se encarga de enviar datos aleatorios a RabbitMQ, simulando la temperatura del ambiente.  El consumidor se encrga de tomar los datos de RabbitMQ y enviarlos a Ubidots, con el fin de que esta plataforma haga gráficas de la temperatura.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
1. Realice un mapa mental de las características del protocolo.
2. Realice la mejor adaptación posible en el caso de este proyecto de IoT con RabbitMQ, eventualmente tener algún simulador de eventos IoT o realizar alguna adaptación con algún hardware Raspberry o Arduino

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
Todo lo propuesto fue implementado.

# 2. Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
El proyecto está compuesto por un productor y un consumidor, el productor se encarga de mandar información al MOM y el consumidor de recuperarla para que pueda ser implemantada en soluciones de IoT.
Se usó el Single Responsibility Principle para realizar el código tanto del productor como del consumidor.

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
El código del productor y del consumidor se desarrolló en el lenguaje de programación Pyhton, se realizó un archivo llamado Producer.py y otro llamado Consumer.py, estos dos archivos se ejecutan localmente para este laboratorio.

Los códigos hacen uso de las siguientes librerías:
- Pika: esta librería es usada tanto en el productor como en el consumidor, se usa para lograr conectarse, enviar y recibir datos de RabbitMQ. Se debe instalar con el comando ```pip install pika```.
- Random: esta librería es usada por el productor para lograr generar datos aleatorios, los cuales serán enviados a RabbitMQ.
- Time: esta librería es usada por el productor para que los datos aleatorios, sean generados y mandados cada cierto tiempo a RabbitMQ.
- Requests: esta libería es usada por el consumidor para mandar los datos que recibe de RabbitMQ a Ubidots.  Se debe instalar con el comando ```pip install requests```.

## Como se ejecuta.
El productor se ejecuta con el siguiente comando:
```python Producer.py```

El consumidor se ejecuta con el siguiente comando:
```python Consumer.py```

## Detalles del desarrollo
**Productor.py**  
El código del productor es muy corto, este lo que hace es conectarse a RabbitMQ y manda datos aleatorios cada x segundos, para enviar esta infomación, hace uso del nombre del exchange y el routing key que fueron definidos en RabbitMQ.

**Consumer.py**  
El código del consumidor contiene tres métodos:
- main: en este método, crea la conexión y el canal de cominicación para lograr recibir los datos de RabbitMQ.
- callback: este método es el que se ejecuta cada vez que se recibe un dato de RabbitMQ, este pone en el dato como valor en un diccionario que tiene el nombre de la variable como llave, e invoca al método post_request para que mande este diccionario a Ubidots.
- post_request: este método hace un POST a Ubidots, para enviarle los datos de la variable que fue recuerada de RabbitMQ.

## Detalles técnicos
El productor y consumidor se corren localemente.  El productor crea números aleatorios simulando la temperatura del ambiente y los manda a RabbitMQ.  El consumidor recupera los datos de RabbitMQ y mediante un POST los envía a Ubidots en formato json.  Ubidots se encarga de hacer una gráfica de línea y una de reloj con los datos de la tempratura.

## Descripción y como se configura los parámetros del proyecto
**Parámetros para Producer.py**  
Los parametros para el productor se encuntran en un archivo llamado constantsP.py.  Estos son los parametros:
- IP = Dirección IP donde se encuntra el MOM de RabbitMQ.  En este caso es '34.192.115.172'.
- PORT = Puerto donde se encuntra el MOM de RabbitMQ.  En este caso es 5672.
- USER = Usuario para acceder a RabbitMQ.
- PASSWORD = Contraseña para acceder a RabbitMQ.
- N = Cantidad de datos que se quieren enviar.  En este caso es 50.
- MIN = Mínimo del número random que se genera para simular los datos.  En este caso es 15.
- MAX = Máximo del número random que se genera para simular los datos.  En este caso es 25.
- EXCHANGE = Nombre del exchange creado.  En este caso es 'my_exchange'.
- RK = Nombre del routing key creado.  En este caso es 'test'.
- TIME = Tiempo en segundos que tarda entre dato y dato para ser enviados.  En este caso es 10.

**Parámetros para Consumer.py**  
Los parametros para el consumidor se encuntran en un archivo llamado constantsC.py.  Estos son los parametros:
- IP = Dirección IP donde se encuntra el MOM de RabbitMQ.  En este caso es '34.192.115.172'.
- PORT = Puerto donde se encuntra el MOM de RabbitMQ.  En este caso es 5672.
- USER = Usuario para acceder a RabbitMQ.
- PASSWORD = Contraseña para acceder a RabbitMQ.
- ENCODING_FORMAT = Formato para decodificar los datos recuperados de MOM.  En este caso es 'UTF-8'.
- TOKEN = Token de Ubidots para permitir enviar información a la plataforma.
- DEVICE_LABEL = Nombre del dispositivo donde se encuntran los datos en Ubidots, en este caso es 'lab-2'.
- VARIABLE_LABEL = Nombre de la variable que se va a enviar.  En esta caso es 'temperature'.

## Resultados o pantallazos 
<img width="945" alt="Captura" src="https://user-images.githubusercontent.com/60080916/187587540-c40e0995-0cf1-4256-8b1d-54472723903c.PNG">

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
El MOM se implementó en RabbitMQ, haciendo uso de un contendor de Docker.  Se encuntra en una instancia de AWS.

# IP o nombres de dominio en nube o en la máquina servidor.
34.192.115.172

## Descripción y cómo se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
- Cuando se crea la instancia en AWS, en el grupo de seguridad, se debe permitir el ingreso del tráfico TCP al puerto 5672 y 15672.
- Hay que asignar una IP elástica a la intancia de AWS.

## Como se lanza el servidor.
Para lanzar el servidor se debe ejecutar el siguiente comando:
```sudo docker start rabbit-server```

## Una mini guia de cómo un usuario utilizaría el software o la aplicación.
El usuario no tiene que interactuar con la aplicación, pues este solo puede visualizar las gráficas en Ubidots.

## Resultados o pantallazos 
<img width="943" alt="Captura2" src="https://user-images.githubusercontent.com/60080916/187590148-6c4f9dcc-cf18-4508-a7a6-3f388776275f.PNG">

# 5. Información relevante.

# Referencias:
## Simulate data in Ubidots using Python
https://help.ubidots.com/en/articles/569964-simulate-data-in-ubidots-using-python

#### versión README.md -> 1.0 (2022-agosto)

# Mapa mental
![Mapa Mental](https://user-images.githubusercontent.com/60080916/187591129-7f8a59f7-3316-4959-a5b3-cf8ff37a508b.jpeg)

