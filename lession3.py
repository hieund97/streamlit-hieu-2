class HinhTron:
    color = "red"
    
    def __init__(self, r=0):
        self.ban_kinh = r
        self.PI = 3.14
    
    @property
    def dien_tich(self):
        return self.PI * self.ban_kinh ** 2
    
    @dien_tich.setter
    def dien_tich(self, dien_tich_moi):
        self.ban_kinh = (dien_tich_moi / self.PI) ** 0.5
       
    @dien_tich.deleter 
    def dien_tich(self):
        self.ban_kinh = None
    
    
circle_1 = HinhTron(5)
print(circle_1.ban_kinh)
print(circle_1.dien_tich)

circle_1.dien_tich = 100

del circle_1.dien_tich

print(circle_1.ban_kinh)
print(circle_1.dien_tich)





