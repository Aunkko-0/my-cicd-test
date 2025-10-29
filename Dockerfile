# 1. เลือก Base Image (Python 3.10 แบบเบาๆ)
FROM python:3.10-slim

# 2. ตั้งค่าโฟลเดอร์ทำงานใน Container
WORKDIR /app

# 3. Copy "รายการส่วนผสม" เข้าไปก่อน
COPY requirements.txt requirements.txt

# 4. ติดตั้ง "ส่วนผสม" (Flask)
RUN pip install -r requirements.txt

# 5. Copy โค้ดทั้งหมดที่เหลือเข้าไป
COPY . .

# 6. บอก Docker ว่าแอปเราจะรันที่ Port 5000
EXPOSE 5000

# 7. คำสั่งที่ใช้ "Run" แอป (เมื่อ Container เริ่มทำงาน)
CMD ["python", "app.py"]