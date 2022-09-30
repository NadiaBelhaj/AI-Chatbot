import torch
from torch.utils.data import Dataset

class ChatbotDataset(Dataset):
    def __init__(self, x, y):
        self.n_samples = len(x)
      

#support indexing such that dataset[i] can be used to get i-th sample
    def __getitem__(self, index):
        return self.data[index], self[index]

#we can call len(dataset) to return the size
    def __len__(self):
        return self.n_samples

   # X: bag of words for each pattern_sentence
   # y: PyTorch CrossEntropyLoss needs only class labels, not one-hot