import random
class Student:
    def __init__(self,ชื่อ,นามสกุล,ชื่อเล่น):
        self.name=ชื่อ
        self.lastname = นามสกุล
        self.score = random.randint(1, 10)
        self.nickname = ชื่อเล่น
        self.score1 = random.randint(1, 10)
    def point(self):
        print(f"ชื่อ: {self.name}, นามสกุล: {self.lastname}, คะแนนสอบ: {self.score}", end="  ")
        if self.score >=5:
            print('สอบผ่าน')
        else :      
            print("สอบตก")
            if self.score1 <5:
                print("สอบไม่ผ่าน")
            else :
                print("สอบผ่าน")
student1 = Student("หนึ่งตะวัน","แสงสูงเนิน","กล้า")
student2 = Student("ฉัตรเฉลิม","ยิ่งดำนุ่น","ตุ้ย")
student3 = Student("ชิติพัทธ์","โสขะรัตน์","ไนท")
student4 = Student("เตชิน","ศรีพุฒ","ไปรท์")
student5 = Student("ปิติพงค์","ภูมิพงค์","ปอน")

student1.point()
student2.point()
student3.point()
student4.point()
student5.point()
