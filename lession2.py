class Dog:
    leg = 4
    sound = "Gâu gâu"
    
    def __init__(self, fur, face, name):
        self.fur = fur
        self.face = face
        self.name = name
                
    def show_info(self):
        print(f"Chó tên {self.name}")
        print(f"Chó có {self.leg} chân")
        print(f"Chó có bộ lông {self.fur}")
        print(f"Chó có khuôn mặt {self.face}")
        print(f"Chó kêu {self.sound}")
     
    @classmethod   
    def change_sound(cls):
        cls.sound = "meo meo"
        return cls.sound
    
    @staticmethod
    def favorite_food():
        return "Pate"
        
        
    
poodle = Dog("Xoăn", "Tròn", 'Poodle')
print(Dog.change_sound())
print(poodle.sound)
print(Dog.favorite_food())