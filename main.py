import eel
import search

@eel.expose
def kimetsu_search(search_word,csv_path):
    search.kimetsu_search(search_word,csv_path)

eel.init('template')
eel.start('index.html')