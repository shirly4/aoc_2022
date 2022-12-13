def main():
    with open("input.txt", "r") as f:
        signal = f.read().strip()

    # part1
    window = 4
    for i in range(0, len(signal) - window):
        if len(set(signal[i : i + window])) == window:
            index = i + window
            break
    print(f"answer part 1 is: {index}")

    # other method
    index = next(
        window + i
        for i in range(0, len(signal) - window)
        if len(set(signal[i : i + window])) == window
    )
    print(f"answer part 1 other method is: {index}")

    # part2
    window = 14
    for i in range(index, len(signal) - window):
        if len(set(signal[i : i + window])) == window:
            index2 = i + window
            break
    print(f"answer part 2 is: {index2}")

    # other method
    index2 = next(
        window + i
        for i in range(index, len(signal) - window)
        if len(set(signal[i : i + window])) == window
    )
    print(f"answer part 2 other method is: {index2}")


if __name__ == "__main__":
    main()
