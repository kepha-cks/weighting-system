from flask import Flask, render_template, request, redirect, url_for, flash, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import json
import logic
import io
import csv
from openpyxl import Workbook

# PDF Imports
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hclv-careernet-secure-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hclv.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# --- DATABASE MODELS ---
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    role = db.Column(db.String(20))

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    gender = db.Column(db.String(1))
    combination = db.Column(db.String(10))
    o_level_json = db.Column(db.Text)
    a_level_json = db.Column(db.Text)
    subsidiaries = db.Column(db.Integer, default=0)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

# --- CUSTOM DECORATORS ---
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'Administrator':
            flash('Admin privileges required to access this page.')
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    return decorated_function

# --- HELPER FUNCTION FOR ELIGIBILITY ---
def get_eligible_students_data(course_code):
    """
    Calculates eligibility for all students for a specific course.
    Returns the course object and a list of eligible student data with dynamic statuses.
    """
    course = next((c for c in logic.COURSE_DATABASE if c['code'] == course_code), None)
    if not course:
        return None, None

    students = Student.query.all()
    eligible_data = []

    for s in students:
        s_data = {
            'a_levels': json.loads(s.a_level_json) if s.a_level_json else {},
            'o_levels': json.loads(s.o_level_json) if s.o_level_json else {},
            'gender': s.gender,
            'subs': s.subsidiaries
        }
        
        # 1. Check if student meets essential subject requirements
        # compute_weight_for_course returns 0 if essential subjects are missing/failed
        a_level_weight = logic.compute_weight_for_course(s_data['a_levels'], course, s.gender, s.subsidiaries)
        
        if a_level_weight == 0:
            # Student did not meet essential subject criteria, skip them for this report
            continue

        # 2. Calculate Total Weight
        o_bonus = logic.calculate_olevel_bonus(s_data['o_levels'])
        total_weight = a_level_weight + o_bonus
        cutoff = course['cutoffs'].get(s.gender)
        
        # 3. Determine Status Dynamically (Matching logic.py logic)
        status = "Not Qualified"
        gap = 0
        
        if cutoff is not None:
            if total_weight >= cutoff:
                status = "Qualified"
            else:
                gap = round(cutoff - total_weight, 1)
                # Check for Borderline status (within 2.0 points)
                if gap <= 2.0:
                    status = "Borderline"
        else:
            status = "N/A"

        eligible_data.append({
            'name': s.name,
            'gender': s.gender,
            'combination': s.combination,
            'o_bonus': o_bonus,
            'total_weight': total_weight,
            'cutoff': cutoff,
            'status': status,
            'gap': gap
        })
            
    return course, eligible_data

# --- ROUTES ---

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password')
            
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    students = Student.query.all()
    # Pass courses to template for the search feature
    return render_template('dashboard.html', students=students, user=current_user, courses=logic.COURSE_DATABASE)

# --- CSV EXPORT ROUTE ---
@app.route('/export/course/<course_code>')
@login_required
def export_course_students(course_code):
    course, eligible_data = get_eligible_students_data(course_code)
    if not course:
        flash("Course not found.")
        return redirect(url_for('dashboard'))

    output = io.StringIO()
    writer = csv.writer(output)
    
    writer.writerow(['Name', 'Gender', 'Combination', 'O-Level Bonus', 'Total Weight', 'Cutoff', 'Gap', 'Status'])
    
    for row in eligible_data:
        writer.writerow([
            row['name'], row['gender'], row['combination'], row['o_bonus'], 
            row['total_weight'], row['cutoff'], row['gap'], row['status']
        ])

    output.seek(0)
    response = make_response(output.getvalue())
    response.headers['Content-Disposition'] = f'attachment; filename={course_code}_eligible_students.csv'
    response.headers['Content-type'] = 'text/csv'
    return response

# --- PDF EXPORT ROUTE ---
@app.route('/export/course/<course_code>/pdf')
@login_required
def export_course_pdf(course_code):
    course, eligible_data = get_eligible_students_data(course_code)
    if not course:
        flash("Course not found.")
        return redirect(url_for('dashboard'))

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize='letter')
    styles = getSampleStyleSheet()
    elements = []

    # Title
    elements.append(Paragraph(f"HCLV CareerNet - Eligibility Report", styles['Title']))
    elements.append(Paragraph(f"Course: {course['name']} ({course_code})", styles['Heading2']))
    elements.append(Spacer(1, 0.2 * inch))

    # Table Data
    table_data = [['Name', 'Gender', 'Comb', 'Weight', 'Cutoff', 'Gap', 'Status']]
    
    for row in eligible_data:
        table_data.append([
            Paragraph(row['name'], styles['Normal']),
            row['gender'],
            row['combination'],
            str(row['total_weight']),
            str(row['cutoff']) if row['cutoff'] else 'N/A',
            str(row['gap']),
            row['status']
        ])

    # Create Table
    table = Table(table_data, colWidths=[2.5*inch, 0.5*inch, 0.7*inch, 0.6*inch, 0.6*inch, 0.5*inch, 1*inch])
    
    # Table Style
    style_commands = [
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#002147')), # Header Blue
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#D4AF37')),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'), # Left align names
    ]
    
    # Dynamic Row Styling based on Status
    for i, row in enumerate(eligible_data):
        row_index = i + 1 # +1 because header is row 0
        if row['status'] == "Qualified":
            style_commands.append(('BACKGROUND', (0, row_index), (-1, row_index), colors.HexColor('#d4edda'))) # Light Green
            style_commands.append(('TEXTCOLOR', (0, row_index), (-1, row_index), colors.HexColor('#155724')))
        elif row['status'] == "Borderline":
            style_commands.append(('BACKGROUND', (0, row_index), (-1, row_index), colors.HexColor('#fff3cd'))) # Light Yellow/Orange
            style_commands.append(('TEXTCOLOR', (0, row_index), (-1, row_index), colors.HexColor('#856404')))
        else: # Not Qualified
            style_commands.append(('BACKGROUND', (0, row_index), (-1, row_index), colors.HexColor('#f8d7da'))) # Light Red
            style_commands.append(('TEXTCOLOR', (0, row_index), (-1, row_index), colors.HexColor('#721c24')))

    table.setStyle(TableStyle(style_commands))
    elements.append(table)

    doc.build(elements)
    buffer.seek(0)

    response = make_response(buffer.getvalue())
    response.headers['Content-Disposition'] = f'attachment; filename={course_code}_eligibility_report.pdf'
    response.headers['Content-type'] = 'application/pdf'
    return response

# --- NEW ROUTE: ADD TEACHER ---
@app.route('/admin/add_teacher', methods=['GET', 'POST'])
@login_required
@admin_required
def add_teacher():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists.')
            return redirect(url_for('add_teacher'))
            
        hashed_pw = generate_password_hash(password, method='scrypt')
        new_teacher = User(username=username, password=hashed_pw, role='Teacher')
        db.session.add(new_teacher)
        db.session.commit()
        flash(f'Teacher account "{username}" created successfully!')
        return redirect(url_for('dashboard'))
        
    return render_template('add_teacher.html')

@app.route('/student/add', methods=['GET', 'POST'])
@login_required
def add_student():
    if request.method == 'POST':
        name = request.form.get('name')
        gender = request.form.get('gender')
        combination = request.form.get('combination')
        subs = int(request.form.get('subsidiaries', 0))
        
        # Collect O-Levels
        o_subs = request.form.getlist('o_sub')
        o_grades = request.form.getlist('o_grade')
        # Filter out empty entries
        o_data = {o_subs[i]: o_grades[i] for i in range(len(o_subs)) if o_subs[i] and o_grades[i]}
        
        # VALIDATION: O-Level is mandatory
        if not o_data:
            flash('Error: At least one O-Level subject and grade is required.', 'error')
            return redirect(url_for('add_student'))
        
        # Collect A-Levels (Optional)
        a_subs = request.form.getlist('a_sub')
        a_grades = request.form.getlist('a_grade')
        a_data = {a_subs[i]: a_grades[i] for i in range(len(a_subs)) if a_subs[i] and a_grades[i]}

        student = Student(
            name=name, gender=gender, combination=combination,
            o_level_json=json.dumps(o_data), 
            a_level_json=json.dumps(a_data),
            subsidiaries=subs
        )
        db.session.add(student)
        db.session.commit()
        flash('Student added successfully!')
        return redirect(url_for('dashboard'))
        
    return render_template('add_student.html')

@app.route('/analyze/<int:student_id>')
@login_required
def analyze(student_id):
    student = db.session.get(Student, student_id)
    
    # Prepare Data for Logic Engine
    s_data = {
        'a_levels': json.loads(student.a_level_json),
        'o_levels': json.loads(student.o_level_json),
        'gender': student.gender,
        'subs': student.subsidiaries
    }
    
    # Run Engine
    report, o_bonus = logic.get_student_report(s_data)
    
    return render_template('analysis.html', 
                           student=student, 
                           report=report, 
                           o_bonus=o_bonus)

@app.route('/predict/<int:student_id>/<course_code>')
@login_required
def predict(student_id, course_code):
    student = db.session.get(Student, student_id)
    s_data = {
        'a_levels': json.loads(student.a_level_json),
        'o_levels': json.loads(student.o_level_json),
        'gender': student.gender,
        'subs': student.subsidiaries
    }
    
    # Get Report for context
    report, o_bonus = logic.get_student_report(s_data)
    prediction = logic.predict_requirements(s_data, course_code)
    
    return render_template('analysis.html', 
                           student=student, 
                           report=report, 
                           o_bonus=o_bonus, 
                           prediction=prediction, 
                           active_course=course_code)

@app.route('/export/<int:student_id>')
@login_required
def export_report(student_id):
    student = db.session.get(Student, student_id)
    s_data = {
        'a_levels': json.loads(student.a_level_json),
        'o_levels': json.loads(student.o_level_json),
        'gender': student.gender,
        'subs': student.subsidiaries
    }
    report, o_bonus = logic.get_student_report(s_data)

    wb = Workbook()
    ws = wb.active
    ws.title = "Career Report"
    
    # Styling
    ws.append(['HCLV CareerNet - Holy Cross Lake View SSS'])
    ws.append(['Student Report'])
    ws.append([])
    ws.append(['Name:', student.name])
    ws.append(['Gender:', student.gender])
    ws.append(['Combination:', student.combination])
    ws.append(['O-Level Bonus:', o_bonus])
    ws.append([])
    ws.append(['Course', 'Code', 'Total Weight', 'Cutoff', 'Status'])
    
    for r in report:
        ws.append([r['course'], r['code'], r['weight'], r['cutoff'], r['status']])

    output = io.BytesIO()
    wb.save(output)
    output.seek(0)
    
    response = make_response(output.getvalue())
    response.headers['Content-Disposition'] = f'attachment; filename={student.name}_career_report.xlsx'
    response.headers['Content-type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    return response

@app.route('/student/edit/<int:student_id>', methods=['GET', 'POST'])
@login_required
def edit_student(student_id):
    student = db.session.get(Student, student_id)
    
    if request.method == 'POST':
        # Update basic info
        student.name = request.form.get('name')
        student.gender = request.form.get('gender')
        student.combination = request.form.get('combination')
        student.subsidiaries = int(request.form.get('subsidiaries', 0))
        
        # Update O-Levels
        o_subs = request.form.getlist('o_sub')
        o_grades = request.form.getlist('o_grade')
        student.o_level_json = json.dumps({o_subs[i]: o_grades[i] for i in range(len(o_subs)) if o_subs[i]})

        # Update A-Levels
        a_subs = request.form.getlist('a_sub')
        a_grades = request.form.getlist('a_grade')
        student.a_level_json = json.dumps({a_subs[i]: a_grades[i] for i in range(len(a_subs)) if a_subs[i]})
        
        db.session.commit()
        flash('Student record updated successfully!')
        return redirect(url_for('dashboard'))
        
    # For GET request, parse existing JSON for the form
    o_data = json.loads(student.o_level_json) if student.o_level_json else {}
    a_data = json.loads(student.a_level_json) if student.a_level_json else {}
    
    return render_template('edit_student.html', 
                           student=student, 
                           o_data=o_data, 
                           a_data=a_data)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

def create_initial_user():
    with app.app_context():
        db.create_all()
        admin_user = User.query.filter_by(username='admin').first()
        
        if not admin_user:
            hashed_pw = generate_password_hash('admin', method='scrypt')
            admin_user = User(username='admin', password=hashed_pw, role='Administrator')
            db.session.add(admin_user)
            db.session.commit()
            print("System initialized. Login: admin / admin")
        else:
            if admin_user.role != 'Administrator':
                admin_user.role = 'Administrator'
                db.session.commit()
                print("Updated 'admin' user role to Administrator.")

if __name__ == '__main__':
    create_initial_user()
    app.run(debug=True)