from pika import BlockingConnection, ConnectionParameters




class ConnectionRabbitMq:
    def connect(self):
        try:
            connection = BlockingConnection(
                ConnectionParameters(
                    'localhost'
                )
            )
            return connection
        except Exception as e:
            raise e