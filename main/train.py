import os
import sys
import numpy as np
import json
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from features.network import wordCollection, tokenize, stem
from features.model import Brain


with open("static/intents.json", "r") as f:
    intents = json.load(f)

allWords = []
tags = []
xy = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)

    for pattern in intent['patterns']:
        w = tokenize(pattern)
        allWords.extend(w)
        xy.append((w, tag))

ignoreWords = [',', '?', '.', '!', '/']
allWords = [stem(w) for w in allWords if w not in ignoreWords]
allWords = sorted(set(allWords))
tags = sorted(set(tags))

xTrain = []
yTrain = []

for (patternSentence, tag) in xy:
    collection = wordCollection(patternSentence, allWords)
    xTrain.append(collection)

    label = tags.index(tag)
    yTrain.append(label)

xTrain = np.array(xTrain)
yTrain = np.array(yTrain)

numEpochs = 1000
batchSize = 8
learningRate = 0.001
inputSize = len(xTrain[0])
hiddenSize = 8
outputSize = len(tags)

print("\nTraining The Model...")

class ChatDataset(Dataset):

    def __init__(self):
        self.n_samples = len(xTrain)
        self.x_data = xTrain
        self.y_data = yTrain

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.n_samples

dataset = ChatDataset()

trainLoader = DataLoader(dataset=dataset, batch_size=batchSize, shuffle=True, num_workers=0)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = Brain(inputSize, hiddenSize, outputSize).to(device=device)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learningRate)

for epoch in range(numEpochs):
    for (words,labels) in trainLoader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)
        outputs = model.link(words)
        loss = criterion(outputs,labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch+1) % 100 == 0:
        print(f"Epoch: [{epoch+1}/{numEpochs}], Loss: {loss.item():.4f}")

print(f"Final Loss: {loss.item():.4f}\n")

data = {
    "model_state":model.state_dict(),
    "input_size":inputSize,
    "hidden_size":hiddenSize,
    "output_size":outputSize,
    "all_words":allWords,
    "tags":tags
}

FILE = "static/trainedData.pth"
torch.save(data, FILE)

print("Training Completed!")
print(f"Training File saved as {FILE}\n")

os.execv(sys.executable, ["python", "ui_main.py"])