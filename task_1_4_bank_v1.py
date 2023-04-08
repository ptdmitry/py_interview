"""
Написать программу «Банковский депозит». Клиент банка делает депозит на определенный срок.
В зависимости от суммы и срока вклада определяется процентная ставка:
1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 и более года — 5 % годовых).
10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 и более года – 6.5 % годовых).
100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 и более года — 7.5 % годовых).
Проценты начисляются на депозит в конце каждого месяца.
Необходимо написать функцию, в которую будут передаваться параметры:
сумма вклада и срок вклада (в месяцах), а на выходе возвращать сумму вклада на конец срока
"""

MIN_DEPOSIT = 1_000
MID_DEPOSIT_1 = 10_000
MID_DEPOSIT_2 = 100_000
MAX_DEPOSIT = 1_000_000
MIN_PERIOD = 8
MID_PERIOD = 12
MAX_PERIOD = 24
YEAR = 12
PERCENT_100 = 100
ZERO = 0


def bank_deposit(deposit: int, period: int) -> str:
    percent = ZERO
    if MIN_DEPOSIT <= deposit < MID_DEPOSIT_1 and MIN_PERIOD == period == MAX_PERIOD:
        percent = 5
    elif MIN_DEPOSIT <= deposit < MID_DEPOSIT_1 or MID_DEPOSIT_1 <= deposit < MID_DEPOSIT_2 \
            and period == MID_PERIOD or period == MIN_PERIOD:
        percent = 6
    elif MID_DEPOSIT_1 <= deposit < MID_DEPOSIT_2 or MID_DEPOSIT_2 <= deposit < MAX_DEPOSIT \
            and period == MID_PERIOD or period == MIN_PERIOD:
        percent = 7
    elif MID_DEPOSIT_1 <= deposit < MID_DEPOSIT_2 and period == MAX_PERIOD:
        percent = 6.5
    elif MID_DEPOSIT_2 <= deposit < MAX_DEPOSIT and period == MID_PERIOD:
        percent = 8
    elif MID_DEPOSIT_2 <= deposit < MAX_DEPOSIT and period == MAX_PERIOD:
        percent = 7.5
    for i in range(period):
        deposit = deposit * (percent / PERCENT_100) / YEAR + deposit
    return f'{deposit:.2f}'


if __name__ == '__main__':
    print(bank_deposit(10000, 24))
