#!/usr/bin/env python3

USAGE = """USAGE: {script} initial_sum percent fixed_period set_period 
                            OR
USAGE: {script} percent fixed_period set_period

\tCalculate deposit yield. See script source for more details."""

def deposit_sp(initial_sum, fixed_period, set_period, per):
    """Calculates the yield of the deposit for set period."""
    growth = (1 + per) ** (set_period / fixed_period)
    return initial_sum * growth

def deposit_1p(initial_sum, per):
    """Calculates the yield of the deposit for one period."""
    growth_one_period = (1 + per)
    return initial_sum * growth_one_period

def deposit_5p(initial_sum, per):
    """Calculates the yield of the deposit for five periods."""
    growth_five_periods = (1 + per)**5
    return initial_sum * growth_five_periods

def percentage_for_the_period(per,fixed_period, set_period):
    """Calculates the yield of the deposit for set period without sum."""
    growth_profit = (1+per) ** (fixed_period / set_period)
    return (growth_profit-1)*100


def main(args):
    """Gets called when run as a script."""
    if len(args) == (4 + 1):
        args = args[1:]
        initial_sum, percent, fixed_period, set_period = map(float, args)

        per = percent / 100

        res_sp = round(deposit_sp(initial_sum, fixed_period, set_period, per), 2)
        res_1p = round(deposit_1p(initial_sum, per), 2)
        res_5p = round(deposit_5p(initial_sum, per), 2)

        print(f'for set period you will get {res_sp}, net profit is {round(res_sp-initial_sum, 2)} \n'
              f'for one fixed period you will get {res_1p}, net profit is {round(res_1p-initial_sum, 2)}\n'
              f'for five fixed period you will get {res_5p}, net profit is {round(res_5p-initial_sum, 2)}')
    elif len(args) == (3+1):
        args = args[1:]
        percent, fixed_period,  set_period = map(float, args)

        per = percent / 100

        res_pr = round(percentage_for_the_period(per, fixed_period, set_period), 2)

        print(f'percentage is {res_pr}')

    else:
        exit(USAGE.format(script=args[0]))

if __name__ == '__main__':
    import sys

main(sys.argv)