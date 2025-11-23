from scripts.W2H2_RPS import get_comp_choice, choices


def test_get_comp_choice_returns_valid_int():
    """Ensure the computer choice generator returns a valid integer key."""
    val = get_comp_choice()
    assert isinstance(val, int)
    assert val in choices.keys()
