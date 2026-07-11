#For dubbing only
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import customtkinter as ctk

from Utils import data_helper as dh
from Utils import data_validator as dv
from Utils import user_interface_helper as uih
from Automation import open_browser as op

from .pop_up_message import show_input_warning, show_submit_message


def run_automation():
    dh.transcribe_prompt() # Genrate prompt
    op.time.sleep(0.5)
    prompt = dh._get_formatted_prompt()
    response = op.automate_browser(prompt)
    valid, message = dv._validate_response(response)
    if valid:
        dh._set_response(response)
    else:
        dh._set_response(message)

def reset(textbox):
    textbox.configure(state="normal")
    textbox.delete("1.0", "end")
    textbox.configure(state="disabled")
    dh._reset_raw_prompt()
    dh._reset_formatted_prompt()
    dh._reset_response()

def show_response(textbox):
    #Update textbox with response
    response = dh._get_response()
    textbox.configure(state="normal")
    textbox.delete("1.0", "end")
    textbox.insert("1.0", response)
    textbox.configure(state="disabled")

def user_interface():
    w,h=uih._get_monitor_size()
    default_w = int(w/1.7)
    default_h = int(h/1.4)
    app = ctk.CTk()
    app.geometry(f"{default_w}x{default_h}")
    app.title("Automated ESL RASP Generator")
    ctk.set_appearance_mode("Light")
    ctk.set_default_color_theme("blue")
    response = ""

    difficulty_range_placeholder = dh._getValues_difficulty_range()[0]

    #State of input when required
    input_state = {"topic": False, "nop": False, "noq": False}

    #Dropdown inputs
    language = ctk.StringVar(value="English")
    difficulty_range_from = ctk.StringVar(value=difficulty_range_placeholder)
    difficulty_range_to = ctk.StringVar(value=difficulty_range_placeholder)


    #UX
    main_frame = ctk.CTkFrame(app)
    main_frame.grid(row=1, column=1)
    main_frame.place(relx=0.5, rely=0.5, anchor="center")
    main_frame.configure(width=default_w, height=default_h)
    main_frame.grid_columnconfigure(0, weight=1) 
    main_frame.grid_columnconfigure(1, weight=2)
    main_frame.grid_rowconfigure(0, weight=1)

    top_frame = ctk.CTkFrame(main_frame)
    left_frame = ctk.CTkFrame(main_frame) # for inputs
    right_frame = ctk.CTkFrame(main_frame) # for response

    top_frame.grid(row=0, columnspan = 2, column=0, sticky="nsew", padx=2, pady=2)
    left_frame.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
    right_frame.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
    
    left_frame.grid_columnconfigure(1, weight=1)
    left_frame.grid_rowconfigure((1, 2, 3, 4, 5, 6, 7, 8), weight=1)

    title = ctk.CTkLabel(
        top_frame,
        text="Automated ESL RASP Generator",
        font=("Arial", (default_h) * 0.08)
    )
    title.grid(row=0, column=0, padx=30, pady=10)

    description = ctk.CTkLabel(
        top_frame,
        text="English as Second Language, Reading and Speaking Practice is an automated generator through the process of auto-clicking and Chatgpt's Free text generation. \n Note: Requirement: Chrome. You shoul close all of your chrome(s), so it will produce a result — if not, try again!",
        font=("Arial", (default_h) * 0.02)
    )
    description.grid(row=1, column=0, padx=30, pady=5)

    textbox = ctk.CTkTextbox(right_frame, wrap="word")
    textbox.insert("1.0", response)
    textbox.configure(state="disabled")
    textbox.pack(fill="both", expand=True, padx=5, pady=5)

    #topic dropdown5
    topic_input = uih.input_widget(
        left_frame,
        lambda parent: ctk.CTkEntry(
        parent,
        placeholder_text="(e.g. Music)"
        ), 
        lambda parent: uih._custom_input_label(parent, "Topic"),
        lambda parent: uih._custom_input_warning_label(parent, lambda: input_state["topic"]),
        )
    
    #number of questions
    number_of_question = uih.input_widget(
        left_frame,
        lambda parent: ctk.CTkEntry(
        parent,
        placeholder_text="Recommend: 3"
        ), 
        lambda parent: uih._custom_input_label(parent, "Number of Questions"),
        lambda parent: uih._custom_input_warning_label(parent, lambda: input_state["noq"]),
        )
    
    #number of paragraph
    number_of_paragraph = uih.input_widget(
        left_frame,
        lambda parent: ctk.CTkEntry(
        parent,
        placeholder_text="Recommend: 3"
        ), 
        lambda parent: uih._custom_input_label(parent, "Number of Paragraphs"),
        lambda parent: uih._custom_input_warning_label(parent, lambda: input_state["nop"]),
        )
    
    #langauge dropdown
    language_input = uih.input_widget(
        left_frame,
        lambda parent: ctk.CTkOptionMenu(
        parent,
        values=dh._get_languages(),
        variable=language
        ), 
        lambda parent: uih._custom_input_label(parent, "Language"),
        lambda parent: uih._custom_input_warning_label(parent, lambda: False),
        )

    #difficulty ranging from
    difficulty_range_from_dropdown = uih.input_widget(
        left_frame,
        lambda parent: ctk.CTkOptionMenu(
        parent,
        values=dh._getValues_difficulty_range(),
        variable=difficulty_range_from
        ), 
        lambda parent: uih._custom_input_label(parent, "Difficulty ranging from"),
        lambda parent: uih._custom_input_warning_label(parent, lambda: False),
        )

    #difficulty ranging to
    difficulty_range_to_dropdown = uih.input_widget(
        left_frame,
        lambda parent: ctk.CTkOptionMenu(
        parent,
        values=dh._getValues_difficulty_range(),
        variable=difficulty_range_to
        ), 
        lambda parent: uih._custom_input_label(parent, "Difficulty ranging from"),
        lambda parent: uih._custom_input_warning_label(parent, lambda: False),
        )

    def validate_data():
        store_raw_data = dh.RawData()

        #Dropdown
        language_input = language.get()
        drf = dh._getKey_diffculty_range(difficulty_range_from.get())
        drt = dh._getKey_diffculty_range(difficulty_range_to.get())
        
        #Input
        topic = topic_input.entry.get()
        nop = number_of_paragraph.entry.get()
        noq = number_of_question.entry.get()

        validation_response = dv._validate_input(topic, input_state["topic"], 
                                              nop, input_state["nop"], noq, 
                                              input_state["noq"])
        input_state["topic"] = validation_response["states"]["topic_state"]
        input_state["nop"] = validation_response["states"]["nop_state"]
        input_state["noq"] = validation_response["states"]["noq_state"]
        
        # Show Warning(s)
        topic_input.refresh()
        number_of_paragraph.refresh()
        number_of_question.refresh()
        
        #store_data
        #Dropdown
        store_raw_data.language = language_input
        store_raw_data.drf = drf
        store_raw_data.drt = drt
        #Input
        store_raw_data.topic = topic
        store_raw_data.number_of_paragraph = nop
        store_raw_data.number_of_question = noq

        def proceed_automation():
            dh._set_raw_prompt(store_raw_data)
            run_automation()
            show_response(textbox)
        submit_message = f"The language you want to practice is {language_input} and the topic is about {topic} with {nop} paragraph(s) each level. The ESL level is ranging from {drf} to {drt} with {noq} question(s) to practice. \n\n Are you sure, you want to proceed with this idea?"
        if validation_response["approve"] == True:
            show_submit_message(app, proceed_automation, submit_message)
        else:
            show_input_warning(app, validation_response["response_message"])
    
    submit_button = uih.custom_button(left_frame, validate_data, "Submit")
    reset_button = uih.custom_button(right_frame, lambda: reset(textbox), 'Reset')

    language_input.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
    topic_input.grid(row=2, column=1,sticky="nsew", padx=5, pady=5)
    difficulty_range_from_dropdown.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)
    difficulty_range_to_dropdown.grid(row=4, column=1, sticky="nsew", padx=5, pady=5)
    number_of_paragraph.grid(row=5, column = 1, sticky="nsew", padx=5, pady=5)
    number_of_question.grid(row=6, column = 1, sticky="nsew", padx=5, pady=5)
    submit_button.grid(row=7, column=1, sticky="nsew", padx=5, pady=5)
    
    reset_button.pack(padx=5, pady=5)
    
    app.mainloop()

if __name__ == "__main__":
    pass
