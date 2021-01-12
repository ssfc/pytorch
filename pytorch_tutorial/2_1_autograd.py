# https://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html


import torch, torchvision
from torch import nn, optim


model = torchvision.models.resnet18(pretrained=True)

# Freeze all the parameters in the network
for param in model.parameters():
    param.requires_grad = False

model.fc = nn.Linear(512, 10)

# Optimize only the classifier
optimizer = optim.SGD(model.fc.parameters(), lr=1e-2, momentum=0.9)




