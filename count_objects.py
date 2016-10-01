bitmap = ["            ********         ",
          "          **        **       ",
          "         *      *      *     ",
          "     ****    *** ***    *    ",
          "         *      *      *     ",
          "  *       **         **      ",
          "            *********        "]

def belongs_to(object, row, col):
    for bit in object:

        R, C = bit[0], bit[1]

        if row-1 == R and \
            (col-1 == C or \
             col+1 == C or \
             col == C):
            return True

        if row == R and col-1 == C:
            return True

def get_parents(objects, row, col):
    return [i for i in range(len(objects)) if belongs_to(objects[i],
                                                         row, col)]

def resolv(bitmap):
    objects = []
    for row in range(len(bitmap)):
        for col in range(len(bitmap[0])):
            if bitmap[row][col] != '*':
                continue
            parents = get_parents(objects, row, col)
            if len(parents) > 1:
                # merge
                for parent in parents[1:]:
                    print "Merging %s into %s" %(objects[parent],
                                                 objects[parents[0]])
                    objects[parents[0]].extend(objects[parent])
                    objects[parents[0]].append([row, col])
                    del objects[parent]
            elif len(parents) == 1:
                objects[parents[0]].append([row, col])
            else:
                objects.append([[row, col]])

    return len(objects)

if __name__ == "__main__":
    objects = resolv(bitmap) 
    print "Different objects: %d" % objects
    assert objects == 3
