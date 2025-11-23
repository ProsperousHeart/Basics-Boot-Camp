from scripts.W2H2_RPS import Choice


def test_make_one_choice():
    choice = Choice()
    assert choice.make_choice() in ["rock", "paper", "scissors"]
