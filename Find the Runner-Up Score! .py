if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    #print(arr)
    arr1=[]
    arr1=[i for i in arr if i!=max(arr)]
    print(max(arr1))
