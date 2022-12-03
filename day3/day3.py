import string

def main():
    f=open('advent_oc/day3/input.txt','r').read().splitlines()
    
    #answer 1
    answer1=0
    for rucksack in f:
        item1=list(rucksack[0:len(rucksack)//2])
        item2=list(rucksack[len(rucksack)//2:])
        common_letter=''.join(set(list(item1)).intersection(list(item2)))
        alphabet=dict(enumerate(string.ascii_letters,1))
        priority=[priority for priority in alphabet if alphabet[priority]==common_letter]
        answer1+=priority[0]

    print(answer1)

    #answer 2
    answer2=0
    for elf in range (0,len(f),3):
        common_letter=''.join(set(f[elf]).intersection(list(f[elf+1])).intersection(list(f[elf+2])))
        priority=[priority for priority in alphabet if alphabet[priority]==common_letter]
        answer2+=priority[0]

    print(answer2)    

        






if __name__=="__main__":
    main()
