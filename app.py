from generate_prompt import generate_prompt, _parse_formatted_prompt, Range



def main():
    langauge = input("What langauge?: ")
    topic = input("the topic is about?: ")
    number_of_paragraph = int(input("number of paragraph: "))
    from_character, from_number = input("Diffuclty starts with level?: ")
    to_character, to_number = input("Difficulty ends with level?: ")
    range = Range((to_character, int(to_number)), (from_character, int(from_number)))
    number_of_questions = int(input("Number of questions you want per sections: "))
    p = generate_prompt(langauge, topic, number_of_paragraph, range, number_of_questions)
    print(_parse_formatted_prompt(p))



if __name__ == "__main__":
    main()

