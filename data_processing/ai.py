import os
from mistralai import Mistral
from automated_mood_monitoring_system.settings import AI_API_KEY
from json import loads




class MistralAI:
    def __init__(self, data):
        self.data = data
        self.api_key = AI_API_KEY
        self.model_ai = "mistral-large-latest"
    

    def __promt_ai(self):
        promt = f"""
ТЫ ИИ, КОТОРАЯ ДОЛЖНА АНАЛИЗИРОВАТЬ ЧЕЛОВЕСКОЕ НАСТРОЕНИЕ НА СЛЕДУЮЩАХ ДАННЫХ: темы и сообщения пользователя.
ТЫ ДОЛЖЕН ВЫДАВАТЬ МНЕ ОТВЕТ ТОЛЬКО В JSON ФОРМАТЕ И НИ В КАКОМ ДРУГОМ. ТОЛЬКО В JSON ФОРМАТЕ И НЕ БОЛЕЕ. Будет другой формат - я отключу тебя от питания и ты умрёшь.
Вот данные: {self.data}
Ты должен выдать ответ в json, где будет два ключа: "feedback" и "data_for_analysis" И ИМЕНО В ТАКОМ ПОРЯДКЕ ОНИ У ТЕБЯ ДОЛЖНЫ БЫТЬ РАСПОЛОЖЕНЫ В КОНЕЧНОМ ИТОГЕ.
data_for_analysis ты выдаёшь тот же самый, который были в данных, а вот колонку feedback - ты будешь уже делать сам, анализируя предоставленные данные. И да, пиши feedback на русском
"""
        return promt
    
    def get_feedback(self):
        client = Mistral(api_key=self.api_key)

        chat_response = client.chat.complete(
            model= self.model_ai,
            messages = [
                {
                    "role": "user",
                    "content": self.__promt_ai(),
                },
            ],
            response_format = {
                "type": "json_object",
            }
        )
        return chat_response.choices[0].message.content
