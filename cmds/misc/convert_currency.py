from forex_python.converter import CurrencyRates
from speech.speech_tts import SmortTTS
from speech.speech_recog import SmortRecognizer
from decimal import Decimal

c = CurrencyRates(force_decimal=False)
talker = SmortTTS()
recognizer = SmortRecognizer()


money_to_code = {"USD": "dollar", "EUR": "euro", "INR": "indian rupees", "AFA": "ffghanistan afghani",
                 "ALL": "albanien lek", "DZD": "algerian dinar", "AOR": "angolan kwanza reajustado",
                 "ARS": "argentine peso", "AMD": "armenian dram", "AWG": "aruban guilder", "AUD": "australian dollar",
                 "AZN": "azerbaijanian new manat", "BSD": "bahamian dollar", "BHD": "bahraini dinar", "BDT": "bangladeshi taka",
                 "BBD": "barbados dollar", "BYN": "belarusian ruble", "BZD": "belize dollar", "BMD": "bermudian dollar",
                 "BTN": "bhutan ngultrum", "BOB": "bolivian boliviano", "BWP": "botswana pula"}

def convert_currency():
    pass
