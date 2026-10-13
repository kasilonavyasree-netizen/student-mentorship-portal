import streamlit as st
import sqlite3
import pandas as pd

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Student Mentorship Portal",
    page_icon="🎓",
    layout="wide"
)


# =========================================================
# CUSTOM PROFESSIONAL UI
# =========================================================

st.markdown("""
<style>

    /* Main background */
    [data-testid="stAppViewContainer"] {
        background-color: #f5f7fb;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #111827;
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Main headings */
    h1 {
        font-weight: 700;
    }

    h2 {
        font-weight: 650;
    }

    h3 {
        font-weight: 600;
    }

    /* Buttons */
    .stButton > button {
        width: 100%;
        border-radius: 8px;
        height: 45px;
        font-weight: 600;
        border: none;
    }

    /* Metric cards */
    [data-testid="stMetric"] {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
    }

    /* Text input boxes */
    input {
        border-radius: 8px !important;
    }

    /* Text areas */
    textarea {
        border-radius: 8px !important;
    }

    /* Select boxes */
    div[data-baseweb="select"] {
        border-radius: 8px;
    }

    /* Dataframes */
    [data-testid="stDataFrame"] {
        border-radius: 10px;
    }

    /* Cards */
    .feature-card {
        background-color: white;
        padding: 22px;
        border-radius: 12px;
        margin-bottom: 15px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.06);
    }

    .hero-box {
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        margin-bottom: 25px;
        box-shadow: 0px 3px 10px rgba(0,0,0,0.07);
    }

    .footer {
        text-align: center;
        padding: 20px;
        color: #6b7280;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# DATABASE CONNECTION
# =========================================================

conn = sqlite3.connect(
    "mentorship.db",
    check_same_thread=False
)

cursor = conn.cursor()


# =========================================================
# CREATE STUDENTS TABLE
# =========================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    branch TEXT,
    skills TEXT,
    career_goal TEXT
)
""")


# =========================================================
# CREATE MENTORS TABLE
# =========================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS mentors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    skills TEXT,
    experience TEXT
)
""")


# =========================================================
# CREATE REQUESTS TABLE
# =========================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT NOT NULL,
    mentor_name TEXT NOT NULL,
    message TEXT,
    status TEXT DEFAULT 'Pending'
)
""")


# =========================================================
# CREATE PROJECTS TABLE
# =========================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT NOT NULL,
    project_name TEXT NOT NULL,
    technology TEXT,
    description TEXT,
    project_link TEXT
)
""")


conn.commit()


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🎓 Student Portal")

st.sidebar.caption(
    "Mentorship & Project Showcase"
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "👨‍🎓 Student Registration",
        "👨‍🏫 Mentor Registration",
        "🔍 Find Mentor",
        "📩 Mentorship Request",
        "🚀 Project Showcase"
    ]
)

st.sidebar.markdown("---")

st.sidebar.caption(
    "Student Mentorship Portal"
)


# =========================================================
# HOME
# =========================================================

if page == "🏠 Home":

    st.markdown("""
    <div class="hero-box">
        <h1>🎓 Student Mentorship Portal</h1>
        <h3>Connect • Learn • Build</h3>
        <p>
        A platform where students can connect with mentors,
        receive guidance and showcase their projects.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Database counts

    student_count = cursor.execute(
        "SELECT COUNT(*) FROM students"
    ).fetchone()[0]

    mentor_count = cursor.execute(
        "SELECT COUNT(*) FROM mentors"
    ).fetchone()[0]

    project_count = cursor.execute(
        "SELECT COUNT(*) FROM projects"
    ).fetchone()[0]

    request_count = cursor.execute(
        "SELECT COUNT(*) FROM requests"
    ).fetchone()[0]


    # Metrics

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "👨‍🎓 Students",
            student_count
        )

    with col2:
        st.metric(
            "👨‍🏫 Mentors",
            mentor_count
        )

    with col3:
        st.metric(
            "🚀 Projects",
            project_count
        )

    with col4:
        st.metric(
            "📩 Requests",
            request_count
        )


    st.markdown("---")

    st.subheader("✨ Portal Features")


    col1, col2 = st.columns(2)


    with col1:

        st.markdown("""
        <div class="feature-card">

        <h3>👨‍🎓 Student Features</h3>

        <p>✅ Create student profile</p>
        <p>✅ Search for mentors</p>
        <p>✅ Send mentorship requests</p>
        <p>✅ Showcase projects</p>

        </div>
        """, unsafe_allow_html=True)


    with col2:

        st.markdown("""
        <div class="feature-card">

        <h3>👨‍🏫 Mentor Features</h3>

        <p>✅ Create mentor profile</p>
        <p>✅ Display expertise</p>
        <p>✅ Receive student requests</p>
        <p>✅ Guide students</p>

        </div>
        """, unsafe_allow_html=True)


# =========================================================
# STUDENT REGISTRATION
# =========================================================

elif page == "👨‍🎓 Student Registration":

    st.title("👨‍🎓 Student Registration")

    st.write(
        "Create your student profile."
    )

    st.markdown("---")

    name = st.text_input(
        "Student Name"
    )

    email = st.text_input(
        "Email"
    )

    branch = st.selectbox(
        "Branch",
        [
            "Computer Science",
            "Electronics",
            "Electrical",
            "Mechanical",
            "Civil",
            "Other"
        ]
    )

    skills = st.text_input(
        "Skills",
        placeholder="Python, SQL, Power BI"
    )

    career_goal = st.text_area(
        "Career Goal",
        placeholder="Example: Become a Data Analyst"
    )

    if st.button("Register Student"):

        if name and email:

            cursor.execute(
                """
                INSERT INTO students
                (name, email, branch, skills, career_goal)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    name,
                    email,
                    branch,
                    skills,
                    career_goal
                )
            )

            conn.commit()

            st.success(
                "✅ Student registered successfully!"
            )

        else:

            st.warning(
                "Please enter your name and email."
            )


# =========================================================
# MENTOR REGISTRATION
# =========================================================

elif page == "👨‍🏫 Mentor Registration":

    st.title("👨‍🏫 Mentor Registration")

    st.write(
        "Create your mentor profile."
    )

    st.markdown("---")

    name = st.text_input(
        "Mentor Name"
    )

    email = st.text_input(
        "Email"
    )

    skills = st.text_input(
        "Skills / Expertise",
        placeholder="Python, Data Analytics, Power BI"
    )

    experience = st.text_input(
        "Experience",
        placeholder="Example: 3 Years"
    )

    if st.button("Register Mentor"):

        if name and email:

            cursor.execute(
                """
                INSERT INTO mentors
                (name, email, skills, experience)
                VALUES (?, ?, ?, ?)
                """,
                (
                    name,
                    email,
                    skills,
                    experience
                )
            )

            conn.commit()

            st.success(
                "✅ Mentor registered successfully!"
            )

        else:

            st.warning(
                "Please enter your name and email."
            )


# =========================================================
# FIND MENTOR
# =========================================================

elif page == "🔍 Find Mentor":

    st.title("🔍 Find a Mentor")

    st.write(
        "Search for mentors based on their skills."
    )

    st.markdown("---")

    search_skill = st.text_input(
        "Search Skill",
        placeholder="Example: Python"
    )

    if search_skill:

        mentors = pd.read_sql_query(
            """
            SELECT
                name AS 'Mentor Name',
                email AS 'Email',
                skills AS 'Skills',
                experience AS 'Experience'
            FROM mentors
            WHERE skills LIKE ?
            """,
            conn,
            params=(
                "%" + search_skill + "%",
            )
        )

        if len(mentors) > 0:

            st.success(
                f"Found {len(mentors)} mentor(s)"
            )

            st.dataframe(
                mentors,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.warning(
                "No mentors found with that skill."
            )

    else:

        st.info(
            "Enter a skill to search for mentors."
        )


# =========================================================
# MENTORSHIP REQUEST
# =========================================================

elif page == "📩 Mentorship Request":

    st.title("📩 Mentorship Request")

    st.write(
        "Select a mentor and request guidance."
    )

    st.markdown("---")

    students = pd.read_sql_query(
        "SELECT name FROM students",
        conn
    )

    mentors = pd.read_sql_query(
        "SELECT name FROM mentors",
        conn
    )


    if len(students) == 0:

        st.warning(
            "Please register a student first."
        )

    elif len(mentors) == 0:

        st.warning(
            "Please register a mentor first."
        )

    else:

        student_name = st.selectbox(
            "Select Student",
            students["name"].tolist()
        )

        mentor_name = st.selectbox(
            "Select Mentor",
            mentors["name"].tolist()
        )

        message = st.text_area(
            "Message",
            placeholder="Explain why you need mentorship..."
        )

        if st.button("📩 Send Request"):

            if message:

                cursor.execute(
                    """
                    INSERT INTO requests
                    (student_name, mentor_name, message)
                    VALUES (?, ?, ?)
                    """,
                    (
                        student_name,
                        mentor_name,
                        message
                    )
                )

                conn.commit()

                st.success(
                    "✅ Mentorship request sent successfully!"
                )

            else:

                st.warning(
                    "Please enter a message."
                )


    st.markdown("---")

    st.subheader("📋 Existing Requests")


    requests = pd.read_sql_query(
        """
        SELECT
            student_name AS 'Student',
            mentor_name AS 'Mentor',
            message AS 'Message',
            status AS 'Status'
        FROM requests
        ORDER BY id DESC
        """,
        conn
    )


    if len(requests) > 0:

        st.dataframe(
            requests,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No mentorship requests yet."
        )


# =========================================================
# PROJECT SHOWCASE
# =========================================================

elif page == "🚀 Project Showcase":

    st.title("🚀 Student Project Showcase")

    st.write(
        "Share your projects and explore projects "
        "created by other students."
    )

    st.markdown("---")

    st.subheader("➕ Add Your Project")

    students = pd.read_sql_query(
        "SELECT name FROM students",
        conn
    )


    if len(students) == 0:

        st.warning(
            "Please register a student first."
        )

    else:

        student_name = st.selectbox(
            "Select Student",
            students["name"].tolist()
        )

        project_name = st.text_input(
            "Project Name",
            placeholder="Example: EV Data Analysis Dashboard"
        )

        technology = st.text_input(
            "Technology Used",
            placeholder="Python, Power BI, SQL"
        )

        description = st.text_area(
            "Project Description",
            placeholder="Briefly describe your project..."
        )

        project_link = st.text_input(
            "Project Link (Optional)",
            placeholder="GitHub or project URL"
        )


        if st.button("🚀 Add Project"):

            if project_name and technology:

                cursor.execute(
                    """
                    INSERT INTO projects
                    (
                        student_name,
                        project_name,
                        technology,
                        description,
                        project_link
                    )
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        student_name,
                        project_name,
                        technology,
                        description,
                        project_link
                    )
                )

                conn.commit()

                st.success(
                    "✅ Project added successfully!"
                )

            else:

                st.warning(
                    "Please enter project name and technology."
                )


    st.markdown("---")

    st.subheader("🌟 Student Projects")


    projects = pd.read_sql_query(
        """
        SELECT
            student_name AS 'Student',
            project_name AS 'Project',
            technology AS 'Technology',
            description AS 'Description',
            project_link AS 'Project Link'
        FROM projects
        ORDER BY id DESC
        """,
        conn
    )


    if len(projects) > 0:

        st.dataframe(
            projects,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No projects have been added yet."
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <div class="footer">
        🎓 Student Mentorship & Project Showcase Portal
        <br>
        Built with Python • Streamlit • SQLite
    </div>
    """,
    unsafe_allow_html=True
)