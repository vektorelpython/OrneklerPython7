class EvcilHayvan():
    ismi = ""
    tuy = ""
    cins=""
    goz = ""
    def beslenme():
        print("Beslendi")


class Kedi(EvcilHayvan):
    def beslenme():
        print("Kedi Mamasıyla Beslendi")
    def miyavla():
        print("Miyavladı")



class Kopek(EvcilHayvan):
    def Havlama():
        print("Havladı")
