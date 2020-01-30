def saddle_points(matrix):
    if len(set(len(i) for i in matrix)) not in [0, 1]:
        raise ValueError("please provide proper input")
    else:
        matrix_transpose = list(zip(*matrix))
        saddles_list = []
        for n_row, row in enumerate(matrix):
            for n_col, col in enumerate(matrix_transpose):
                if max(row) == min(matrix_transpose[n_col]):
                    saddle_dict = dict()
                    saddle_dict['row'] = n_row + 1
                    saddle_dict['column'] = n_col + 1
                    saddles_list.append(saddle_dict)
    return saddles_list if len(saddles_list) != 0 else [dict()]


