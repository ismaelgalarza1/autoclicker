import os 
import customtkinter

customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("blue")

 #creating the Window 
app = customtkinter.CTk()

#Changing the title of the application 
app.title("Auto Clicker")

#adjusting the minimum widow on start up 
app.minsize(720,420)

def test():
    print("Testing")


label1 = customtkinter.CTkLabel(app, text="Auto clicker and mouse mover")
label1.grid(row=0, column=29, columnspan=2)
#add start and end buttons 

startBtn = customtkinter.CTkButton(app, text="Start", command=test)
startBtn.grid(row=30, column=29)

endBtn = customtkinter.CTkButton(app, text="Finish", command=test)
endBtn.grid(row=30, column=30,padx=10)






app.mainloop()