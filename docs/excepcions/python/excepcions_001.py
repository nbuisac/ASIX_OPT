try:
    a = float(input("Entra el primer numerador -> "))
    b = float(input("Entra el primer denominador -> "))
    c = a / b
    print(f"{a} / {b} = {c}")
except ValueError: ## quan a/b no es pot convertir a float
    print("ERROR: El valor ha de ser numèric")
except ZeroDivisionError: ## quan dividim per zero
    print("ERROR: El denominador no pot ser zero")
except TypeError: ## Aquest no es dona aquí. Es donaria en concatenar un string i un número enter: "hola" + 23
    print("ERROR: Tipus de dada incompatible amb la operació")
except Exception: ## qualsevol tipus d'error
    print("ERROR: Consulta l'administrador")
else: ## si no es produeix cap excepció
    print("Programa Finalitzat correctament")
finally: ## S'executa SEMPRE
    print("Fins una altra")