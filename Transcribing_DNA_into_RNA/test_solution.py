from solution import transcribe_dna


def test_transcribe_dna():
    sequence = "GATGGAACTTGACTACGTAAATT"

    assert transcribe_dna(sequence) == "GAUGGAACUUGACUACGUAAAUU"


def test_sequence_without_thymine():
    assert transcribe_dna("ACG") == "ACG"


def test_only_thymine():
    assert transcribe_dna("TTTT") == "UUUU"


def test_empty_sequence():
    assert transcribe_dna("") == ""


def test_preserves_other_nucleotides():
    assert transcribe_dna("AACCGG") == "AACCGG"
