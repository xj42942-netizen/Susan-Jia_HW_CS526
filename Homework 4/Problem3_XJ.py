from collections import defaultdict

def count_right_triangles(points):
    n = len(points)
    if n < 3:
        return 0
    
    count = 0
    
    for i in range(n):
        x0, y0 = points[i]
        vectors = {}
        
        for j in range(n):
            if i == j:
                continue
            
            dx = points[j][0] - x0
            dy = points[j][1] - y0
            
            if (dx, dy) not in vectors:
                vectors[(dx, dy)] = 0
            vectors[(dx, dy)] += 1
        
        vec_list = list(vectors.keys())
        for k in range(len(vec_list)):
            dx1, dy1 = vec_list[k]
            for m in range(k + 1, len(vec_list)):
                dx2, dy2 = vec_list[m]
                # Check if perpendicular: dx1*dx2 + dy1*dy2 == 0
                if dx1 * dx2 + dy1 * dy2 == 0:
                    count += vectors[(dx1, dy1)] * vectors[(dx2, dy2)]
    
    return count

# Test with files
def test_file(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())
        points = []
        for _ in range(n):
            x, y = map(int, f.readline().split())
            points.append((x, y))
        answer = count_right_triangles(points)
        print(f"{filename} -> answer: {answer}")

# Run tests
test_file('righttangles_1.txt')
test_file('rightangles_2.txt')
test_file('rightangles_3.txt')
