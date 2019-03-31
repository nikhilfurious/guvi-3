class main():
    def func(self):
        a = int(input())
        l = []
        l = input().split()
        count = 0
        for i in range (0,a):
            b = int(l[i])
            if (i==b) and (i<a-1):
                print (b,end=' ')
            elif (i==b) and (i==a-1):
                print (b,end='')
            else:
                count+=1
        if (count == a):
            print (-1)

ob = main()
ob.func()