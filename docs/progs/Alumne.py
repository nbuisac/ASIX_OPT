class Alumne:
    __id_maxim = 0
    def __init__(self, nom, edat):
        Alumne.__id_maxim += 1
        self.__edat = edat
        self.__nom = nom
        self.__id = Alumne.__id_maxim
    @classmethod
    def get_quants(cls):
        return cls.__id_maxim       # pg 44
    def __eq__(self, altre):
        return self.__edat == altre.edat
    def __lt__(self, altre):
        return self.__edat < altre.edat
    def __gt__(self, altre):
        return self.__edat > altre.edat
    def assigna_carrec(self, carrec):
        self.carrec = carrec
    @property
    def edat(self):
        return self.__edat
    @edat.setter
    def edat(self, nova_edat):
        if isinstance(nova_edat, int):
            if nova_edat >= 0 and nova_edat <= 125:
                self.__edat = nova_edat
            else:
                raise(ValueError("ERROR: edat impossible, cal que estigui entre 0 i 125"))
        else:
            raise(TypeError("ERROR: l'edat ha de ser un enter entre 0 i 125"))

print(Alumne.get_quants())
a1 = Alumne("Joan", 18)
a2 = Alumne("Maria", 19)
a3 = Alumne("Abril", 19)
print(Alumne.get_quants())
print(a1 > a2)
print(a1 < a2)
print(a1 == a2)
a1.edat = a1.edat + 1
print(a2 > a3)
print(a2 < a3)
print(a2 == a3)
