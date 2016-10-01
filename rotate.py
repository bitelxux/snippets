"""
Given a square matrix, rotate it 90 degrees clockwise
"""

def create_matrix(dim):
   indx = 0
   matrix = []
   for _ in range(dim):
      row = []
      for _ in range(dim):
         row.append("%02d" % indx)
         indx += 1
      matrix.append(row)
   return matrix

def render(what):
    for row in what:
        print row
    print "\n"

def rotate_zip():
    return zip(*matrix[::-1])
    
def inplace_rotate(m):
    rings = len(m) / 2
    size = len(m) - 1
 
    for ring in range(rings): 
        for i in range(ring, size - ring):
            pivot = m[ring][i]
            #Left -> Top
            m[ring][i] = m[size - i][ring]
            #Bottom -> left
            m[size - i][ring] = m[size - ring][size - i]
            #Right -> bottom
            m[size - ring][size - i] = m[i][size - ring]
            #Top -> Right
            m[i][size - ring] = pivot


if __name__ == "__main__":
    matrix = create_matrix(6)
    render(matrix)
    # zip method. not inplace
    m1 = rotate_zip()
    render(m1)
    # inplace method
    inplace_rotate(matrix)
    render(matrix)
 
    
