class Salary:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus
    def annual(self):
        return (self.pay*12)+self.bonus

class employee:
    def __init__(self,name,age,pay,bonus):
        self.name=name
        self.age=age
        self.pay=pay
        self.bonus=bonus
        self.obj_salary=Salary(pay,bonus)
    
    def total_salary(self):
        return self.obj_salary.annual()

emp=employee('ajay',12,1,1)

print(emp.total_salary())