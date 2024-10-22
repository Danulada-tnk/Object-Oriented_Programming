
name = input("กรุณาป้อนชื่อจริง: ")
print(name)
student_id = input("กรุณาป้อนรหัสประจำตัวนักศึกษา: ")
print(student_id)
year = input("กรุณาป้อนชั้นปี: ")
print(year)
nickname = input("กรุณาป้อนชื่อเล่น: ")
print(nickname)
height = float(input("กรุณาป้อนส่วนสูง (เมตร): "))
print(height)
weight = float(input("กรุณาป้อนน้ำหนัก (กิโลกรัม): "))
print(weight)
total = height + weight

print(f"ชื่อ: {name} | รหัส: {student_id}")
print(f"ชั้นปี: {year}")
print(f"ชื่อเล่น: {nickname}")
print(f"สูง: {height} เมตร | น้ำหนัก: {weight} กิโลกรัม")