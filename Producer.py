import pika
import random
import time
import constantsP


connection = pika.BlockingConnection(pika.ConnectionParameters(constantsP.IP, constantsP.PORT, '/', pika.PlainCredentials(constantsP.USER, constantsP.PASSWORD)))
channel = connection.channel()
print('Running Producer Application...')

n = 0
while(n < constantsP.N):
    data = str(random.randint(constantsP.MIN, constantsP.MAX))
    channel.basic_publish(exchange=constantsP.EXCHANGE, routing_key=constantsP.RK, body=data)
    print("Sent:", data)
    time.sleep(constantsP.TIME)

connection.close()