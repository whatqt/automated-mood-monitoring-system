import sys
sys.path.append('..')
from automated_mood_monitoring_system.settings import CONNECTION_RABBITMQ
from data_processing.ai import MistralAI
from data_processing.serializer import ProcessingDataSerializer
from json import dumps, loads




class Consumer:
    def __init__(self):
        self.connection = CONNECTION_RABBITMQ
    
    def __callback(self, ch, method, properties, body):
        mistral_ai = MistralAI(body.decode())
        feedback = loads(mistral_ai.get_feedback())
        serializer = ProcessingDataSerializer(data=feedback)
        if serializer.is_valid():
            serializer.save()
            print(
                {
                    "status": "data is saved",
                    "feedback": feedback
                }
            )
        print(serializer.errors)

    def processing(self):
        channel = self.connection.channel()
        channel.basic_consume(
            queue="data_for_analysis",
            on_message_callback=self.__callback,
            auto_ack=True
        )
        print("Ожидаем сообщений")
        channel.start_consuming()

cons = Consumer()
cons.processing()






