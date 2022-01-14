import numpy as np


# A function for converting the matrix below into a Markov matrix (all the rows add to 1)
def markov_converter(input_matrix):
    for i in range(len(input_matrix)):
        # The sum of all of the value points that are leaving the type state
        total_outgoing = 0.0
        for j in range(len(input_matrix)):
            if input_matrix[i, j] != 72.0:
                total_outgoing = total_outgoing + input_matrix[i, j]
        # All the value points that are being kept
        input_matrix[i, i] = 72.0 - total_outgoing
    scalar = 1.0 / 72.0
    input_matrix = float(scalar) * input_matrix
    return input_matrix


# Multiplying an initial vector by a Markov matrix a bunch of times until it reaches equilibrium
def markov_analysis(type_matrix, repeats=5000):
    start = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    for i in range(repeats):
        start = start @ type_matrix
    return start


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # For this matrix, the row is the attacking type, column is defensive
    #                   nrm  fir  wtr  ele  grs  ice  fig  psn  grd  fly  psy  bug  roc  gho  dra  drk  stl  fai
    types = np.matrix([[72.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 1.0, 0.0, 2.0, 2.0, 1.0, 2.0],
                       [2.0, 72.0, 1.0, 2.0, 4.0, 4.0, 2.0, 2.0, 2.0, 2.0, 2.0, 4.0, 1.0, 2.0, 1.0, 2.0, 4.0, 2.0],
                       [2.0, 4.0, 72.0, 2.0, 1.0, 2.0, 2.0, 2.0, 4.0, 2.0, 2.0, 2.0, 4.0, 2.0, 1.0, 2.0, 2.0, 2.0],
                       [2.0, 2.0, 4.0, 72.0, 1.0, 2.0, 2.0, 2.0, 0.0, 4.0, 2.0, 2.0, 2.0, 2.0, 1.0, 2.0, 2.0, 2.0],
                       [2.0, 1.0, 4.0, 2.0, 72.0, 2.0, 2.0, 1.0, 4.0, 1.0, 2.0, 1.0, 4.0, 2.0, 1.0, 2.0, 1.0, 2.0],
                       [2.0, 1.0, 1.0, 2.0, 4.0, 72.0, 2.0, 2.0, 4.0, 4.0, 2.0, 2.0, 2.0, 2.0, 4.0, 2.0, 1.0, 2.0],
                       [4.0, 2.0, 2.0, 2.0, 2.0, 4.0, 72.0, 1.0, 2.0, 1.0, 1.0, 1.0, 4.0, 0.0, 2.0, 4.0, 4.0, 1.0],
                       [2.0, 2.0, 2.0, 2.0, 4.0, 2.0, 2.0, 72.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 2.0, 2.0, 0.0, 4.0],
                       [2.0, 4.0, 2.0, 4.0, 1.0, 2.0, 2.0, 4.0, 72.0, 0.0, 2.0, 1.0, 4.0, 2.0, 2.0, 2.0, 4.0, 2.0],
                       [2.0, 2.0, 2.0, 1.0, 4.0, 2.0, 4.0, 2.0, 2.0, 72.0, 2.0, 4.0, 1.0, 2.0, 2.0, 2.0, 1.0, 2.0],
                       [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 4.0, 4.0, 2.0, 2.0, 72.0, 2.0, 2.0, 2.0, 2.0, 0.0, 1.0, 2.0],
                       [2.0, 1.0, 2.0, 2.0, 4.0, 2.0, 1.0, 1.0, 2.0, 1.0, 4.0, 72.0, 2.0, 1.0, 2.0, 4.0, 1.0, 1.0],
                       [2.0, 4.0, 2.0, 2.0, 2.0, 4.0, 1.0, 2.0, 1.0, 4.0, 2.0, 4.0, 72.0, 2.0, 2.0, 2.0, 1.0, 2.0],
                       [0.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 4.0, 2.0, 2.0, 72.0, 2.0, 1.0, 2.0, 2.0],
                       [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 72.0, 2.0, 1.0, 0.0],
                       [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 1.0, 2.0, 2.0, 2.0, 4.0, 2.0, 2.0, 4.0, 2.0, 72.0, 2.0, 1.0],
                       [2.0, 1.0, 1.0, 1.0, 2.0, 4.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 4.0, 2.0, 2.0, 2.0, 72.0, 4.0],
                       [2.0, 1.0, 2.0, 2.0, 2.0, 2.0, 4.0, 1.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 4.0, 4.0, 1.0, 72.0]])
    # The type matrix is transposed because we want each column to show how many points it gets from every other type
    # Right now the row shows how many points it gets from every other type
    # Transposing it is easier than rewriting the whole matrix
    returned = markov_analysis(markov_converter(types.T))
    returned.sort()
    # The values sorted from lowest to greatest
    # The values with their types are in the comment below
    print(returned)

# nrm 0.04875765 fir 0.06125141 wtr 0.06101428 ele 0.05596097 grs 0.0468558 ice 0.05096011 fig 0.05544622
# psn 0.05277598 grd 0.06252834 fly 0.05735752 psy 0.04973326 bug 0.04828049 roc 0.05353046
# gho 0.06087448 dra 0.05023632 drk 0.05396784 stl 0.06944522 fai 0.06102366
