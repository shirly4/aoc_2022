from collections import deque
import math


def main():
    with open("input.txt", "r") as f:
        monkeys = f.read().split("\n\n")

    monkeys_items = []
    monkeys_func = []

    for monkey in monkeys:
        monkey_items = deque()
        monkey_infos = monkey.replace(" ", "").splitlines()
        for item in monkey_infos[1].split(":")[1].split(","):
            monkey_items.append(int(item))
        monkeys_items.append(monkey_items)

        instructions = monkey_infos[2].split("=")[1]
        divisible_by = int(monkey_infos[3].split("by")[1])
        toTrue = int(monkey_infos[4][-1])
        toFalse = int(monkey_infos[5][-1])

        monkeys_func.append(
            {
                "instructions": instructions,
                "divisible_by": divisible_by,
                "toTrue": toTrue,
                "toFalse": toFalse,
            }
        )

    monkeys_inspect_items = [0] * len(monkeys_items)

    for i in range(20):

        for i, (monkey_items, monkey_func) in enumerate(
            zip(monkeys_items, monkeys_func)
        ):
            monkeys_inspect_items[i] += len(monkey_items)

            while monkey_items:
                old = monkey_items.popleft()
                new = eval(monkey_func["instructions"])

                new //= 3
                if new % monkey_func["divisible_by"] == 0:
                    to = monkey_func["toTrue"]
                else:
                    to = monkey_func["toFalse"]
                monkeys_items[to].append(new)

    answer1 = math.prod(sorted(monkeys_inspect_items)[-2:])

    print(f"answer part 1 is: {answer1}")

    monkeys_items = []
    monkeys_func = []

    divisible_by_product = 1

    for monkey in monkeys:
        monkey_items = deque()
        monkey_infos = monkey.replace(" ", "").splitlines()
        for item in monkey_infos[1].split(":")[1].split(","):
            monkey_items.append(int(item))
        monkeys_items.append(monkey_items)

        instructions = monkey_infos[2].split("=")[1]
        divisible_by = int(monkey_infos[3].split("by")[1])
        divisible_by_product *= divisible_by

        toTrue = int(monkey_infos[4][-1])
        toFalse = int(monkey_infos[5][-1])

        monkeys_func.append(
            {
                "instructions": instructions,
                "divisible_by": divisible_by,
                "toTrue": toTrue,
                "toFalse": toFalse,
            }
        )

    monkeys_inspect_items = [0] * len(monkeys_items)

    for i in range(10000):

        for i, (monkey_items, monkey_func) in enumerate(
            zip(monkeys_items, monkeys_func)
        ):
            monkeys_inspect_items[i] += len(monkey_items)

            while monkey_items:
                old = monkey_items.popleft()
                new = eval(monkey_func["instructions"])

                new %= divisible_by_product

                if new % monkey_func["divisible_by"] == 0:
                    to = monkey_func["toTrue"]
                else:
                    to = monkey_func["toFalse"]

                monkeys_items[to].append(new)

    answer2 = math.prod(sorted(monkeys_inspect_items)[-2:])

    print(f"answer part 2 is: {answer2}")


if __name__ == "__main__":
    main()
