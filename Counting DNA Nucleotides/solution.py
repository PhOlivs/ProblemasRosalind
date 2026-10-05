from pathlib import Path

# Conta os nucleotídeos A, C, G e T em uma sequência de DNA.

def count_nucleotides(sequence: str) -> tuple[int, int, int, int]:
# Retorna as quantidades na ordem: A, C, G, T
    sequence = sequence.strip()

    return (
        sequence.count("A"),
        sequence.count("C"),
        sequence.count("G"),
        sequence.count("T"),
    )


def main() -> None:
    input_file = Path(__file__).with_name("counting_dna_nucleotides.txt")
    sequence = input_file.read_text().strip()

    counts = count_nucleotides(sequence)

    print(*counts)


if __name__ == "__main__":
    main()
