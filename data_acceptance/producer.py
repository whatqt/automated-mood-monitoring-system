from automated_mood_monitoring_system.settings import CONNECTION_RABBITMQ



class SendData:
    def __init__(self, data):
        self.data = data
        self.connection = CONNECTION_RABBITMQ
    
    def send(self):
        channel = self.connection.channel()
        channel.queue_declare(queue="data_for_analysis")
        channel.basic_publish(
            exchange='',
            routing_key="data_for_analysis",
            body=self.data
        )

        print("Сообщение было отправлено в брокер для бд")