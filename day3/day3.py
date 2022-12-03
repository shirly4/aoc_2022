import string

def main():
    with open("input.txt", "r")  as f:
        lines = f.read().splitlines()

    all_letters=string.ascii_letters
    alphabet={letter:index for index, letter in enumerate(all_letters,1)}

    #answer 1
    answer1=0
    for rucksack in lines:
        item1=list(rucksack[0:len(rucksack)//2])
        item2=list(rucksack[len(rucksack)//2:])

        common_letter=''.join(set(item1).intersection(item2))
        answer1+=alphabet[common_letter]

    print(answer1)

    #answer 2
    answer2=0
    for elf in range (0,len(lines),3):
        common_letter=''.join(set(lines[elf]).intersection(list(lines[elf+1]),list(lines[elf+2])))
        answer2+=alphabet[common_letter]

    print(answer2)    

if __name__=="__main__":
    main()
