def main():
    with open("input.txt", "r") as f:
        grid = f.read().splitlines()

    n_col = len(grid[0])
    n_row = len(grid)
    

    n_visibles = n_col + n_row - 1 + n_col-1 + n_row-2 #Edges are visible
 
    for i in range(1, n_row-1):
        for j in range(1, n_col-1):
            tree_size = int(grid[i][j])

            is_visible_left=True
            for l in range(j-1, -1, -1):
                if int(grid[i][l]) >= tree_size:
                    is_visible_left = False
                    break
            
            is_visible_right = True
            for r in range(j+1, n_col):
                 if int(grid[i][r]) >= tree_size:
                    is_visible_right=False
                    break

            is_visible_top = True
            for t in range(i-1, -1, -1):
                if int(grid[t][j])>=tree_size:
                        is_visible_top =False
                        break

            is_visible_bottom = True
            for b in range(i+1,n_row):
                if int(grid[b][j])>=tree_size:
                        is_visible_bottom = False
                        break
            
            if any((is_visible_left, is_visible_right, is_visible_top, is_visible_bottom)):
                n_visibles+=1

    print(f"answer part 1 is: {n_visibles}") 


    max_scenic_score = 0
        
    for i in range(1, n_row-1):
        for j in range(1, n_col-1):
            tree_size = int(grid[i][j])

            scenic_tree_score = 1

            for n_trees,l in enumerate(range(j-1, -1, -1),1):
                if int(grid[i][l]) >= tree_size:
                    break
            scenic_tree_score*=n_trees
            
            for n_trees,r in enumerate(range(j+1, n_col),1):
                if int(grid[i][r]) >= tree_size:
                    break
            scenic_tree_score*=n_trees
          
            for n_trees,t in enumerate(range(i-1, -1, -1),1):
                if int(grid[t][j])>=tree_size:
                        break
            scenic_tree_score*=n_trees

            for n_trees,b in enumerate(range(i+1,n_row),1):
                if int(grid[b][j])>=tree_size:
                        break
            scenic_tree_score*=n_trees

            max_scenic_score = max_scenic_score if max_scenic_score >= scenic_tree_score else scenic_tree_score
            
    print(f"answer part 2 is: {max_scenic_score}")       

if __name__=="__main__":
    main()
