# Creating data set
# EMPTY SQUARE
a =". . . . . . . . . . . . . . . . . . . .\
    . . . . . . . . . . . . . . . . . . . .\
    . . . . . . . . . . . . . . . . . . . .\
    . . . . . . . . . . . . . . . . . . . .\
    . . . . . . . # # # # . . . . . . . . .\
    . . . . . . . # . . # . . . . . . . . .\
    . . . . . . . # . . # . . . . . . . . .\
    . . . . . . . # # # # . . . . . . . . .\
    . . . . . . . . . . . . . . . . . . . .\
    . . . . . . . . . . . . . . . . . . . ."
# FILLED SQUARE
b =". . . . . . . . . . . . . . . . . . . .\
    . . . . . . . . . . . . . . . . . . . .\
    . . . . # . . . . . . . . . . . . . . .\
    . . . # # # . . . . . . . . . . . . . .\
    . . # # # # # . . . . . . . . . . . . .\
    . . . # # # . . . . . . . . . . . . . .\
    . . . . # . . . . . . . . . . . . . . .\
    . . . . . . . . . . . . . . . . . . . .\
    . . . . . . . . . . . . . . . . . . . .\
    . . . . . . . . . . . . . . . . . . . ."
# FILLED RECTANGLE
c =". . . . . . . . . . . . . . . . . . . .\
    . . . . . . . . . . . . . . . . . . . .\
    . . . . . . . # # # # # . . . . . . . .\
    . . . . . . . # # # # # . . . . . . . .\
    . . . . . . . # # # # # . . . . . . . .\
    . . . . . . . # # # # # . . . . . . . .\
    . . . . . . . # # # # # . . . . . . . .\
    . . . . . . . # # # # # . . . . . . . .\
    . . . . . . . # # # # # . . . . . . . .\
    . . . . . . . . . . . . . . . . . . . ."
# EMPTY RECTANGLE
d =". . . . . . . . . . . . . . . . . . . .\
    . . . . . . . . . . . . . . . . . . . .\
    . . . . . . . # # # # # . . . . . . . .\
    . . . . . . . # . . . # . . . . . . . .\
    . . . . . . . # . . . # . . . . . . . .\
    . . . . . . . # . . . # . . . . . . . .\
    . . . . . . . # . . . # . . . . . . . .\
    . . . . . . . # . . . # . . . . . . . .\
    . . . . . . . # # # # # . . . . . . . .\
    . . . . . . . . . . . . . . . . . . . ."
# EMPTY TRIANGLE
e =". . . . . . . . . . . . . . . . . . . .\
    . . . . . # . . . . . . . . . . . . . .\
    . . . . . # # . . . . . . . . . . . . .\
    . . . . . # . # . . . . . . . . . . . .\
    . . . . . # . . # . . . . . . . . . . .\
    . . . . . # # # # # . . . . . . . . . .\
    . . . . . . . . . . . . . . . . . . . .\
    . . . . . . . . . . . . . . . . . . . .\
    . . . . . . . . . . . . . . . . . . . .\
    . . . . . . . . . . . . . . . . . . . ."
# FILLED TRIANGLE
f =". . . . . . . . . . . . . . . . . . . .\
    . . . . . . . . . . . . . . . . . . . .\
    . . . . . . . . . . . # # # # # # # . .\
    . . . . . . . . . . . . # # # # # . . .\
    . . . . . . . . . . . . . # # # . . . .\
    . . . . . . . . . . . . . . # . . . . .\
    . . . . . . . . . . . . . . . . . . . .\
    . . . . . . . . . . . . . . . . . . . .\
    . . . . . . . . . . . . . . . . . . . .\
    . . . . . . . . . . . . . . . . . . . ."
# Creating labels
y =[[1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1]]

import numpy as np
import matplotlib.pyplot as plt

A=[1 if x=="#" else 0 for x in a.split()]
B=[1 if x=="#" else 0 for x in b.split()]
C=[1 if x=="#" else 0 for x in c.split()]
D=[1 if x=="#" else 0 for x in d.split()]
E=[1 if x=="#" else 0 for x in e.split()]
F=[1 if x=="#" else 0 for x in f.split()]
'''
# visualizing the data, and plotting shape.
for char in [A,B,C,D,E,F]:
    plt.imshow(np.array(char).reshape(10,20))
    plt.show()
'''

# converting data and labels into numpy array
"""
Convert the matrix of 0 and 1 into one hot vector 
so that we can directly feed it to the neural network,
these vectors are then stored in a list x.
"""
x =[np.array(A).reshape(1, 200), np.array(B).reshape(1, 200), 
    np.array(C).reshape(1, 200), np.array(D).reshape(1, 200),
    np.array(E).reshape(1, 200), np.array(F).reshape(1, 200)]
 
# Labels are also converted into NumPy array
y = np.array(y)

# activation function
 
def sigmoid(x):
    return(1/(1 + np.exp(-x)))
   
# Creating the Feed forward neural network
# 1 Input layer(1, 200)
# 1 hidden layer (1, 10)
# 1 output layer(6, 6)
 
def f_forward(x, w1, w2):
    # hidden
    z1 = x.dot(w1)# input from layer 1 
    a1 = sigmoid(z1)# out put of layer 2 
     
    # Output layer
    z2 = a1.dot(w2)# input of out layer
    a2 = sigmoid(z2)# output of out layer
    return(a2)

# initializing the weights randomly
def generate_wt(x, y):
    l =[]
    for i in range(x * y):
        l.append(np.random.randn())
    return(np.array(l).reshape(x, y))
     
# for loss we will be using mean square error(MSE)
def loss(out, Y):
    s =(np.square(out-Y))
    s = np.sum(s)/len(y)
    return(s)
   
# Back propagation of error 
def back_prop(x, y, w1, w2, alpha):
     
    # hidden layer
    z1 = x.dot(w1)# input from layer 1 
    a1 = sigmoid(z1)# output of layer 2 
     
    # Output layer
    z2 = a1.dot(w2)# input of out layer
    a2 = sigmoid(z2)# output of out layer
    # error in output layer
    d2 =(a2-y)
    d1 = np.multiply((w2.dot((d2.transpose()))).transpose(), (np.multiply(a1, 1-a1)))
 
    # Gradient for w1 and w2
    w1_adj = x.transpose().dot(d1)
    w2_adj = a1.transpose().dot(d2)
     
    # Updating parameters
    w1 = w1-(alpha*(w1_adj))
    w2 = w2-(alpha*(w2_adj))
     
    return(w1, w2)

def train(x, Y, w1, w2, alpha = 0.01, epoch = 10):
    acc =[]
    losss =[]
    for j in range(epoch):
        l =[]
        for i in range(len(x)):
            out = f_forward(x[i], w1, w2)
            l.append((loss(out, Y[i])))
            w1, w2 = back_prop(x[i], y[i], w1, w2, alpha)
        #print("epochs:", j + 1, "======== acc:", (1-(sum(l)/len(x)))*100)   
        acc.append((1-(sum(l)/len(x)))*100)
        losss.append(sum(l)/len(x))
    return(acc, losss, w1, w2)
  
def predict(x, w1, w2):
    Out = f_forward(x, w1, w2)
    maxm = 0
    k = 0
    for i in range(len(Out[0])):
        if(maxm<Out[0][i]):
            maxm = Out[0][i]
            k = i
    if(k == 0):
        print("Image is EMPTY SQUARE.")
    elif(k == 1):
        print("Image is FILLED SQUARE.")
    elif(k == 2):
        print("Image is FILLED RECTANGLE.")
    elif(k == 3):
        print("Image is EMPTY RECTANGLE.")
    elif(k == 4):
        print("Image is EMPTY TRIANGLE.")
    else:
        print("Image is FILLED TRIANGLE.")
    plt.imshow(x.reshape(10, 20))
    plt.show()

w1 = generate_wt(200, 10)
w2 = generate_wt(10, 6)
"""The arguments of train function are data set list x, 
correct labels y, weights w1, w2, learning rate = 0.1, 
no of epochs or iteration.The function will return the
matrix of accuracy and loss and also the matrix of 
trained weights w1, w2"""
 
acc, losss, w1, w2 = train(x, y, w1, w2, 0.1, 100)

import matplotlib.pyplot as plt1
'''
# plotting accuracy
plt1.plot(acc)
plt1.ylabel('Accuracy')
plt1.xlabel("Epochs:")
plt1.show()
 
# plotting Loss
plt1.plot(losss)
plt1.ylabel('Loss')
plt1.xlabel("Epochs:")
plt1.show()
'''

"""
The predict function will take the following arguments:
1) image matrix
2) w1 trained weights
3) w2 trained weights
"""
predict(x[1], w1, w2)
