# Student Mentorship & Project Showcase Portal

## 1. Project Overview
The Student Mentorship & Project Showcase Portal is a web application designed to connect students with mentors and provide a platform for showcasing academic projects.

## 2. Objectives
- Help students find mentors based on their skills.
- Allow students and mentors to register.
- Enable students to submit mentorship requests.
- Provide a platform to showcase academic projects.

## 3. Technologies Used
- Python
- Streamlit
- SQLite
- Pandas

## 4. Features
- Home dashboard
- Student registration
- Mentor registration
- Skill-based mentor search
- Mentorship requests
- Project showcase
- Database integration

## 5. System Architecture
- User Interface: Streamlit
- Application Logic: Python
- Database: SQLite

## 6. Project Structure
```text
student-mentorship-portal/
├── app.py
├── requirements.txt
└── README.md

## 7. Installation and Execution

Follow these steps to run the Student Mentorship & Project Showcase Portal on your local computer.

### Prerequisites
Before running the application, ensure that you have installed:
- Python 3.10 or a compatible version
- pip (Python package installer)
- Git (optional, for cloning the repository)

### Step 1: Clone the Repository

Open Command Prompt or a terminal and execute:

```bash
git clone https://github.com/kasilonav yasree-netizen/student-mentorship-portal.git
```

### Step 2: Navigate to the Project Folder

```bash
cd student-mentorship-portal
```

### Step 3: Install Required Dependencies

Install the Python libraries listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

### Step 5: Open the Application

After the application starts, open the local address displayed in the terminal. It will usually be:

`http://localhost:8501`

The application will open in your default web browser.

### Database Information

The application uses SQLite to store student details, mentor information, mentorship requests, and project records.

The database is initialized by the application when required. Each local installation may have its own database, separate from the online application.

### Troubleshooting

- If Python is not recognized, install Python and ensure it is added to your system PATH.
- If a package is missing, run `pip install -r requirements.txt` again.
- If the Streamlit command is not recognized, try `python -m streamlit run app.py`.
- If port 8501 is already in use, follow the alternative local address shown in the terminal.

- ## 8. Live Application

The Student Mentorship & Project Showcase Portal is available online.

**Live Demo:** [Open the Application](YOUR_STREAMLIT_APP_URL)

Replace `YOUR_STREAMLIT_APP_URL` with the actual URL provided by Streamlit Community Cloud.

## 9. Project Team

This project was developed as a five-member college mini-project.

### Team Contributions
- **Member 1:** Project coordination and dashboard
- **Member 2:** Student registration module
- **Member 3:** Mentor registration and search module
- **Member 4:** Mentorship request module
- **Member 5:** Project showcase, testing, and documentation

Team members and responsibilities should be updated to reflect their actual contributions.
