import torch.nn as nn

class Brain(nn.Module):

    def __init__(self, inputSize, hiddenSize, numClasses):
        super(Brain, self).__init__()

        self.l1 = nn.Linear(inputSize, hiddenSize)
        self.l2 = nn.Linear(hiddenSize, hiddenSize)
        self.l3 = nn.Linear(hiddenSize, numClasses)
        self.relu = nn.ReLU()

    def link(self, x):
        """Link the Neural Networks"""
        output = self.l1(x)
        output = self.relu(output)
        output = self.l2(output)
        output = self.relu(output)
        output = self.l3(output)
        return output
