import pytest
from app import BankAccount


def test_initial_balance_default():
    assert BankAccount().get_balance() == 0


def test_initial_balance_custom():
    assert BankAccount(100).get_balance() == 100


def test_deposit_increases_balance():
    acc = BankAccount(100)
    assert acc.deposit(50) == 150


def test_deposit_zero_raises_error():
    acc = BankAccount()
    with pytest.raises(ValueError):
        acc.deposit(0)


def test_deposit_negative_raises_error():
    acc = BankAccount()
    with pytest.raises(ValueError):
        acc.deposit(-10)


def test_withdraw_decreases_balance():
    acc = BankAccount(100)
    assert acc.withdraw(40) == 60


def test_withdraw_all_money():
    acc = BankAccount(100)
    assert acc.withdraw(100) == 0


def test_withdraw_more_than_balance_raises_error():
    acc = BankAccount(50)
    with pytest.raises(ValueError):
        acc.withdraw(100)


def test_withdraw_negative_raises_error():
    acc = BankAccount(50)
    with pytest.raises(ValueError):
        acc.withdraw(-5)


def test_add_interest():
    acc = BankAccount(1000)
    assert acc.add_interest(10) == 1100


def test_add_zero_interest():
    acc = BankAccount(1000)
    assert acc.add_interest(0) == 1000


def test_negative_interest_raises_error():
    acc = BankAccount(1000)
    with pytest.raises(ValueError):
        acc.add_interest(-5)


def test_multiple_operations():
    acc = BankAccount(100)
    acc.deposit(50)
    acc.withdraw(30)
    assert acc.get_balance() == 120


def test_deposit_decimal_amount():
    acc = BankAccount(100)
    assert acc.deposit(0.5) == 100.5


def test_two_deposits():
    acc = BankAccount()
    acc.deposit(10)
    acc.deposit(15)
    assert acc.get_balance() == 25


def test_interest_on_zero_balance():
    assert BankAccount().add_interest(10) == 0


def test_interest_fractional_rate():
    assert BankAccount(200).add_interest(2.5) == 205


def test_failed_withdraw_keeps_balance():
    acc = BankAccount(50)
    with pytest.raises(ValueError):
        acc.withdraw(100)
    assert acc.get_balance() == 50


def test_failed_deposit_keeps_balance():
    acc = BankAccount(50)
    with pytest.raises(ValueError):
        acc.deposit(-5)
    assert acc.get_balance() == 50


def test_get_balance_does_not_change_balance():
    acc = BankAccount(80)
    acc.get_balance()
    assert acc.get_balance() == 80


def test_deposit_then_withdraw_all():
    acc = BankAccount(50)
    acc.deposit(50)
    assert acc.withdraw(100) == 0


def test_interest_then_withdraw():
    acc = BankAccount(1000)
    acc.add_interest(10)
    assert acc.withdraw(100) == 1000