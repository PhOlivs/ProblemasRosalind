from solution import count_nucleotides


def test_count_nucleotides():
    sequence = "AAAACCCGGT"

    assert count_nucleotides(sequence) == (4, 3, 2, 1)


def test_empty_sequence():
    assert count_nucleotides("") == (0, 0, 0, 0)


def test_only_one_nucleotide():
    assert count_nucleotides("AAAA") == (4, 0, 0, 0)


def test_all_nucleotides_once():
    assert count_nucleotides("ACGT") == (1, 1, 1, 1)


def test_lowercase_is_not_accepted():
    assert count_nucleotides("acgt") == (0, 0, 0, 0)
