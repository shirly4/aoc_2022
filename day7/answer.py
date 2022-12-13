from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, List, Union
from functools import cached_property


@dataclass
class Directory:
    name: str
    parent: Optional[Directory] = None
    children: List[Union[Directory, File]] = field(default_factory=list)

    @cached_property
    def size(self) -> int:
        return sum(child.size for child in self.children)


@dataclass
class File:
    name: str
    size: int
    parent: Directory


def total_size_of_low_memory_dir(directory: Directory, low_memory_threshold: int):
    if directory.size <= low_memory_threshold:
        return directory.size + sum(
            total_size_of_low_memory_dir(dire, LOW_MEMORY_THRESHOLD)
            for dire in directory.children
            if isinstance(dire, Directory)
        )
    return sum(
        total_size_of_low_memory_dir(dire, LOW_MEMORY_THRESHOLD)
        for dire in directory.children
        if isinstance(dire, Directory)
    )


def min_dir_size_above(directory: Directory, min_size: int):
    return min(
        [directory.size]
        + [
            min_dir_size_above(dire, min_size)
            for dire in directory.children
            if isinstance(dire, Directory) and dire.size >= min_size
        ]
    )


def min_dir_size_above_safe(directory: Directory, min_size: int):
    if directory.size < min_size:
        raise ValueError(
            f"The size of the directory ({directory.size}) is below {min_size=}"
        )
    return min_dir_size_above(directory, min_size)


LOW_MEMORY_THRESHOLD = 100000

SPACE_NEEDED = 30000000
DISK_SPACE = 70000000


def main():
    with open("input.txt", "r") as f:
        terminal = f.read().splitlines()

    root_directory = Directory(name="/")

    # first command has to be cd /
    current_directory = root_directory

    for prompt in terminal[1:]:
        if prompt.startswith("$"):
            _, *command = prompt.split()
            if command[0] == "cd":
                if command[1] == "..":
                    current_directory = current_directory.parent
                else:
                    current_directory = next(
                        dire
                        for dire in current_directory.children
                        if dire.name == command[1]
                    )
        else:
            dir_or_size, name = prompt.split()

            if name not in (dire.name for dire in current_directory.children):
                if dir_or_size.isnumeric():
                    size = int(dir_or_size)
                    current_directory.children.append(
                        File(name=name, size=size, parent=current_directory)
                    )
                else:
                    current_directory.children.append(
                        Directory(name=name, parent=current_directory)
                    )

    answer1 = total_size_of_low_memory_dir(root_directory, LOW_MEMORY_THRESHOLD)
    print(f"answer part 1 is: {answer1}")

    min_space_to_remove = SPACE_NEEDED - (DISK_SPACE - root_directory.size)

    answer2 = min_dir_size_above_safe(root_directory, min_space_to_remove)
    print(f"answer part 2 is: {answer2}")


if __name__ == "__main__":
    main()
