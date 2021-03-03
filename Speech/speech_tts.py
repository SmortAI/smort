import pyttsx3


class SmortTTS:
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    rate = engine.getProperty("rate")

    def get_speed_rate(self):
        print(self.rate)

    def set_speed_rate(self, new_rate):
        self.engine.setProperty("rate", new_rate)
        print("New rate is: " + str(new_rate))

    def get_voices(self):
        for voice in self.voices:
            print(voice.id)

    def set_voice(self, voice_id):
        try:
            self.engine.setProperty("voice", voice_id)
        except Exception as e:
            print("Error: " + str(e))

    def say_tts(self, msg):
        self.engine.say(msg)
        self.engine.runAndWait()
