NUMBER_OF_DISKS = 4
# we won't need number_of_moves because recursion 
#number_of_moves = 2 ** NUMBER_OF_DISKS - 1
#print(number_of_moves)
rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1)),
    'B': [],
    'C': []
}
# we won't need make_allowed_move() because recursion 
"""
def make_allowed_move(rod1, rod2):
    forward = False
    if not rods[rod2]:
        forward = True
    elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
        forward = True
    if forward:
        print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
        rods[rod2].append(rods[rod1].pop())
    else:
        print(f"Moving disk {rods[rod2][-1]} from {rod2} to {rod1}")
        rods[rod1].append(rods[rod2].pop())
    # display our progress
    print(rods, '\n')
# print(rods['A'])
#print(type(rods["A"]))
"""
def move(n, source, auxiliary, target):
    if n > 0:
        # move n - 1 disks from source to auxiliary, so they are out of the way
        move( n-1, source, target, auxiliary)
        # move the nth disk from source to target
        rods[target].append(rods[source].pop())
        # display our progress
        print(rods, '\n')
    
    # commenting down because we are going to use recursion to calculate smaller version of the same problem
    """
    for i in range(number_of_moves):
        remainder = (i + 1) % 3
        if remainder == 1:
            if n % 2 != 0:
                print(f"Move {i + 1} allowed between {source} and {target}")
                make_allowed_move(source, target)
            else:
                print(f"Move {i + 1} allowed between {source} and {auxiliary}")
                make_allowed_move(source, auxiliary)
        elif remainder == 2:
            if n % 2 != 0:
                print(f"Move {i + 1} allowed between {source} and {auxiliary}")
                make_allowed_move(source, auxiliary)
            else:    
                print(f"Move {i + 1} allowed between {source} and {target}")
                make_allowed_move(source, target)
        elif remainder == 0:
            print(f"Move {i + 1} allowed between {auxiliary} and {target}")
            make_allowed_move(auxiliary, target)
    """
# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, 'A', 'B', 'C')