### **🔍 Three-Tier Architecture in Your Intra-School Event Management Desktop Application**  

Your **Intra-School Event Management System** follows the **Three-Tier Architecture**, which divides the application into three layers:  

1️⃣ **Presentation Layer (UI Layer)**  
2️⃣ **Business Logic Layer (Application Layer)**  
3️⃣ **Data Layer (Database Layer)**  

Each layer has a distinct role in maintaining the modularity, security, and scalability of your application.  

---

## **1️⃣ Presentation Layer (UI Layer) – The Frontend (Tkinter)**
📌 **Purpose:**  
- This layer interacts directly with users (Admins, Teachers, and Students).  
- It provides an intuitive graphical interface for event management, login, file submission, feedback, and more.  
- It ensures a smooth user experience using **Tkinter** for UI design.  

📌 **Components in Your Application:**  
- `main.py` → Login interface  
- `student_dashboard.py` → Student's main screen  
- `teacher_dashboard.py` → Teacher's main screen  
- `admin_dashboard.py` → Admin panel  
- `manage_events.py` → Event management UI  
- `submit_work.py` → File submission interface  
- `view_submissions.py` → Teachers' view of student submissions  
- **Widgets Used:** `Frames, Buttons, Labels, Entry Fields, ListBoxes`  

📌 **Responsibilities:**  
✅ Displays forms, buttons, and event details  
✅ Captures user inputs (login credentials, event details, file uploads)  
✅ Sends requests to the **Business Logic Layer** for processing  

---

## **2️⃣ Business Logic Layer (Application Layer) – The Backend (Python)**
📌 **Purpose:**  
- This layer processes user requests, applies business rules, and interacts with the database.  
- It contains all the logic for user authentication, event creation, role-based access, and CRUD operations.  
- It ensures that only authorized users can perform specific actions.  

📌 **Components in Your Application:**  
- `login.py` → Verifies user credentials and determines role-based redirection  
- `manage_users.py` → Admin functionalities for adding/removing users  
- `manage_events.py` → Handles event CRUD operations  
- `submit_work.py` → Processes student file submissions  
- `feedback.py` → Allows teachers to provide feedback on student work  
- **Functions Used:** `validate_user()`, `get_dashboard()`, `fetch_events()`, `submit_feedback()`, etc.  

📌 **Responsibilities:**  
✅ Validates user credentials and assigns roles (Admin, Teacher, Student)  
✅ Redirects users to their respective dashboards  
✅ Manages event creation, deletion, and updates  
✅ Stores, retrieves, and validates student submissions  
✅ Ensures business logic for event participation and feedback  

---

## **3️⃣ Data Layer (Database Layer) – MySQL Database**
📌 **Purpose:**  
- Stores and manages application data persistently using MySQL.  
- Ensures data integrity, consistency, and security through well-structured tables.  
- Provides efficient queries for CRUD operations.  

📌 **Components in Your Application:**  
- **Database:** `intra_school_event_management`  
- **Tables Used:**  
  - `users` → Stores user credentials and roles  
  - `students` → Stores student-specific details  
  - `teachers` → Stores teacher-specific details  
  - `events` → Stores event details (name, date, venue, organizer)  
  - `event_participation` → Stores event participants  
  - `event_files` → Stores uploaded student work  
  - `feedback` → Stores teacher feedback on student work  

📌 **Responsibilities:**  
✅ Stores user credentials securely  
✅ Maintains event details and participation records  
✅ Stores and retrieves submitted student files  
✅ Manages relationships between students, teachers, and events  
✅ Ensures role-based data access (only teachers can give feedback, only students can submit work)  

---

## **🎯 How These Three Layers Communicate in Your Application?**  
1️⃣ **User interacts with the UI (Presentation Layer)**  
   - Example: A student logs in and submits work through `submit_work.py`.  

2️⃣ **Business Logic Layer processes the request**  
   - The login details are verified using `login.py`.  
   - If valid, the student is redirected to `student_dashboard.py`.  
   - When submitting work, `submit_work.py` processes the file and sends it to MySQL.  

3️⃣ **Database Layer stores and retrieves data**  
   - `event_files` table stores the file details.  
   - Teachers can view submissions by querying the `event_files` table.  
   - Teachers give feedback, which gets stored in the `feedback` table.  

---

## **✅ Advantages of Using Three-Tier Architecture in Your Application**
🔹 **Scalability** → Each layer can be modified independently.  
🔹 **Security** → User authentication ensures only authorized users access sensitive data.  
🔹 **Maintainability** → Bug fixing and feature updates are easier due to modular design.  
🔹 **Performance Optimization** → Database queries are separated from UI, reducing load.  

---

### **🚀 Conclusion**
Your application is **well-structured** using the **Three-Tier Architecture**, ensuring **modularity, maintainability, and efficiency**. If you plan to **expand it into a web-based or mobile application**, this architecture will allow seamless transition and scalability.

---

Would you like any modifications or further explanations? 🚀😃