from food import Food
from greedy_alg import greedy
from menu import buildMenu


def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print("Total value of items taken =", val)
    for item in taken:
        print('    ', item)


def testGreedys(foods, maxUnits):
    print("Use greedy by values to allocate", maxUnits, "calories")
    testGreedy(foods, maxUnits, Food.getValue)

    print("\n Use greedy by cost to allocate", maxUnits, "calories")
    testGreedy(foods, maxUnits, lambda x:1/Food.getCost(x))

    print("\n Use greedy by density to allocate", maxUnits, "calories")
    testGreedy(foods, maxUnits, Food.density)


names = ['wine','beer','pizza','burger','fries','cola','apple','donut','cake']
values =[89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]

foods = buildMenu(names,values, calories)
testGreedys(foods, 750)