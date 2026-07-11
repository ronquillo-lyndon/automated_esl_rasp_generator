import customtkinter as ctk


def _xy_position(app, popup_w, popup_h):
    app_x = app.winfo_x()
    app_y = app.winfo_y()
    app_width = app.winfo_width()
    app_height = app.winfo_height()

    # to center
    x = app_x + (app_width - popup_w) // 2
    y = app_y + (app_height - popup_h) // 2
    return x,y

def show_input_warning(app, message):
    popup = ctk.CTkToplevel(app)
    popup.title("Warning")
    popup_width = 300
    popup_height = 150
    x, y = _xy_position(app, popup_width, popup_height)
    popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")
    popup.transient(app)
    popup.grab_set()

    label = ctk.CTkLabel(
        popup,
        text=message,
        wraplength=250
    )
    label.pack(pady=20)

    ok_button = ctk.CTkButton(
        popup,
        text="OK",
        command=popup.destroy
    )
    ok_button.pack(pady=10)

    return popup

def show_submit_message(app, proceed_command, message):
    popup = ctk.CTkToplevel(app)
    popup.title("Verify Input")
    popup_width = 300
    popup_height = 250
    x, y = _xy_position(app, popup_width, popup_height)
    popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")
    popup.transient(app)
    popup.grab_set()

    label = ctk.CTkLabel(
        popup,
        text=message,
        wraplength=250
    )
    label.pack(pady=20)

    cancel_button = ctk.CTkButton(
        popup,
        text="Close",
        command=popup.destroy
    )
    cancel_button.pack(pady=5)

    def _proceed():
        popup.destroy()
        proceed_command()
    proceed_button = ctk.CTkButton(
        popup,
        text="Proceed",
        command=_proceed
    )
    proceed_button.pack(pady=5)

    return popup
