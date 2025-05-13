def multiplicar(a, b):
    try:
        return a * b
    except Exception as e:
        return f"Erro ao multiplicar: {e}"

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: divisão por zero."
    except Exception as e:
        return f"Erro ao dividir: {e}"
