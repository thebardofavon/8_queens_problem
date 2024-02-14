class StackFrontier:

    def __init__(self):
        self.frontier = []

    def add(self, state):
        self.frontier.append(state)

    def pop(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

    def empty(self):
        return len(self.frontier) == 0


class Queens:

    def __init__(self):
        self.size = 8

    def solve_iddfs(self):
        solutions = set()
        self.num_explored = 0

        for depth in range(1, self.size + 1):
            frontier = StackFrontier()
            frontier.add([])
            self.explored = set()

            while not frontier.empty():
                solution = frontier.pop()
                self.explored.add(tuple(solution))
                if self.conflict(solution):
                    continue
                row = len(solution)
                if row == self.size:
                    solutions.add(tuple(solution)) 
                    continue
                for col in range(self.size):
                    queen = (row, col)
                    queens = solution.copy()
                    queens.append(queen)
                    if (not self.conflict(queens)):
                        frontier.add(queens)
                        self.num_explored += 1
                    
        return solutions

    def conflict(self, solution):
        for i in range(1, len(solution)):
            for j in range(0, i):
                a, b = solution[i]
                x, y = solution[j]
                if a == x or b == y or abs(a - x) == abs(b - y):
                    return True
        return False
    
    def print_board(self, solutions):
        i = 1
        for solution in solutions:
            print("Solution: ", i)
            i += 1
            for row in range(8):
                print("+---" * 8 + "+")
                print("|", end="")
                for col in range(8):
                    if (row, col) in solution:
                        print(" Q |", end="")
                    else:
                        print("   |", end="")
                print()
            
            print("+---" * 8 + "+")
            print("\n\n")


def main():
    queens = Queens()
    solutions = queens.solve_iddfs()
    print("Using Iterative Deepening Depth-First Search...")
    queens.print_board(solutions)
    # print(solutions)
    print("No.of solutions: ", len(solutions))
    print("No.of states explored: ", queens.num_explored)
    print("No.of states in explored set: ", len(queens.explored))


if __name__ == "__main__":
    main()
