from pathlib import Path

# Transcreve uma sequência de DNA para RNA,
def transcribe_dna(sequence: str) -> str:
# Substitui T por U
    return sequence.strip().replace("T", "U")


def main() -> None:
    input_file = Path(__file__).with_name("rosalind_rna.txt")
    sequence = input_file.read_text().strip()

    print(transcribe_dna(sequence))


if __name__ == "__main__":
    main()
