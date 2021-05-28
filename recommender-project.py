import numpy as np
import pyGM as gm

# names of 500 movies to be rated:
with open('top-names.txt') as f: names = f.read().split('\n')
    
# ratings = int(2000 x 500) ratings of 500 movies by 2000 people; -1 = not rated
ratings = np.loadtxt('top-ratings-missing.txt')
nUsers,nMovies = ratings.shape

X = (ratings >= 7).astype(int);   # did each user like the movie?  (binary)
# (use any threshold you like, but "7+" might be "worth recommending"?)

# Let's split into training & test:
np.random.seed(0)
pi = np.random.permutation(nUsers)
iTr,iTe = pi[:int(nUsers*.7)], pi[int(nUsers*.7):]
Xtr,Xte = X[iTr,:],X[iTe,:]