# Rabbits and Recurrence Relations

Problema da plataforma Rosalind sobre o crescimento de uma população de coelhos utilizando uma relação de recorrência.

## Objetivo

Determinar o número de pares de coelhos presentes após `n` meses, considerando que cada par de coelhos em idade reprodutiva produz `k` novos pares a cada geração.

O problema utiliza um modelo simplificado no qual:

- A população começa com um par de coelhos.
- Os coelhos atingem idade reprodutiva após um mês.
- Os coelhos não morrem.
- Cada par reprodutivo produz `k` novos pares.
- A população de cada mês depende dos valores calculados nos meses anteriores.

## Entrada

Dois números inteiros positivos:

```text
n k
```

Onde:

- `n` representa o número de meses;
- `k` representa o número de pares de filhotes produzidos por cada par reprodutivo.

## Saída

O número total de pares de coelhos presentes após `n` meses.

## Exemplo

### Entrada

```text
5 3
```

### Evolução

```text
Mês 1 → 1
Mês 2 → 1
Mês 3 → 1 + 3 × 1 = 4
Mês 4 → 4 + 3 × 1 = 7
Mês 5 → 7 + 3 × 4 = 19
```

### Saída

```text
19
```

## Relação de recorrência

Se `F(n)` representa o número de pares de coelhos após `n` meses, podemos definir:

```text
F(n) = F(n - 1) + k × F(n - 2)
```

com as condições iniciais:

```text
F(1) = 1
F(2) = 1
```

O termo `F(n - 1)` representa os pares que já existiam no mês anterior.

O termo `k × F(n - 2)` representa os novos pares produzidos pelos pares que já estavam em idade reprodutiva.

## Abordagem

A solução utiliza **programação dinâmica**.

Em vez de calcular repetidamente os mesmos termos da recorrência, os resultados anteriores são armazenados e utilizados para calcular o próximo termo.

Para calcular o resultado até o mês `n`, mantemos apenas os dois valores anteriores:

```text
anterior_2 = F(n - 2)
anterior_1 = F(n - 1)
```

Então calculamos:

```text
atual = anterior_1 + k × anterior_2
```

Depois, os valores são atualizados para o próximo mês.

Essa abordagem evita chamadas recursivas repetidas e permite resolver o problema de maneira eficiente.

## Complexidade

Para `n` meses:

- **Tempo:** `O(n)`
- **Espaço:** `O(1)`

A solução percorre os meses apenas uma vez e mantém somente os dois termos anteriores da sequência.

## Solução

A implementação está disponível em [`solution.py`](./solution.py).

## Testes

Os testes automatizados estão disponíveis em [`test_solution.py`](./test_solution.py).

Os testes verificam:

- O exemplo fornecido pela Rosalind;
- O caso básico com um mês;
- O comportamento quando `k = 1`;
- Diferentes valores de `n` e `k`;
- Casos pequenos que permitem verificar manualmente a recorrência.

Os testes podem ser executados com:

```bash
pytest
```

## Conceito estudado

Este problema introduz a utilização de **relações de recorrência** e **programação dinâmica** para construir soluções maiores a partir de resultados menores.

A ideia é importante em algoritmos porque muitos problemas podem ser divididos em subproblemas menores cujos resultados podem ser reutilizados.

A recorrência utilizada neste exercício também generaliza a sequência de Fibonacci. Quando `k = 1`, temos:

```text
F(n) = F(n - 1) + F(n - 2)
```

que corresponde à recorrência tradicional de Fibonacci.

## Referência

Problema original:

[Rosalind — Rabbits and Recurrence Relations](https://rosalind.info/problems/fib/)
