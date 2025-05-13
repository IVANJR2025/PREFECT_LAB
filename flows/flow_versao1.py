# flows/flow_versao1.py

from prefect import flow, task
from calculadora import operacoes

@task
def executar_operacoes():
    print("Soma: ", operacoes.somar(2, 3))
    print("Subtração: ", operacoes.subtrair(5, 2))

@flow(name="flow_versao1")
def flow_basico():
    executar_operacoes()

if __name__ == "__main__":
    flow_basico()
