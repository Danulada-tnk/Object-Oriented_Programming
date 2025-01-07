class student:
    def __init__(self,name,id,age,):
        self .name= name
        self .id= id
        self .age= age
        self .grade = {}
    def score (self):
        self .score['math'] = int(input('คะแนนคณิต: '))
        self .score['thai'] = int(input('คะแนนไทย: '))
        self .score['english'] = int(input('คะแนนอังกฤษ: '))
        self .score['science'] = int(input('คะแนนวิทย์: '))
        self .score['social'] = int(input('คะแนนสังคม: '))
        return self .grades
    def grade(self,grade):
        if grade >=80 :
            grade = 4
        elif grade >=70 :
            grade = 3
        elif grade >=60 :
            grade = 2
        elif grade >=50 :
            grade = 1
        else :
            grade = 0
            



        
