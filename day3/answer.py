import string


def main():
    with open("input.txt", "r") as f:
        rucksacks = f.read().splitlines()
    alphabet = string.ascii_letters

    priorites_mapping = {letter:index for index, letter in enumerate(alphabet, 1)}


    sum_priorities=0
    for rucksack in rucksacks:

        compart1 = set(rucksack[:len(rucksack)//2])
        compart2 = set(rucksack[len(rucksack)//2:])

      
        sum_priorities+=sum(priorites_mapping[common_letter] for common_letter in compart1&compart2)
    print(f"answer part 1 is : {sum_priorities}")

    sum_priorities=0
    batch = 3
    for i in range(0,len(rucksacks), batch):
        sum_priorities+=sum(priorites_mapping[common_letter] for common_letter in set.intersection(*map(set,rucksacks[i:i+batch])))
     
    print(f"answer part 2 is : {sum_priorities}")


if __name__ =="__main__":
    main()
  

    
    
