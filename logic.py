
GRADE_POINTS = {'A': 6, 'B': 5, 'C': 4, 'D': 3, 'E': 2, 'O': 1, 'F': 0}
O_LEVEL_WEIGHTS = {
    '1': 0.3, '2': 0.3, 'A': 0.3, 'B': 0.3, 
    '3': 0.2, '4': 0.2, '5': 0.2, '6': 0.2, 'C': 0.2, 'D': 0.2,
    '7': 0.1, '8': 0.1, 'E': 0.1,
    '9': 0.0, 'F': 0.0
}

COURSE_DATABASE = [
    {
        "name": "Bachelor of Medicine and Surgery", "code": "MAM",
        "essential": ["Biology", "Chemistry"], "relevant": ["Math", "Physics"],
        "desirable": ["General Paper", "Sub-Maths"],
        "cutoffs": {"M": 43.9, "F": 39.8}
    },
    {
        "name": "Bachelor of Dental Surgery", "code": "BDS",
        "essential": ["Biology", "Chemistry"], "relevant": ["Physics", "Math"],
        "desirable": ["General Paper"],
        "cutoffs": {"M": 41.0, "F": 39.1}
    },
    {
        "name": "Bachelor of Science in Civil Engineering", "code": "CIV",
        "essential": ["Math", "Physics"], "relevant": ["Chemistry", "Economics", "Geography", "Technical Drawing"],
        "desirable": ["General Paper"],
        "cutoffs": {"M": 42.0, "F": 23.4}
    },
    {
        "name": "Bachelor of Laws", "code": "LAW",
        "essential": ["History", "Divinity", "Literature"], 
        "relevant": ["Economics", "Geography", "General Paper"],
        "desirable": ["Sub-Maths"],
        "cutoffs": {"M": 58.0, "F": 56.0}
    },
    {
        "name": "Bachelor of Science in Electrical Engineering", "code": "ELE",
        "essential": ["Math", "Physics"], "relevant": ["Chemistry", "Economics"],
        "desirable": ["General Paper"],
        "cutoffs": {"M": 39.7, "F": 30.3}
    },
    {
        "name": "Bachelor of Commerce", "code": "COE",
        "essential": ["Math", "Economics"], "relevant": ["Geography", "Physics", "Entrepreneurship"],
        "desirable": ["General Paper"],
        "cutoffs": {"M": 48.1, "F": 37.9}
    },
    {
        "name": "Bachelor of Science in Computer Science", "code": "CSC",
        "essential": ["Math"], 
        "relevant": ["Physics", "Economics", "Chemistry"],
        "desirable": ["General Paper"],
        "cutoffs": {"M": 40.4, "F": 28.7}
    },
    {
        "name": "Bachelor of Pharmacy",
        "code": "PHA",
        "essential": ["Biology", "Chemistry"],
        "relevant": ["Math", "Physics"],
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 42.0, "F": 39.3}
    },
    {
        "name": "Bachelor of Nursing Science",
        "code": "NUR",
        "essential": ["Biology", "Chemistry"],
        "relevant": ["Agriculture", "Economics", "Foods & Nutrition", "Maths", "Physics"],
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 40.6, "F": 38.9}
    },
    {
        "name": "Bachelor of Science in Medical Radiography",
        "code": "BMR",
        "essential": ["Biology", "Physics"],
        "relevant": ["A'Level Science Subjects"], # Best done science subject
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 38.4, "F": 34.0}
    },
    {
        "name": "Bachelor of Environmental Health Science",
        "code": "BEH",
        "essential": ["Biology", "Chemistry"],
        "relevant": ["Mathematics", "Physics", "Economics", "Geography", "Agriculture"],
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 36.5, "F": 36.9}
    },
    {
        "name": "Bachelor of Veterinary Medicine",
        "code": "VET",
        "essential": ["Biology", "Chemistry"],
        "relevant": ["Maths", "Physics", "Agriculture", "Food & Nutrition"],
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 38.6, "F": 25.6}
    },
    {
        "name": "Bachelor of Biomedical Laboratory Technology",
        "code": "MLT",
        "essential": ["Biology", "Chemistry"],
        "relevant": ["All A' Level Subjects"], # 3rd best done of all subjects
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 41.2, "F": 39.1}
    },
    {
        "name": "Bachelor of Science in Agriculture",
        "code": "AGR",
        "essential": ["Biology", "Chemistry", "Agriculture"], # Best 2 done
        "relevant": ["Biology", "Agriculture", "Physics", "Chemistry", "Maths", "Geography"], # Better done
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 23.2, "F": 19.6}
    },
    {
        "name": "Bachelor of Science in Food Science and Technology",
        "code": "FST",
        "essential": ["Biology", "Chemistry"],
        "relevant": ["Physics", "Agriculture", "Foods & Nutrition", "Maths"],
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 30.4, "F": 29.7}
    },
    {
        "name": "Bachelor of Science in Agricultural Engineering",
        "code": "AGE",
        "essential": ["Mathematics", "Physics"],
        "relevant": ["Chemistry", "Agriculture", "Economics", "Geom. & Mech. Drawing", "Geom. & Bld. Drawing"],
        "desirable": ["General Paper", "Computer Studies"],
        "cutoffs": {"M": 19.1, "F": 33.1} # Note: Text shows M lower than F
    },
    {
        "name": "Bachelor of Agribusiness Management",
        "code": "AGM",
        "essential": ["Mathematics", "Biology", "Chemistry", "Physics", "Agriculture", "Geography", "Economics"], # Best 2
        "relevant": ["Biology", "Chemistry", "Agriculture", "Geography", "Mathematics", "Physics", "Economics", "Entrepreneurship"],
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 40.3, "F": 27.5}
    },
    {
        "name": "Bachelor of Architecture",
        "code": "ARC",
        "essential": ["Mathematics", "Fine Art", "Geom. & Mech. Drawing", "Geom. & Bld. Drawing"], # Math & one better done
        "relevant": ["Economics", "Geography", "Physics", "Fine Art", "Geom. & Mech. Drawing", "Geom. & Bld. Drawing", "Entrepreneurship"],
        "desirable": ["General Paper", "Computer Studies"],
        "cutoffs": {"M": 42.5, "F": 36.6}
    },
    {
        "name": "Bachelor of Science in Land Surveying and Geomatics",
        "code": "LSG",
        "essential": ["Mathematics", "Physics"],
        "relevant": ["Economics", "Geography", "Chemistry", "Fine Art", "Entrepreneurship", "Geom. & Mech. Drawing", "Geom. & Bld. Drawing"],
        "desirable": ["General Paper", "Computer Studies"],
        "cutoffs": {"M": 39.3, "F": 27.4}
    },
    {
        "name": "Bachelor of Science in Mechanical Engineering",
        "code": "MEC",
        "essential": ["Mathematics", "Physics"],
        "relevant": ["Economics", "Chemistry", "Geom. & Mech. Drawing", "Geom. & Bld. Drawing", "Entrepreneurship"],
        "desirable": ["General Paper", "Computer Studies"],
        "cutoffs": {"M": 40.1, "F": 26.8}
    },
    {
        "name": "Bachelor of Science in Quantity Surveying",
        "code": "SQS",
        "essential": ["Mathematics", "Physics", "Economics", "Geography", "Fine Art", "Geom. & Mech. Draw", "Geom. & Bld. Drawing"], # Math & one better
        "relevant": ["Economics", "Geography", "Physics", "Chemistry", "Fine Art", "Geom. & Mech. Draw", "Geom. & Bld. Drawing", "Entrepreneurship"],
        "desirable": ["General Paper", "Computer Studies"],
        "cutoffs": {"M": 39.0, "F": 27.5}
    },
    {
        "name": "Bachelor of Statistics",
        "code": "STA",
        "essential": ["Maths"],
        "relevant": ["Economics", "Physics", "Chemistry", "Biology", "Geography", "Entrepreneurship"],
        "desirable": ["General Paper", "Computer Studies"],
        "cutoffs": {"M": 33.8, "F": 30.6}
    },
    {
        "name": "Bachelor of Science in Actuarial Science",
        "code": "SAS",
        "essential": ["Maths"],
        "relevant": ["Economics", "Physics", "Geography", "Chemistry", "Entrepreneurship"],
        "desirable": ["General Paper", "Computer Studies"],
        "cutoffs": {"M": 31.6, "F": 34.8}
    },
    {
        "name": "Bachelor of Arts in Economics",
        "code": "ECO",
        "essential": ["Economics"],
        "relevant": ["Mathematics", "Physics", "Geography", "Entrepreneurship", "History", "Agriculture"],
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 40.2, "F": 33.0}
    },
    {
        "name": "Bachelor of Science with Education (Biological)",
        "code": "EDB",
        "essential": ["Biology", "Chemistry"],
        "relevant": ["Physics", "Mathematics"],
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 32.7, "F": 23.7}
    },
    {
        "name": "Bachelor of Science with Education (Physical)",
        "code": "EDP",
        "essential": ["Mathematics", "Physics", "Chemistry"], # Math & one better
        "relevant": ["Physics", "Chemistry", "Biology", "Economics", "Geography"],
        "desirable": ["General Paper", "Computer Studies"],
        "cutoffs": {"M": 31.9, "F": 21.9}
    },
    {
        "name": "Bachelor of Science with Education (Economics)",
        "code": "EEC",
        "essential": ["Mathematics", "Economics"],
        "relevant": ["Chemistry", "Physics", "Biology", "Geography"],
        "desirable": ["Computer Studies", "General Paper"],
        "cutoffs": {"M": 24.7, "F": 21.7}
    },
    {
        "name": "Bachelor of Fine Art",
        "code": "BFA",
        "essential": ["Fine Art", "Geom. & Mech. Drawing", "Geom. & Bld. Drawing", "Music"],
        "relevant": ["Remaining A' Level Subjects"],
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": None, "F": 29.6} # Male cutoff missing in text
    },
    {
        "name": "Bachelor of Arts in Music",
        "code": "MUS",
        "essential": ["All A' Level subjects"], # Best 2
        "relevant": ["All A' Level subjects"], # 3rd best
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 46.4, "F": 37.3}
    },
    {
        "name": "Bachelor of Arts in Drama and Film",
        "code": "BDF",
        "essential": ["All A' Level Arts Subjects"], # Best 2
        "relevant": ["All A' Level subjects"], # 3rd best
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 47.3, "F": 40.2}
    },
    {
        "name": "Bachelor of Science (Biological)",
        "code": "SCB",
        "essential": ["Biology", "Chemistry"],
        "relevant": ["Math", "Physics"],
        "desirable": ["General Paper", "Computer Studies"],
        "cutoffs": {"M": 25.5, "F": 35.3}
    },
    {
        "name": "Bachelor of Science (Physical)",
        "code": "SCP",
        "essential": ["Mathematics", "Physics", "Chemistry"], # Math & one better
        "relevant": ["Chemistry", "Biology", "Physics", "Economics"],
        "desirable": ["General Paper", "Computer Studies"],
        "cutoffs": {"M": 23.9, "F": 28.6}
    },
    {
        "name": "Bachelor of Science (Economics)",
        "code": "SEC",
        "essential": ["Mathematics", "Economics"],
        "relevant": ["Chemistry", "Physics", "Biology"],
        "desirable": ["General Paper", "Computer Studies"],
        "cutoffs": {"M": 18.7, "F": 26.8}
    },
    {
        "name": "Bachelor of Science in Industrial Chemistry",
        "code": "BIC",
        "essential": ["Chemistry", "Maths", "Physics"], # Chem and Math or Phys
        "relevant": ["Biology", "Physics", "Mathematics"],
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 40.4, "F": 32.7}
    },
    {
        "name": "Bachelor of Science in Fisheries and Aquaculture",
        "code": "BFS",
        "essential": ["Chemistry", "Biology", "Agriculture"], # Best 2
        "relevant": ["Math", "Physics", "Biology", "Chemistry", "Agriculture"],
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 24.1, "F": 26.7}
    },
    {
        "name": "Bachelor of Sports Science",
        "code": "BSP",
        "essential": ["Biology", "Physics", "Chemistry", "Agriculture"], # Best 2
        "relevant": ["Economics", "Maths", "Physics", "Chemistry", "Biology", "Agriculture"],
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 29.0, "F": 23.5}
    },
    {
        "name": "Bachelor of Science in Conservation Biology",
        "code": "BCB",
        "essential": ["Biology", "Chemistry", "Agriculture"], # Best 2
        "relevant": ["Geography", "Biology", "Physics", "Chemistry", "Agriculture"],
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 22.7, "F": 26.9}
    },
    {
        "name": "Bachelor of Science in Software Engineering",
        "code": "BSW",
        "essential": ["Maths", "Physics", "Economics", "Geography", "Chemistry", "Biology"], # Math & one best
        "relevant": ["Physics", "Chemistry", "Economics", "Geography", "Biology"],
        "desirable": ["General Paper", "Computer Studies"],
        "cutoffs": {"M": 40.8, "F": 27.4}
    },
    {
        "name": "Bachelor of Science in Biomedical Engineering",
        "code": "BBI",
        "essential": ["Maths", "Physics", "Biology"], # Maths & one better
        "relevant": ["Physics", "Biology", "Chemistry", "Economics", "Geom. & Mech. Drawing", "Geom. & Bld. Drawing"],
        "desirable": ["General Paper", "Computer Studies"],
        "cutoffs": {"M": 42.9, "F": 32.5}
    },
    {
        "name": "Bachelor of Cytotechnology",
        "code": "BYT",
        "essential": ["Biology", "Chemistry"],
        "relevant": ["Physics", "Maths", "Economics", "Agriculture", "F/Nutrition"],
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 38.6, "F": 31.8}
    },
    {
        "name": "Bachelor of Agricultural and Rural Innovation",
        "code": "BAR",
        "essential": ["Biology", "Chemistry", "Geography", "Agriculture"], # Best 2
        "relevant": ["Chemistry", "Biology", "Physics", "Maths", "Economics", "Geography", "Foods & Nutrition", "Entrepreneurship", "Agriculture"],
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 41.2, "F": 31.1}
    },
    {
        "name": "Bachelor of Science in Human Nutrition",
        "code": "HUN",
        "essential": ["Biology", "Chemistry"],
        "relevant": ["Agriculture", "Foods & Nutrition", "Physics", "Maths", "Economics"],
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 31.9, "F": 31.8}
    },
    {
        "name": "Bachelor of Science in Petroleum Geoscience and Production",
        "code": "BPG",
        "essential": ["Chemistry", "Physics", "Mathematics"], # Best 2
        "relevant": ["Biology", "Chemistry", "Physics", "Maths", "Economics", "Geography"],
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 42.0, "F": 39.7}
    },
    {
        "name": "Bachelor of Business Administration",
        "code": "ADM",
        "essential": ["Economics", "Entrepreneurship"],
        "relevant": ["Remaining A'Level Subjects"],
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 46.0, "F": 40.4}
    },
    {
        "name": "Bachelor of Social Work",
        "code": "SOW",
        "essential": ["All A' Level Subjects"], # Best 2
        "relevant": ["All A' Level Subjects"], # 3rd best
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 48.7, "F": 43.7}
    },
    {
        "name": "Bachelor of Science in Speech and Language Therapy",
        "code": "BSL",
        "essential": ["Biology", "Chemistry"],
        "relevant": ["A'Level Science Subjects"],
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 29.3, "F": None} # Female cutoff missing/dash in text
    },
    {
        "name": "Bachelor of Optometry",
        "code": "BPT",
        "essential": ["Biology", "Physics", "Mathematics"], # Bio & either Phys or Math
        "relevant": ["Chemistry", "Physics", "Mathematics"],
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 42.2, "F": 36.9}
    },
    {
        "name": "Bachelor of Science in Forestry",
        "code": "BOF",
        "essential": ["Biology", "Chemistry", "Agriculture", "Physics", "Mathematics", "Geography"], # Best 2
        "relevant": ["Biology", "Chemistry", "Agriculture", "Physics", "Mathematics", "Geography", "Economics", "Entrepreneurship", "Technical Drawing", "Wood Work", "Metal Work"],
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 34.2, "F": 19.2}
    },
    {
        "name": "Bachelor of Information Systems and Technology",
        "code": "IST",
        "essential": ["Chemistry", "Physics", "Mathematics", "Economics", "Geography", "Entrepreneurship"], # Two better done
        "relevant": ["All A' level subjects"], # Any other best
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": 40.6, "F": 41.6}
    },
    {
        "name": "Bachelor of Science in Water and Irrigation Engineering",
        "code": "BWE",
        "essential": ["Maths", "Physics"],
        "relevant": ["Chemistry"],
        "desirable": ["General Paper", "Computer Studies"],
        "cutoffs": {"M": 31.1, "F": 32.6}
    },
    {
        "name": "Bachelor of Science in Quantitative Economics",
        "code": "BQE",
        "essential": ["Maths", "Economics"],
        "relevant": ["Physics", "Geography", "Entrepreneurship"],
        "desirable": ["General Paper", "Computer Studies"],
        "cutoffs": {"M": 27.9, "F": 27.9}
    },
    {
        "name": "Bachelor of Science in Population Studies",
        "code": "BPS",
        "essential": ["All A' Level subjects"], # Best 2
        "relevant": ["Remaining A' Level subjects"],
        "desirable": ["General Paper", "Sub-Maths", "Computer Studies"],
        "cutoffs": {"M": None, "F": 39.5} # Male cutoff missing/dash in text
    },
    {
        "name": "Bachelor of Science in Land Economics",
        "code": "SLE",
        "essential": ["Mathematics", "Economics", "Geography", "Physics", "Fine Art", "Geom. & Mech. Draw", "Geom. & Bld. Drawing"], # Math & one better
        "relevant": ["Economics", "Geography", "Physics", "Chemistry", "Fine Art", "Entrepreneurship", "Geom. & Mech. Draw", "Geom. & Bld. Drawing"],
        "desirable": ["General Paper", "Computer Studies"],
        "cutoffs": {"M": 36.3, "F": 31.3}
    }
]

def normalize_grade(grade):
    """Helper to convert lowercase grades to uppercase for logic."""
    return str(grade).upper().strip()

def calculate_olevel_bonus(grades_dict):
    """
    Calculates O-Level bonus based on UNEB criteria.
    Input: {'Math': '1', 'English': 'B'}
    Returns: Sum of best 10 subjects weights.
    """
    weights = []
    for sub, grade in grades_dict.items():
        g = normalize_grade(grade)
        w = O_LEVEL_WEIGHTS.get(g, 0.0)
        weights.append(w)
    
    weights.sort(reverse=True)
    top_10 = weights[:10]
    return round(sum(top_10), 1)

def compute_weight_for_course(student_a_levels, course, gender, subsidiaries_count):
    """
    Computes admission weight for a specific course.
    Returns: Total A-Level Weight (without O-Level bonus) or 0 if ineligible.
    """
    essential_subs = course['essential']
    student_essential_grades = []
    for sub in essential_subs:
        if sub in student_a_levels:
            student_essential_grades.append(GRADE_POINTS.get(normalize_grade(student_a_levels[sub]), 0))
    
    if len(student_essential_grades) < len(essential_subs):
        if len(essential_subs) == 2 and len(student_essential_grades) < 2:
            return 0
    student_essential_grades.sort(reverse=True)
    essential_pts = sum(student_essential_grades[:2])
    essential_weight = essential_pts * 3
    relevant_pts = 0
    for sub, grade in student_a_levels.items():
        if sub in course['relevant'] and sub not in essential_subs:
            pts = GRADE_POINTS.get(normalize_grade(grade), 0)
            if pts > relevant_pts:
                relevant_pts = pts
    
    relevant_weight = relevant_pts * 2
    desirable_pts = 0
    for sub, grade in student_a_levels.items():
        if sub in course['desirable'] and sub not in essential_subs:
            pts = GRADE_POINTS.get(normalize_grade(grade), 0)
            if pts > desirable_pts:
                desirable_pts = pts
    
    desirable_weight = desirable_pts * 1
    sub_bonus = subsidiaries_count * 1.0
    
    gender_bonus = 1.5 if gender == 'F' else 0.0

    total_alevel = essential_weight + relevant_weight + desirable_weight + sub_bonus + gender_bonus
    return total_alevel

def get_student_report(student_data):
    """
    Generates full eligibility report.
    student_data: { 'a_levels': {}, 'o_levels': {}, 'gender': 'M', 'subs': 1 }
    """
    o_bonus = calculate_olevel_bonus(student_data['o_levels'])
    report = []

    for course in COURSE_DATABASE:
        a_level_weight = compute_weight_for_course(
            student_data['a_levels'], 
            course, 
            student_data['gender'], 
            student_data['subs']
        )
        
        if a_level_weight == 0:
            continue 

        total_weight = a_level_weight + o_bonus
        cutoff = course.get('cutoffs', {}).get(student_data['gender'])
        if cutoff is None:
            cutoff = 40.0
        status = "Not Qualified"
        gap = 0
        
        if cutoff is not None and total_weight >= cutoff:
            status = "Qualified"
        else:
            gap = round(cutoff - total_weight, 1)
            if gap <= 2.0:
                status = "Borderline"

        report.append({
            "course": course['name'],
            "code": course['code'],
            "weight": total_weight,
            "cutoff": cutoff,
            "status": status,
            "gap": gap,
            "essential_subs": course['essential'] 
        })
    status_order = {"Qualified": 0, "Borderline": 1, "Not Qualified": 2}
    report.sort(key=lambda x: (status_order[x['status']], -x['weight']))
    
    return report, o_bonus
def predict_requirements(student_data, course_code):
    """
    Calculates what grades are needed to qualify for a specific course.
    """
    course = next((c for c in COURSE_DATABASE if c['code'] == course_code), None)
    if not course:
        return None

    o_bonus = calculate_olevel_bonus(student_data['o_levels'])
    current_a_level_weight = compute_weight_for_course(
        student_data['a_levels'], course, student_data['gender'], student_data['subs']
    )
    if current_a_level_weight == 0:
        missing = [s for s in course['essential'] if s not in student_data['a_levels']]
        return {
            "needed": f"Missing essential subjects: {', '.join(missing)}",
            "suggestions": ["This course requires specific subjects not currently offered by the student."],
            "gap": 0
        }

    total_weight = current_a_level_weight + o_bonus
    cutoff = course['cutoffs'].get(student_data['gender'])
    
    if cutoff is not None and total_weight >= cutoff:
        return {"needed": "Already Qualified", "suggestions": [], "gap": 0}

    gap = round(cutoff - total_weight, 1)
    suggestions = []
    for sub in course['essential']:
        if sub in student_data['a_levels']:
            current_grade = normalize_grade(student_data['a_levels'][sub])
            current_pts = GRADE_POINTS.get(current_grade, 0)
            if current_pts < 6: # Not an A
                gain = 3 
                if gain >= gap:
                    suggestions.append(f"Improve {sub} by 1 grade (e.g., {current_grade} → next grade).")
                else:
                    suggestions.append(f"Improve {sub} by multiple grades (needs +{gap} points).")

    return {
        "needed": f"Need {gap} more points to reach cutoff.",
        "suggestions": suggestions,
        "gap": gap
    }