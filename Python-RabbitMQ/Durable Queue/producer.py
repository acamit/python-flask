import pika, sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost')) # connected to a broker on localhost, add IP address for remote server.
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True) # send message to the queue named "hello"

# Use default exchange and publish to hello queue
message = ' '.join(sys.argv[1:]) or 'Hello world'
channel.basic_publish(exchange='',
                    routing_key='hello',
                    body=message,
                    properties=pika.BasicProperties(
                        delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE
                        )
                    )

print("[x] Sent '%r'" % message)

connection.close()