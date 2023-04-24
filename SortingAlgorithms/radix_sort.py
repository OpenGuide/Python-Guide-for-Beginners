def radixsort(array, radix=10):
    cont = False
    placement = 1

    # sort by unsigned numeric value
    while cont:
        cont = False
        # prepare empty buckets
        buckets = [list() for _ in range(radix)]

        # put numbers into buckets
        for i in array:
            buckets[(i // placement) % radix].append(i)
            # if there are numbers outside the current placement continue
            if i > placement:
                cont = True

        # rejoin buckets
        array = list()
        list(map(array.extend, buckets))

        # advance placement
        placement *= radix

    # sort by sign
    return [x for x in array if x < 0] + [x for x in array if x >= 0]

radixsort([1, 6, 5, 0, 11, -1, -25, 2, 4, -23, 6, 11, -11, -24, 29, -1, -101, 8, 6])
radixsort([-80, -89, -40, -24, 44, -55, -62, 66, -6, -6, 25, 98, -54, -54, 71, 86])
