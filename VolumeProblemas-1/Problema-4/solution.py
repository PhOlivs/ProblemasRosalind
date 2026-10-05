from pathlib import Path


def rabbit_pairs(months: int, offspring: int) -> int:
    """
    Calcula o número de pares de coelhos após determinado
    número de meses.

    Cada par reprodutivo produz 'offspring' novos pares.

    Recorrência:
        F(n) = F(n - 1) + offspring * F(n - 2)
    """

    if months <= 2:
        return 1

    previous_two = 1
    previous_one = 1

    for _ in range(3, months + 1):
        current = previous_one + offspring * previous_two

        previous_two = previous_one
        previous_one = current

    return previous_one


def main() -> None:
    input_file = Path(__file__).with_name("rosalind_fib.txt")
    months, offspring = map(int, input_file.read_text().split())

    print(rabbit_pairs(months, offspring))


if __name__ == "__main__":
    main()
