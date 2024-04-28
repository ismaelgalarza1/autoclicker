import customtkinter
import pyautogui
import time
import threading
from PIL import Image, ImageTk, ImageSequence
from queue import Queue

# Global variables
clicking_running = False
clicking_thread = None
queue = Queue()

def clicker():
    global clicking_running
    while clicking_running:
        pyautogui.doubleClick(interval=1)  # Double-click every 19 minutes
        time.sleep(1140)
        print("Clicking..")
        if not queue.empty():
            break
    print("Clicking stopped.")

def start_clicker():
    global clicking_thread
    global clicking_running
    if not clicking_thread or not clicking_thread.is_alive():
        clicking_running = True
        clicking_thread = threading.Thread(target=clicker)
        clicking_thread.start()
        print("Starting Program and GIF....")

        image_path = "asset/3Rbj.gif"
        frames = load_gif_frames(image_path)

        gif_label = customtkinter.CTkLabel(app)
        gif_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        update_label(gif_label, frames, 0)

def stop_clicker():
    global clicking_running
    global clicking_thread
    if clicking_thread and clicking_thread.is_alive():
        clicking_running = False  # Stop the clicking thread gracefully
        queue.put("stop")
        clicking_thread.join()
        print("Program and Gif finished.")

def load_gif_frames(image_path):
    gif_image = Image.open(image_path)
    frames = []

    for frame in ImageSequence.Iterator(gif_image):
        resized_frame = frame.resize((200, 200))
        tk_frame = ImageTk.PhotoImage(resized_frame)
        frames.append(tk_frame)

    return frames

def update_label(gif_label, frames, frame_index):
    gif_label.configure(image=frames[frame_index])
    app.after(100, update_label, gif_label, frames, (frame_index + 1) % len(frames))

def create_gui():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    global app
    app = customtkinter.CTk()
    app.title("Auto Clicker")
    app.minsize(350, 320)
    app.maxsize(351, 321)

    label1 = customtkinter.CTkLabel(app, text="Auto clicker and mouse mover")
    label1.grid(row=0, column=0, columnspan=2, padx=15, pady=10)

    startBtn = customtkinter.CTkButton(app, text="Start", command=start_clicker)
    startBtn.grid(row=2, column=0, padx=5, pady=5)

    endBtn = customtkinter.CTkButton(app, text="Finish", command=stop_clicker_and_restart)
    endBtn.grid(row=2, column=1, padx=5, pady=5)

    app.mainloop()

def stop_clicker_and_restart():
    stop_clicker()
    start_clicker()

if __name__ == "__main__":
    create_gui()
