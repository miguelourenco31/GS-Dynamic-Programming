#!/usr/bin/env python3
"""
garagem_autonoma.py

Implementa quatro versões do Problema da Mochila 0/1,
aplicado ao contexto do projeto “Garagem Autônoma de Logística”.

Fases:
1. Estratégia Gulosa (Greedy)
2. Recursiva Pura
3. Recursiva com Memoização (Top-Down)
4. Programação Dinâmica Iterativa (Bottom-Up)
"""

from dataclasses import dataclass
from typing import List, Tuple, Dict


@dataclass
class Projeto:
    nome: str
    valor: int   # Benefício (equivalente ao "value" no knapsack)
    custo: int   # Custo ou tempo necessário (equivalente ao "peso"/"hours")


# ------------------------
# Fase 1 – Estratégia Gulosa
# ------------------------
def mochila_gulosa(projetos: List[Projeto], capacidade: int) -> Tuple[int, List[str]]:
    """
    Seleciona projetos priorizando a maior razão valor/custo.
    OBS: não garante o resultado ótimo.
    """
    projetos_ordenados = sorted(projetos, key=lambda p: p.valor / p.custo, reverse=True)
    restante = capacidade
    valor_total = 0
    escolhidos = []

    for p in projetos_ordenados:
        if p.custo <= restante:
            escolhidos.append(p.nome)
            valor_total += p.valor
            restante -= p.custo

    return valor_total, escolhidos


# ------------------------
# Fase 2 – Recursiva Pura
# ------------------------
def mochila_recursiva(projetos: List[Projeto], capacidade: int) -> Tuple[int, List[str]]:
    """
    Solução recursiva pura – testa todas as combinações possíveis.
    """
    n = len(projetos)

    def resolver(i: int, c: int) -> Tuple[int, List[str]]:
        if i < 0 or c <= 0:
            return 0, []

        projeto = projetos[i]
        valor_sem, itens_sem = resolver(i - 1, c)

        if projeto.custo > c:
            return valor_sem, itens_sem

        valor_com, itens_com = resolver(i - 1, c - projeto.custo)
        valor_com += projeto.valor
        itens_com = itens_com + [projeto.nome]

        if valor_com > valor_sem:
            return valor_com, itens_com
        else:
            return valor_sem, itens_sem

    return resolver(n - 1, capacidade)


# ------------------------
# Fase 3 – Recursiva com Memoização
# ------------------------
def mochila_memo(projetos: List[Projeto], capacidade: int) -> Tuple[int, List[str]]:
    """
    Versão recursiva otimizada com cache (memoização).
    """
    n = len(projetos)
    memo: Dict[Tuple[int, int], Tuple[int, List[str]]] = {}

    def resolver(i: int, c: int) -> Tuple[int, List[str]]:
        if i < 0 or c <= 0:
            return 0, []
        if (i, c) in memo:
            return memo[(i, c)]

        projeto = projetos[i]
        valor_sem, itens_sem = resolver(i - 1, c)

        if projeto.custo > c:
            memo[(i, c)] = (valor_sem, itens_sem)
            return memo[(i, c)]

        valor_com, itens_com = resolver(i - 1, c - projeto.custo)
        valor_com += projeto.valor
        itens_com = itens_com + [projeto.nome]

        if valor_com > valor_sem:
            memo[(i, c)] = (valor_com, itens_com)
        else:
            memo[(i, c)] = (valor_sem, itens_sem)

        return memo[(i, c)]

    return resolver(n - 1, capacidade)


# ------------------------
# Fase 4 – Programação Dinâmica Iterativa
# ------------------------
def mochila_pd(projetos: List[Projeto], capacidade: int) -> Tuple[int, List[str]]:
    """
    Solução iterativa usando tabela de programação dinâmica (Bottom-Up).
    """
    n = len(projetos)
    tabela = [[0] * (capacidade + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        projeto = projetos[i - 1]
        for c in range(capacidade + 1):
            if projeto.custo > c:
                tabela[i][c] = tabela[i - 1][c]
            else:
                tabela[i][c] = max(
                    tabela[i - 1][c],
                    projeto.valor + tabela[i - 1][c - projeto.custo],
                )

    # Reconstrução dos itens escolhidos
    valor_final = tabela[n][capacidade]
    itens_escolhidos = []
    c = capacidade

    for i in range(n, 0, -1):
        if tabela[i][c] != tabela[i - 1][c]:
            projeto = projetos[i - 1]
            itens_escolhidos.append(projeto.nome)
            c -= projeto.custo

    itens_escolhidos.reverse()
    return valor_final, itens_escolhidos


# ------------------------
# Casos de Teste
# ------------------------
def exemplo_enunciado():
    """
    Exemplo do enunciado original.
    """
    projetos = [
        Projeto("A", 12, 4),
        Projeto("B", 10, 3),
        Projeto("C", 7, 2),
        Projeto("D", 4, 3),
    ]
    capacidade = 10
    return projetos, capacidade


def exemplo_garagem_autonoma():
    """
    Caso temático – Garagem Autônoma de Logística.
    """
    projetos = [
        Projeto("Instalação de Painéis Solares", 50, 6),
        Projeto("Sistema de Baterias", 40, 5),
        Projeto("Braços Robóticos Autônomos", 45, 6),
        Projeto("Frota de Drones de Entrega", 35, 4),
        Projeto("Estação de Recarga Elétrica", 30, 3),
        Projeto("Painel Central de IA", 55, 5),
        Projeto("Esteiras e Triagem Inteligente", 28, 3),
        Projeto("Ferramentas de Manutenção", 12, 2),
    ]
    capacidade = 10
    return projetos, capacidade


def executar_testes():
    print("=== TESTE: Caso do Enunciado ===")
    projetos, capacidade = exemplo_enunciado()
    print(f"Capacidade: {capacidade}")
    print("Projetos:", [(p.nome, p.valor, p.custo) for p in projetos])
    for func in (mochila_gulosa, mochila_recursiva, mochila_memo, mochila_pd):
        valor, itens = func(projetos, capacidade)
        print(f"{func.__name__:20s} → Valor Máximo: {valor:3d} | Itens: {itens}")
    print()

    print("=== TESTE: Garagem Autônoma de Logística ===")
    projetos, capacidade = exemplo_garagem_autonoma()
    print(f"Capacidade: {capacidade}")
    print("Projetos:", [(p.nome, p.valor, p.custo) for p in projetos])
    for func in (mochila_gulosa, mochila_recursiva, mochila_memo, mochila_pd):
        valor, itens = func(projetos, capacidade)
        print(f"{func.__name__:20s} → Valor Máximo: {valor:3d} | Itens: {itens}")
    print()


if __name__ == "__main__":
    executar_testes()
