class employee:
    def __init__(self,ชื่อ,อาชีพ,เงินเดือน):
        self .name= ชื่อ
        self .jod= อาชีพ
        self .monthly= เงินเดือน
    
    def salary(self):
        return self.monthly * 12
    
employee1 = employee("โซเฟีย","ครู",12000)
employee2 = employee("ปีเตอร์","หมอ",45000)    
employee3 = employee("บ็อบ","โปรแกรมเมอร์",40000)

print(employee1.name,'ประกอบอาชีพ',employee1.jod,'มีเงินเดือนทั้งปี = ',employee1.salary() )
print(employee2.name,'ประกอบอาชีพ',employee2.jod,'มีเงินเดือนทั้งปี = ',employee2.salary() )
print(employee3.name,'ประกอบอาชีพ',employee3.jod,'มีเงินเดือนทั้งปี = ',employee3.salary() )

