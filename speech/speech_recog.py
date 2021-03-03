import speech_recognition as sr


class SmortRecognizer:
    mic = sr.Microphone()
    recognizer = sr.Recognizer()

    def adjust_for_bg_noise(self, duration):
        self.recognizer.adjust_for_background_noise(duration=duration)
        print("Adjusted")

    def recognize(self):
        with self.mic as source:
            audio = self.recognizer.listen(source)

            try:
                text = self.recognizer.recognize_sphinx(audio)
                return text

            except Exception as e:
                print(e)
                return
