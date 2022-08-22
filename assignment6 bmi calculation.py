#BMI

weight=int(input("ป้อนน้ำหนักของคุณ (kg) :"))
high=int(input("ป้อนส่วนสูงของคุณ (cm) :"))/100

bmi=(weight/(high**2))

result="ไม่ทราบค่าที่ชัดเจน"
if  bmi >=0 and bmi<18.5 :
    result="ต่ำกว่าเกณ"
elif bmi >=18.5 and bmi <=22.9:
    result="สมส่วน"
elif bmi >=23.0 and bmi <=24.9:
    result="น้ำหนักเกิน"
elif bmi >=25 and bmi <=29.9:
    result="โรคอ้วนระดับ1"
elif bmi >=30:
    result="อ้วนอันตราย"
print(result)