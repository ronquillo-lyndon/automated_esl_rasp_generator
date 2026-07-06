import json

# Helper for getting difficulties of ESL
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
    return key

if __name__ == "__main__":
    pass