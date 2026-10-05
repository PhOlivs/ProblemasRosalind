from solution import reverse_complement


def test_reverse_complement():
    assert reverse_complement("AAAACCCGGT") == "ACCGGGTTTT"


def test_all_nucleotides():
    assert reverse_complement("ACGT") == "ACGT"


def test_only_adenine():
    assert reverse_complement("AAAA") == "TTTT"


def test_only_cytosine():
    assert reverse_complement("CCCC") == "GGGG"


def test_empty_sequence():
    assert reverse_complement("") == ""
