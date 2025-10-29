# test_app.py
from app import add

def test_add():
    assert add(2, 3) == 5
    assert add(10, 10) == 20
    
# เราจงใจใส่ Bug ใน Test นี้เพื่อให้เห็นว่า CI "Fail" ได้
def test_add_fail():
    assert add(1, 1) == 3 # นี่คือ Test ที่จะ "พัง"