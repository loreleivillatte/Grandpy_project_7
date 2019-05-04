import requests
import wikipedia
import re
import py_bot.config as id_g


def get_map(user_search):
    """
    :param user_search: input user
    :return: lat, lng, address
    """
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    payloads = {
        'query': user_search,
        'key': id_g.KEY
    }
    response = requests.get(url=url, params=payloads)
    data_json = response.json()
    try:
        lat_map = data_json["results"][0]["geometry"]["location"]["lat"]
        lng_map = data_json["results"][0]["geometry"]["location"]["lng"]
        data_address = data_json['results'][0]["formatted_address"]
        return lat_map, lng_map, data_address
    except IndexError:
        sentence = "GrandPy Bot (perplexe) : Je ne trouve aucun résultat"
        return sentence


def format_response(address):
    """
    :param address: address Google map
    :return: formatted address
    """
    number = '[0-9]+'
    address = address.split(',')[0:1]
    address = ''.join(address)
    address = re.split(number, address)
    parse_address = ''.join(address)
    return parse_address


def get_section(user_search):
    """
    :param user_search: formatted address from Google
    :return: section of wikipedia
    """
    wikipedia.set_lang("fr")
    try:
        result_wiki = wikipedia.summary(user_search, sentences=1)
        return "GrandPy Bot : " + result_wiki
    except wikipedia.exceptions.DisambiguationError:
        search_random = wikipedia.random(pages=0)
        result_random = wikipedia.summary(search_random, sentences=1)
        return "GrandPy Bot (confus) : " + result_random
    except wikipedia.exceptions.WikipediaException:
        pass
