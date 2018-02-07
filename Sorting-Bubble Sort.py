#Sorting: Bubble Sort


n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))


def bubblesort(n, a):
    swaps = 0
    for i in range (0,(n-1)):
        for j in range(0,(n-1-i)):
                    if (a[j]>a[j+1]):
                        a[j],a[j+1] = a[j+1],a[j]
                        swaps+=1

    print('Array is sorted in %d swaps.' %swaps)
    return a


myarr = bubblesort(n,a)

print('First Element: '+str(myarr[0]))
print('Last Element: '+str(myarr[n-1]))
