from operator import add, sub, mul

def div(x, y):
    if y == 0:
        raise ZeroDivisionError
    ret = x/y
    if ret != int(ret):
        raise ZeroDivisionError
    return int(ret)


numbers = [3, 5, 7, 2, 25, 75]
actions = [add, sub, mul, div]

solutions = []

true_solutions = {}

def shortest_solution(solutions, n):
    candidate_solutions = list(filter(lambda x: x[0] == n, solutions))
    sorted_solutions = sorted(candidate_solutions, key=len)
    return sorted_solutions[0]



def solve(numbers, answer):
    global solutions
    if len(numbers) < 2:
        return False

    for x, y, rest in my_perms(numbers):
        for action in actions:
            try:
                n = Node(x, y, action)
                o = int(n)
            except:
                continue
            solutions.append((o, n))
            if o == answer:
                true_solutions[o] = shortest_solution(solutions, answer)
                solutions = []
                return True
            if solve([n, *rest], answer):
                return True


def my_perms(iterable):
    for i, num in enumerate(iterable[:-1]):
        for j, num in enumerate(iterable[i+1:], i+1):
            new_list = remove_from_list(remove_from_list(iterable, j), i)
            yield (iterable[i], iterable[j], new_list)


def remove_from_list(list_, index):
    return list_[:index] + list_[index+1:]

def find_all():
    for n in range(100, 1000):
        if n not in true_solutions and not solve(numbers, n):
            print(f"Can't solve for {n}")
        else:
            print(f"Done {n}")


class Node:
    act_strs = {
        add: " + ",
        sub: " - ",
        div: " / ",
        mul: " * "
    }

    def __init__(self, x, y, action):
        self.x = x
        self.y = y
        self.action = action
        self.result = self._get_result()

    def _get_result(self):
        try:
            return self.action(int(self.x), int(self.y))
        except:
            return None

    def __str__(self):
        return f'({self.x}{Node.act_strs[self.action]}{self.y})'

    def __int__(self):
        return self.result

    def _len(self, x):
        if isinstance(x, int):
            return 1
        return len(x)

    def __len__(self):
        return self._len(self.x) + self._len(self.y)


