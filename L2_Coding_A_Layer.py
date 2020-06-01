# Model one newron with three inputs (input layer)

inputs = [1, 2, 3]
weights = [0.2, 0.8, -0.5]
bias = 2

output1 = (inputs[0] * weights[0]
           + inputs[1] * weights[1]
           + inputs[2] * weights[2]) + bias

print(output1)

# Key Points

"""
1. Every newron has its unique bias
2. What is Input layer?
   Input in theory either could be one of two things
   1. Input layer of the newral network (which is going to be a vector of values). Whatever values your are tracking. 
   For example when you try to predict server equipment vailure or not from various sensors like heat sensor, humidity senson and other 
   sensors.

   In a nut shell. Each value is from the seperate sensors
   inputs=[1,2,3]
   inputs[0]- Heat Sensor
   input[1]- Humidity Sensor
   Input[3]- Other Sensor

   2. You input to the newron could be either from the true input layer or values from output of previous newron


"""

# Model one newron with four inputs (Output layer)

inputs = [1, 2, 3, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2

output1 = (inputs[0] * weights[0]
           + inputs[1] * weights[1]
           + inputs[2] * weights[2]
           + inputs[3] * weights[3]) + bias

print(output1)

"""

  what is going to change?
  1. you are going to have one extra unique weights
  2. Do you going to have any extra biases?
     No. bcz we are only modeling single newron. It does not matter 4 newrons inputing to this newron
"""

# Model 3 newrons with 4 inputs
