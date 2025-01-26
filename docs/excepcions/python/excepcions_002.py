def suma(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Errada en els paràmetres")
    return a + b

try:
    x = input("Entra un número -> ")
    y = input("Entra un número -> ")
    print(f"{x} + {y} = {suma(x, y)}")
except Exception:
    print("S'ha produit un error")