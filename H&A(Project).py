print("-------Welcome to H&A Health Managemnt System-------")

class Parent:
    def __init__(self):
        pass
    def Get_Dataone(self,name,fmnumber):
        self.name = input("What is your name? ")
        print(self.name)
        self.fmnumber = int(input("Enter your FAmily-Member-Number(fmnumber): "))
        print(self.fmnumber)
    
    def Display_Dataone(self,name,fmnumber):
        return(self.name,self.fmnumber)
class Children:
    def __init__(self):
        pass
        
    def Get_Datatwo(self,height,weight,Age,Exercise):
        self.height = int(input("Enter Your Height in(cm): "))
        print(self.height)
        self.weight = int(input("Enter Your Weight(kg): "))
        print(self.weight)
        self.Age = int(input("Enter Your Age: "))
        print(self.Age)
        self.Exercise = input("Have you done Exercise today?(Yes/No) ")
        print(self.Exercise)
    
    def Display_Datatwo(self,height,weight,Age,Exercise):
        return(self.height,self.weight,self.Age,self.Exercise)
class Doctor(Parent,Children):
    pass

d = Doctor()#multiple inheritance
d.Get_Dataone("heta",1)
d.Get_Datatwo(161,54,82/140,131)

f = open("person.txt","rt")
content = f.read()
print(content)
f.close()

print("------Thank You To Test Our Software.--------")