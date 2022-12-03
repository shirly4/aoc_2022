def main():
    l=open('advent_oc/day2/input.txt','r').read().splitlines()

    
    points=0
    shape_score={'X':1, 'Y':2, 'Z':3}
    A_points={'X':3,'Y':6,'Z':0} 
    B_points={'X':0,'Y':3,'Z':6} 
    C_points={'X':6,'Y':0,'Z':3} 


    for i in l:
        points+=shape_score[i[2]]
        if i[0]=='A':
            points+=A_points[i[2]]
        elif i[0]=='B':
            points+=B_points[i[2]]
        else :
            points+=C_points[i[2]]
    print(points)

    #X : perdre
    #Y : égalité
    #Z : gagner
    pts=0
    result={'X':0,'Y':3,'Z':6}
    lose={'A':3,'B':1,'C':2}
    draw={'A':1,'B':2,'C':3}
    win={'A':2,'B':3,'C':1}

    for i in l:
        pts+=result[i[2]]
        if i[2]=='X': 
            pts+=lose[i[0]]
        elif i[2]=='Y':
            pts+=draw[i[0]]
        else :
            pts+=win[i[0]]
    print(pts)



if __name__=="__main__":
    main()
