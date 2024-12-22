```md
# Atividade: Desenvolvimento de Agente Inteligente com A*

## Objetivo
Nessa atividade, vocês irão desenvolver um agente inteligente capaz de resolver problemas de forma autônoma. 
O agente será baseado em objetivos e utilizará o algoritmo A* para encontrar soluções.

### 1. Escolha do problema
Selecione um problema, com exemplos como:
- a. Quebra-cabeça dos 8;
- b. Problema do caixeiro viajante;
- c. Planejamento de rotas em mapas;
- d. Entre outros.

### 2. Modelagem do agente
- a. Defina os componentes do agente;
- b. Represente o estado do mundo, as ações possíveis e o custo das ações;
- c. Defina as propriedades do ambiente de tarefas.

### 3. Implementação
- a. Utilize a linguagem Python para implementar o ambiente de tarefa, o agente e o algoritmo A*;
- b. Dica: Utilize bibliotecas como o NetworkX para representar grafos e heapq para implementar a fila de prioridade do A*.

### 4. Vídeo
- a. Grave um vídeo de no máximo 5 minutos;
- b. Explique o problema escolhido e sua formulação;
- c. A implementação do agente e do algoritmo A*;
- d. Uma demonstração do agente resolvendo o problema;
- e. Disponibilize o vídeo na plataforma do YouTube;
- f. Dica: Utilize slides ou animações para auxiliar na explicação.

### 5. Postagem
Poste o código e o link de acesso ao vídeo no SIGAA.

---

## Descrição do Agente: Algoritmo A* no Sistema Solar

O agente representado pelo algoritmo A* atua como um solucionador de problemas de busca em grafos. Seu objetivo é 
encontrar o caminho mais curto entre astros do Sistema Solar, considerando as distâncias entre eles. O agente é 
classificado como:
- **Racional**: escolhe ações que otimizam o custo até o destino;
- **Determinístico**: as transições no grafo são fixas e conhecidas;
- **Solucionador de Problemas**: pertence à categoria de agentes que resolvem problemas de busca.

### Funcionamento do Algoritmo A*
O agente utiliza uma função heurística baseada na diferença das distâncias médias dos astros ao Sol para estimar o 
custo de alcançar o destino. Sua estrutura de dados central é uma **fila de prioridades**, que gerencia a exploração 
dos nós priorizando os de menor custo.

O algoritmo A* combina:
- **Custo real acumulado (g(n))**: o custo do ponto inicial até o nó atual;
- **Heurística (h(n))**: uma estimativa do custo restante até o destino.

### Modelagem do Ambiente
O ambiente modelado é o **Sistema Solar**, onde astros como o Sol, planetas e satélites são representados como **nós** 
de um grafo. As **arestas** do grafo são ponderadas com as distâncias médias entre os astros. O ambiente é:
- **Totalmente observável**: todas as informações estão disponíveis para o agente;
- **Estático**: as relações e distâncias não mudam durante a execução;
- **Discreto**: o grafo é uma representação discreta dos astros e suas conexões.

### Problema a Ser Resolvido
O problema a ser resolvido é encontrar o caminho mais curto entre dois astros no Sistema Solar, incluindo, se necessário,
paradas intermediárias definidas pelo usuário. O grafo tem nós que representam astros e arestas ponderadas pelas 
distâncias médias em milhões de quilômetros. A entrada consiste no ponto de origem, no destino final e, opcionalmente, 
nas paradas intermediárias. A saída é o caminho mais curto, com o custo total do trajeto.

### Implementação do Algoritmo A*
Na implementação, o grafo é criado utilizando a biblioteca **NetworkX**. Cada nó representa um astro e as arestas 
correspondem às conexões entre os astros, com pesos baseados nas distâncias médias. Conexões especiais foram adicionadas
manualmente para modelar satélites naturais, como a Lua e Fobos.

A **função heurística** é calculada como a diferença das distâncias médias dos astros ao Sol. Por exemplo, para Marte e 
Terra, a heurística seria:  
**227.9 - 149.6 = 78.3** milhões de quilômetros.

### Execução do Algoritmo
Durante a execução do algoritmo, uma **fila de prioridades** armazena os nós a serem explorados, priorizando aqueles 
com menor soma de custo acumulado e heurística. O custo total é atualizado para cada nó explorado, e ao alcançar o 
destino, o caminho é reconstruído retroativamente.

### Entrada e Validação
A entrada do usuário define a origem, o destino e as paradas intermediárias. Validações garantem que apenas astros 
válidos sejam considerados. Por fim, o grafo completo é visualizado, com os pesos das arestas e destacando o caminho 
encontrado, incluindo os astros visitados e as conexões seguidas.

### Problemas encontrados

Infelizmente não consegui resolver o problema de escala. Os planetas interiores ainda ficam sobrepostos quando são 
apresentados nos grafos.
```