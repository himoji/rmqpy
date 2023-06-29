import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='q')

def sendMsg(msg):
    channel.basic_publish(exchange='',
                        routing_key='q',
                        body=msg)
    print(f" [x] Sent '{msg}'")

while True:
    x = input("Mssg: ")
    if x=="": break
    sendMsg(x)
    
connection.close()