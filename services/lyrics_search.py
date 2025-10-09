from duckduckgo_search import DDGS
import json

def search_lyrics(song_title, artist, language):

    print("Search lyrics function responding")
    settings_dict ={
        "Norsk": ["sang tekst", "no"],
        "Svensk": ["sång text", "se"], 
        "Engelsk":["song lyrics", "en"]
        }

    print("Language", language)

    found_match = False
    lang = "no"  #Default to Norwegian

    for key, value in settings_dict.items():
        # print(f"Checking key: {key}, Value: {value}")
        if language.lower() == key.lower():
            search_string = f"{song_title} {artist} {value[0]}"
            lang = value[1]
            found_match = True
            break

    if not found_match:
        print("\nNo matching language found. Defaulting to Norwegian.")
        search_string = f"{song_title} {artist} sang tekst"
        lang = "no"

    print(f"Search string being used: {search_string}. Language: {lang}")

    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(search_string, max_results=5):
            results.append({
                "title": r.get("title"),
                "url": r.get("href"),
                "snippet": r.get("body")
            })

    print(f"Found {len(results)} results")
    return results

   
   
    # Present the results as a numbered list
    #print("\nSearch Results:")
    #for i, url in enumerate(gsearch_list, start=1):
    #    print(f"{i}. {url}")

    #selected_number = int(input("\nEnter the number of the URL you'd like to scrape (1-5): "))

        # Return the results as JSON4
    

# Add this function call at the end of the script to test it
if __name__ == "__main__":
    search_result = search_lyrics("Here comes the sun", "George Harrison", "Engelsk")
    if search_result:
         print(json.dumps(search_result, indent=2, ensure_ascii=False))
    else:
        print("No results found.")