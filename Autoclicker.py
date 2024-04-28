import os 
import customtkinter

customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("blue")

 #creating the Window 
app = customtkinter.CTk()

frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill="both", expand=True)

#Changing the title of the application 
app.title("Auto Clicker")

#adjusting the minimum widow on start up 
app.minsize(720,420)

#add start and end buttons 

startBtn = customtkinter.CTkButton(master=frame, text="Start")
startBtn.grid(row=9, column=4)

endBtn = customtkinter.CTkButton(master=frame, text="Finish")
endBtn.grid(row=9, column=7)






app.mainloop()