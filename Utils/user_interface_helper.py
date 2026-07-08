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

def _custom_input_warning_label(parent, warning=False):
    if warning == True:
        return ctk.CTkLabel(
            parent,
            text = "required",
            text_color="#e13809",
        )
    return None


def input_widget(parent, input_creator, input_label, warning_label):
    frame = ctk.CTkFrame(parent)
    input_label(frame).grid(row=0, column=0)

    input_c = input_creator(frame)
    
    warning = warning_label(frame)
    if warning:
        warning.grid(row=0, column=1)
    input_c.grid(row=1, column=0, columnspan=2, sticky="ew")

    frame.entry = input_c #for inside value

    return frame