"""
    Constroi uma funcao python que executa o calculo da formula de Bhaskara e retorna os valores de x' e x"
    para equacoes do tipo a(x^2) + b(x) + c = 0;
        - Entrada: 3 coeficientes a, b e c inteiros
    
    Modo de utilizacao:
        - Na funcao main, modifique os valores dos coeficientes a, b e c e ponha o script para execucao.
"""
__author__ = "Elias Cícero Moreira Guedes"
__date__ = "14 de Setembro de 2021"
__credits__ = ["Igor Souza, ministrante do curso 'Criando APIs em Python'"]


from math import sqrt
from typing import Tuple


def calculate_delta(a:int, b: int, c: int) -> int:
    """
        Calcula e retorna o valor do delta.
    """

    return (b**2) - (4*a*c)


def calculate_bhaskara(a: int, b: int, c: int) -> Tuple[float, float]:
    """
        Calcula e retorna o resultado da formula de bhaskara. 
    """

    assert isinstance(a, int), "o valor do coeficiente a nao eh inteiro"
    assert a != 0, "o valor do coeficiente a nao pode ser igual a 0"
    assert isinstance(b, int), "o valor do coeficiente b nao eh inteiro"
    assert isinstance(c, int), "o valor do coeficiente c nao eh inteiro"


    delta = calculate_delta(a=a, b=b, c=c)

    if delta < 0:
        print(f"A equacao nao possui raizes pertencentes ao conjunto dos numeros reais, pois delta = {round(delta, 2)} < 0")
        return
    
    x1 = ((-b) + (sqrt(delta))) / (2*a)
    x2 = ((-b) - (sqrt(delta))) / (2*a)

    print(f"As raizes da equacao {a}(x^2) {'+' if b > 0 else ''}{b}(x) {'+' if c > 0 else ''}{c} sao x1 = {round(x1, 2)} e x2 = {round(x2, 2)}")

    return x1, x2


if __name__ == "__main__":
    """
        Modifique os valores de a, b e c a sua escolha.
    """

    a = -1
    b = 6
    c = -9

    calculate_bhaskara(a=a, b=b, c=c)