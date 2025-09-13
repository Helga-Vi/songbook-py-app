from bs4 import BeautifulSoup
import requests
import json

#Henter websiden, parser html-kodene og finner tekstdelen av den. Henter også rett encoding for å skrive til fil.
#Encoding er tilpasset alfabetet for språkene f.eks. utf-8. Særlig viktig når æøå brukes.
def scrape_lyrics(choice, gsearch_list):

    html = requests.get(gsearch_list[choice-1])
    lang_encoding = html.encoding
    soup = BeautifulSoup(html.text, 'html.parser')
    song_text = soup.get_text()

    #Skriver ut sangteksten til fil:
    filename = search_string + " " + lang
    text_file = open(filename+".txt", "w", encoding = lang_encoding)
    text_file.write(song_text)
    text_file.close()
        
    print(f"\nSjekk tekstfilen på C:/brukere/dittnavn. Den heter {filename}")
        