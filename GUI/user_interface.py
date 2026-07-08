#For dubbing only
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import customtkinter as ctk
from Utils import data_helper as dh
from Utils import user_interface_helper as uih
from Automation import generate_prompt as gp
from Automation import open_browser as op

def user_interface():
    w,h=uih._get_monitor_size()
    app = ctk.CTk()
    app.geometry(f"{(int(w/2))}x{int(h/2)}")
    app.title("Automated ESL RASP Generator")
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")
    difficulty_range_placeholder = dh._getValues_difficulty_range()[0]

    #data
    store_raw_data = dh.RawData()
    
    #Dropdown inputs
    language = ctk.StringVar(value="English")
    difficulty_range_from = ctk.StringVar(value=difficulty_range_placeholder)
    difficulty_range_to = ctk.StringVar(value=difficulty_range_placeholder)

    #langauge dropdown
    language_input = uih.input_widget(
        app,
        lambda parent: ctk.CTkOptionMenu(
        parent,
        values=dh._get_languages(),
        variable=language
        ), 
        lambda parent: uih._custom_input_label(parent, "Language"),
        lambda parent: uih._custom_input_warning_label(parent, False),
        )
    language_input.pack(padx=20, pady=10)

    #langauge dropdown
    topic_input = uih.input_widget(
        app,
        lambda parent: ctk.CTkEntry(
        parent,
        placeholder_text="(e.g. Music)",
        ), 
        lambda parent: uih._custom_input_label(parent, "Topic"),
        lambda parent: uih._custom_input_warning_label(parent, True),
        )
    topic_input.pack(padx=20, pady=10)

    #number of paragraph
    number_of_paragraph = uih.input_widget(
        app,
        lambda parent: ctk.CTkEntry(
        parent,
        placeholder_text="Recommend: 3",
        ), 
        lambda parent: uih._custom_input_label(parent, "Number of Paragraphs"),
        lambda parent: uih._custom_input_warning_label(parent, True),
        )
    number_of_paragraph.pack(padx=20, pady=10)

    #difficulty ranging from
    difficulty_range_from_dropdown = uih.input_widget(
        app,
        lambda parent: ctk.CTkOptionMenu(
        parent,
        values=dh._getValues_difficulty_range(),
        variable=difficulty_range_from
        ), 
        lambda parent: uih._custom_input_label(parent, "Difficulty ranging from"),
        lambda parent: uih._custom_input_warning_label(parent, False),
        )
    difficulty_range_from_dropdown.pack(padx=20, pady=10)

    #difficulty ranging to
    difficulty_range_to_dropdown = uih.input_widget(
        app,
        lambda parent: ctk.CTkOptionMenu(
        parent,
        values=dh._getValues_difficulty_range(),
        variable=difficulty_range_to
        ), 
        lambda parent: uih._custom_input_label(parent, "Difficulty ranging from"),
        lambda parent: uih._custom_input_warning_label(parent, False),
        )
    difficulty_range_to_dropdown.pack(padx=20, pady=10)

    #number of questions
    number_of_question = uih.input_widget(
        app,
        lambda parent: ctk.CTkEntry(
        parent,
        placeholder_text="Recommend: 3",
        ), 
        lambda parent: uih._custom_input_label(parent, "Number of Questions"),
        lambda parent: uih._custom_input_warning_label(parent, True),
        )
    number_of_question.pack(padx=20, pady=10)

    #Verify valid inputs
    def submit():
        
        store_raw_data.language = language.get()
        store_raw_data.topic = topic_input.entry.get()
        store_raw_data.number_of_paragraph = number_of_paragraph.entry.get()
        store_raw_data.drf = dh._getKey_diffculty_range(difficulty_range_from.get())
        store_raw_data.drt = dh._getKey_diffculty_range(difficulty_range_to.get())
        store_raw_data.number_of_question = number_of_question.entry.get()
        print(language.get())
        print(topic_input.entry.get())
        print(number_of_paragraph.entry.get())
        print(difficulty_range_from.get())
        print(difficulty_range_to.get())
        print(number_of_question.entry.get())
        #test
        # c1, n1 = store_raw_data.drf
        # c2, n2 = store_raw_data.drt
        # rang = gp.Rang((c1, n1), (c2, n2))
        # g_p = gp.generate_prompt("English", "Shabu", 3, rang, 2)
        # prompt = gp._parse_formatted_prompt(g_p)
        # op.time.sleep(1)
        # print(prompt)
        # op.automate_browser(prompt)   

        # dh._set_raw_prompt(store_raw_data)
    def reset():
        dh._reset_raw_prompt()
    submit_button = uih.custom_button(app, submit, "Submit")
    reset_button = uih.custom_button(app, reset, 'Reset')
    submit_button.pack(padx=20, pady=10)
    reset_button.pack(padx=20, pady=10)
    app.mainloop()

if __name__ == "__main__":
    pass
