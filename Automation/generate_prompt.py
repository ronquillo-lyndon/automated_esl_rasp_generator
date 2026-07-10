from Utils import data_validator as dv

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
        prompt["Body"] = f"Generate English essay about {topic} in {number_of_paragraph} paragraph format, From {range_f} to {range_t} – Each level should have their own essay. So, I can test my {langauge} speaking and Reading skills. Ensure to add questions in each essay to practice and improve my comprehension and ability to formulate answers in {langauge}. The Questions part should be divided into two section Comprehension and Speaking, Each section should have {number_of_questions} questions."
        prompt["Format"] = f"// And the format of 'each' ESL level is: \n[Title {topic}, ESL LEVEL]\n[ESSAY PASSAGE]\n[IMPORTANT VOCABULARIES WITH MEANING]//format must be on term-meaning format\nComprehension Questions\n[THE {number_of_questions} QUESTIONS]\nSpeaking Questions\n[THE {number_of_questions} QUESTIONS]. [NOTE: 1.) STRICTLY FOLLOW THE INSTRUCTION, NO NEED FOR RECOMMENDATION. 2) strictly add these codes at the beginning of the text response {dv.start_response} and at the end of the text response {dv.end_response}]"
        return prompt
    _format()
    return prompt


def _parse_formatted_prompt(Formatted_prompt : dict):
    temp = list(Formatted_prompt.values())
    return f"You are an {temp[0]} assiting his/her student.\nThe topic Title is about {temp[1]}.\n{temp[2]}.\nAnd in Markdown style do this format:\n{temp[3]}"

if __name__ == "__main__":
    pass