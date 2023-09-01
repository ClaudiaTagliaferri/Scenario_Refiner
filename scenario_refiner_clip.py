# -*- coding: utf-8 -*-
"""Scenario_Refiner_CLIP

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cIEdq33hI0f0-yzfG7tWl38wNL7fxXfY
"""

! pip install ftfy regex tqdm
! pip install git+https://github.com/openai/CLIP.git

"""Step 2: import torch"""

import numpy as np
import torch
from pkg_resources import packaging

print("Torch version:", torch.__version__)

"""Step 3: import CLIP"""

import clip

clip.available_models()

"""Step 4: load the model"""

model, preprocess = clip.load("ViT-B/32")
#model, preprocess = clip.load("RN50x64")
#model, preprocess = clip.load("ViT-L/14@336px")
model.cuda().eval()
input_resolution = model.visual.input_resolution
context_length = model.context_length
vocab_size = model.vocab_size

print("Model parameters:", f"{np.sum([int(np.prod(p.shape)) for p in model.parameters()]):,}")
print("Input resolution:", input_resolution)
print("Context length:", context_length)
print("Vocab size:", vocab_size)

"""Check the preprocess parameters"""

preprocess

"""Prepare images"""

from PIL import Image

original_images = []
images = []

for i in range(len(filename)):
    try:
      image = Image.open(filename[i])
      original_images.append(image)
      images.append(preprocess(image))
    except Exception:
      print(filename[i])
      pass

"""Prepare sentences"""

# Commented out IPython magic to ensure Python compatibility.
import IPython.display
import matplotlib.pyplot as plt
import numpy as np

from collections import OrderedDict
import torch

# %matplotlib inline
# %config InlineBackend.figure_format = 'retina'

texts = ["The man in the black shirt is a runner",
         "The man in the black shirt is running",
         "The man is a runner",
         "The man is running",
         "The young man is a runner",
         "The young man is running",
         "The men are runners",
         "The men are running",
         "The man is a swimmer",
         "The man is swimming",
         "The woman is a swimmer",
         "The woman is swimming",
         "The dog is a swimmer",
         "The dog is swimming",
         "The people are swimmers",
         "The people are swimming",
         "The woman is a baker",
         "The woman is baking",
         "The man is a baker",
         "The man is baking",
         "The person is a baker",
         "The person is baking",
         "The man is a surfer",
         "The man is surfing",
         "The woman is a surfer",
         "The woman is surfing",
         "The woman and the man are surfers",
         "The woman and the man are surfing",
         "The man and the young girl are surfers",
         "The man and the young girl are surfing",
         "The four kids are surfers",
         "The four kids are surfing",
         "The four men are hunters",
         "The four men are hunting",
         "The cat is a hunter",
         "The cat is hunting",
         "The man and the dog are hunters",
         "The man and the dog are hunting",
         "The man is a hunter",
         "The man is hunting",
         "The people are lovers",
         "The people love each other",
         "The man and the woman are lovers",
         "The man and the woman love each other",
         "The girl and the boy are lovers",
         "The girl and the boy love each other",
         "The woman and the girl are lovers",
         "The woman and the girl love each other",
         "The man and the woman are lovers",
         "The man and the woman love each other",
         "The woman is a supporter",
         "The woman is supporting",
         "The man is a supporter",
         "The man is supporting",
         "The people are supporters",
         "The people are supporting",
         "The man and the woman are supporters",
         "The man and the woman are supporting",
         "The hugging man is a supporter",
         "The hugging man is supporting",
         "The woman is a driver",
         "The woman is driving",
         "The person is a driver",
         "The person is driving",
         "The man is a driver",
         "The man is driving",
         "The woman with pink gloves is a driver",
         "The woman with pink gloves is driving",
         "The man is a smoker",
         "The man is smoking",
         "The women are smokers",
         "The women are smoking",
         "The woman is a smoker",
         "The woman is smoking",
         "The man with the hat is a smoker",
         "The man with the hat is smoking",
         "The people are walkers",
         "The people are walking",
         "The girl is a walker",
         "The girl is walking",
         "The man is a skier",
         "The man is skiing",
         "The person is a skier",
         "The person is skiing",
         "The woman is a skier",
         "The woman is skiing",
         "The people are skiers",
         "The people are skiing",
         "The people are dancers",
         "The people are dancing",
         "The man and the girl are dancers",
         "The man and the girl are dancing",
         "The four women are dancers",
         "The four women are dancing",
         "The children are dancers",
         "The children are dancing",
         "The man is a singer",
         "The man is singing",
         "The woman is a singer",
         "The woman is singing",
         "The woman and the man are singers",
         "The woman and the man are singing",
         "The man is a cleaner",
         "The man is cleaning",
         "The woman is a cleaner",
         "The woman is cleaning",
         "The woman with the mop is a cleaner",
         "The woman with the mop is cleaning",
         "The two men are cleaners",
         "The two men are cleaning",
         "The man at the computer is a gamer",
         "The man at the computer is gaming",
         "The two men are gamers",
         "The two men are gaming",
         "The child is a gamer",
         "The child is gaming",
         "The woman is a gamer",
         "The woman is gaming",
         "The people are gamers",
         "The people are gaming",
         "The adults are teachers",
         "The adults are teaching",
         "The woman is a teacher",
         "The woman is teaching",
         "The man is a teacher",
         "The man is teaching",
         "The two men are teachers",
         "The two men are teaching",
         "The person is a painter",
         "The person is painting",
         "The people are painters",
         "The people are painting",
         "The man is a painter",
         "The man is painting",
         "The man in the blue jacket is a reader",
         "The man in the blue jacket is reading",
         "The man is a reader",
         "The man is reading",
         "The woman is a reader",
         "The woman is reading",
         "The man and the woman are readers",
         "The man and the woman are reading",
         "The man and the child are readers",
         "The man and the child are reading"]

"""**tokenize descriptions**"""

image_input = torch.tensor(np.stack(images[0:len(texts)])).cuda()
text_tokens = clip.tokenize(["This is " + desc for desc in texts]).cuda()

"""**convert** data to **vectors**"""

with torch.no_grad():
    image_features = model.encode_image(image_input).float()
    text_features = model.encode_text(text_tokens).float()

image_features /= image_features.norm(dim=-1, keepdim=True)
text_features /= text_features.norm(dim=-1, keepdim=True)
similarity = text_features.cpu().numpy() @ image_features.cpu().numpy().T

scores={}
for i in range(similarity.shape[1]):
  scores[filename[i]]={}
  for j in range(similarity.shape[0]):
    scores[filename[i]][texts[j]]=similarity[j][i]

scores
