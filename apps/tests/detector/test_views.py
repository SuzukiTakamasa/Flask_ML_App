
def test_index(client):
    rv = client.get("/")
    assert "Login" in rv.data.decode()
    assert "Image Register" in rv.data.decode()

def signup(client, username, email, password):
    """Sign up"""
    data = dict(username=username, email=email, password=password)
    return client.post("/auth/signup", data=data, follow_redirects=True) #Redirect after post a request

def test_index_signup(client):
    """Execute sign up"""
    rv = signup(client, "admin", "flaskapp@example.com", "password")
    assert "admin" in rv.data.decode()

    rv = client.get("/")
    assert "Logout" in rv.data.decode()
    assert "Image Register" in rv.data.decode()