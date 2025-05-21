class Student:
    name = ""
    score = {}
    school = ""
    class_name = ""
    address = ""
    
    def score_average(self):
        list_score = self.score.values()
        
        return sum(list_score) / len(list_score)
    
    def show_rank(self):
        score_average = self.score_average()
        
        if score_average > 9:
            print("Xuat sac")
        elif score_average > 8:
            print("Gioi")
        elif score_average > 7:
            print("Kha")
        elif score_average > 5:
            print("Trung binh")
        else:
            print("Yeu")
    
    def show_info_student(self):
        print(f"Học sinh tên: {self.name}")
        print(f"Diem trung binh: {self.score_average()}")
        print("Xep loai: ", end= " ")
        print(f"Học sinh trường {self.school}")
        print(f"Lớp {self.class_name}")
        print(f"Dia chi {self.address}")
        self.show_rank()
        
    def find_highest_score_subject(self):
        highest_score = 0
        highest_subject = ""
        for subject, score in self.score.items():
            if score > highest_score:
                highest_score = score
                highest_subject = subject
        return highest_subject, highest_score


hs1 = Student()
hs1.name = "Nguyen Van A"
hs1.score = {"Toan": 9, "Ly": 8, "Hoa": 7}
hs1.school = "THPT Chuyen Ha Noi"
hs1.class_name = "12A1"
hs1.address = "Ha Noi"
hs1.show_info_student()

hs2 = Student()
hs2.name = "Nguyen Van B"
hs2.score = {"Toan": 4, "Ly": 5, "Hoa": 6}
hs2.show_info_student()

highest_subject, highest_score = hs1.find_highest_score_subject()
print(f"Môn học có điểm cao nhất: {highest_subject} với điểm số {highest_score}")
