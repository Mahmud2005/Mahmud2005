from tkinter.font import families


class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
    
    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism
    
    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya
    
    def get_fullname(self):
        """Talabaning ism-familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"
    
    def get_age(self,yil):
        """Talabaning yoshini qaytaradi"""
        return yil-self.tyil
    
    def tanishtir(self):
        print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")
talaba1 = Talaba("Mahmud","Tursunboyev",2005)
print(talaba1.get_lastname())
print(talaba1.tanishtir())
print(talaba1.__dict__)
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

print(see_methods(Talaba))
print(talaba1.__dict__)
class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
      
    def set_bosqich(self,bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = bosqich
        
    def update_bosqich(self):
        """Talabanining bosqichini 1taga ko'paytirish"""
        self.bosqich += 1    
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism
    
    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya
    
    def get_fullname(self):
        """Talabaning ism-familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"
    
    def get_age(self,yil):
        """Talabaning yoshini qaytaradi"""
        return yil-self.tyil
#talaba1 = Talaba()
#print(talaba1.get_age(2005)) 
#print(type(talaba1))
#




def son(*sonlar,**raqamalari):
    print(sonlar)
son(1,2,3,4,one=5,two=6)
