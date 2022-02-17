import requests
import json

def get_synonims(word):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/synonyms"

    headers = {
        'x-rapidapi-key': "6f67384d0bmshd202c937d900822p131470jsna91e41c585cd",
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    
    r = json.loads(response.text)
    
    print(r)

    return r['synonyms'] if 'synonyms' in r else []
    
def get_example(word):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/definitions"

    headers = {
        'x-rapidapi-key': "6f67384d0bmshd202c937d900822p131470jsna91e41c585cd",
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    
    r = json.loads(response.text)
    
    print("Definitions")
    print(r)

    return r['definitions'] if 'definitions' in r and len(r['definitions']) > 0 else ["I don't know what is it)"]

def get_frequency(word):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/frequency"

    headers = {
        'x-rapidapi-key': "6f67384d0bmshd202c937d900822p131470jsna91e41c585cd",
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    r = json.loads(response.text)
    
    print(r)

    return r['frequency']['diversity'] if 'frequency' in r else 1

def get_random_words(words, complexity):
    return ["nanachi", "say", "na"]