# search imports
import cmds.search.browser_search

# misc imports
import cmds.misc.convert_currency
import cmds.misc.exit


class SmortCommandHandler:


    def process_input(self, inp):
        processed_cmd = str(inp).lower().split()

        if (processed_cmd):
            return processed_cmd

        else:
            return

    def call_cmd(self, processed):
        pass
