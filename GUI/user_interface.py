#For dubbing only
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import customtkinter as ctk

from Utils import data_helper as dh
from Utils import data_validator as dv
from Utils import user_interface_helper as uih
from Automation import open_browser as op

def run_automation():
    dh.transcribe_prompt() # Genrate prompt
    op.time.sleep(0.5)
    prompt = dh._get_formatted_prompt()
    # response = op.automate_browser(prompt)
    # valid, message = dv._validate_response(response)
    # print(response)
    # print(valid)
    # if valid:
    #     dh._set_response(response)
    print(prompt)

def reset():
    dh._reset_raw_prompt()
    dh._reset_formatted_prompt()
    dh._reset_response()

def user_interface():
    w,h=uih._get_monitor_size()
    default_w = int(w/1.8)
    default_h = int(h/1.6)
    app = ctk.CTk()
    app.geometry(f"{default_w}x{default_h}")
    app.title("Automated ESL RASP Generator")
    ctk.set_appearance_mode("Dark")
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

    left_frame = ctk.CTkFrame(main_frame) # for inputs
    right_frame = ctk.CTkFrame(main_frame) # for response

    left_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
    right_frame.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
    
    left_frame.grid_columnconfigure(1, weight=1)
    left_frame.grid_rowconfigure((1, 2, 3, 4, 5, 6, 7, 8), weight=1)

    title = ctk.CTkLabel(
        main_frame,
        text="Automated ESL RASP Generator",
        font=("Arial", (default_h) * 0.10)
    )
    title.grid(row=0, columnspan=2, column=0, padx=10, pady=10)

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

        if validation_response["approve"] == True:
            dh._set_raw_prompt(store_raw_data)
                    # Update textbox with response5
                    # textbox.configure(state="normal")
                    # textbox.delete("1.0", "end")
                    # textbox.insert("1.0", response)
                    # textbox.configure(state="disabled")
            run_automation()
    
    submit_button = uih.custom_button(left_frame, validate_data, "Submit")
    reset_button = uih.custom_button(left_frame, reset, 'Reset')

    language_input.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
    topic_input.grid(row=2, column=1,sticky="nsew", padx=5, pady=5)
    difficulty_range_from_dropdown.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)
    difficulty_range_to_dropdown.grid(row=4, column=1, sticky="nsew", padx=5, pady=5)
    number_of_paragraph.grid(row=5, column = 1, sticky="nsew", padx=5, pady=5)
    number_of_question.grid(row=6, column = 1, sticky="nsew", padx=5, pady=5)
    submit_button.grid(row=7, column=1, sticky="nsew", padx=5, pady=5)
    reset_button.grid(row=8, column=1, sticky="nsew", padx=5, pady=5)
    
    app.mainloop()

if __name__ == "__main__":
    pass
