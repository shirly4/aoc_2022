import bisect


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    # part1
    max_cal = 0
    cal_sum=0
    for line in lines:
        if line:
            cal_sum+=int(line)
        else:
            max_cal = max_cal if max_cal>cal_sum else cal_sum
            cal_sum=0
    print(f"answer part 1 is: {max_cal}")


    # part2
    cal_sum_list=[]
    cal_sum=0
    for line in lines:
        if line:
            cal_sum+=int(line)
        else:
            cal_sum_list.append(cal_sum)
            cal_sum=0
    top3_sum = sum(sorted(cal_sum_list)[-3:])

    print(f"answer part 2 is: {top3_sum}")

    # part2 a little more efficient
    top3_sum_list = [0,0,0]
    cal_sum=0
    for line in lines:
        if line:
            cal_sum+=int(line)
        else:
            if cal_sum>top3_sum_list[0]: # work without the condition but it is litte more efficient to avoid 
                                 # the call of the function insort when the result is obvious
                                 # moreover the top3_sum will contain number bigger and bigger 
                                # hence the case when a sum will not be top3 will be higher
                                # so we are skipping a lot of function calls with the price of an extra check
                bisect.insort(top3_sum_list, cal_sum)
                top3_sum_list = top3_sum_list[1:]
            cal_sum=0
    top_3_sum_bonus = sum(top3_sum_list)
    print(f"answer part 2 bonus is: {top_3_sum_bonus}")

if __name__ == "__main__":
    main()
