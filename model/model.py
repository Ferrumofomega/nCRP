"""
Nested Chinese Restaurant Process inspired by Blei (https://cocosci.berkeley.edu/tom/papers/ncrp.pdf)
Posterior inference with Edward's BBVI.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import edward as ed
from edward.models import Categorical, Dirichlet, Beta, DirichletProcess, \
    Multinomial, Bernoulli, Exponential, DirichletMultinomial

import numpy as np
import tensorflow as tf
from scipy.stats import norm
import uuid

# DATA


# MODEL

N = 1000
K = 4

level_1_alpha = 0.5
level_2_alpha = 2.0
level_3_alpha = 2.0

# Food feature space - A food is composed of a shape, a color, and a taste vector
sweetness = [1, 0]
sourness = [1, 0]
umaminess = [1, 0]
bitterness = [1, 0]
saltiness = [1, 0]
tastes = [sweetness, sourness, umaminess, bitterness, saltiness]

shapes = ['grape-shaped', 'apple-shaped', 'carrot-shaped', 'broccoli-shaped']
colors = ['green', 'red', 'yellow', 'orange']

alpha = map(float, [1, 2, 3])
n = 2
dist = DirichletMultinomial(n, alpha)

# This creates the nCRP categorization portion of the model
# food_category = "cat"+str(uuid.uuid4())
# food_sub_category = 'sub-cat'+str(uuid.uuid4())
# food_instance = "instance"+str(uuid.uuid4())

# INFERENCE
