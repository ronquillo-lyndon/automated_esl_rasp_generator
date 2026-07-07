#For dubbing only
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import customtkinter as ctk
from Utils import data_helper as dh
from Utils import user_interface_helper as uih

#Customize button helper for number of paragraph (nof) input
def _increase(nof : ctk.CTkEntry):
    val = int(nof.get())
    nof.delete(0, "end")
    nof.insert(0, str(val + 1))

def _decrease(nof : ctk.CTkEntry):
    val = int(nof.get())
    nof.delete(0, "end")
    nof.insert(0, str(max(0, val - 1)))

def custom_button(app : ctk.CTk, func, button_text):
    return ctk.CTkButton(
        master=app, 
        text=f"{button_text}", 
        command=func,
        width=160,
        height=40,
        corner_radius=15,
        fg_color="#1f538d", # Hex color for custom fill
        hover_color="#14375e"
    )

def _user_interface():
    w,h=uih._get_monitor_size()
    app = ctk.CTk()
    app.geometry(f"{(int(w/2))}x{int(h/2)}")
    app.title("Automated ESL RASP Generator")
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

    store_raw_data = dh.RawData()
    number_of_paragraph = 1
    number_of_questions = 1

    def submit():
        dh._set_raw_prompt(store_raw_data)
    def reset():
        dh._reset_raw_prompt()

    submit_button = custom_button(app, submit, "Submit")
    reset_button = custom_button(app, reset, 'Reset')
    
    language = ctk.CTkEntry(app, placeholder_text="Language (e.g. English)")
    topic = ctk.CTkEntry(app, placeholder_text="Topic (e.g. Music)")
    difficulty_range_placeholder = dh._getValues_difficulty_range()[0]
    difficulty_range_from = ctk.StringVar(value=difficulty_range_placeholder)
    difficulty_range_to = ctk.StringVar(value=difficulty_range_placeholder)

    difficulty_range_from_dropdown = ctk.CTkOptionMenu(
        app,
        values=dh._getValues_difficulty_range(),
        variable=difficulty_range_from
    )
    difficulty_range_to_dropdown = ctk.CTkOptionMenu(
        app,
        values=dh._getValues_difficulty_range(),
        variable=difficulty_range_to
    )
    
    
    nof_display = ctk.CTkEntry(app)
    nof_display.insert(0, str(number_of_paragraph))

    language.pack(padx=20, pady=10)
    topic.pack(padx=20, pady=10)

    difficulty_range_from_dropdown.pack(padx=20, pady=10)
    difficulty_range_to_dropdown.pack(padx=20, pady=10)

    nof_display.pack(pady=10)
    ctk.CTkButton(app, 
                  text="-", 
                  command=lambda: _decrease(nof_display)
                  ).pack(padx=20, pady=10)
    ctk.CTkButton(app, 
                  text="+", 
                  command=lambda: _increase(nof_display)
                  ).pack(padx=20, pady=10)

    submit_button.pack(padx=20, pady=10)
    reset_button.pack(padx=20, pady=10)
    app.mainloop()

if __name__ == "__main__":
    _user_interface()
