# School Management System – Odoo Module

This module provides core functionalities for managing a school, including students, teachers, classes, and subjects. It is designed for Odoo 17 and follows best practices for modular and maintainable development.

---

## 🌟 Features

- Manage **Students**: Personal info, academic state, photo, automatic age calculation, and unique student code.
- Manage **Teachers**: Assign subjects, personal details, and contact info.
- Organize **Classes**: Assign students, teachers (advisors), and subjects.
- Define **Subjects**: With a unique code and description.
- Record **Grades**: Per student, per subject, with exam types (midterm, final, quiz).
- Status tracking with **statebar** for students (e.g., draft → applied → enrolled → graduated).
- Sequence-generated **Student ID**.
- Search enhancements (by full name or national ID).
- Validation on birthdate, email, and phone number.

---

## 🏗️ Module Structure 
school_management/
├── init.py
├── manifest.py
├── models/
│ ├── student.py
│ ├── teacher.py
│ ├── subject.py
│ ├── class.py
├── views/
│ ├── student_views.xml
│ ├── teacher_views.xml
│ ├── subject_views.xml
│ ├── class_views.xml
├── data/
│ └── ir_sequence.xml
└── security/
└── ir.model.access.csv


---

## 🔧 Installation

1. Place the `school_management` folder inside your Odoo `addons/` directory.
2. Activate developer mode in Odoo.
3. Update the app list.
4. Install the **School Management System** module.

---

## 📝 Usage

- Navigate to the **School** menu.
- Manage Students, Teachers, Classes, and Subjects via their respective menu entries.
- Each model has tree and form views for management.
- Add student grades from the Student form or Grades menu.

---

## ⚙️ Dependencies

- Odoo 17
- No external Python libraries required.

---

## 📌 Future Improvements

- Attendance management.
- Parent contact tracking.
- Timetable and scheduling.
- Reporting and analytics dashboard.

---

## 👩‍💻 Author

**Gihan Atef Nazmy**  
_Backend Developer – Odoo 17 Focus_  
📧 gihanelsayed187@gmail.com  
📍 Cairo, Egypt  
🌐 [LinkedIn](https://www.linkedin.com/in/gihanatef/)

---

## 📄 License

This module is open source and available under the MIT License.

