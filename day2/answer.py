OUTCOME_PART1_MAPPING = {
    ("A", "X"): 4,   
    ("B", "X"): 1,
    ("C", "X"): 7,
    ("A", "Y"): 8,
    ("B", "Y"): 5,
    ("C", "Y"): 2,
    ("A", "Z"): 3,
    ("B", "Z"): 9,
    ("C", "Z"): 6    
}

OUTCOME_PART2_MAPPING = {
    ("A", "X"):3,
    ("A", "Y"):4,
    ("A", "Z"):8,
    ("B", "X"):1,
    ("B", "Y"):5,
    ("B", "Z"):9,
    ("C", "X"):2,
    ("C", "Y"):6,
    ("C", "Z"):7,
}

def main():
    with open("input.txt", "r") as f:
        rounds = f.read().splitlines()

    my_points = 0
    for rond in rounds:
        my_points+=OUTCOME_PART1_MAPPING[tuple(rond.split())] 

    print(f"answer part 1 is: {my_points}")

    my_points=0
    for rond in rounds:
        my_points+=OUTCOME_PART2_MAPPING[tuple(rond.split())] 
        

    print(f"answer part 2 is: {my_points}")


if __name__ == "__main__":
    main()