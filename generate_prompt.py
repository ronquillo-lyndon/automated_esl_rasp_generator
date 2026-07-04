
class Rang: #Range I used Rang/rang to not confuse python
    r_from = tuple()
    r_to =  tuple()

    def __init__(self, r_from, r_to):
        self.r_from = r_from
        self.r_to = r_to
    
    # r = identifier of range in getter
    def get_char(self, r):
        if r == 't':
            return self.r_to[0]
        return self.r_from[0]
    
    def get_num(self, r):
        if r == 't':
            return self.r_to[1]
        return self.r_from[1]

prompt = {
    "Role": "",
    "Title": "",
    "Body": "",
    "Format" : ""
}

def generate_prompt(langauge, topic, number_of_paragraph, range : Rang, number_of_questions):
    range_f, range_t = "", ""
    def _check_range(r):
        range_temp = ""
        if range.get_char(r) == 'A' and range.get_num(r) == 1:
            range_temp = "Beginner"
        if range.get_char(r) == 'A' and range.get_num(r) == 2:
            range_temp = "Elementary"
        if range.get_char(r) == 'B' and range.get_num(r) == 1:
            range_temp = "Intermediate"
        if range.get_char(r) == 'B' and range.get_num(r) == 2:
            range_temp = "Upper Intermediate"
        if range.get_char(r) == 'C' and range.get_num(r) == 1:
            range_temp = "Advanced"
        if range.get_char(r) == 'C' and range.get_num(r) == 2:
            range_temp = "Proficient"
        return range_temp
    
    range_f = _check_range("f")
    range_t = _check_range("t")

    def _format():
        prompt["Role"] = "ESL Teacher"
        prompt["Title"] = f"{topic}"
        prompt["Body"] = f"Generate English essay about {topic} in {number_of_paragraph} paragraph format, From {range_f} to {range_t} – Each level should have their own essay. So, I can test my {langauge} speaking and Reading skills. Ensure to add questions in each essay to practice and improve my comprehension and ability to formulate answers in {langauge}. The Questions part should be divided into two section Comprehension and Speaking, Each section should have {number_of_questions} questions"
        prompt["Format"] = f"// And the format of 'each' ESL level is: \n[Title {topic}, ESL LEVEL]\ncontent\n[ESSAY PASSAGE]\n[IMPORTANT VOCABULARIES WITH MEANING]//format must be on term-meaning format\nComprehension Questions\n[THE {number_of_questions} QUESTIONS]\nSpeaking Questions\n[THE {number_of_questions} QUESTIONS]"
        return prompt
    _format()
    return prompt


def _parse_formatted_prompt(Formatted_prompt : dict):
    temp = list(Formatted_prompt.values())
    return f"You are an {temp[0]} assiting his/her student.\nThe topic Title is about {temp[1]}.\n{temp[2]}.\nAnd in Markdown style do this format:\n{temp[3]}"

if __name__ == "__main__":
    rang = Rang(('A', 1), ('B', 1))
    g_p = generate_prompt("English", "Shabu", 3, rang, 2)
    p =_parse_formatted_prompt(g_p)
    for line in p:
        print(line)

"""
Beginner (A1) – Can understand and use simple words and phrases. Can introduce themselves and ask basic questions.
Elementary (A2) – Can communicate in everyday situations, such as shopping, ordering food, and talking about routines.
Intermediate (B1) – Can handle most travel situations, discuss familiar topics, and understand the main points of clear speech.
Upper Intermediate (B2) – Can communicate fluently on many topics, understand more complex texts, and express opinions clearly.
Advanced (C1) – Can use English effectively for work, study, and social situations with good accuracy and flexibility.
Proficient (C2) – Can understand and use English at a level close to that of a highly educated native speaker.
"""