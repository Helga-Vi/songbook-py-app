from googlesearch import search
import requests
from bs4 import BeautifulSoup

def search_lyrics(song_title, artist, language):

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

        num=0
        for y in gsearch_list:
            num +=1
            print(num, y)


