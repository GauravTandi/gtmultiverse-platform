from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# dummy user (temporary)
USER_DB = {
    "test@example.com" : "1234"
}


class LoginRequest(BaseModel):
    email: str
    password: str

@app.post("/login")
def login(data: LoginRequest):
    # basic validation
    if not data.email or not data.password:
        return {"status": "error", "message": "Empty fields"}
    
    # check user
    if data.email in USER_DB and USER_DB[data.email] == data.password:
        print(f"Login success: {data.email}")
        return {"status":"success", "message": "Login successful"}
    else:
        print(f"Login failed: {data.email}")
        return {"status":"error", "message": "Invaild credentials"}