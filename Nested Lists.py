if __name__ == '__main__':
    sub_list=[]
    records=[]
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        sub_list.append(name)
        sub_list.append(score)
        records.append(sub_list)
        sub_list=[]
    
    
    #print(records)
    second_lowest=sorted(list(set([x[1] for x in records])))[1]
    print(second_lowest)
    second_students=sorted([s for s,g in records if g==second_lowest])
    for s in second_students:
        print(s)
    

