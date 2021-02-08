# Penkta uzduotis
class fifth:
    def get_input(self):
        try:
            number_list = []
            max_length = 5
            while len(number_list) < max_length:
                while True:
                    try:
                        number = int(input("Įveskite skaičių:"))
                        number_list.append(number)
                        break
                    except ValueError:
                        print('Veskite, tik skaičius!')
                        continue
            number_list.sort()
            print('Sąrašas didėjančia tvarka: ' + str(number_list))
        except:
            print('Bandykite iš naujo!')

f=fifth()
f.get_input()