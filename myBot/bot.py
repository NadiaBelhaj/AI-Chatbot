from myBot.neural import NeuralNetwork
from myBot.utils import load_data, tokenize, analyze_words
import random
import torch

# Loading data from json
intents = load_data('myBot')

# Loading training data
FILE = "myBot"

data = torch.load(FILE)

all_words = data['words']
tags = data['tags']



input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']


# Model set to evaluate


model.eval()

def bot_response(message):
    message = tokenize(message)
    X = analyze_words(message, all_words)
    output = model(X)
    print(output)

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.6:
                return (random.choice(intent['responses']))
    else:
        return "Pardon. je n'ai pas compris ton message"