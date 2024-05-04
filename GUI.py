import customtkinter
import pyautogui
import time

def startClicking():
    clicks = 0
    pyautogui.doubleClick(interval=1)  # Double-click every 19 minutes
    clickingLabel = customtkinter.CTkLabel(app, text="App will click every 19 minutes....")
    clickingLabel.grid(row=1, column=0,columnspan=2)
    print("Clicking..")
    time.sleep(11)


def stopClicking():
    print("Clicking has stop...")
    destoryLabel = customtkinter.CTkLabel(app, text="App will close in 5 Seconds....")
    destoryLabel.grid(row=1, column=0,columnspan=2)
    app.after(3000, lambda: app.destroy() ) #destroy will close the app in 5 seconds



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

    startBtn = customtkinter.CTkButton(app, text="Start", command=startClicking)
    startBtn.grid(row=2, column=0, padx=5, pady=5)

    endBtn = customtkinter.CTkButton(app, text="Stop", command=stopClicking)
    endBtn.grid(row=2, column=1, padx=5, pady=5)

    app.mainloop()

if __name__ == "__main__":
    create_gui()
