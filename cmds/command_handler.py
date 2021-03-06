# search imports
import search.browser_search

# misc imports
import misc.convert_currency
import misc.exit

import speech.speech_tts
import main


class SmortCommandHandler:
    talker = speech.speech_tts.SmortTTS()

    def process_input(self, inp):
        processed_cmd = str(inp).lower().split()

        if (processed_cmd):
            return processed_cmd

        else:
            return

    def call_cmd(self, processed):
        if (processed != []):
            if (processed[0] == "search"):
                if (main.smort.is_tts):
                    self.talker.say_tts("Opening browser")
                else:
                    print("opening browser")

                search.browser_search.browser_search(processed)

            elif (processed[0] == "exit" or processed[0] == "terminate"):
                if (main.smort.is_tts):
                    self.talker.say_tts("Bye! Thanks for using me!")
                else:
                    print("Bye! Thanks for using SmortAI")

                misc.exit.exit_smort()
