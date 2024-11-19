def maxVal(toConsider, avial):
    """

    :param toConsider: is a list of items
    :param avial: avialiable weight
    :return: A turple of the total value of a solution of the 0/1 knapsack_problem and the items of that solution
    """
    if toConsider == [] or avial == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avial:
        result = maxVal(toConsider[1:], avial)
    else:
        nextItem = toConsider[0]

        withVal, withToTake = maxVal(toConsider[1:], avial=nextItem.getCost())

        withVal += nextItem.getValue()

        withoutVal, withoutToTake = maxVal(toConsider[1:], avial)

        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)

    return result
