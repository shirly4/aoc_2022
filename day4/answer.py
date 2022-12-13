import re


def main():
    with open("input.txt", "r") as f:
        tasks = f.read().splitlines()

    regex_splitter = re.compile(r",|-")
    tasks_splitter = [
        tuple(int(ids) for ids in regex_splitter.split(task)) for task in tasks
    ]

    n_overlap = 0
    for id_start_elf1, id_end_elf1, id_start_elf2, id_end_elf2 in tasks_splitter:
        if (id_start_elf1 <= id_start_elf2 and id_end_elf2 <= id_end_elf1) or (
            id_start_elf2 <= id_start_elf1 and id_end_elf1 <= id_end_elf2
        ):
            n_overlap += 1

    print(f"answer part 1 is: {n_overlap}")

    n_overlap = 0
    for id_start_elf1, id_end_elf1, id_start_elf2, id_end_elf2 in tasks_splitter:
        if not ((id_end_elf1 < id_start_elf2) or (id_end_elf2 < id_start_elf1)):
            n_overlap += 1

    print(f"answer part 2 is: {n_overlap}")


if __name__ == "__main__":
    main()
