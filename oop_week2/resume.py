name = input("กรุณาป้อนชื่อจริง: ")
student_id = input("กรุณาป้อนรหัสประจำตัวนักศึกษา: ")
year = input("กรุณาป้อนชั้นปี: ")
nickname = input("กรุณาป้อนชื่อเล่น: ")
height = float(input("กรุณาป้อนส่วนสูง (เมตร): "))
weight = float(input("กรุณาป้อนน้ำหนัก (กิโลกรัม): "))
total = height + weight

print("ชื่อ" + name + "รหัส" + student_id)
print("ชั้นปี" + year) 
print("ชื่อเล่น" + nickname)
print("สูง"  + str (height) + "น้ำหนัก" + str (weight))