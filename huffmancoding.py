class Knot():

	def __init__(self, value):
		self.value = value
		self.character = None
		self.right_branch = None
		self.left_branch = None

class Tree():

	def __init__(self):
		self.root = None


def order_knots(array):#orders knots according to their values

    if len(array) <= 1:
        return array

    pivot_index = len(array)-1
    array[0], array[-1] = array[-1], array[0]
    size_border = 0
    
    for i in range(len(array)-1):
        if array[i].value<array[pivot_index].value:
            array[i], array[size_border] = array[size_border], array[i]
            size_border += 1

    array[pivot_index], array[size_border] = array[size_border], array[pivot_index]
    pivot_index = size_border

    return(order_knots(array[:pivot_index]) + [array[pivot_index]] + order_knots(array[pivot_index+1:]))


def new_knot(knots):#makes a new knot with branches folded from two knots with the lowest values
	if len(knots) < 2:
		return None
	new_knot = Knot(knots[-1].value+knots[-2].value)
	new_knot.left_branch = knots[-1]
	new_knot.right_branch = knots[-2]
	del knots[-1:-3:-1]
	knots.append(new_knot)
	return knots


def print_knots(knots):
	for knot in knots:
		print(knot.value, knot.character)
	print('\n')


chars = ['e','i','a','t','s','p','n']
frequency = [15,12,10,4,3,13,1]

knots = [] #adds Knots objects into the list, sets knot's value and character
for i in range(len(chars)):
	knots.append(Knot(frequency[i]))
	knots[-1].character = chars[i]

while len(knots) >= 2:
	knots = order_knots(knots)[::-1]
	knots = new_knot(knots)

print_knots(knots)


# print_knots(knots)
# knots = order_knots(knots)[::-1]
# print_knots(knots)
# knots = new_knot(knots)
# print_knots(knots)
# knots = order_knots(knots)[::-1]
# print_knots(knots)