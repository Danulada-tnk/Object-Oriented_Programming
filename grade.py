print('โปรแกรมตัดเกรด')
score = int(input('กรอกคะแนนของคุณ : '))
if score < 0 or score > 100:
    print('ไม่ให้น้อยกว่า 0 และมากกว่า 100')
elif score >=80:
    print('คุณได้เกรด 4')
elif score >=70:
    print('คุณได้เกรด 3')
elif score >=60:
    print('คุณได้เกรด 2')
elif score >=50:
    print('คุณได้เกรด 1')
else:
    print('คุณได้เกรด 0')
    print('ต้องการแก้ หรือ ไม่แก้ ถ้าต้องการพิม 1 ไม่ต้องการพิม 2')
    c = int(input('กรอกตัวเลือก :'))
    if c == 1:
        score1 = 50 - score
        print(f'คุณขาดคะแนนอีก {score1}')
    elif c == 2:
        print('สอบตกเหมือนเดิม')
    else:
        print('กรุณาเลือก 1 และ 2')      