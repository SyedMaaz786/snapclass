# SnapClass

SnapClass is an AI-powered attendance management system built using Streamlit, integrating face recognition and voice recognition to automate classroom attendance.

---

## Features

### Teacher Dashboard

- Create and manage subjects
- Take attendance using images (face recognition)
- Take attendance using voice commands
- View attendance records

### Student Management

- Student enrollment system
- Subject-based student tracking

### AI-Based Attendance

- Face recognition pipeline for automatic attendance
- Voice recognition pipeline for alternative attendance input

---

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Database**: Supabase
- **AI/ML**:
  - Face Recognition Model (pre-trained, integrated)
  - Voice Recognition Pipeline
- **Libraries**:
  - OpenCV
  - NumPy
  - Pandas

---

## Project Structure

src/
├── components/ # UI components (dialogs, cards)
├── database/ # DB operations (Supabase)
├── pipelines/ # AI pipelines (face + voice)
├── screens/ # App screens (teacher, student)
├── ui/ # Base layout and styling

app.py # Main entry point
requirements.txt # Dependencies

---

## How It Works

1. Teacher selects a subject
2. Uploads classroom images
3. Face recognition model detects students
4. Matches faces with enrolled students
5. Marks attendance automatically

OR

1. Teacher uses voice attendance
2. Voice pipeline detects names
3. Attendance is marked

---

## Environment Variables

Create a `secrets.toml` file:
SUPABASE_URL=your_url
SUPABASE_KEY=your_key

---

## Run Locally

pip install -r requirements.txt
streamlit run app.py

Notes:
Face recognition model is integrated from external source
Designed as a real-world AI + full-stack project
Focused on automation and scalability

Author:
SYED MAAZ
