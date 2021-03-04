import speech_recognition as sr


class SmortRecognizer:
    mic = sr.Microphone()
    recognizer = sr.Recognizer()

    wake_word = "hey smart guy"  # change later. reason its not "smort" is it recognizes smort as an accent of smart.

    def adjust_for_bg_noise(self, duration):
        with self.mic as source:
            self.recognizer.adjust_for_ambient_noise(self.mic, duration=duration)
        print("Adjusted")

    def recognize(self):
        with self.mic as source:
            audio = self.recognizer.listen(source)

            try:
                text = self.recognizer.recognize_google(audio)
                return text

            except Exception as e:
                print(e)
                return
