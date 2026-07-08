from src.database.config import supabase
import bcrypt



def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()

def check_pass(pwd, hashed):
    return bcrypt.checkpw(pwd.encode(), hashed.encode())


def check_teacher_exists(username):
    # Check for unique username, returns false when username is already taken
    response = supabase.table("teachers").select("username").eq("username", username).execute()
    return len(response.data) > 0 



import uuid
def create_teacher(email, username, password, name):

    # 1. create Supabase auth user
    user = supabase.auth.sign_up({
        "email": email,
        "password": password
    })

    if user.user is None:
        return None

    # 2. insert into teachers table
    data = {
        "username": username,
        "name": name,
        "user_id": user.user.id,
        "email": email
    }

    response = supabase.table("teachers").insert(data).execute()
    return response.data


def teacher_login(email, password):

    user = supabase.auth.sign_in_with_password({
        "email": email,
        "password": password
    })

    if user.session is None:
        return None

    # attach JWT
    supabase.postgrest.auth(user.session.access_token)

    # get ONLY this user's teacher row
    response = supabase.table("teachers") \
        .select("*") \
        .eq("user_id", user.user.id) \
        .execute()

    if response.data:
        return response.data[0]

    return None


def get_all_students():
    response = supabase.table('students').select("*").execute()
    return response.data

def create_student(new_name, face_embedding=None, voice_embedding=None):
    data = {
        'name': new_name,
        'face_embeddings': face_embedding,
        'voice_embeddings': voice_embedding
    }
    response = supabase.table('students').insert(data).execute()
    return response.data


def create_subject(subject_code, name, section, teacher_id):
    data = {"subject_code": subject_code, "name": name, "section": section, "teacher_id": teacher_id}
    response = supabase.table("subjects").insert(data).execute()
    return response.data

def get_teacher_subjects(teacher_id):
    response = supabase.table('subjects').select("*, subject_students(count), attendance_logs(timestamp)").eq("teacher_id", teacher_id).execute()
    subjects = response.data


    for sub in subjects:
        sub['total_students'] = sub.get("subject_students", [{}])[0].get('count', 0) if sub.get('subject_students') else 0
        attendance = sub.get('attendance_logs', [])
        unique_sessions = len(set(log['timestamp'] for log in attendance))
        sub['total_classes'] = unique_sessions


        sub.pop('subject_student', None)
        sub.pop('attendance_logs', None)

    return subjects


def  enroll_student_to_subject(student_id, subject_id):
    data = {'student_id': student_id, "subject_id": subject_id}
    response= supabase.table('subject_students').insert(data).execute()
    return response.data


def  unenroll_student_to_subject(student_id, subject_id):
    response= supabase.table('subject_students').delete().eq('student_id', student_id).eq('subject_id', subject_id).execute()
    return response.data



def get_student_subjects(student_id):
    response = supabase.table('subject_students').select('*, subjects(*)').eq('student_id', student_id).execute()
    return response.data


def get_student_attendance(student_id):
    response = supabase.table('attendance_logs').select('*, subjects(*)').eq('student_id', student_id).execute()
    return response.data


def create_attendance(logs):
    response = supabase.table('attendance_logs').insert(logs).execute()
    return response.data

def get_attendance_for_teacher(teacher_id):
    response = supabase.table('attendance_logs').select("*, subjects!inner(*)").eq('subjects.teacher_id', teacher_id).execute()
    return response.data

def get_attendance_with_students(teacher_id):
    response = supabase.table('attendance_logs').select("*, subjects!inner(*), students(name)").eq('subjects.teacher_id', teacher_id).execute()
    return response.data

def update_attendance(log_id, is_present):
    response = supabase.table('attendance_logs').update({'is_present': is_present}).eq('id', log_id).execute()
    return response.data
