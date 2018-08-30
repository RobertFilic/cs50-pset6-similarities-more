from enum import Enum


class Operation(Enum):
    """Operations"""

    DELETED = 1
    INSERTED = 2
    SUBSTITUTED = 3

    def __str__(self):
        return str(self.name.lower())


def distances(a, b):
    """Calculate edit distance from a to b"""
    # 1. Set up a list of lists
    matrix = [[None for i in range(len(b)+1)] for j in range(len(a)+1)]

    # 2. Add value for base cases (1st row/column)
    ## First position is always None
    matrix[0][0] = (0, None)

    ## 1st row and column
    for i in range(1, len(b) + 1):
        matrix[0][i] = (i, Operation.INSERTED)


    for j in range(1, len(a) + 1):
        matrix[j][0] = (j, Operation.DELETED)


    # 3. Add other values - find min of all options
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):

            if a[i-1] == b[j-1]:
                cost = matrix[i-1][j-1][0]
                operation = Operation.SUBSTITUTED
                matrix[i][j] = (cost, operation)

            else:
                # Calculate substitutin, deletion and insertion
                substitution = matrix[i - 1][j - 1][0] + 1
                deletion = matrix[i-1][j][0] + 1
                insertion = matrix[i][j-1][0] + 1

                # Compare
                compare = [deletion, insertion, substitution]
                cost = min(compare)
                op = compare.index(min(compare))
                if op == 0:
                    operation = Operation.DELETED
                if op == 1:
                    operation = Operation.INSERTED
                if op == 2:
                    operation = Operation.SUBSTITUTED

                matrix[i][j] = (cost, operation)
    return matrix

