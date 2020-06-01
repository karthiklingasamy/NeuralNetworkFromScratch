inputs = [1, 2, 3, 2.5]  # vector


weights = [
    [0.2, 0.8, -0.5, 1.0],
    [0.5, -0.91, 0.26, -0.5],    # Matrix
    [-0.26, -0.27, 0.17, 0.87]

]

biases = [2, 3, 0.5]  # Vector

some_value = -0.5
weight = 0.7
bias = 0.7

print(some_value * weight)  # weights here help multiples of negative
# weights changing the magnitude

# Offset the value. Biasis will never going to impact anything negatively
print(some_value+bias)

"""
zip(weights, biases)

[0.2, 0.8, -0.5, 1.0],2
[0.5, -0.91, 0.26, -0.5],3
[-0.26, -0.27, 0.17, 0.87],0.5
"""


# Key Points
# 1. Optimizer will tune the weights and biases in an attempt to fit the data
# 2. Biasis will never going to impact anything negatively
# Activation functions- These are the functions determines the final output to another layer or output layer of the network


"""

Array:
lst=[1,5,6,2]        Shape:(4,)       Type: 1D array(Numpy),Vector (Math)
lol=[
  [1,2,3,4],
  [5,6,7,8]          shape:(2,4)      Type:2D Array(Numpy), Matrix (Math)
]

lololo=[[[1,2,3,4],
         [5,6,7,8]]
       [[5,2,1,2],
        [5,5,6,7]]    shape :(3,2,4)   Type: 3 D Array
       [[2,3,4,5],
        [3,5,7,8]]
]


"""
