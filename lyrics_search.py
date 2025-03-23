from googlesearch import search
import requests
from bs4 import BeautifulSoup
import json

def search_lyrics(song_title, artist, language):

    print("Search lyrics function responding")
    settings_dict ={"Norsk": ["sang tekst", "no"],"Svensk": ["sång text", "se"], "Engelsk":["song lyrics", "en"]}

    for key, value in settings_dict.items():
        if language in key:
            search_string = str(song_title +" "+ artist +" "+value[0])
            lang = value[1]
        else:
            search_string = song_title +" "+ artist +" "+ settings_dict["Norsk"][0]
            lang = settings_dict["Norsk"][1]

        print(search_string, lang)

        Gsearch = search(search_string, num_results=3, sleep_interval = 5, lang=lang)
        gsearch_list = list(Gsearch)

        return json.dumps([{"title": result.title, "content": result.content} for result in Gsearch])

# Add this function call at the end of the script to test it
if __name__ == "__main__":
    search_lyrics("Here comes the sun", "George Harrison", "Engelsk")
