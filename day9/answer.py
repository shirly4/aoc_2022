from dataclasses import dataclass
import math


def sign(x):
    if x == 0:
        return 0
    return math.copysign(1, x)


@dataclass(unsafe_hash=True)
class Vector2d:
    x: int
    y: int

    def __add__(self, other):
        if not isinstance(other, Vector2d):
            raise TypeError("Can only add two vectors together")
        return Vector2d(x=self.x + other.x, y=self.y + other.y)

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        if not isinstance(other, Vector2d):
            raise TypeError("Can only substract two vectors together")
        return Vector2d(x=self.x - other.x, y=self.y - other.y)


def norm_inf(u: Vector2d, v: Vector2d):
    return max(abs(u.x - v.x), abs(u.y - v.y))


DIRECTION_VECTOR = {
    "U": Vector2d(x=0, y=1),
    "D": Vector2d(x=0, y=-1),
    "R": Vector2d(x=1, y=0),
    "L": Vector2d(x=-1, y=0),
}


def main():
    print(sign(0))
    with open("input.txt", "r") as f:
        motions = f.read().splitlines()
    motions = [tuple(split.split()) for split in motions]

    starting_position = Vector2d(x=0, y=0)

    tail_position = starting_position
    head_position = starting_position

    tail_visited_position = {tail_position}

    for direction, step in motions:

        for _ in range(int(step)):

            head_position += DIRECTION_VECTOR[direction]
            if norm_inf(tail_position, head_position) > 1:
                delta = head_position - tail_position
                tail_position += Vector2d(x=sign(delta.x), y=sign(delta.y))
            tail_visited_position.add(tail_position)

    print(f"answer part 1 is= {len(tail_visited_position)}")

    knot_positions = [starting_position for _ in range(9)]
    head_position = starting_position
    tail_visited_position = {knot_positions[-1]}

    # motions = [("R",5), ("U", 8), ("L", 8), ("D", 3), ("R", 17), ("D", 10), ("L",25 ), ("U", 20)]

    for direction, step in motions:
        for _ in range(int(step)):

            head_position += DIRECTION_VECTOR[direction]

            ahead_knot_position = head_position
            for i, knot_position in enumerate(knot_positions):
                if norm_inf(knot_position, ahead_knot_position) > 1:
                    delta = ahead_knot_position - knot_position
                    knot_positions[i] += Vector2d(x=sign(delta.x), y=sign(delta.y))

                    ahead_knot_position = knot_positions[i]
                else:
                    break

            tail_visited_position.add(knot_positions[-1])

    print(f"answer part 2 is= {len(tail_visited_position)}")


if __name__ == "__main__":
    main()
