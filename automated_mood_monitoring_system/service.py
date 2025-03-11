from pika import BlockingConnection, ConnectionParameters




class ConnectionRabbitMq:
    def connect(self):
        try:
            connection = BlockingConnection(
                ConnectionParameters(
                    'localhost',
                    heartbeat=0
                )
            )
            return connection
        except Exception as e:
            print(f"Ошибка подключения: {e}")
