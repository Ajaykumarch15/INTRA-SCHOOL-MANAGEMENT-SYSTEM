import tkinter as tk
from auth.login import login
from student.student_dashboard import student_dashboard
from teacher.teacher_dashboard import teacher_dashboard
from admin.admin_dashboard import admin_dashboard

def on_login_success(user_role):

    if user_role == 'student':
        student_dashboard()
    elif user_role == 'teacher':
        teacher_dashboard()
    elif user_role == 'admin':
        admin_dashboard()
    else:
        print("Unknown role. Access denied.")

def main():
    root = tk.Tk()
    root.title("Intra School Event Management")
    root.geometry("1600x900")
    # frame
    frame = tk.Frame(root, bg="white", borderwidth=5, padx=10, pady=10)
    frame.place(relx=0.5, rely=0.5, anchor="center",width=900,height=300)

    #welcome label
    welcome_label = tk.Label(frame, text="WELCOME TO INTRA SCHOOL EVENT MANAGEMENT SYSTEM", font=("Arial", 16,'bold'),bg="white",fg="dark slate gray")
    welcome_label.pack(pady=10)

    #login button
    btn_login = tk.Button(frame, text="Login",font=("Arial",10), command=lambda: login(on_login_success,root),width=20,height=2,bg="blue",borderwidth=3,relief='raised')
    btn_login.pack(pady=20)

    #exit button
    btn_exit = tk.Button(frame, text="Exit", command=root.destroy,width=20,height=2,bg="red")
    btn_exit.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
