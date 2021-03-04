# create SmortAI class later
from speech import speech_recog
from speech import speech_tts
from cmds import command_handler


class SmortAI:
    tts = speech_tts.SmortTTS()  # text-to-speech instance
    recog = speech_recog.SmortRecognizer()  # recognizer instance
    cmd_handler = command_handler.SmortCommandHandler()

    def __init__(self, tts_rate, is_tts, is_recog):
        self.tts_rate = tts_rate  # tts_rate = talking speed
        self.is_tts = is_tts  # is_tts = talk in text-to-speech or in plain text
        self.is_recog = is_recog  # is_recog = recognize or simply write in console for commands

        self.tts.set_speed_rate(self.tts_rate)

    def main_loop(self):
        print("Please wait. Adjusting to background noise.")

        self.recog.adjust_for_bg_noise(duration=5)

        while True:
            print("Listening..")
            if (self.is_recog):
                inp = smort.recog.recognize()
            else:
                inp = input("").lower()

            print(inp)

            if (inp != None):
                inp = inp.lower()
            else:
                continue

            if (self.recog.wake_word in inp):  # check for wake word

                if (self.is_tts):
                    self.tts.say_tts("I am ready")  # remember to play ready sound (like alexa)
                else:
                    print("I am ready")

                cmd = self.recog.recognize()
                processed_inp = self.cmd_handler.process_input(cmd)

                print(processed_inp)
                self.cmd_handler.call_cmd(processed_inp)

                if (self.is_tts):
                    self.tts.say_tts(self.cmd_handler.outp)
                else:
                    print("Output: " + self.cmd_handler.outp)


if (int(input("Want TTS in your Bot? 1 = yes, 0 = no: ")) == 1):
    want_tts = True
else:
    want_tts = False

if (int(input("Want Speech Recognition? 1 = yes, 0 = no: ")) == 1):
    want_recog = True
else:
    want_recog = False

smort = SmortAI(115, want_tts, want_recog)

if __name__ == '__main__':
    smort.main_loop()
