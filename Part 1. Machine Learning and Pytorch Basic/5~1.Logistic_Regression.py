# 수정 필요
# Higher Implementation with Class

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class BinaryClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(8,1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        return self.sigmoid(self.linear(x))

model = BinaryClassifier()

# x_data = [[1,2], [2,3], [3,1], [4,3], [5,3], [6,2]]
# y_data = [[0], [0], [0], [1], [1], [1]]

# x_train = torch.FloatTensor(x_data)
# y_train = torch.FloatTensor(y_data)

optimizer = optim.SGD(model.parameters(), lr=1)

nb_epochs = 100
for epoch in range(nb_epochs + 1):
    hypothesis = model(x_train)

    cost = F.binary_cross_entropy(hypothesis, y_train)

    optimizer.zero_grad()
    cost.backward
    optimizer.step()

    if epoch % 10 == 0:
        prediction = hypothesis >= torch.FloatTensor([0.5])
        correct_prediction = prediction.float() == y_train
        accuracy = correct_prediction.sum().item() / len(correct_prediction)
        print('Epoch {:4d}/{} Cost: {:.6f} Accuracy {:2.2f}%'.format(epoch,
         nb_epochs, cost.item(), accuracy * 100))

