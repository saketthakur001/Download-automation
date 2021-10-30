# print(len('  *  '))

def tower_builde(n_floors, block_size):
    space = n_floors-1
    star = 1
    lis = []
    for i in range(1,n_floors+1):
        lis.append(' '*space+'*'*star+' '*space)
        space -= 1; star += 2
    print(lis)
# print(tower_builder(20))
print(len('**********************'))# len 22

def tower_builder(n_floors, block_size):
    b, l = block_size
    space = 
    lis = []
    for l1 in range(n_floors):
        for l2 in range(block_size[1]):
            print([' '*space+'*'*star+' '*space])
        star += block_size[0]*2

tower_builder(3,(2, 3))# len 10
