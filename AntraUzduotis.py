# Antra uzduotis
class antra:
    def get_input(self):
        try:
            number = input("Įveskite numerį:")
            self.output_calculation(int(number))
        except:
            print('Bandykite iš naujo')


    def output_calculation(self, number):
        try:
            even_odd=["lyginis", "nelyginis"]
            print('Jūsų skaičius yra: '+str(number)+' ir jis yra: '+even_odd[number % 2])
        except:
            print('Bandykite iš naujo')

a=antra()
a.get_input()
