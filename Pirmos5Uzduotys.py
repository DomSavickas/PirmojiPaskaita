# Pirma uzduotis
import datetime
class pirma:
    def get_input(self):
        name = input("Įveskite vardą:")
        lastname = input("Įveskite pavardę:")
        user_age = input("Įveskite amžių:")
        self.calculate_years(user_age)
        self.output_information(name, lastname, user_age)

    def output_calculation(self, calculation):
        print('Metai bus: '+calculation+', kai jums bus 100 metų')

    def output_information(self, name, lastname, user_age):
        print('Sveikiname: '+name+' '+lastname+' jums yra: '+user_age)

    def calculate_years(self, user_age):
        years_until_100=100-user_age
        current_date=datetime.datetime.current_date()
        current_year=current_date.year
        calculation=current_year+years_until_100
        self.output(calculation)
p=pirma()
p.get_input()
