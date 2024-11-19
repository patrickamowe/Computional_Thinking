def greedy(items, maxCost, keyFunction):
    """

    :param items:
    :param maxCost:
    :param keyFunction:
    :return:
    """

    itemsCopy = sorted(items, key=keyFunction, reverse=True)

    result = []
    totalValue, totalCost = 0.0, 0.0

    for i in range(len(itemsCopy)):
        if (totalCost + itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalValue += itemsCopy[i].getValue()
            totalCost += itemsCopy[i].getCost()

    return (result, totalValue)