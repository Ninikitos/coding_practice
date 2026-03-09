edge_list = [(1,2), (1,3), (2,3), (2,4), (4,5), (5,6), (6,7), (7,1)]


def transform_edges(arr: list[tuple]) -> dict[int, list]:
    """
    Edge list -> adjacency list (undirected graph)

    Input:  [(1,2), (1,3), (2,3)]
    Output: {1: [2, 3], 2: [1, 3], 3: [1, 2]}

    Each edge (u, v) is added in both directions:
      u -> v  and  v -> u
    For a directed graph remove the second setdefault line.
    """
    result = {}
    for u, v in arr:
        result.setdefault(u, []).append(v)
        result.setdefault(v, []).append(u)
    return result


def transform_edges_v2(arr: list[tuple]) -> dict[int, list]:
    result = {}
    for i, el in enumerate(arr):
        if el[0] not in result:
            edges = [el[1]]
            result[el[0]] = edges
        else:
            result[el[0]].append(el[1])

        if el[1] not in result:
            edges = [el[0]]
            result[el[1]] = edges
        else:
            result[el[1]].append(el[0])
    return result


def transform_adj_list(adj_list: dict[int, list[int]]) -> list[list[int]]:
    """
    Adjacency list -> adjacency matrix

    Input:  {1: [2, 3], 2: [1, 3], 3: [1, 2]}
    Output: [[0, 1, 1],
             [1, 0, 1],
             [1, 1, 0]]

    Row i, column j = 1 if edge i->j exists, otherwise 0.

    Note: Assumes dictionary keys are strictly from 1 to N.
    """
    n = len(adj_list)
    result = []
    for i in range(1, n + 1):
        row_data = [1 if j in adj_list[i] else 0 for j in range(1, n + 1)]
        result.append(row_data)
    return result


def transform_adj_list_v2(adj_list: dict[int, list[int]]) -> list[list[int]]:
    col = row = len(adj_list) + 1
    result = []
    for i in range(1, row):
        row_data = []
        for j in range(1, col):
            if j in adj_list[i]:
                row_data.append(1)
            else:
                row_data.append(0)
        result.append(row_data)
    return result


def transform_adj_matrix(edge_matrix: list[list[int]]) -> list[tuple]:
    """
    Adjacency matrix -> edge list

    Input:  [[0, 1, 1],
             [1, 0, 1],
             [1, 1, 0]]
    Output: [(1,2), (1,3), (2,3)]

    Condition i < j — avoids duplicates like (1,2) and (2,1).
    Matrix indices start at 0, so edges are written as (i+1, j+1).
    ! For a directed graph — remove the i < j condition.
    """
    result = []
    for i in range(len(edge_matrix)):
        for j in range(len(edge_matrix[i])):
            if edge_matrix[i][j] == 1 and i < j:
                result.append((i+1, j+1))
    return result


print('Original edge list: ', edge_list)

adj_list = transform_edges(edge_list)
print('adj_list: ', adj_list)

adj_matrix = transform_adj_list(adj_list)
print('adj_matrix: ', adj_matrix)

edge_list_new = transform_adj_matrix(adj_matrix)
print('edge_list: ', edge_list_new)