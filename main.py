# create SmortAI class later
from Speech import speech_recog
from Speech import speech_tts


class SmortAI:
    tts = speech_tts.SmortTTS()  # text-to-speech instance
    recog = speech_recog.SmortRecognizer()  # recognizer instance

    def __init__(self, tts_rate, is_tts, is_recog):
        self.tts_rate = tts_rate  # tts_rate = talking speed
        self.is_tts = is_tts  # is_tts = talk in text-to-speech or in plain text
        self.is_recog = is_recog  # is_recog = recognize or simply write in console for commands

        self.tts.set_speed_rate(self.tts_rate)

    def main_loop(self):
        self.tts.say_tts(self.recog.recognize())


smort = SmortAI(115, True, True)

if __name__ == '__main__':
    smort.main_loop()
