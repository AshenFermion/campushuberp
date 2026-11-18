def make_id_generator(prefix):
    counter=0
    def generate():
        nonlocal counter; counter+=1; return f"{prefix}{counter:03d}"
    return generate
student_ids=make_id_generator("ST"); faculty_ids=make_id_generator("FC"); course_ids=make_id_generator("CS"); enrollment_ids=make_id_generator("EN")
