"""
Усовершенствовать программу «Банковский депозит».
Третьим аргументом в функцию должна передаваться фиксированная
ежемесячная сумма пополнения вклада. Считаем, что клиент вносит средства
в последний день каждого месяца, кроме первого и последнего.
Если 3м аргументом передан 0, то вызов должен быть совпадать с задачей 4
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


def bank_deposit(deposit: int, period: int, cash: int = 0) -> str:
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
        deposit = deposit * (percent / PERCENT_100) / YEAR + deposit + cash
    return f'{deposit:.2f}'


if __name__ == '__main__':
    print(bank_deposit(10000, 24, 300))
