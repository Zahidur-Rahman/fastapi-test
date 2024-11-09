def test_create_user(client):
    data={"email":"ping45@firstapitutorial.com","password":"supersecret"}
    response=client.post("/user/",json=data)
    assert response.status_code==201
    assert response.json()["email"]== "ping45@firstapitutorial.com"