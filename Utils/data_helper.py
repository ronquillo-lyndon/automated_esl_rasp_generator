import json

# data as single object
class RawData:
    def __init__(self, language="", topic="", number_of_paragraph=0, drf="", drt="", number_of_question=0):
        self.language=language
        self.topic=topic
        self.number_of_paragraph=number_of_paragraph
        self.drf = drf
        self.drt =drt
        self.number_of_question=number_of_question

 
# Helpers for getting difficulties of ESL
def _get_difficulty_range():
    with open("Data/difficulty_range.json", "r", encoding="utf-8") as file:
        difficulty_range = json.load(file)
    return difficulty_range

def _getValues_difficulty_range():
    difficulty_range = _get_difficulty_range()
    range_temp = []
    index = -1
    for difficulty in difficulty_range.values():
        index += 1
        range_temp.insert(index, difficulty)

    return range_temp

def _getKey_diffculty_range(difficulty_range_value):
    difficulty_range = _get_difficulty_range()
    key = [k for k, v in difficulty_range.items() if v == difficulty_range_value]
    return key[0]

# Helpers for prompt
# raw prompt
def _get_raw_prompt():
    with open("Data/store_data.json", "r", encoding="utf-8") as file:
        raw_prompt = json.load(file)["raw_prompt"]
    return raw_prompt

def _reset_raw_prompt():
    with open("Data/store_data.json", "r", encoding="utf-8") as file:
        store_data  = json.load(file)

    store_data["raw_prompt"] = {
            "language": "",
            "topic": "",
            "number_of_paragraph": 0,
            "difficulty_range": {"difficulty_range_from": "", "difficulty_range_to": ""},
            "number_of_question": 1
        }
    with open("Data/store_data.json", "w") as file:
        json.dump(store_data, file, indent=4)
# formatted prompt
def _get_formatted_prompt():
    with open("Data/store_data.json", "r", encoding="utf-8") as file:
        formatted_prompt = json.load(file)["formatted_prompt"]
    return formatted_prompt

def _reset_formatted_prompt():
    with open("Data/store_data.json", "r", encoding="utf-8") as file:
        store_data  = json.load(file)

    store_data["formatted_prompt"] = ""
    with open("Data/store_data.json", "w") as file:
        json.dump(store_data, file, indent=4)
# response
def _get_response():
    with open("Data/store_data.json", "r", encoding="utf-8") as file:
        response = json.load(file)["response"]
    return response

def _reset_response():
    with open("Data/store_data.json", "r", encoding="utf-8") as file:
        store_data  = json.load(file)

    store_data["response"] = ""
    with open("Data/store_data.json", "w") as file:
        json.dump(store_data, file, indent=4)

# Setters
def _set_raw_prompt(raw : RawData):
    with open("Data/store_data.json", "r", encoding="utf-8") as file:
        store_data  = json.load(file)
        
    store_data["raw_prompt"] = {
            "language": raw.language,
            "topic": raw.topic,
            "number_of_paragraph": raw.number_of_paragraph,
            "difficulty_range": {"difficulty_range_from": raw.drf, "difficulty_range_to": raw.drt},
            "number_of_question": raw.number_of_question
        }
    with open("Data/store_data.json", "w") as file:
        json.dump(store_data, file, indent=4)

def _set_formatted_prompt(formatted_prompt):
    with open("Data/store_data.json", "r", encoding="utf-8") as file:
        store_data  = json.load(file)

    store_data["formatted_prompt"] = f"{formatted_prompt}"
    with open("Data/store_data.json", "w") as file:
        json.dump(store_data, file, indent=4)

def _set_response(response):
    with open("Data/store_data.json", "r", encoding="utf-8") as file:
        store_data  = json.load(file)

    store_data["response"] = f"{response}"
    with open("Data/store_data.json", "w") as file:
        json.dump(store_data, file, indent=4)

#Language
def _get_languages():
    with open("Data/language.json", "r", encoding="utf-8") as file:
        language = json.load(file)
    return language

if __name__ == "__main__":
    pass