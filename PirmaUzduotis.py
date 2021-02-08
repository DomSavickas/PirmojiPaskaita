# Pirma uzduotis
import datetime
class first:
    def get_input(self):
        try:
            name = input("Įveskite vardą:")
            lastname = input("Įveskite pavardę:")
            user_age = input("Įveskite amžių:")
            self.calculate_years(int(user_age))
            self.output_information(name, lastname, user_age)
        except:
            print('Bandykite iš naujo!')

    def output_calculation(self, calculation):
        try:
            print('Metai bus: '+calculation+', kai jums bus 100 metų')
        except:
            print('Bandykite iš naujo!')

    def output_information(self, name, lastname, user_age):
        try:
            print('Sveikiname: '+name+' '+lastname+' jums yra: '+user_age)
        except:
            print('Bandykite iš naujo!')

    def calculate_years(self, user_age):
        try:
            years_until_100=100-user_age
            current_date=datetime.datetime.now()
            current_year=current_date.year
            calculation=current_year+years_until_100
            self.output_calculation(str(calculation))
        except:
            print('Bandykite iš naujo!')
fi=first()
fi.get_input()
