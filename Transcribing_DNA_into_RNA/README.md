# Transcribing DNA into RNA

Problema da plataforma Rosalind sobre a transcrição de uma sequência de DNA em uma sequência de RNA.

## Objetivo

Dada uma sequência de DNA correspondente a uma fita codificadora, produzir sua sequência de RNA transcrita.

Durante a transcrição, cada ocorrência do nucleotídeo `T` (Timina) é substituída por `U` (Uracila).

Os demais nucleotídeos permanecem inalterados:

```text
A → A
C → C
G → G
T → U
```

## Entrada

Uma sequência de DNA contendo apenas os nucleotídeos:

```text
A C G T
```

A sequência possui comprimento de no máximo 1000 nucleotídeos.

## Saída

A sequência de RNA correspondente à sequência de DNA fornecida, com todas as ocorrências de `T` substituídas por `U`.

A sequência de saída utiliza o alfabeto:

```text
A C G U
```

## Exemplo

### Entrada

```text
GATGGAACTTGACTACGTAAATT
```

### Saída

```text
GAUGGAACUUGACUACGUAAAUU
```

## Abordagem

A solução será implementada em Python.

Como a transcrição descrita pelo problema consiste apenas na substituição de `T` por `U`, podemos utilizar o método `replace()` da linguagem Python.

A sequência é inicialmente tratada com `strip()` para remover espaços ou quebras de linha provenientes do arquivo de entrada.

A transformação principal é:

```python
sequence.replace("T", "U")
```

Essa operação percorre a sequência e substitui todas as ocorrências de `T` por `U`.

## Complexidade

Considerando uma sequência de tamanho `n`, a operação possui:

- **Tempo:** `O(n)`
- **Espaço:** `O(n)`

O espaço adicional ocorre porque strings em Python são imutáveis e uma nova string é criada para armazenar o resultado da substituição.

## Solução

A implementação está disponível em [`solution.py`](./solution.py).

## Testes

Os testes automatizados estão disponíveis em [`test_solution.py`](./test_solution.py).

Os testes verificam diferentes situações, incluindo:

- Transcrição do exemplo fornecido pela Rosalind
- Sequências sem `T`
- Sequências compostas apenas por `T`
- Sequência vazia
- Preservação dos nucleotídeos `A`, `C` e `G`

Os testes podem ser executados com:

```bash
pytest
```

## Referência

Problema original:

[Rosalind — Transcribing DNA into RNA](https://rosalind.info/problems/rna/)

## Conceito estudado

Este problema introduz o conceito de **transcrição**, processo biológico no qual uma sequência de DNA é utilizada como molde para a produção de uma molécula de RNA.

Neste exercício, é utilizada uma simplificação do processo biológico: a sequência fornecida corresponde à fita codificadora, portanto a transcrição pode ser representada diretamente pela substituição de `T` por `U`.
