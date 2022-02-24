import pika
# create connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost')) # connected to a broker on localhost, add IP address for remote server.

# create a channel
channel = connection.channel()

# send message to the queue named "hello"
channel.queue_declare(queue='hello') 

# Use default exchange and publish to hello queue
message = 'Hello Again'

# 4 publish using channel to default exchange
channel.basic_publish(exchange='', routing_key='hello',  body=message)
print("[x] Sent '%r'" % message)

connection.close()