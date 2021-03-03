import cmds.search.browser_search


class SmortCommandHandler:

    outp = ""

    def process_input(self, inp):
        processed_cmd = str(inp).lower().split()

        if (processed_cmd):
            return processed_cmd

        else:
            return

    def call_cmd(self, processed):
        if (processed[0] == "search"):
            # search

            SmortCommandHandler.outp = cmds.search.browser_search.browser_search(processed)

            if (SmortCommandHandler.outp == "opening browser"):
                # continue loop
                pass
            else:
                print("Something went wrong.")
                quit(0)

        # add all cmds here
