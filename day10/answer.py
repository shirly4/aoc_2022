def main():
    with open("input.txt", "r") as f:
        instructions = list(map(lambda x:x.split(), f.read().strip().splitlines()))

    #print(sum(int(instruc[1]) for instruc in instructions[:20] if len(instruc)>1))
    
  
    x_value = [1]
    for i,instruc in enumerate(instructions):
        if len(instruc)>1:
            x_value.append(x_value[-1])
            x_value.append(x_value[-1]+int(instruc[1]))

        else:
            x_value.append(x_value[-1])
    answer_1 = sum(((i*40)+20)*x_value[((i*40)+20)-1] for i in range(6))
    print(f"answer part 1 is: {answer_1}")

    x_value = 1
    cycle = 0
    drawing = ['','', '', '', '', '']
  
    for instruc in instructions:
        cycle+=1 #start cycle
        # draw at position cycle - 1

        if x_value - 1 <= (cycle - 1)%40 <=x_value+1:
            drawing[(cycle-1)// 40]+="#"
        else:
            drawing[(cycle-1) // 40]+="-"        
        if len(instruc) >1:
            #new cycle 
            cycle+=1
            #draw at position cycle - 1
            if x_value - 1 <= (cycle - 1)%40 <=x_value+1:
                drawing[(cycle-1)// 40]+="#"
            else:
                drawing[(cycle-1) // 40]+="-"
            # finish executing instruction
            x_value+= int(instruc[1])
            pass
        else:
            pass
       


    answer_2 = "\n".join(drawing)

    print(f"answer part 2 is:\n{answer_2}")
if __name__=="__main__":
    main()
