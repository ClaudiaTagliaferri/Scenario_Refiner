# -*- coding: utf-8 -*-
"""Scenario_Refiner_ViLT(LIMO)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J7IOSWpGMDcrh95VL0_o8JZ5APjmyaKy

# Using ViLT for image-text retrieval

In this notebook, we are going to illustrate how to use the Vision-and-Language Transformer (ViLT) for scoring texts given an image (you can also use it the other way around).

ViLT docs: https://huggingface.co/docs/transformers/master/en/model_doc/vilt

## Set-up environment
"""

!pip install -q git+https://github.com/huggingface/transformers.git

"""## Define processor + model

Here we'll define the processor (which allows to prepare data for the model), as well as the model itself.

We also move the model to the GPU, if it's available.
"""

from transformers import ViltProcessor, ViltForImageAndTextRetrieval
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-coco")
model = ViltForImageAndTextRetrieval.from_pretrained("dandelin/vilt-b32-finetuned-coco")
model.to(device)

"""## Prepare image"""

from PIL import Image


#plt.figure(figsize=(16, 5))
original_images = []

for i in range(len(filename)):
    try:
      image = Image.open(filename[i])
      original_images.append(image)
    except Exception:
      print(filename[i])
      pass

"""## Prepare sentences"""

import numpy as np

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

"""# Inference
model computes a score for every image-text pair
"""

from tqdm.notebook import tqdm
import os

image_paths = [os.path.abspath(image.filename) for image in tqdm(original_images)]
scores = {}

for image_path in tqdm(image_paths):
    scores[image_path] = {}
    image = Image.open(image_path).convert("RGB")

    for text in tqdm(texts):
        # encode
        encoding = processor(image, text, return_tensors="pt")
        # forward pass
        outputs = model(**encoding)
        # get score
        score = outputs.logits[:, 0].item()
        scores[image_path][text] = score
scores