from forex_python.converter import CurrencyRates
from speech.speech_tts import SmortTTS
from speech.speech_recog import SmortRecognizer
from decimal import Decimal

c = CurrencyRates(force_decimal=False)
talker = SmortTTS()
recognizer = SmortRecognizer()


money_to_code = {"USD": "dollar", "EUR": "euro", "INR": "indian rupees"}

def convert_currency():
    pass
