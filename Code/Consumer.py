import pika
import requests
import constantsC


def callback(ch, method, properties, body):
    payload = {constantsC.VARIABLE_LABEL: body.decode(encoding=constantsC.ENCODING_FORMAT)}
    post_request(payload)


def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, constantsC.DEVICE_LABEL)
    headers = {"X-Auth-Token": constantsC.TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
    return True


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(constantsC.IP, constantsC.PORT, '/', pika.PlainCredentials(constantsC.USER, constantsC.PASSWORD)))
    channel = connection.channel()
    channel.basic_consume(queue='my_app', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    while (True):
        main()
