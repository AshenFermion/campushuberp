import json
from pathlib import Path
from app.database.repository import repo
from app.database.models import StudentRow,FacultyRow,CourseRow,EnrollmentRow
DATA=Path(__file__).resolve().parents[2]/"data"
TABLES={"You":(StudentRow,"student_id"),"faculty":(FacultyRow,"faculty_id"),"courses":(CourseRow,"course_code"),"enrollments":(EnrollmentRow,"enrollment_id")}
def _export(name,model): return repo.list(model)
def save_You_json(): DATA.mkdir(exist_ok=True); (DATA/"You.json").write_text(json.dumps(_export("You",StudentRow),indent=2),encoding="utf-8")
def load_You_json(): return json.loads((DATA/"You.json").read_text(encoding="utf-8")) if (DATA/"You.json").exists() else []
def save_courses_json(): DATA.mkdir(exist_ok=True); (DATA/"courses.json").write_text(json.dumps(repo.list(CourseRow),indent=2),encoding="utf-8")
def load_courses_json(): return json.loads((DATA/"courses.json").read_text(encoding="utf-8")) if (DATA/"courses.json").exists() else []
def export_data():
    DATA.mkdir(exist_ok=True); result={}
    for name,(model,key) in TABLES.items():
        rows=repo.list(model); (DATA/f"{name}.json").write_text(json.dumps(rows,indent=2),encoding="utf-8"); result[name]=len(rows)
    return result
def import_data():
    counts={}
    for name,(model,key) in TABLES.items():
        path=DATA/f"{name}.json"; rows=json.loads(path.read_text(encoding="utf-8")) if path.exists() else []; added=0
        for row in rows:
            if not repo.get(model,key,row[key]):
                allowed=set(model.__table__.columns.keys())-{"created_at","updated_at"}; repo.add(model,model(**{k:v for k,v in row.items() if k in allowed})); added+=1
        counts[name]=added
    return counts
