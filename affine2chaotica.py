# Format a b c d e f p -> [a, b// c, d][x//y]+[e//f] where p is the probability weight

# Barnsley Fern affine transformations
# function_set = [[0.0, 0.0, 0.0, 0.16, 0.0, 0.0, 0.01],
#                 [0.85, 0.04, -0.04, 0.85, 0.0, 1.6, 0.85],
#                 [0.2, -0.26, 0.23, 0.22, 0.0, 1.6, 0.07],
#                 [-0.15, 0.28, 0.26, 0.24, 0.0, 0.44, 0.07]]

# Joe affine transformations
# function_set = [[0, 0.053, -0.629, 0, -5.283, 4.03, 1/12],
#                 [0.143, 0, 0, -0.053, -5.619, 8.513, 1/12],
#                 [0.143, 0, 0,  0.083, -5.619, 3.057, 1/12],
#                 [0, 0.053, 0.129, 0, -6.952, 4.73, 1/12],
#                 [-0.0123806, -0.0649723, 0.523819, 0.00189797, -2.555, 7.235, 1/12],
#                 [-0.0123806, -0.0649723, 0.523819, 0.00189797, -1.226, 7.235, 1/12],
#                 [0.104432, 0.00529117,  0.0570516, 0.0527352, -2, 8.113, 1/12],
#                 [0.104432, 0.00529117,  0.0570516, 0.0527352, -2, 3.113, 1/12],
#                 [-0.0123806, -0.0649723, 0.523819, 0.00189797, 0.25, 7.235, 1/12],
#                 [0.093, 0, 0, 0.053, 0.861, 7.536, 1/12],
#                 [0.093, 0, 0, 0.053, 0.861, 5.536, 1/12],
#                 [0.093, 0, 0, 0.053, 0.861, 3.536, 1/12]]

function_set = [[0, 0.053, -0.429, 0, -7.083, 5.43, 1/19],
                [0.143, 0, 0, -0.053, -5.619, 8.513, 1/19],
                [0.143, 0, 0, 0.083, -5.619, 2.057, 1/19],
                [0, 0.053, 0.429, 0, -3.952, 5.43, 1/19],
                [0.119, 0, 0, 0.053, -2.555, 4.536, 1/19],
                [-0.0123806, -0.0649723, 0.423819, 0.00189797, -1.226, 5.235, 1/19],
                [0.0852291, 0.0506328,   0.420449, 0.0156626, -0.421, 4.569, 1/19],
                [0.104432, 0.00529117,  0.0570516, 0.0527352, 0.976, 8.113, 1/19],
                [-0.00814186, -0.0417935,   0.423922, 0.00415972, 1.934, 5.37, 1/19],
                [0.093, 0, 0, 0.053, 0.861, 4.536, 1/19],
                [0, 0.053, -0.429, 0, 2.447, 5.43, 1/19],
                [0.119, 0, 0, -0.053, 3.363, 8.513, 1/19],
                [0.119, 0, 0, 0.053, 3.363, 1.487, 1/19],
                [0, 0.053, 0.429, 0, 3.972, 4.569, 1/19],
                [0.123998, -0.00183957, 0.000691208, 0.0629731, 6.275, 7.716, 1/19],
                [0, 0.053, 0.167, 0, 5.215, 6.483, 1/19],
                [0.071, 0, 0, 0.053, 6.279, 5.298, 1/19],
                [0, -0.053, -0.238, 0, 6.805, 3.714, 1/19],
                [-0.121, 0, 0, 0.053, 5.941, 1.487, 1/19]]

import numpy as np

# Calculates the angle between two vectors in degrees
def angle(vector_1, vector_2):
    vector_1 = np.array(vector_1)
    vector_2 = np.array(vector_2)
    # Calculate signed angle between vectors
    # Using answer https://stackoverflow.com/questions/2150050/finding-signed-angle-between-vectors by Derek Ledbetter
    angle = np.rad2deg(np.arctan2( vector_1[0]*vector_2[1] - vector_1[1]*vector_2[0], vector_1[0]*vector_2[0] + vector_1[1]*vector_2[1] ))
    return angle

# Calculates the affine transformation
def affine_transformation(f, c0, c1):
    x = c0 * f[0] + c1 * f[1]
    y = c0 * f[2] + c1 * f[3]
    return [x, y]

for i in range(len(function_set)):
# calculate length and angle for the unit square x vector
    x = affine_transformation(function_set[i], 1, 0)

    length_x = np.linalg.norm(x)

    angle_x = angle(x, [1,0])

    translation_x = function_set[i][4]

    # calculate length and angle for the unit square y vector
    y = affine_transformation(function_set[i], 0, 1)

    length_y = np.linalg.norm(y)

    angle_y = angle(y, [0,1])
    angle_y = angle_y + 90

    translation_y = -function_set[i][5]

    print("Transform #{}".format(i+1))
    print("Length x: {}, angle x: {}, translation x: {}".format(length_x, angle_x, translation_x))
    print("Length y: {}, angle y: {}, translation y: {}".format(length_y, angle_y, translation_y))
