import customtkinter as ctk
from screeninfo import get_monitors

def _get_monitor_size():
    width = 0
    height = 0
    for monitor in get_monitors():
        width = monitor.width
        height = monitor.height

    return width, height

def custom_button(app : ctk.CTk, func, button_text):
    return ctk.CTkButton(
        master=app, 
        text=f"{button_text}", 
        command=func,
        width=140,
        height=40,
        corner_radius=15,
        fg_color="#1f538d",
        hover_color="#14375e"
    )

# input customization
def _custom_input_label(parent, label=""):
    return ctk.CTkLabel(
        parent,
        text =label,
        text_color="white",
    )

def _custom_input_warning_label(parent, get_state_warning):
    warning_label =  ctk.CTkLabel(
            parent,
            text = "required",
            width=50,
            anchor="e",
            text_color="#e13809",
        )
    #Just like react where it changes when an event happen
    def refresh():
        if get_state_warning():
            warning_label.configure(text="Invalid")
        else:
            warning_label.configure(text="")

    refresh()

    return warning_label, refresh
   
def input_widget(parent, input_creator, input_label, warning_label):
    frame = ctk.CTkFrame(parent, fg_color="transparent")
    frame.grid_columnconfigure(0, weight=1)
    
    top = ctk.CTkFrame(frame, fg_color="transparent")
    top.grid(row=0, column=0, sticky="ew")
    top.grid_columnconfigure(0, weight=1)
    
    
    input_label(top).grid(row=0, column=0, sticky="w")

    warning, refresh = warning_label(top)
    warning.grid(row=0, column= 1, sticky="e")

    input_c = input_creator(frame)
    input_c.grid(row=1, column = 0, sticky = "ew", padx = 5, pady = 5)

    frame.entry = input_c #for input value
    frame.refresh = refresh #for warning to shows up
    return frame