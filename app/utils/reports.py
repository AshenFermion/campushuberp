from app.utils.generators import student_report,faculty_report,course_report
from app.utils.file_manager import ReportWriter
from concurrent.futures import ThreadPoolExecutor

def _write(filename,records):
    with ReportWriter(f"reports/{filename}") as f:
        for record in records: f.write(record+"\n")
    return filename

def generate_reports():
    jobs=[("You.txt",student_report()),("faculty.txt",faculty_report()),("courses.txt",course_report())]
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures=[pool.submit(_write,name,list(records)) for name,records in jobs]
        return [f.result() for f in futures]

class StudentIterator:
    def __init__(self,students): self._it=iter(students)
    def __iter__(self): return self
    def __next__(self): return next(self._it)
