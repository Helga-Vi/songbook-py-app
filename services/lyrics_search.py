from googlesearch import search
import json

def search_lyrics(song_title, artist):

    print("Search lyrics function responding")
    #settings_dict ={
    #    "Norsk": ["sang tekst", "no"],
    #    "Svensk": ["sång text", "se"], 
    #    "Engelsk":["song lyrics", "en"]
    #    }

    #print("Language", language)

    #found_match = False

    #for key, value in settings_dict.items():
        #print(f"Checking key: {key}, Value: {value}")
    #    if language.lower() == key.lower():
    #        search_string = f"{song_title} {artist} {value[0]}"
    #        lang = value[1]
    #        found_match = True
    #        break

    #if not found_match:
    #        print("\nNo matching language found. Defaulting to Norwegian.")
    search_string = f"{song_title} {artist} sang tekst"
    #        lang = "no"

    #print(search_string, lang)

    Gsearch = search(search_string, num_results=5, sleep_interval = 5)
    gsearch_list = list(Gsearch)

    print(gsearch_list)

    # Present the results as a numbered list
    print("\nSearch Results:")
    for i, url in enumerate(gsearch_list, start=1):
        print(f"{i}. {url}")

    selected_number = int(input("\nEnter the number of the URL you'd like to scrape (1-5): "))

        # Return the results as JSON
    return json.dumps(gsearch_list, indent=2)

# Add this function call at the end of the script to test it
if __name__ == "__main__":
    search_result = search_lyrics("Here comes the sun", "George Harrison", "Engelsk")
    if search_result:
        print("\nJSON Output:")
        print(search_result)