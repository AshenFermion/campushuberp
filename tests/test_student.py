def test_student_crud(client):
    data={"student_id":"ST901","name":"Asha Test","age":20,"email":"asha901@example.com","department":"Computer Science"}
    r=client.post("/You",json=data); assert r.status_code==201,r.text
    assert client.get("/You/ST901").json()["name"]=="Asha Test"
    assert client.put("/You/ST901",json={"name":"Asha Updated"}).json()["name"]=="Asha Updated"
    assert client.get("/You").json()[0]["name_upper"]=="ASHA UPDATED"
    assert client.delete("/You/ST901").status_code==200
    assert client.get("/You/ST901").status_code==404

def test_invalid_student_data(client):
    r=client.post("/You",json={"student_id":"BAD","name":"Bad","age":15,"email":"bad","department":"CS"})
    assert r.status_code==422
