import customtkinter
import pyautogui



def clicker():
    pyautogui.doubleClick(interval=10)  # Double-click every 19 minutes
    print("Clicking..")

def create_gui():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    global app
    app = customtkinter.CTk()
    app.title("Auto Clicker")
    app.minsize(350, 320)
    app.maxsize(351, 321)

    label1 = customtkinter.CTkLabel(app, text="Auto clicker")
    label1.grid(row=0, column=0, columnspan=2, padx=15, pady=10)

    startBtn = customtkinter.CTkButton(app, text="Start", command=start_clicker)
    startBtn.grid(row=2, column=0, padx=5, pady=5)

    endBtn = customtkinter.CTkButton(app, text="Stop", command=stop_clicker)
    endBtn.grid(row=2, column=1, padx=5, pady=5)

    app.mainloop()

if __name__ == "__main__":
    create_gui()
