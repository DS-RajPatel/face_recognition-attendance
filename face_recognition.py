# import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
from datetime import date
from datetime import datetime
import numpy as np
from tkinter import messagebox
from time import strftime
import pandas as pd
import datetime
import csv
import share

class Face_Recognition:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Pannel")

        # This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\rajpa\Documents\Python_Test_Projects\Images_GUI\banner.jpg")
        img=img.resize((1366,130))
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"Images_GUI\bg2.jpg")
        bg1=bg1.resize((1366,768))
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)
    
        exit_btn=Button(self.root,text="Exit",command=self.close_window,width=9,font=("verdana",12,"bold"),fg="white",bg="Red")
        exit_btn.grid(row=0,column=5,padx=10,pady=25,sticky=W)

        #title section
        title_lb1 = Label(bg_img,text="Face Recognition",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        title_lb2 = Label(bg_img,text=f"{share.value}",font=("verdana",15),bg="white",fg="navyblue")
        title_lb2.place(x=450,y=50,width=500,height=25)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"Images_GUI\f_det.jpg")
        std_img_btn=std_img_btn.resize((180,180))
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.face_recog,image=self.std_img1,cursor="hand2")
        std_b1.place(x=600,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.face_recog,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=600,y=350,width=180,height=45)
    #=====================Attendance===================


    def mark_attendance(self, i, r, n):
        try:
            folder_path = os.path.join(r"C:\Users\rajpa\Documents\Python_Test_Projects\attendance", share.value)
            os.makedirs(folder_path, exist_ok=True)
            today = datetime.date.today().strftime("%Y-%m-%d")  # Get current date in YYYY-MM-DD format
            filename = os.path.join(folder_path,f"{today}.csv")  # Create filename with date
            if not os.path.exists(filename):
                with open(filename, 'a', newline='\n') as f:
                    writer = csv.writer(f)
                    writer.writerow(["std_id", "Roll_no", "Name", "Time", "Date", "Status"])


        # Step 1: Check if the entry already exists for the user and current date
            entry_exists = False
            with open(filename, 'r', newline='\n') as f:
                reader = csv.reader(f)
                next(reader)  # Skip header row
                for row in reader:
                    if row[:3] == [str(i), str(r), n] and row[-2] == today:  # Check if entry already exists for the user and current date
                        entry_exists = True
                        break

        # Step 2: If entry doesn't exist, insert the record
            if not entry_exists:
                with open(filename, 'a', newline='\n') as f:
                    writer = csv.writer(f)
                    now = datetime.datetime.now().strftime("%H:%M:%S")
                    writer.writerow([i, r, n, now, today, "Present"])
                    print(f"Attendance marked for {today} successfully.")
            else:
                print("Record already exists in the attendance record.")
    
        except Exception as e:
            print(f"An error occurred: {e}")

        
    #================face recognition==================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            global i,r,n;
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord=[]
            
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                print(id)
                confidence=int((100*(1-predict/300)))

                
                if confidence > 77:
                    conn = mysql.connector.connect(username='root', password='1234',host='localhost',database='face_recognition',port=3306)
                    cursor = conn.cursor()
                    cursor.execute("select Name, Roll_No,Student_id from student where Student_ID=" + str(id))
                    row = cursor.fetchone()
                    if row is not None:
                        n, r = row[0], row[1]
                    
                        print(r)
                        cv2.putText(img, f"Student_ID:{id}", (x, y-80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0), 2)
                        cv2.putText(img, f"Name:{n}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0), 2)
                        cv2.putText(img, f"Roll-No:{r}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0), 2)
                        self.mark_attendance(id, r, n)
                    else:
                        cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),3)    

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),3)    

                coord=[x,y,w,y]
            
            return coord    


        #==========
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        videoCap=cv2.VideoCapture(0)

        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Detector",img)
            key = cv2.waitKey(100)
            if key & 0xFF == ord('q'):
                break

        videoCap.release()
        cv2.destroyAllWindows()
        

    def close_window(self):
        self.root.destroy()



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()