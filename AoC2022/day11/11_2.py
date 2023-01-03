#11_2
import re
import numpy as np

monkey_instructions = open('input11.txt').read().split('\n\n')
monkeys = [[] for i in range(len(monkey_instructions))]

def main():
    inspected = [0 for i in range(len(monkey_instructions))]

    for monkey in monkey_instructions:
        parse(monkey)
    prod_tests = np.prod([monkey.test for monkey in monkeys])

    for round in range(10000):
        for monkey in monkeys:
            for item in monkey.items:
                op = ''.join(monkey.operation).replace('old',str(item))
                item = eval(op) % prod_tests #Kids, don't try this at home!
                monkey.inspected += 1
                if item % monkey.test == 0:
                    monkeys[monkey.true].items.append(item)
                else:
                    monkeys[monkey.false].items.append(item)
            monkey.items = []
        
    mult_list = lambda list : list[0] * list[1]
    print(mult_list(sorted([x.inspected for x in monkeys])[-2:]))

def parse(monkey_data):
    global monkeys
    monkey = Monkey()
    for key, rx in rx_dict.items():
        match = rx.search(monkey_data)
        if match:
            match key:
                case 'monkey':
                    monkey.no = int(match.group('monkeyno'))
                case 'items':
                    monkey.items = [int(x.replace(',','').strip()) for x in match.group('items').split(',')]
                case 'operation':
                    monkey.operation = match.group('operation').strip().split()[-3:]
                case 'test':
                    monkey.test = int(match.group('test').split()[-1])
                case 'true':
                    monkey.true = int(match.group('true').split()[-1])
                case 'false':
                    monkey.false = int(match.group('false').split()[-1])
                case other:
                    print('KEY ERROR!')
    monkeys[monkey.no] = monkey                 

class Monkey:
    no = -1
    items = []
    operation = []
    test = 'hej'
    true = 'tru'
    false = 'fals'
    inspected = 0

rx_dict ={
    'monkey': re.compile(r'Monkey (?P<monkeyno>\d):'),
    'items': re.compile(r'items: (?P<items>.*)\n'),
    'operation': re.compile(r'Operation: (?P<operation>.*)\n'),
    'test': re.compile(r'Test: (?P<test>.*)\n'),
    'true': re.compile(r'true: (?P<true>.*)\n'),
    'false': re.compile(r'false: (?P<false>.*)')
}

if __name__ == "__main__":
    main()