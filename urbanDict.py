import requests


# Api key
AUTH_KEY = ""

# API endpoint
URL = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

# request header
headers = {"x-rapidapi-key": AUTH_KEY}


def define(phrase, i=0):
    """Returns the 'i'th definition for the given phrase

        if i is not given, returns the top_result

        'Not Found' if there were no results
        """

    term = {"term": phrase}
    response = requests.get(URL, term, headers=headers)
    json_result = response.json()
    if not json_result["list"]:
        result = "Not Found"
    elif i > len(json_result["list"]) - 1:
        result = None
    else:
        untidied_result = json_result["list"][i]["definition"]
        definition = untidied_result.replace("[", "").replace("]", "")
        result = definition

    return result


def multiDefine(phrase, n):
    """Return the first n definitions for the given phrase as an array

        if there are less than n definitions for the phrase, returns
        all available definitions

        return 'Not Found' if there is no definition
        """

    definitions = []
    for j in range(n):
        currentDefinition = define(phrase, i=j)
        if currentDefinition == "Not Found":
            definitions = "Not Found"
            break
        elif currentDefinition is None:
            break
        else:
            definitions.append(currentDefinition)
    return definitions


if __name__ == "__main__":
    print(define("kjshdfjksda"))  # returns Not Found
    print(define("nerd"))
    print(multiDefine("hello, world", 100))
