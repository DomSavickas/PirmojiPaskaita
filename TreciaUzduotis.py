# Trecia uzduotis
class trecia:
    def get_input(self):
        try:
            char_list=[]
            max_length=5
            while len(char_list)<max_length:
                char = input("Įveskite simbolį, raidę ar skaičių:")
                char_list.append(char)
            print('Pirmi trys simboliai: '+char_list[0]+' '+char_list[1]+' '+char_list[2])
            print('Paskutiniai du simboliai: '+char_list[3]+' '+char_list[4])
            print('Sąrašas nuo galo: '+str(char_list[::-1]))
        except:
            print('Bandykite iš naujo')

t=trecia()
t.get_input()