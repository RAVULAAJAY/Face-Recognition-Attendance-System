from tkinter import *
from D import Attendance
import os
import cv2
from PIL import Image 
from numpy import * 
from tkinter import messagebox 
import mysql.connector
from datetime import datetime  
 

class Face_Recognition_System:

    def __init__(self, window):
        self.window = window
        self.window.title("Face Recognition System")

        def student():
            from B import Student
            Student(self.window)
        def attendance():
            Attendance(self.window)


        self.boy = PhotoImage(file = "Images\\12.png")
        student_details = Button(self.window, font=("aerial", 20, "bold"), text="Student Details", image =  self.boy,
                         background="#ffdab9", compound=TOP, height=250, width=240, relief=RAISED, border=0, command= student,
                         borderwidth=6, activebackground="#fa8072")
        student_details.place(x=220, y=100)

        self.face = PhotoImage(file = "Images\\Face2.png")
        face_recog = Button(self.window, font=("aerial", 20, "bold"), text="Face Recognition", image=self.face,
                         background="#ffdab9", compound=TOP, height=250, width=240, relief=RAISED, border=0,
                         borderwidth=6, activebackground="#fa8072", command = self.face_recog)
        face_recog.place(x=1060, y=100)

        self.atten = PhotoImage(file = "Images\\Attendance.png")
        attend = Button(self.window, font=("aerial", 20, "bold"), text="Attendance", image=self.atten,
                         background="#ffdab9", compound=TOP, height=250, width=240, relief=RAISED, border=0,
                         borderwidth=6, activebackground="#fa8072", command = attendance)
        attend.place(x=640, y=100)

        self.group = PhotoImage(file = "Images\\Group.png")
        face_samples = Button(self.window, command = self.open_img, font=("aerial", 20, "bold"), text="Face Samples", image=self.group, background="#ffdab9",
                         compound=TOP, height=250, width=240, relief=RAISED, border=0, borderwidth=6,
                         activebackground="#fa8072")
        face_samples.place(x=640, y=440)


        self.exi = PhotoImage(file = "Images\\EXIT.png")
        close = Button(self.window, font=("aerial", 20, "bold"), text="Exit",background="#ffdab9",image=self.exi,
                         compound=TOP, height=250, width=240, relief=RAISED, border=0, borderwidth=6, command = self.close,
                         activebackground="#fa8072")
        close.place(x=1060, y=440)


        self.trai = PhotoImage(file = "Images\\5.png")
        train = Button(self.window, font=("aerial", 20, "bold"), text="Train Data",background="#ffdab9", image=self.trai,
                         compound=TOP, height=250, width=240, relief=RAISED, border=0, borderwidth=6, command = self.train,
                         activebackground="#fa8072")
        train.place(x=220, y=440)

    def close(self):
        import os
        os._exit(0)

    def open_img(self):
        import os
        if os.path.exists("Faces"):
            os.startfile("Faces")
        else:
            messagebox.showerror("Error", "Faces directory does not exist.", parent=self.window)

    def train(self):
        import os
        faces_dir = "Faces"
        if not os.path.exists(faces_dir) or not os.listdir(faces_dir):
            messagebox.showerror("Error", "No photo samples found in the Faces directory to train. Please add student photo samples first.", parent=self.window)
            return

        path = [os.path.join(faces_dir, file) for file in os.listdir(faces_dir)]
        faces = []
        ids = []

        for image in path:
            basename = os.path.basename(image)
            if not basename.startswith("user.") or not basename.endswith(".jpg"):
                continue
            try:
                id = int(basename.split('.')[1])
            except (IndexError, ValueError):
                continue
            
            try:
                img = Image.open(image).convert('L')
                image_np = array(img, "uint8")
                faces.append(image_np)
                ids.append(id)
                cv2.imshow("Training", image_np)
                cv2.waitKey(1)
            except Exception:
                continue

        if not faces:
            messagebox.showerror("Error", "No valid face samples found for training.", parent=self.window)
            cv2.destroyAllWindows()
            return

        ids = array(ids)
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifire.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training images completed!!")

    def mark_attendance(self, i, n):
        import os
        if not os.path.exists("Attendance"):
            os.makedirs("Attendance")
        
        file_path = "Attendance\\Attendance.csv"
        if not os.path.exists(file_path):
            with open(file_path, "w", newline="") as f:
                pass

        with open(file_path, "r+", newline="\n") as f:
            myDatalist = f.readlines()
            
            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M:%S")
            
            already_marked = False
            for line in myDatalist:
                entry = line.strip().split(",")
                if len(entry) >= 3:
                    existing_id = entry[0].strip()
                    existing_name = entry[1].strip()
                    existing_date = entry[2].strip()
                    if (existing_id == str(i).strip() or existing_name == str(n).strip()) and existing_date == d1:
                        already_marked = True
                        break
            
            if not already_marked:
                f.seek(0, os.SEEK_END)
                position = f.tell()
                if position == 0:
                    f.write(f"{i}, {n}, {d1}, {dtString}, Present")
                else:
                    f.write(f"\n{i}, {n}, {d1}, {dtString}, Present")

    def draw_boundary(self, img, classifier, scaleFactor, minNeighbors, color, text, clf, student_dict):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        featuers = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

        coord = []

        for (x, y, w, h) in featuers:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            id, predict = clf.predict(gray_image[y:y + h, x:x + w])

            confidence = int((100 * (1 - predict / 300)))

            student_id_str = str(id)
            if student_id_str in student_dict:
                i, n = student_dict[student_id_str]
            else:
                n = "Unknown"
                i = "Unknown"

            if confidence > 74 and i != "Unknown":
                cv2.putText(img, f"StudentID:{i}", (x, y - 80), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 0), 2)
                cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 0), 2)
                self.mark_attendance(i, n)
            else:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 0), 3)

            coord = [x, y, w, y]
        return coord

    def face_recog(self):
        import os
        if not os.path.exists("classifire.xml"):
            messagebox.showerror("Error", "Classifier data file (classifire.xml) not found. Please click 'Train Data' first.", parent=self.window)
            return

        if not os.path.exists("haarcascade_frontalface_default.xml"):
            messagebox.showerror("Error", "Haarcascade classifier file not found in the project directory.", parent=self.window)
            return

        student_dict = {}
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="$/F%rdyUQmX-i7",
                                           database="frs")
            cursor = conn.cursor()
            cursor.execute("select StudentID, Name from student")
            rows = cursor.fetchall()
            import hashlib
            for r in rows:
                student_id = str(r[0])
                hash_id = str(int(hashlib.sha256(student_id.encode('utf-8')).hexdigest(), 16) % (10**8))
                student_dict[hash_id] = (student_id, str(r[1]))
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load students from database: {str(e)}", parent=self.window)
            return

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifire.xml")

        videoCap = cv2.VideoCapture(0)
        if not videoCap.isOpened():
            messagebox.showerror("Error", "Could not open webcam. Please verify it is connected and not in use.", parent=self.window)
            return

        while True:
            ret, img = videoCap.read()
            if not ret or img is None:
                break
            self.draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf, student_dict)
            cv2.imshow("Face Detector", img)

            if cv2.waitKey(1) == 27:
                break
        videoCap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    window = Tk()
    s = Face_Recognition_System(window)
    icon = PhotoImage(file = "Images\\logo.png")
    window.iconphoto(True, icon)
    window.geometry("1540x800+-10+0")
    window.configure(background="#008080")
    window.mainloop()
