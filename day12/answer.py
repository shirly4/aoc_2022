import string
from collections import deque


def find_path(start_index, end, grid):
    letter_ordering = {letter: i for i, letter in enumerate(string.ascii_lowercase)}
    queue = deque([[start_index]])
    seen = set([start_index])
    n_line = len(grid)
    n_col = len(grid[0])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        elevation = grid[x][y]

        if elevation == end:
            return path
        if elevation == "S":
            elevation = "a"
        for xt, yt in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= xt < n_line and 0 <= yt < n_col:
                elevation_next = grid[xt][yt]
                if elevation_next == "E":
                    elevation_next = "z"
                elif elevation_next == "S":
                    elevation_next = "a"
                if (
                    letter_ordering[elevation_next] - 1 <= letter_ordering[elevation]
                    and (xt, yt) not in seen
                ):
                    queue.append(path + [(xt, yt)])
                    seen.add((xt, yt))


def main():
    with open("input.txt", "r") as f:
        grid = f.read().splitlines()

    start_index = next(
        (i, j)
        for i, line in enumerate(grid)
        for j, elevation in enumerate(line)
        if elevation == "S"
    )

    answer1 = len(find_path(start_index, "E", grid)) - 1
    print(f"answer part 1 is: {answer1}")

    answer2 = min(
        len(find_path((i, j), "E", grid)) - 1
        for i, line in enumerate(grid)
        for j, elevation in enumerate(line)
        if elevation in {"S", "a"} and find_path((i, j), "E", grid) is not None
    )
    print(f"answer part 2 is: {answer2}")


if __name__ == "__main__":
    main()
