import customtkinter as ctk
from open_browser import _get_monitor_size

difficulty_range = {"A1": "Beginner", 
                    "A2": "Elementary",
                    "B1": "Intermediate",
                    "B2": "Upper Intermediate",
                    "C1": "Advanced",
                    "C2": "Proficient",
                    }

def _getValues_difficulty_range():
    range_temp = []
    index = -1
    for difficulty in difficulty_range.values():
        index += 1
        range_temp.insert(index, difficulty)

    return range_temp

def _getKey_diffculty_range(difficulty_range_value):
    key = [k for k, v in difficulty_range.items() if v == difficulty_range_value]
    return key

#Customize button helper for number of paragraph (nof) input
def _increase(nof : ctk.CTkEntry):
    val = int(nof.get())
    nof.delete(0, "end")
    nof.insert(0, str(val + 1))

def _decrease(nof : ctk.CTkEntry):
    val = int(nof.get())
    nof.delete(0, "end")
    nof.insert(0, str(max(0, val - 1)))

def _user_interface():
    w,h=_get_monitor_size()
    app = ctk.CTk()
    app.geometry(f"{(int(w/2))}x{int(h/2)}")
    app.title("Automated ESL RASP Generator")
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

    # Customizing a button
    def submit():
        pass

    custom_button = ctk.CTkButton(
        master=app, 
        text="Submit", 
        command=submit,
        width=160,
        height=40,
        corner_radius=15,
        fg_color="#1f538d", # Hex color for custom fill
        hover_color="#14375e"
    )
    
    
    
    language = ctk.CTkEntry(app, placeholder_text="Language (e.g. English)")
    topic = ctk.CTkEntry(app, placeholder_text="Topic (e.g. Music)")
    difficulty_range_placeholder = _getValues_difficulty_range()[0]
    difficulty_range_from = ctk.StringVar(value=difficulty_range_placeholder)
    difficulty_range_to = ctk.StringVar(value=difficulty_range_placeholder)

    difficulty_range_from_dropdown = ctk.CTkOptionMenu(
        app,
        values=_getValues_difficulty_range(),
        variable=difficulty_range_from
    )
    difficulty_range_to_dropdown = ctk.CTkOptionMenu(
        app,
        values=_getValues_difficulty_range(),
        variable=difficulty_range_to
    )
    
    number_of_paragraph =  0
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

    custom_button.pack(padx=20, pady=40)
    app.mainloop()



if __name__ == "__main__":
    _user_interface()
