def test_enrollment_lifecycle(client):
    assert client.post("/You",json={"student_id":"ST911","name":"Enrolled Student","age":21,"email":"enrolled911@example.com","department":"CS"}).status_code==201
    assert client.post("/courses",json={"course_code":"CS911","course_name":"Test Course","credits":3}).status_code==201
    r=client.post("/enrollments",json={"enrollment_id":"EN911","student_id":"ST911","course_code":"CS911"})
    assert r.status_code==201,r.text
    assert len(client.get("/enrollments").json())==1
    assert client.delete("/enrollments/EN911").status_code==200

def test_invalid_enrollment_reference(client):
    r=client.post("/enrollments",json={"enrollment_id":"EN912","student_id":"ST999","course_code":"CS999"})
    assert r.status_code==404
