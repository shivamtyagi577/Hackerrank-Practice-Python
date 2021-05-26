if __name__ == '__main__':
    N = int(input())
    lists = []
    for i in range(N) :
        inputs = input().split()
        if(inputs[0] == "pop") :
            lists.pop()
        elif(inputs[0] == "print") :
            print(lists)
        elif(inputs[0] == "reverse") :
            lists.reverse()
        elif(inputs[0] == "sort") :
            lists.sort()
        elif(inputs[0] == "append") :
            e = int(inputs[1])
            lists.append(e)
        elif(inputs[0] == "remove") :
            e = int(inputs[1])
            lists.remove(e)
        else :
            e = int(inputs[2])
            x = int(inputs[1])
            lists.insert(x,e)
