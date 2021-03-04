# search imports
import cmds.search.browser_search

# misc imports
import cmds.misc.convert_currency
import cmds.misc.exit


class SmortCommandHandler:
    outp = ""

    def process_input(self, inp):
        processed_cmd = str(inp).lower().split()

        if (processed_cmd):
            return processed_cmd

        else:
            return

    def call_cmd(self, processed):
        # browser search

        if (processed[0] == "search"):
            # search

            SmortCommandHandler.outp = cmds.search.browser_search.browser_search(processed)

            if (SmortCommandHandler.outp == "opening browser"):
                # continue loop
                pass
            else:
                print("Something went wrong.")
                quit(0)

        # convert currency
        if (len(processed) > 1 and processed[0] == "convert" and processed[1] == "currencies" or
                processed[1] == "currency" or processed[1] == "prices"):
            #  convert prices

            SmortCommandHandler.outp = cmds.misc.convert_currency.convert_currency()  # function not finished yet!!!

        # exit bot
        if (processed[0] == "exit"):
            SmortCommandHandler.outp = cmds.misc.exit.exit_smort()

