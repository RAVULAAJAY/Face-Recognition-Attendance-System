# Face Recognition Attendance System

### The Face Recognition Attendance System is an application that automates attendance tracking using advanced facial recognition technology. By capturing and identifying student, the system streamlines the attendance process, reduces errors, and enhances efficiency.

### The system not only tracks attendance but also maintains a comprehensive database of student details. This includes personal information such as names, student IDs, classes, contact information, etc allowing for easy reference and management.

### Users can quickly search for students within the system by using various criteria such as name, student ID, semester or department. This feature ensures that educators can easily access relevant information without extensive manual effort.                    



    


## Resources 
### 1) **Tkinter** library for creating Graphical User Interface (GUI).
#### Front page  
   ![image at](https://github.com/RAVULAAJAY/Face-Recognition-Attendance-System/blob/main/Images/21.png)

#### Student Deails Page
   ![image at](https://github.com/RAVULAAJAY/Face-Recognition-Attendance-System/blob/32f3fa89659b3d151aa92ffc9b46de7d86e41f71/Images/Screenshot%202026-06-28%20121520.png)

#### Attendance Page 
   ![image at](https://github.com/RAVULAAJAY/Face-Recognition-Attendance-System/blob/f503443233f330f6ae9b1703f6811fb38c0930b6/Images/Screenshot%202026-06-28%20121540.png)

### 2) **OpenCV** library for face detection and recognition using:     
### a) **Haarcascade** algorithm for face detection.
 ![image at](https://github.com/RAVULAAJAY/Face-Recognition-Attendance-System/blob/main/Images/Main-1.jpg)



                   
### b) **LBPH** algorithm for face recognition and training the dataset of images.
![image at](https://github.com/RAVULAAJAY/Face-Recognition-Attendance-System/blob/5d8f7cc5292512101762840387f7a1ea5ad83e74/Images/Screenshot%202026-06-28%20124507.png)
                 

### 3) **OS** library for reading, writing and opening files and folders.

### 4) **Datetime** library for retrieving the current date and time when a student's face is recognized.

### 5) **Pillow** library for manipulating image sizes and opening images.

### 6) **MySQL Connector** for creating and modifying databases.

### 7) **Numpy** library for storing and accessing 2d arrays created by LBPH algorithm while converting images to pixel values.
![image at](https://github.com/RAVULAAJAY/Face-Recognition-Attendance-System/blob/main/Images/Screenshot%202024-10-10%20055346.png)

### 8) **CSV** library for reading and writing CSV files that contain attendance records.

### 9) The **sys** library is used to determine the system on which the code is running and to set the appropriate options for building a GUI application using **cx_Freeze**.

## Tech Stack

### **Language:** Python ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

### **Librabries:** Tkinter, OpenCV, OS, Numpy, Pillow, Datetime,    Mysql.connector, Csv, Sys, Cx_Freeze

### **Algorithms:** Haarcascade, LBPH

### **Database:** MySQL ![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white) 

## Demo
### 1) **The Face Recognition Button will not work when there is no face present in the records :**
![image at](https://github.com/RAVULAAJAY/Face-Recognition-Attendance-System/blob/main/Images/fr.png)

   ### a) If the Faces folder is not present in the main folder.


   ### b) If the Faces folder does not contain any face.

  ###  c) If you have added images inside the Faces folder and not pressed the train button after adding the images.
  ![image at](https://github.com/RAVULAAJAY/Face-Recognition-Attendance-System/blob/main/Images/train.png)

### 2) Press the **escape key** to close the training and face recognition window.

## Features

### - Keeps a record of students in a school or university.
### - Students can be searched through various categories such as name, student - id, department and semester.
### - Allows modification of student details and searching through records.
### - Captures student faces for recognition purposes.
### - Automatically marks and stores student attendance.
### - This software can be integrated with CCTV cameras for automated attendance - tracking, eliminating the need for manual attendance management.

### You need to install some libraries using the command terminal so that the code runs smoothly on your device. You can use the given commands and run it on your command terminal.

### 1) OpenCV:

    pip install opencv-python
### 2) Pillow:
   
    pip install Pillow

### 3) Numpy:
    
    pip install numpy
### 4) MySQL Connector:
   
    pip install mysql-connector-python
   
   
### Setting up databse :
1) Install MySQL Workbench by watching the installation part of this video -- https://www.youtube.com/watch?v=5OdVJbNCSso

   Do everything same as done in this video but install the latest versions.

3) Find these lines in the code and replace the password in this line with your password :

     a) For database that has the details of the user.
     
           conn = mysql.connector.connect(host="localhost", username="root", password="@8234mo!", database="credentials")
    
    b) For database that contains the details of the students.
           
           conn = mysql.connector.connect(host = "localhost", username = "root", password = "@8234mo!", database = "frs")

3) Open Your MySQL WorkBench and Run these lines one by one on it.

a) `create database credentials;`

b) `use credentials;`

c) `CREATE TABLE details (
        Email varchar(50) NOT NULL,
        First_Name varchar(40) DEFAULT NULL,
        Last_Name varchar(40) DEFAULT NULL,
        Mobile varchar(15) DEFAULT NULL,
        Password varchar(100) DEFAULT NULL,
        PRIMARY KEY (Email)
  );`
  
d) `create database frs;`

e) `use frs;`


f) `CREATE TABLE student (
         StudentID varchar(20) DEFAULT NULL,
         Name varchar(50) DEFAULT NULL,
         Department varchar(50) DEFAULT NULL,
         Course varchar(50) DEFAULT NULL,
         Semester varchar(50) DEFAULT NULL,
         Year year DEFAULT NULL,
         Mobile varchar(50) DEFAULT NULL,
         Email varchar(50) DEFAULT NULL,
         School varchar(50) DEFAULT NULL,
         Parent_Name varchar(50) DEFAULT NULL,
         DOB date DEFAULT NULL,
         Address varchar(100) DEFAULT NULL
)`

## Support

### For support, reach out to Ravula Ajay.
