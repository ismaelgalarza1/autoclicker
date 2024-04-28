import customtkinter
import pyautogui
import time
import threading

# Global variable to keep track of whether the clicking process is running
clicking_running = False
clicking_thread = None

def clicker():
    global clicking_running
    while clicking_running:
        pyautogui.doubleClick(interval=1)  # Double-click every 19 minutes
        time.sleep(11)
        print("Clicking..")

def start_clicker():
    global clicking_thread
    global clicking_running
    if not clicking_thread or not clicking_thread.is_alive():
        clicking_running = True
        clicking_thread = threading.Thread(target=clicker)
        clicking_thread.start()
        print("Starting program..")
        

def stop_clicker():
    global clicking_running
    global clicking_thread
    clicking_running = False
    if clicking_thread and clicking_thread.is_alive():
        clicking_thread.join()
        print("Stopping..")

customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("blue")

# Creating the Window 
app = customtkinter.CTk()

# Changing the title of the application 
app.title("Auto Clicker")

# Adjusting the minimum window on start up 
app.minsize(500, 120)
app.maxsize(501, 121)

label1 = customtkinter.CTkLabel(app, text="Auto clicker and mouse mover")
label1.grid(row=0, column=29, padx=10, pady=10)

# Add start and end buttons 
startBtn = customtkinter.CTkButton(app, text="Start", command=start_clicker)
startBtn.grid(row=2, column=29, padx=80, pady=25)

endBtn = customtkinter.CTkButton(app, text="Finish", command=stop_clicker)
endBtn.grid(row=2, column=30)

app.mainloop()
