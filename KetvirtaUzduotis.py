# Ketvirta uzduotis
class fourth:
    def get_input(self):
        try:
            name = input("Įveskite ieškomą vardą:")
            self.output_search(name)
        except:
            print('Bandykite iš naujo!')

    def output_search(self, name):
        try:
            name_profession_dictionary={
                "John": "Singer",
                "Robert": "Cosmonaut",
                "Jessica": "Actress"
            }
            if name in name_profession_dictionary:
                print('Profession found: '+name_profession_dictionary[name])
            else:
                print("Profession not found")
        except:
            print('Bandykite iš naujo!')

fo=fourth()
fo.get_input()