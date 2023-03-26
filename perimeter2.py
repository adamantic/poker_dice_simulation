def calculate_perimeter(rectangles):
    perimeter = 0
    for i, rect1 in enumerate(rectangles):
        for rect2 in rectangles[i+1:]:
            if overlap(rect1, rect2):
                overlap_sides = get_overlap_sides(rect1, rect2)
                perimeter -= sum(overlap_sides)
    for rect in rectangles:
        perimeter += 2 * (rect[2] - rect[0] + rect[3] - rect[1])
    return perimeter


def overlap(rect1, rect2):
    return (rect1[0] < rect2[2] and rect1[2] > rect2[0] and
            rect1[1] < rect2[3] and rect1[3] > rect2[1])


def get_overlap_sides(rect1, rect2):
    sides = []
    if rect1[0] < rect2[0]:  # rect1 left of rect2
        sides.append(min(rect1[2], rect2[2]) - rect2[0])
    else:  # rect1 right of rect2
        sides.append(rect2[2] - max(rect1[0], rect2[0]))
    if rect1[1] < rect2[1]:  # rect1 above rect2
        sides.append(min(rect1[3], rect2[3]) - rect2[1])
    else:  # rect1 below rect2
        sides.append(rect2[3] - max(rect1[1], rect2[1]))
    return sides


if __name__ == '__main__':
    filename = input('Which data file do you want to use? ')
    rectangles = []
    with open(filename, 'r') as f:
        for line in f:
            x1, y1, x2, y2 = map(int, line.split())
            rectangles.append((x1, y1, x2, y2))
    perimeter = calculate_perimeter(rectangles)
    print('The perimeter is:', perimeter)