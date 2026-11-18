def test_faculty_crud(client):
    data={"faculty_id":"FC901","name":"Test Faculty","age":44,"email":"fc901@example.com","department":"Physics"}
    assert client.post("/faculty",json=data).status_code==201
    assert client.get("/faculty/FC901").status_code==200
    assert client.put("/faculty/FC901",json={"department":"Applied Physics"}).json()["department"]=="Applied Physics"
    assert client.delete("/faculty/FC901").status_code==200
