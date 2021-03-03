import webbrowser as wb
import speech.speech_tts


def browser_search(processed):
    processed.pop(0)

    try:
        joined_query = " ".join(processed).replace("search", "")
        wb.open_new_tab("https://duckduckgo.com/?q=" + joined_query)

        return "opening browser"
    except Exception as e:
        print(e)

        return "failed"
