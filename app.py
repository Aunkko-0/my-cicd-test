# app.py
from flask import Flask

# --- นี่คือฟังก์ชันเดิมของเรา ---
def add(a, b):
    return a + b
# ------------------------------

app = Flask(__name__)

@app.route('/')
def hello():
    # ใช้ฟังก์ชัน add ของเรามาโชว์ผลลัพธ์
    result = add(2, 3)
    return f"Hello, DevOps Trainee! 2 + 3 = {result}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)