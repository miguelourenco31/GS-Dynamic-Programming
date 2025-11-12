# Global Solution - Dynamic-Programming

Este projeto aplica o **Problema da Mochila 0/1** ao contexto do sistema **Garagem Autônoma de Logística**,
onde o objetivo é selecionar o melhor conjunto de iniciativas (projetos) dentro de uma capacidade limitada
de tempo, energia ou recursos técnicos.

---

##  Equipe
- Nome Miguel Marques Lourenço de Souza - RM: 555426
- Nome Lorenzzo Vendruscolo - RM: 558305

---

##  Objetivo
Implementar quatro abordagens diferentes para o **Problema da Mochila (Knapsack 0/1)**,
comparando desempenho e resultados de otimização.

A aplicação foi adaptada ao cenário da **Garagem Autônoma de Logística**, 
onde uma inteligência artificial (AURORA) precisa decidir, de forma eficiente, 
como utilizar os recursos disponíveis (energia, tempo e robôs) durante o período noturno.

---

##  Fases Implementadas
| Fase | Método | Descrição |
|------|---------|------------|
| 1 | `mochila_gulosa()` | Seleção baseada em maior razão valor/custo. (não garante ótimo) |
| 2 | `mochila_recursiva()` | Solução recursiva pura (explora todas as combinações). |
| 3 | `mochila_memo()` | Versão recursiva otimizada com cache (memoização). |
| 4 | `mochila_pd()` | Solução iterativa com tabela de Programação Dinâmica (ótima). |

---

##  Estrutura do Código
- `Projeto`: classe que define nome, valor e custo de cada subsistema da garagem.
- Cada função retorna `(valor_total, lista_de_itens_escolhidos)`.
- Dois conjuntos de teste:
  - `exemplo_enunciado()` → caso do PDF da disciplina.
  - `exemplo_garagem_autonoma()` → cenário temático do projeto.

---

## Como Executar
Requisitos:  
- Python 3.8 ou superior.

Comando:
bash
python garagem_autonoma.py 

---

Relação com o Projeto “Garagem Autônoma de Logística”

Este código representa a camada lógica da Inteligência Artificial,
que opera à noite na garagem autônoma enquanto os trabalhadores humanos descansam.

Durante o dia:

Humanos realizam as entregas e supervisionam o sistema.
Durante a noite:

A IA precisa decidir quais tarefas noturnas realizar — como carregar veículos, embalar produtos e reorganizar o espaço — utilizando apenas a energia solar e eólica armazenada.

No código, esse processo é modelado pelo Problema da Mochila 0/1:

Cada tarefa ou subsistema é tratado como um projeto com um valor (benefício) e um custo (energia ou tempo).
A capacidade da mochila representa a energia ou tempo total disponível durante o turno noturno.
O algoritmo decide quais tarefas executar para maximizar o resultado total da operação sem ultrapassar a energia disponível.
Assim, o código simula a tomada de decisão da IA da garagem:
“Dada uma quantidade limitada de energia e tempo, quais ações os robôs devem executar para alcançar o maior impacto possível até o amanhecer?”

Essa modelagem demonstra como técnicas de programação dinâmica e otimização
podem ser aplicadas em cenários reais de automação e sustentabilidade —
alinhando o projeto aos temas do Futuro do Trabalho e dos ODS da ONU
(energia limpa, trabalho digno e inovação sustentável).

---

Tecnologias Utilizadas

- Python 3
- Programação Dinâmica
- Estruturas de Dados e Recursão
- Lógica de Otimização e Análise de Complexidade

