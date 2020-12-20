import datetime

class Worker:
    def __init__(self, surname_initials, born_date, hiring_date, salary_amount):
        self.surname_initials = surname_initials
        self.born_date = datetime.datetime(*born_date)
        self.hiring_date = datetime.datetime(*hiring_date)
        self.salary_amount = salary_amount

    def experience(self):
        """calculation of experience"""
        exp = datetime.datetime.today() - self.hiring_date
        exp_hours = exp.total_seconds() // 3600
        exp_years = exp_hours // 8760
        exp_mounth = (exp_hours % 8760) // 730

        return (exp_years, exp_mounth)

    def age(self):
        """calculation of age"""
        age = datetime.datetime.today() - self.born_date
        age_hours = age.total_seconds() // 3600
        return age_hours // 8760

    def salary_sum(self):
        """calculation of salary amount"""
        years, month = self.experience()
        return ((years * 12) + month) * self.salary_amount