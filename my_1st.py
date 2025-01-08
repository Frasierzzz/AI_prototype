import argparse
from datetime import datetime

def parse_input():
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        '--bd',
        type=str,
        required=True,
        help='birth day of the user. (in YYYYMMDD format)'
    )

    parser.add_argument(
        '--name',
        type=str,
        default="Nathikarn",
        help='input the name of people who are using the app.'
    )

    args = parser.parse_args()
    return args

def printHello(who):
    print(f"Hello World, {who}!!")

def cal_todayVbd(bd):
    td = datetime.today()
    birth_date = datetime.strptime(bd, '%Y%m%d')
    if birth_date > td:
        raise ValueError("Birthday cannot be in future!")
    diff = td - birth_date
    return diff.days

if __name__ == "__main__":
    input_v = parse_input()
    print('This is my 1st .py file')
    printHello(input_v.name)
    print(f"Your birth day is {cal_todayVbd(input_v.bd)} from today")
    