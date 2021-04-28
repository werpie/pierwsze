

lancuch_lista = list(lancuch)
nowy = []
for i in range(3):
    znak1=input("podaj jaki znak zamienic")
    znak2=input("na jaki go zamienic?")
    for litera in lancuch_lista:
        if litera==znak1:
            nowy+=znak2
        else:
            nowy+=litera
    nowy = "".join(nowy)
    print(nowy)
    lancuch_lista=nowy
    nowy=[]
