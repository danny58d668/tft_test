import tkinter as tk

def create_gui(id):
    def on_button_click():
        # Function to be executed when the button is clicked
        user_input = entry.get()
        label.config(text=f"You entered: {user_input}")

    # Create the main window
    window = tk.Tk()
    window.title("Tkinter Example")

    # Set the window size (width x height)
    window.geometry("400x200")

    # Create a label
    label = tk.Label(window, text="USER ID:")
    label.pack()

    entry = tk.Entry(window)
    entry.pack()

    button = tk.Button(window, text=id, command=on_button_click)
    button.pack()
    window.mainloop()


a = "test text"
create_gui(a)
