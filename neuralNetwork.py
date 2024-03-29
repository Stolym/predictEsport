import numpy as np
import random
import matplotlib.pyplot as plt
import dataFormatter as ffd
#import fakedata as ffd
import time
import lstm_ricky as lry

class HiddenLayer:
    def __init__(self, size, batch, dropout = 0, activation = "sigmoid"):
        self.size = size
        self.batch = batch
        self.current_activation = []
        self.weights = []
        self.bias = []
        self.dropout = dropout
        self.activation = activation
        self.function_activation = {
            "sigmoid": self.sigmoid,
            "relu": self.relu,
        }
        self.function_dactivation = {
            "sigmoid": self.derivate_sigmoid,
            "relu": self.derivate_relu,
        }
        self.preMount()

    def preMount(self):
        self.weights = (np.random.rand(self.batch, self.size) * 2) - 1
        self.bias = np.random.randint(1, 5, size=(self.batch, self.size))

    def derivate_tanh(self, x):
        return 1-np.tanh(x)**2

    def derivate_relu(self, x):
        x[x < 0] = 0
        x[x > 0] = 1
        return x
    def derivate_sigmoid(self, x):
        return x*(1-x)
    def tanh(self, x):
        return np.tanh(x)
    def relu(self, x):
        x[x < 0] = 0
        return x
    def sigmoid(self, x):
        return 1/(1 + np.exp(-x))

    def mountForward(self, x):
        self.current_activation = self.function_activation.get(self.activation, "error function not find")(np.dot(x, self.weights))

    def mountBackward(self, y):
        print(self.current_activation.T)
        print((self.current_activation - y) * 2)
        print(self.function_dactivation.get(self.activation, "error function not find")((self.current_activation - y) * 2) * 0.01)
        self.weights_delta = np.dot(self.current_activation.T, self.function_dactivation.get(self.activation, "error function not find")((self.current_activation - y) * 2) * 0.01)
        self.weights += self.weights_delta


class NeuralNetwork:
    def __init__(self, params):
        self.mountLayer(params)
        self.losses = []
        self.cost = []
        self.accurency = []

    def mountLayer(self, params):
        self.layer={}
        self.activations = params["activation"]
        #print(self.activations)
        for i in range(1, len(params["size"])):
            self.layer["W"+str(i)] = np.array(np.random.rand(params["size"][i], params["size"][i - 1]), dtype=np.float64) * 2 - 1
            self.layer["B"+str(i)] = np.array(np.zeros((params["size"][i],1)), dtype=np.float64)

    def backpropLayer(self, i):
        _DA = self.layer["DA"+str(i)]
        W = self.layer["W"+str(i)]
        Z = self.layer["Z"+str(i)]
        _A = self.layer["A"+str(i - 1)]
        activation =  self.activations[i]
        if (activation == "relu"):
            self.layer["DZ"+str(i)] = self.derivate_relu(_DA, Z)
            self.layer["DW"+str(i)] = np.dot(self.layer["DZ"+str(i)], _A.T)/_A.shape[0]
            self.layer["DB"+str(i)] = np.sum(self.layer["DZ"+str(i)], axis=1, keepdims=True)/_A.shape[0]
            self.layer["DA"+str(i - 1)] = np.dot(W.T, self.layer["DZ"+str(i)])
        elif (activation == "sigmoid"):
            self.layer["DZ"+str(i)] = self.derivate_sigmoid(_DA, Z)
            self.layer["DW"+str(i)] = np.dot(self.layer["DZ"+str(i)], _A.T)/_A.shape[0]
            self.layer["DB"+str(i)] = np.sum(self.layer["DZ"+str(i)], axis=1, keepdims=True)/_A.shape[0]
            self.layer["DA"+str(i - 1)] = np.dot(W.T, self.layer["DZ"+str(i)])
        elif (activation == "tanh"):
            self.layer["DZ"+str(i)] = self.derivate_tanh(_DA, Z)
            self.layer["DW"+str(i)] = np.dot(self.layer["DZ"+str(i)], _A.T)/_A.shape[0]
            self.layer["DB"+str(i)] = np.sum(self.layer["DZ"+str(i)], axis=1, keepdims=True)/_A.shape[0]
            self.layer["DA"+str(i - 1)] = np.dot(W.T, self.layer["DZ"+str(i)])
        elif (activation == "mish"):
            self.layer["DZ"+str(i)] = self.derivate_mish(_DA, Z)
            self.layer["DW"+str(i)] = np.dot(self.layer["DZ"+str(i)], _A.T)/_A.shape[0]
            self.layer["DB"+str(i)] = np.sum(self.layer["DZ"+str(i)], axis=1, keepdims=True)/_A.shape[0]
            self.layer["DA"+str(i - 1)] = np.dot(W.T, self.layer["DZ"+str(i)])

    def derivate_tanh(self, _DA, x):
        return _DA * (1 - np.tanh(x)**2)

    def derivate_relu(self, _DA, x):
        DZ = np.array(_DA, copy = True, dtype=np.float64)
        DZ[x < 0] = 0
        #DZ[x > 0] = 1
        return DZ

    def derivate_sigmoid(self, _DA, x):
        return _DA * (self.sigmoid(x)*(1-self.sigmoid(x)))

    def compute_cost(self, Y, A):
        m = Y.shape[1]
        logprobs = np.multiply(np.log(A), Y) + np.multiply(1 - Y, np.log(1 - A))
        cost = - np.sum(logprobs) / m
        cost = np.squeeze(cost)
        return cost


    def predict(self, input):
        self.layer["A0"] = input
        for i in range(1, len(self.activations)):
            self.forwardLayer(i)
        return self.layer["A"+str(len(self.activations)-1)]

    def train(self, input, output, epoch):
        for _ in range(epoch):
            self.layer["A0"] = input
            for i in range(1, len(self.activations)):
                self.forwardLayer(i)
            #print(self.compute_cost(output, self.layer["A"+str(len(self.activations)-1)]))
            #print(output)
            #print(self.layer["A"+str(len(self.activations)-1)])
            self.layer["COST"]=np.subtract(output, self.layer["A"+str(len(self.activations)-1)])
            self.layer["LOSS"]=np.abs(np.subtract(output, self.layer["A"+str(len(self.activations)-1)]))

            self.losses.append(np.sum(self.layer["LOSS"]))
            self.accurency.append(1 - np.mean(self.layer["LOSS"]))
            self.cost.append(np.sum(np.abs(self.layer["COST"])))
            #self.layer["DA" + str(len(self.activations) - 1)] = np.subtract(output, self.layer["A"+str(len(self.activations)-1)]) * self.sigmoid(self.layer["A"+str(len(self.activations)-1)])*(1-self.sigmoid(self.layer["A"+str(len(self.activations)-1)]))
            self.layer["DA"+str(len(self.activations) - 1)]= - (np.divide(output, self.layer["A"+str(len(self.activations)-1)]) - np.divide(1 - output, 1 - self.layer["A"+str(len(self.activations)-1)]))
            for i in range(len(self.activations) - 1, 0, -1):
                self.backpropLayer(i)
            self.learn()

    def learn(self):
        for i in range(1, len(self.activations)):
            self.layer["W"+str(i)] -= self.layer["DW"+str(i)] * 1e-5
            self.layer["B"+str(i)] -= self.layer["DB"+str(i)] * 1e-5


    def forwardLayer(self, i):
        W = self.layer["W" + str(i)]
        B = self.layer["B" + str(i)]
        _A = self.layer["A"+ str(i - 1)]
        activation = self.activations[i]

        if (activation == "relu"):
            self.layer['Z' + str(i)] = np.dot(W, _A) + B
            self.layer['A' + str(i)] = self.relu(self.layer["Z" + str(i)])
        elif (activation == "sigmoid"):
            self.layer['Z' + str(i)] = np.dot(W, _A) + B
            self.layer['A' + str(i)] = self.sigmoid(self.layer["Z" + str(i)])
        elif (activation == "tanh"):
            self.layer['Z' + str(i)] = np.dot(W, _A) + B
            self.layer['A' + str(i)] = np.tanh(self.layer["Z" + str(i)])
        elif (activation == "mish"):
            self.layer['Z' + str(i)] = np.dot(W, _A) + B
            self.layer['A' + str(i)] = self.mish(self.layer["Z" + str(i)])
            #print(self.layer['A' + str(i)])


    def mish(self, x):
        print(x)
        return x * np.tanh(np.log(1.0 + np.exp(x)))

    def derivate_mish(self, _DA, x):
        omega = np.exp(3 * x) + 4 * np.exp(2 * x) + (6 + 4 * x) * np.exp(x) + 4 * (1 + x)
        delta = 1 + (np.exp(x) + 1)**2
        derivative = np.exp(x) * omega / delta**2
        return derivative * _DA

    def sigmoid(self, x):
        return 1/(1 + np.exp(-x))

    def relu(self, x):
        x[x < 0] = 0
        return x




if __name__ == '__main__':
    memory = lry.Lstm_ricky()
    #data = ffd.Data()
    size_fake = 1
    #data.generate_fake_data(size_fake)
    epoch = 1
    batch = 100
    #for _ in range(7000):
    #    memory.short_memory(data.data_input[_], data.data_output[_])
    #print(memory.short_memory_idx(data.data_input[6999]))
    neural = NeuralNetwork(
        {
            "size": [20, 400, 200, 200, 100, 80, 80, 40, 40, 20, 1],
            "activation": ["input", "sigmoid", "tanh", "relu", "sigmoid", "tanh", "relu", "sigmoid", "tanh", "relu", "sigmoid"],
        }
    );
    #ffd.multi=[[1, 0], [0, 1], [1, 1], [0, 0]]
    #ffd.output=[[1], [1], [0], [0]]
    for _ in range(batch):
        if (_ % (batch/100) == 0):
            print("Train epoch "+str(_))
        neural.train(np.array(ffd.multi, dtype=np.float64).T, np.array(ffd.output, dtype=np.float64).T, epoch)

    sum = 0
    loss_test = []
    for _ in range(100):
        print("Test epoch "+str(_))
        loss_test.append(np.abs(ffd.test_output[_] - np.mean(neural.predict(np.array([ffd.test_multi[_]], dtype=np.float64).T))))
        sum += np.abs(ffd.test_output[_] - np.mean(neural.predict(np.array([ffd.test_multi[_]]).T)))
    print("TOTAL if is closest to 0 its good "+str(sum[0]))

    plt.figure(1)
    plt.plot(range(0, epoch*batch), neural.losses)
    plt.subplot()
    plt.plot(range(0, epoch*batch), neural.cost)
    plt.figure(2)
    plt.plot(range(0, epoch*batch), neural.accurency)
    plt.figure(3)
    plt.plot(range(0, 100), loss_test)
    plt.show()
