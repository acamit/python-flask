import pika, sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost')) # connected to a broker on localhost, add IP address for remote server.
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')
channel.queue_declare(queue='', exclusive=True) # send message to the queue named "hello"

# Use default exchange and publish to hello queue
message = ' '.join(sys.argv[1:]) or 'Hello world'
channel.basic_publish(exchange='logs',
                    routing_key='',
                    body=message,
                    properties=pika.BasicProperties(
                        delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE
                        )
                    )

print("[x] Sent '%r'" % message)

connection.close()