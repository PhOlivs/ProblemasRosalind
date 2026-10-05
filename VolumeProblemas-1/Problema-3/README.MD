# Complementing a Strand of DNA

Problema da plataforma Rosalind sobre a obtenção do **reverse complement** de uma sequência de DNA.

## Objetivo

Dada uma sequência de DNA, determinar sua sequência complementar reversa.

No DNA, as bases nitrogenadas possuem as seguintes relações de complementaridade:

```text
A ↔ T
C ↔ G
```

Para obter o reverse complement, é necessário realizar duas operações:

1. Inverter a ordem dos nucleotídeos da sequência.
2. Substituir cada nucleotídeo pelo seu complemento.

## Entrada

Uma sequência de DNA contendo apenas os nucleotídeos:

```text
A C G T
```

A sequência possui comprimento de no máximo 1000 pares de bases.

## Saída

A sequência de DNA correspondente ao **reverse complement** da sequência fornecida.

## Exemplo

### Entrada

```text
AAAACCCGGT
```

### Etapa 1 — Inversão

A sequência original:

```text
AAAACCCGGT
```

Invertida:

```text
TGGCCCAAAA
```

### Etapa 2 — Complementação

Aplicando as regras:

```text
A → T
T → A
C → G
G → C
```

obtemos:

```text
ACCGGGTTTT
```

### Saída

```text
ACCGGGTTTT
```

## Abordagem

A solução será implementada em Python.

Primeiro, a sequência é invertida utilizando slicing:

```python
sequence[::-1]
```

Em seguida, cada base é substituída pelo seu complemento utilizando um mapeamento:

```python
{
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}
```

A combinação dessas duas operações produz o reverse complement.

Outra possibilidade seria utilizar o método `translate()` do Python para realizar a complementação de forma mais direta.

## Complexidade

Considerando uma sequência de tamanho `n`:

- **Tempo:** `O(n)`
- **Espaço:** `O(n)`

É necessário percorrer a sequência para produzir a sequência complementar e armazenar o resultado.

## Solução

A implementação está disponível em [`solution.py`](./solution.py).

## Testes

Os testes automatizados estão disponíveis em [`test_solution.py`](./test_solution.py).

Os testes verificam:

- O exemplo fornecido pela Rosalind
- Sequências contendo todas as bases
- Sequências compostas por uma única base
- Sequência vazia
- Complementaridade correta das bases

Os testes podem ser executados com:

```bash
pytest
```

## Conceito estudado

Este problema introduz o conceito de **reverse complement**, fundamental para trabalhar com sequências de DNA.

Como as duas fitas de DNA possuem orientação oposta e são complementares, conhecer uma das fitas permite determinar a sequência correspondente na outra fita.

O conceito é utilizado em diversas tarefas de Bioinformática, incluindo análise de sequências, busca de padrões, montagem e anotação de genomas.

## Referência

Problema original:

[Rosalind — Complementing a Strand of DNA](https://rosalind.info/problems/revc/)
