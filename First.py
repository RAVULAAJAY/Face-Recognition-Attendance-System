from tkinter import *
from tkinter import messagebox
import mysql.connector 
  
 
class Login:
    def __init__(self, window):
        self.window = window 

        def sign_up():
            from A1 import Register
            Register(self.window)


        self.logo = PhotoImage(file = "Images\\logo.png").subsample(4, 4)

        from PIL import Image, ImageTk
        img = Image.open("Images\\login_bg.png")
        img = img.resize((1530, 800))
        self.bg_image = ImageTk.PhotoImage(img)
        
        # Single main canvas for everything
        main_canvas = Canvas(self.window, background="#ffffff", highlightthickness=0)
        main_canvas.place(x=0, y=0, width=1530, height=800)
        main_canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        def round_rect(canvas, x1, y1, x2, y2, radius=25, **kwargs):
            points = [x1+radius, y1, x1+radius, y1, x2-radius, y1, x2-radius, y1, x2, y1, x2, y1+radius, x2, y1+radius, x2, y2-radius, x2, y2-radius, x2, y2, x2-radius, y2, x2-radius, y2, x1+radius, y2, x1+radius, y2, x1, y2, x1, y2-radius, x1, y2-radius, x1, y1+radius, x1, y1+radius, x1, y1]
            return canvas.create_polygon(points, **kwargs, smooth=True)

        card_x, card_y = 515, 100
        card_w, card_h = 500, 580

        card_bg = "#ffffff"
        text_color = "#1a252f"
        teal_color = "#008080"
        
        # Shadow
        round_rect(main_canvas, card_x+2, card_y+8, card_x+card_w+8, card_y+card_h+8, radius=30, fill="#222222")
        # Card Background
        round_rect(main_canvas, card_x, card_y, card_x+card_w, card_y+card_h, radius=30, fill=card_bg)

        # Logo and Title
        main_canvas.create_image(card_x+130, card_y+110, image=self.logo)
        main_canvas.create_text(card_x+220, card_y+80, text="The", font=("Helvetica", 32, "bold"), fill=text_color, anchor="w")
        main_canvas.create_text(card_x+220, card_y+130, text="University", font=("Helvetica", 32, "bold"), fill=text_color, anchor="w")

        # Username
        main_canvas.create_text(card_x+50, card_y+210, text="Username", font=("Helvetica", 14), fill="#555555", anchor="w")
        u_bg = round_rect(main_canvas, card_x+50, card_y+230, card_x+450, card_y+280, radius=20, fill="#f0f2f5", outline="#cccccc")
        self.username = Entry(main_canvas, font=("Helvetica", 15), background="#f0f2f5", foreground=text_color, relief="flat", highlightthickness=0, insertbackground=teal_color)
        self.username.place(x=card_x+65, y=card_y+242, height=26, width=370)
        self.username.insert(0, "Enter your username")
        self.username.bind("<FocusIn>", lambda args: [self.username.delete('0', 'end'), main_canvas.itemconfig(u_bg, outline=teal_color, width=2)] if self.username.get() == "Enter your username" else main_canvas.itemconfig(u_bg, outline=teal_color, width=2))
        self.username.bind("<FocusOut>", lambda args: [self.username.insert(0, "Enter your username"), main_canvas.itemconfig(u_bg, outline="#cccccc", width=1)] if self.username.get() == "" else main_canvas.itemconfig(u_bg, outline="#cccccc", width=1))

        # Password
        main_canvas.create_text(card_x+50, card_y+320, text="Password", font=("Helvetica", 14), fill="#555555", anchor="w")
        p_bg = round_rect(main_canvas, card_x+50, card_y+340, card_x+450, card_y+390, radius=20, fill="#f0f2f5", outline="#cccccc")
        self.password = Entry(main_canvas, font=("Helvetica", 15), background="#f0f2f5", foreground=text_color, relief="flat", highlightthickness=0, insertbackground=teal_color)
        self.password.place(x=card_x+65, y=card_y+352, height=26, width=370)
        self.password.insert(0, "Enter your password")
        self.password.bind("<FocusIn>", lambda args: [self.password.delete('0', 'end'), self.password.config(show="*"), main_canvas.itemconfig(p_bg, outline=teal_color, width=2)] if self.password.get() == "Enter your password" else main_canvas.itemconfig(p_bg, outline=teal_color, width=2))
        self.password.bind("<FocusOut>", lambda args: [self.password.config(show=""), self.password.insert(0, "Enter your password"), main_canvas.itemconfig(p_bg, outline="#cccccc", width=1)] if self.password.get() == "" else main_canvas.itemconfig(p_bg, outline="#cccccc", width=1))

        # Login Button
        btn_bg = round_rect(main_canvas, card_x+50, card_y+440, card_x+450, card_y+490, radius=25, fill=teal_color, outline=teal_color)
        btn_txt = main_canvas.create_text(card_x+250, card_y+465, text="Log In", font=("Helvetica", 18, "bold"), fill="white")
        
        def on_enter(e): main_canvas.itemconfig(btn_bg, fill="#006666", outline="#006666")
        def on_leave(e): main_canvas.itemconfig(btn_bg, fill=teal_color, outline=teal_color)
        def on_click(e): self.login()
        
        for item in (btn_bg, btn_txt):
            main_canvas.tag_bind(item, "<Enter>", on_enter)
            main_canvas.tag_bind(item, "<Leave>", on_leave)
            main_canvas.tag_bind(item, "<Button-1>", on_click)

        # Sign Up
        main_canvas.create_text(card_x+220, card_y+530, text="Don't have an account?", font=("Helvetica", 12), fill="#555555", anchor="e")
        sign_up_txt = main_canvas.create_text(card_x+230, card_y+530, text="Sign Up", font=("Helvetica", 12, "bold"), fill=teal_color, anchor="w")
        main_canvas.tag_bind(sign_up_txt, "<Enter>", lambda e: main_canvas.itemconfig(sign_up_txt, fill="#006666"))
        main_canvas.tag_bind(sign_up_txt, "<Leave>", lambda e: main_canvas.itemconfig(sign_up_txt, fill=teal_color))
        main_canvas.tag_bind(sign_up_txt, "<Button-1>", lambda e: sign_up())

  
    def login(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "Perhaps you forgot to enter Username or Password")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="$/F%rdyUQmX-i7",
                                           database="credentials")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from details where Email = %s and Password = %s",
                              (self.username.get(),
                               self.password.get()
                               ))
            row = my_cursor.fetchone()
            conn.close()

            if row != None:
                import os
                self.new_window = Toplevel(self.window)
                self.new_window.geometry("1530x800+-5+0")
                self.new_window.config(background="#008080")
                self.new_window.protocol("WM_DELETE_WINDOW", lambda: os._exit(0))
                from A import Face_Recognition_System
                self.new =  Face_Recognition_System(self.new_window)
                self.window.withdraw()

            else:
                messagebox.showerror("Error", "Invalid Username and Password.")




if __name__ == "__main__":
    import os
    window = Tk()
    window.protocol("WM_DELETE_WINDOW", lambda: os._exit(0))
    Login(window)
    window.title("Face Recognition System")
    window.geometry("1530x800+-5+0")
    window.config(background="#008080")
    icon = PhotoImage(file = "Images\\logo.png")
    window.iconphoto(True, icon)
    window.mainloop()
