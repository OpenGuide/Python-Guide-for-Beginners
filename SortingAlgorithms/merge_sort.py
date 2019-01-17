def mergeSort ( iplist ):
    if len( iplist )>  1:
        mid = len( iplist )//2
        lefthalf = iplist[:mid]
        righthalf = iplist[mid:]

        mergeSort( lefthalf )
        mergeSort( righthalf )

        i=0
        j=0
        k=0
        while i < len( lefthalf ) and j < len( righthalf ):
            if lefthalf[i] < righthalf[j]:
                iplist[k] = lefthalf[i]
                i = i+1
            else:
                iplist[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len( lefthalf ):
            iplist[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len( righthalf ):
            iplist[k] = righthalf[j]
            j = j+1
            k = k+1

print "Enter numbers to be sorted (seperated by space)"
iplist = map( int, raw_input().split() )

mergeSort( iplist )
print iplist
