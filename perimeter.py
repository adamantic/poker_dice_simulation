import sys

def calculate_perimeter(rectangles):
    # Initialize perimeter and dictionary to keep track of overlapping rectangles
    perimeter = 0
    overlaps = {}

    # Loop through rectangles and compute perimeter
    for rect in rectangles:
        perimeter += 2 * (rect[2] - rect[0] + rect[3] - rect[1])

    # Loop through pairs of rectangles and compute overlapping perimeter
    for i in range(len(rectangles)):
        for j in range(i+1, len(rectangles)):
            rect1, rect2 = rectangles[i], rectangles[j]
            # Check if rectangles overlap in x and y axis
            if rect1[0] > rect2[2] or rect1[2] < rect2[0] or rect1[1] > rect2[3] or rect1[3] < rect2[1]:
                continue
            # Check if rectangles already in overlap
            if (i, j) in overlaps or (j, i) in overlaps:
                continue
            # Compute overlapping sides and subtract from perimeter
            overlap_sides = get_overlap_sides(rect1, rect2)
            perimeter -= 2 * sum(overlap_sides)
            # Add rectangles to overlaps dictionary
            if i not in overlaps:
                overlaps[i] = []
            overlaps[i].append(j)
            if j not in overlaps:
                overlaps[j] = []
            overlaps[j].append(i)
            # Remove overlapping sides between previously overlapping rectangles
            for k in overlaps[i]:
                if k == j:
                    continue
                if overlap(rectangles[k], rect2):
                    overlap_sides = get_overlap_sides(rectangles[k], rect2)
                    perimeter += 2 * sum(overlap_sides)
            for k in overlaps[j]:
                if k == i:
                    continue
                if overlap(rectangles[k], rect1):
                    overlap_sides = get_overlap_sides(rectangles[k], rect1)
                    perimeter += 2 * sum(overlap_sides)

    return perimeter


def overlap(rect1, rect2):
    #check if the rectangles overlap
    if rect1[0] > rect2[2] or rect2[0] > rect1[2]:
        return False
    if rect1[1] > rect2[3] or rect2[1] > rect1[3]:
        return False
    return True


def get_overlap_sides(rect1, rect2):
    #find the overlapping sides
    x_overlap = min(rect1[2], rect2[2]) - max(rect1[0], rect2[0])
    y_overlap = min(rect1[3], rect2[3]) - max(rect1[1], rect2[1])
    return x_overlap, y_overlap

testa = [-15, 0, 5, 10]
testb = [-5, 8, 20, 25]

print(get_overlap_sides(testa, testb))

filename = input('Which data file do you want to use? ')
try:
    with open(filename) as file:
        rectangles = []
        for line in file:
            x1, y1, x2, y2 = map(int, line.strip().split())
            rectangles.append((x1, y1, x2, y2))
    perimeter = calculate_perimeter(rectangles)

    print("The perimeter is:",perimeter)

except FileNotFoundError:
    print('Could not open a file named', filename)
    print('Giving up...')
    sys.exit()
