import re
from collections import deque




def main():
    with open("input.txt", "r") as f:
        
        cargo_sheme, instructions = re.split(r"\n\n", f.read())


    
    instructions =[tuple(int(inst) for inst in re.findall(r'\d+', instruction)) for instruction in instructions.splitlines()]

    cargo_load = [deque() for _ in range(9)]
    batch=3
    step=1
    for stack in cargo_sheme.splitlines()[:-1]:
        for index, i in enumerate(range(0, len(stack), batch+step)):
            load = stack[i:i+batch][1]
            if load!=" ":
                cargo_load[index].appendleft(load)
    
    
    for n_crates,stack_from, stack_to in instructions:
        for _ in range(n_crates):
            crate = cargo_load[stack_from-1].pop()
            cargo_load[stack_to-1].append(crate)
    
    print("answer part 1 is:","".join(stack[-1] for stack in cargo_load))

    cargo_load = [deque() for _ in range(9)]
    batch=3
    step=1
    for stack in cargo_sheme.splitlines()[:-1]:
        for index, i in enumerate(range(0, len(stack), batch+step)):
            load = stack[i:i+batch][1]
            if load!=" ":
                cargo_load[index].appendleft(load)
    
    
    for n_crates,stack_from, stack_to in instructions:

        crate_to_move= reversed([cargo_load[stack_from-1].pop() for _ in range(n_crates)])
        cargo_load[stack_to-1].extend(crate_to_move)
        

        
    print("answer part 2 is:","".join(stack[-1] for stack in cargo_load))




    
    
   

if __name__ =="__main__":
    main()
  