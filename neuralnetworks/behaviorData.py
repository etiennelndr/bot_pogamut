# ==============================================================================
# context: teaching - Shared Educational Resources in Computer Science
#          ENIB: module IAS - course on neural networks (since fall'18)
# description: class defining the learning data for the 'Surface learning experiment'
# copyright (c) 2018 ENIB. All rights reserved.
# ------------------------------------------------------------------------------
# usage: python
# dependencies: python 3 (see import statements)
# tested on: python 3.6.5 on MacOS 10.13
#            python 3.x on
# ------------------------------------------------------------------------------
# creation: 22-sep-2018 pierre.chevaillier@enib.fr
# revision: 26-sep-2018 pierre.chevaillier@enib.fr variables labels... 
# ------------------------------------------------------------------------------
# comments:
# - students have noting to change here
# warnings:
# - only for educational purposes
# todos:
#  - test it and then test it again
# ==============================================================================

# Python standard distribution

# Specific modules
import numpy as np

# Home made stuffs
from learningData import LearningData

# ==============================================================================

class TwoDVelocityData(LearningData):

    @classmethod
    def readDataFromFile(cls, dataFilePath):
        samples = np.loadtxt(dataFilePath, delimiter=';')
        X = samples[:, 0:2] # 1st and 2nd columns
        #Y = samples[:, 2:7] # 3rd, 4th, 5th and 6th columns
        Y = samples[:, 2:] # 3rd and 4th columns
        return X, Y

    @classmethod
    def readPredictionsFromFile(cls, predsFilePath):
        Predictions = np.loadtxt(predsFilePath, delimiter=';')
        X = Predictions[:, 0:2] # first two columns
        #Y = Predictions[:, 2:7] # last two column
        Y = samples[:, 2:] # 3rd and 4th columns
        return X, Y

    def __init__(self):
        # Define the dimensions for the Input (X) and the output (Y) variables
        xDim, yDim = 2, 2
        super().__init__(xDim, yDim)
        
        self.X.names = ['x', 'y']
        self.X.units = ['m', 'm']
        #self.Y.names = ['vx', 'vy', 'pitch', 'yaw']
        self.Y.names = ['vx', 'vy']
        #self.Y.labels = ['velocity x', 'veclocity y', 'rotation pitch', 'rotation yaw']
        self.Y.labels = ['velocity x', 'veclocity y']
        #self.Y.units = ['m/s', 'm/s', 'rad/s', 'rad/s']
        self.Y.units = ['m/s', 'm/s']
        self.X.domains = [[0.0, 1.0],[0.0, 1.0]]
        #self.Y.domains = [[439.92, -439.99],[440, -449.52],[65535, 0.0],[65312, 314]]
        self.Y.domains = [[-1.0, 1.0],[-1.0, 1.0]]
        return
    
# ==============================================================================
if __name__ == "__main__":
    print("This module is not runnable")

# end of file
# ==============================================================================