def main():
    l = open('advent_oc/day1/input.txt','r').read().splitlines()
    
    cal=0
    a=[]
    for i in l:
        if i!="":
            cal+=int(i)
        else:       
            a.append(cal)
            cal=0
    a=sorted(a)
    print(max(a))
    print(sum(a[-3:]))

if __name__=="__main__":
    main()
