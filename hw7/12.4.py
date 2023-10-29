import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from sklearn import datasets
import numpy as np

iris = datasets.load_iris()
X = iris["data"].astype(np.float32) 
y = iris["target"].astype(np.int64) 


train_ratio = 0.7
index = np.random.permutation(X.shape[0])
train_index = index[:int(X.shape[0] * train_ratio)]
test_index = index[int(X.shape[0] * train_ratio):]
X_train, y_train = X[train_index], y[train_index]
X_test, y_test = X[test_index], y[test_index]

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        torch.manual_seed(2)
        self.fc1 = nn.Linear(4, 32)
        self.fc2 = nn.Linear(32, 32)
        self.fc3 = nn.Linear(32, 3)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

model = Net()
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

num_epochs = 100
for epoch in range(num_epochs):
    inputs = torch.from_numpy(X_train)
    labels = torch.from_numpy(y_train)
    optimizer.zero_grad()
    outputs = model(inputs)
    loss = criterion(outputs, labels)
    loss.backward()
    optimizer.step()
    if epoch % 10 == 0:
        print("Epoch: %d, Loss: %.4f" % (epoch, loss.item()))


with torch.no_grad():
    inputs = torch.from_numpy(X_test)
    labels = torch.from_numpy(y_test)
    outputs = model(inputs)
    _, predictions = torch.max(outputs, 1)
    accuracy = (predictions == labels).float().mean()
    print("Accuracy: %.2f %%" % (accuracy.item() * 100))
