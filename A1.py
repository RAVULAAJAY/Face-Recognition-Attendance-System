from tkinter import *
from tkinter import messagebox
import mysql.connector
import First  
from PIL import Image, ImageTk

class Register: 
    def __init__(self, window):  
        self.window = window


        frame = Frame(self.window, background = "#ffdab9")# "#fffaf0")
        frame.place(x = 300, y = 71, width = 950, height = 650)

        Label(frame, text = "Create a new account", background="#ffdab9", font = ("aerial",35,"bold"), width = 33).place(x = 0, y = 0)
        Label(frame, text = "First Name", font = ("aerial",25,"bold"), background="#ffdab9").place(x = 60, y = 100)
        Label(frame, text="Mobile No.", font=("aerial", 25, "bold"), background="#ffdab9").place(x=60, y=240)
        Label(frame, text="Password", font=("aerial", 25, "bold"), background="#ffdab9").place(x=60, y=380)

        Label(frame, text = "Last Name", font = ("aerial",25,"bold"), background="#ffdab9").place(x = 530, y = 100)
        Label(frame, text="Email", font=("aerial", 25, "bold"), background="#ffdab9").place(x=530, y=240)
        Label(frame, text="Confirm Password", font=("aerial", 25, "bold"), background="#ffdab9").place(x=530, y=380)

        self.first_name = StringVar()
        f_name = Entry(frame,  font = ("aerial",25,"bold"), background = "#008080", foreground="white", textvariable = self.first_name)
        f_name.place(x = 60, y = 160)

        self.mobile = StringVar()
        mobile = Entry(frame,  font = ("aerial",25,"bold"), background = "#008080", foreground="white", textvariable = self.mobile)
        mobile.place(x = 60, y = 300)

        self.password = StringVar()
        password = Entry(frame,  font = ("aerial",25,"bold"), background = "#008080", foreground="white", textvariable = self.password)
        password.place(x = 60, y = 440)

        self.last_name = StringVar()
        l_name = Entry(frame, font=("aerial", 25, "bold"), background="#008080", foreground="white", textvariable = self.last_name)
        l_name.place(x=530, y=160)

        self.email = StringVar()
        email = Entry(frame,  font = ("aerial",25,"bold"), background = "#008080", foreground="white", textvariable = self.email)
        email.place(x = 530, y = 300)

        self.conf_password = StringVar()
        conf_password = Entry(frame,  font = ("aerial",25,"bold"), background = "#008080", foreground="white", textvariable = self.conf_password)
        conf_password.place(x = 530, y = 440)

        register = Button(frame, text = "Register", command = self.register,background="#008080",foreground="white", activebackground="#ffdab9", font = ("aerial",20,"bold"), relief=RAISED, bd = 10,activeforeground="black", width=15)
        register.place(x = 335, y = 530)

        arrow = Image.open("Images\\Left_Arrow.png")
        arrow = arrow.resize((100,80))
        self.arrow = ImageTk.PhotoImage(arrow)

        previous = Button(self.window, image = self.arrow, background="#008080", borderwidth=0, activebackground = "#008080", command = self.back)#"#ffdab9")
        previous.place(x = 0, y = 0)

    def register(self):
        if self.password.get() != self.conf_password.get() :
            messagebox.showerror("Error", "Passwords do not match.")
        elif self.first_name.get() == "" or self.last_name.get() == "" or len(self.mobile.get()) < 10 or len(self.email.get()) < 10 or self.password.get() == "" or self.conf_password.get() == "":
            messagebox.showerror("Error", "You left one or more fields empty. All fields are mandatory.")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="$/F%rdyUQmX-i7",
                                           database="credentials")
            my_cursor = conn.cursor()
            query = "select * from details where Email = %s"
            val = (self.email.get(),)
            my_cursor.execute(query, val)

            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error","User already exists.Try with another email")
            else:
                my_cursor.execute("insert into details values (%s,%s,%s,%s,%s)",
                                                                            (self.email.get(),
                                                                                    self.first_name.get(),
                                                                                    self.last_name.get(),
                                                                                    self.mobile.get(),
                                                                                    self.password.get()
                                                                             ))
                messagebox.showinfo("User Registered", "User registered successfully.")
            conn.commit()
            conn.close()




    def back(self):
        import os
        self.new = Toplevel(self.window)
        self.new.geometry("1540x800+-10+0")
        self.new.config(background = "#008080")
        self.new.protocol("WM_DELETE_WINDOW", lambda: os._exit(0))
        self.window.withdraw()
        self.new_window = First.Login(self.new)





if __name__ == "__main__":
    window = Tk()
    Register(window)
    window.geometry("1540x800+-10+0")
    window.config(background = "#008080")
    icon = PhotoImage(file = "Images\\logo.png")
    window.iconphoto(True, icon)
    window.title("Face Recognition System")
    window.mainloop()
