import customtkinter
import pyautogui
import time

checkTime = 1140
clickingLabel = None

def countDowntimer():
    global checkTime 
    checkTime -= 1
    minutes = checkTime // 60
    seconds = checkTime % 60
    time_display = f"{minutes:02}:{seconds:02}"
    timer_label.configure(text="Timer: " + time_display)
    time.sleep(1)
    app.after(1000, countDowntimer)

def startClicking():
    pyautogui.doubleClick(interval=1) 
    clickingLabel = customtkinter.CTkLabel(app, text="App will click every 19 minutes....")
    clickingLabel.grid(row=1, column=0, columnspan=2, pady=20)
    print("Clicking..")
    app.after(19 * 60 * 1000, startClicking)
    countDowntimer()

def stopClicking():
    print("Clicking has stopped...")
    if clickingLabel:
        clickingLabel.destroy()
    destroyLabel = customtkinter.CTkLabel(app, text="App will close in 5 Seconds....")
    destroyLabel.grid(row=1, column=0, columnspan=2, pady=20)
    app.after(5000, app.destroy)

def create_gui():
    global app, timer_label
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    app = customtkinter.CTk()
    app.title("Auto Clicker")
    app.minsize(350, 320)
    app.maxsize(351, 321)

    label1 = customtkinter.CTkLabel(app, text="Auto-Clicker")
    label1.grid(row=0, column=0, columnspan=2, padx=15, pady=10)

    timer_label = customtkinter.CTkLabel(app, text="Timer: 00:00")
    timer_label.grid(row=3, column=0, columnspan=2, padx=15, pady=10)

    startBtn = customtkinter.CTkButton(app, text="Start", command=startClicking)
    startBtn.grid(row=2, column=0, padx=5, pady=5)

    endBtn = customtkinter.CTkButton(app, text="Stop", command=stopClicking)
    endBtn.grid(row=2, column=1, padx=5, pady=5)

    app.mainloop()

if __name__ == "__main__":
    create_gui()
