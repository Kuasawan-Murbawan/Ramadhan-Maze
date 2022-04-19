import queue

print("-"*72)
print("                      ・ﾟ✧ R A M A D A N  M A Z E・ﾟ✧  ")
print("-"*72)
print("\nAhmad is afraid that he will be late for tarawih. Can you help him in getting to the IIUM Mosque quickly by finding the shortest path? Jazakallah! \n0 -> Ahmad\nX -> IIUM Mosque. \n\nExample: UDRLU(Up, Down, Right, Left, Up) \n")

def createMaze2():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "X", " ", "#", " ", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "#", "#"])

    return maze


def printMaze(maze, path=""):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))
    
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()
        


def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True


def findEnd(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "X":
        global ans
        ans = moves
        printMaze(maze, moves)
        return True

    return False


# MAIN ALGORITHM (Breadth First Search)

nums = queue.Queue()
nums.put("")
add = ""
maze  = createMaze2()


def printQuestion(maze):
  for x in maze:  # outer loop  
    for i in x:  # inner loop  
        print(i, end = " ") # print the elements  
    print()  
    
printQuestion(maze)

print("\n")
userInput = input("Enter your answer: ")
print("\n\n")


while not findEnd(maze, add): 
    add = nums.get()
    #print(add)
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(maze, put):
            nums.put(put)

  
if userInput == ans:
  print ("\nCongratulations, your answer is correct!")
else:
  print ("\n Not the shortest distance. The shortest is:" + ans)


