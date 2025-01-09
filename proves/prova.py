frase = input("Entra una frase -> ")
paraules = 0
## Estem indicant que l'anterior al primer no era lletra
#  per tal que compti la primera lletra com a inici de paraula
anterior_es_lletra = False
for lletra in frase:
    if lletra.isalpha():
        if not anterior_es_lletra:
            paraules += 1
            anterior_es_lletra = True
    else:
        anterior_es_lletra = False

print(f"\nLa frase té {paraules} paraules")