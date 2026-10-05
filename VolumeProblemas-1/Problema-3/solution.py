from pathlib import Path


def reverse_complement(sequence: str) -> str:
    """
    Retorna o reverse complement de uma sequência de DNA.

    A = T
    T = A
    C = G
    G = C
    """
    complement = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C",
    }

    sequence = sequence.strip()

    return "".join(complement[base] for base in reversed(sequence))


def main() -> None:
    input_file = Path(__file__).with_name("rosalind_revc.txt")
    sequence = input_file.read_text().strip()

    print(reverse_complement(sequence))


if __name__ == "__main__":
    main()
