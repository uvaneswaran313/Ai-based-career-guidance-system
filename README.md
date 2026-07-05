# AI-Based Career Guidance System using Machine Learning and AI

A complete, production-ready web application designed for students and young professionals to discover their optimal career paths in technology. The system uses a **Random Forest Classifier** to match user profiles (academic scores, skills, interests, and personalities) with 18 specialized tech roles. It also provides detailed learning roadmaps, skills gap analysis, an ATS-grade resume scanner, a career assistant chatbot, and an admin analytics dashboard.

---

## 🚀 Key Features

1. **Intelligent Career Profiling & Quiz**: A multi-step questionnaire collecting academic background, technical interests, work preferences, and soft/hard skills.
2. **Machine Learning Classifier**: A Scikit-Learn Random Forest model that predicts the best-matching career path with **86.25% testing accuracy**.
3. **Interactive Learning Roadmaps**: Detailed milestones (Beginner to Job-Ready) with custom checklists tracking courses, projects, and certifications.
4. **ATS Resume Analyzer**: A file parser (PDF/TXT/DOCX) that extracts text, checks keyword matches, scores compatibility, and lists missing skills.
5. **AI Chat Assistant**: An interactive contextual chatbot helping answer queries regarding certifications, roadmaps, resume tips, and interview preps.
6. **Administrative Dashboard**: Aggregated system metrics (total active users, career distributions, popular recommendations) and user table management.
7. **PDF Report Exports**: Generated using Reportlab, compiling matching scores and custom timelines into a downloadable report.

---

## 🛠️ Technology Stack

* **Frontend**: React.js, Vite, Tailwind CSS, Framer Motion, Axios, Chart.js.
* **Backend**: Python, Flask, Flask-CORS, Flask-JWT-Extended, SQLAlchemy.
* **Machine Learning**: Scikit-Learn, Pandas, NumPy, Joblib.
* **Database**: SQLite (Local development default), supports MySQL.

---

## 📂 Project Structure

```
career-guidance-system/
├── backend/
│   ├── app.py                # Main Flask bootstrap & DB seeder
│   ├── config.py             # System & JWT secret configs
│   ├── database.py           # SQLAlchemy database model mappings
│   ├── auth.py               # Auth blueprint (Register, Login, Profile)
│   ├── api.py                # Core REST APIs (Assessments, Chat, Reports)
│   └── resume_analyzer.py    # Resume text extraction and keyword matching
├── machine_learning/
│   ├── train_model.py        # Generates synthetic dataset and trains model
│   └── evaluate_model.py     # Calculates model performance metrics
├── models/
│   ├── career_model.joblib   # Trained Random Forest classifier binary
│   └── encoders.joblib       # Serialized label encoders
├── dataset/
│   └── career_dataset.csv    # Generated synthetic CSV dataset
├── documentation/
│   └── project_report.md     # Full academic report (UML, ERD, DFD)
├── uploads/                  # Temporary upload folder for resume analysis
├── reports/                  # Generated PDF career reports folder
├── frontend/
│   ├── package.json
│   ├── src/
│   │   ├── main.jsx          # React DOM mounting
│   │   ├── App.jsx           # Sidebar layout and client routing
│   │   ├── index.css         # Glassmorphic themes & scrollbar styling
│   │   ├── pages/            # Page templates (Dashboard, Assessment, Careers, etc.)
│   └── vite.config.js        # Vite compilation configuration & API proxy
├── requirements.txt          # Python package requirements
└── setup_env.py              # Environment set up helper (Venv & Portable Node)
```

---

## 💻 Installation & Setup

Ensure you have **Python 3.13** installed on your system.

### 1. Set Up Environment
Run the setup script from the root workspace. This downloads portable Node.js, configures the `.venv` virtual environment, and installs dependencies:
```powershell
python setup_env.py
```

### 2. Scaffold and Install Frontend Packages
Wait for the setup script to complete, then install React dependencies:
```powershell
.\node-env\npm.cmd --prefix frontend install
```

### 3. Generate ML Dataset and Train Model
Train the Random Forest model and produce performance logs:
```powershell
.venv\Scripts\python.exe machine_learning/train_model.py
```

---

## 🏃 Running the Application

To run the application locally, start both the Flask backend and the React Vite dev server:

### Start Backend API Server
Runs on `http://127.0.0.1:5000`:
```powershell
.venv\Scripts\python.exe backend/app.py
```

### Start Frontend Dev Server
Runs on `http://localhost:5173`:
```powershell
.\node-env\npm.cmd --prefix frontend run dev
```

Open your browser and navigate to `http://localhost:5173`.

---

## 🧑‍💻 Credentials (For Evaluation)
* Register a new user using the registration page.
* The first user registered in the database is automatically granted the **Admin** role, unlocking access to the **Admin Panel**.
