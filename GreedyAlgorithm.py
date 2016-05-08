import copy

class TagObject():
    weight = None
    price = None
    status = None  # 0: not be chosen, 1: be chosen, 2: can't be chosen

    def __init__(self, weight, price):
        self.weight = weight
        self.price = price
        self.status = 0

class TagKnapsackProblem():
    objs = None
    total_c = None

    def __init__(self, objs, total_c):
        self.objs = objs
        self.total_c = total_c


def GreedyAlgorithm(problem, spFunc):
    nt_c = 0

    while True:
        idx = spFunc(problem.objs)
        if idx == -1:
            break
        if nt_c + problem.objs[idx].weight <= problem.total_c:
            problem.objs[idx].status = 1
            nt_c += problem.objs[idx].weight
        else:
            problem.objs[idx].status = 2  # this item can't be chosen anymore


def chooseByPrice(objs):
    index = -1
    max_price = 0
    for i, obj in enumerate(objs):
        if obj.status == 0 and obj.price > max_price:
            index = i
            max_price = obj.price
    return index


def chooseByWeight(objs):
    index = -1
    objs_weight = [obj.weight for obj in objs if obj.status == 0]
    if objs_weight:
        min_weight = min(objs_weight)
        for i, obj in enumerate(objs):
            if obj.status == 0 and obj.weight == min_weight:
                index = i
                break
    return index


def chooseByPriceWeight(objs):
    index = -1
    max_price_weight = 0.
    for i, obj in enumerate(objs):
        if obj.status == 0 and float(obj.price) / float(obj.weight) > max_price_weight:
            index = i
            max_price_weight = float(obj.price) / float(obj.weight)
    return index


def main():
    c = 150
    w_i = [35, 30, 60, 50, 40, 10, 25]  # weight list
    p_i = [10, 40, 30, 50, 35, 40, 30]  # price list
    objs = []
    for obj in [TagObject(w, p) for w, p in zip(w_i, p_i)]:
        objs.append(obj)
    objs_price = copy.deepcopy(objs)
    objs_weight = copy.deepcopy(objs)
    objs_price_weight = copy.deepcopy(objs)
    # Choose by price
    problem = TagKnapsackProblem(objs_price, c)
    GreedyAlgorithm(problem, chooseByPrice)
    print sum([obj.price for obj in problem.objs if obj.status == 1])
    # Choose by weight
    problem = TagKnapsackProblem(objs_weight, c)
    GreedyAlgorithm(problem, chooseByWeight)
    print sum([obj.price for obj in problem.objs if obj.status == 1])
    # Choose by price/weight
    problem = TagKnapsackProblem(objs_price_weight, c)
    GreedyAlgorithm(problem, chooseByPriceWeight)
    print sum([obj.price for obj in problem.objs if obj.status == 1])


if __name__ == '__main__':
    main()
