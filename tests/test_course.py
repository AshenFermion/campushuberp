def test_course_crud(client):
    data={"course_code":"CS901","course_name":"Test Course","credits":3}
    assert client.post("/courses",json=data).status_code==201
    assert client.get("/courses/CS901").status_code==200
    assert client.put("/courses/CS901",json={"credits":4}).json()["credits"]==4
    assert client.delete("/courses/CS901").status_code==200
