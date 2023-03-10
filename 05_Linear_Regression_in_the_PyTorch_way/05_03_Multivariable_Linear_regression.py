# -*- coding: utf-8 -*-
"""PyTorchZeroToAll - Lecture 05_03: Multivariable Linear regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A45a-tm7Be1kKPQkCkDU26zyARX3dQ85

# 모두를 위한 딥러닝 시즌2 - PyTorch Lab-04-1 Multivariable Linear regression
"""

import torch
from torch.autograd import Variable

x_train = Variable(torch.FloatTensor([[73, 80, 75],
                                      [93, 88, 93],
                                      [89, 91, 90],
                                      [96, 88, 100],
                                      [73, 66, 70]]))
y_train = Variable(torch.FloatTensor([[152],
                                      [185],
                                      [180],
                                      [196],
                                      [142]]))

class MultivariateLinearRegressionModel(torch.nn.Module):
    def __init__(self):
        super(MultivariateLinearRegressionModel, self).__init__()
        self.linear = torch.nn.Linear(3, 1)

    def forward(self, x):
        y_pred = self.linear(x)
        return y_pred

model = MultivariateLinearRegressionModel()

criterion = torch.nn.MSELoss(reduction='mean')
optimizer = torch.optim.SGD(model.parameters(), lr=1e-5)

epochs = 20
for epoch in range(1, epochs+1):
    y_pred = model(x_train)

    # Compute and print loss
    loss = criterion(y_pred, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print(f"Epoch : {epoch}\ty_pred = {y_pred.squeeze().detach()}\tLoss = {loss.item()}")

