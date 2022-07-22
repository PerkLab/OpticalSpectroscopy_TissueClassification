import numpy as np
# import pip
# pip.main(['install','pandas'])
import pandas as pd

# Select the label and append it to the end of the 
label = 1

# This code is used to access a sequence from slicer and convert it to a numpy array to later export
seqNode  = slicer.mrmlScene.GetFirstNodeByName('Sequence_3')
# The sequence contains n data nodes
name = 'white'
folder = 'C:/OpticalSpectroscopy_TissueClassification/broadbandTestData/white/'

for idx in range(149):#seqNode.GetNumberOfDataNodes()):
    volumeNode = seqNode.GetNthDataNode(idx)
    specArray = slicer.util.arrayFromVolume(volumeNode)
    specArray = np.squeeze(specArray)
    specArray = np.transpose(specArray)
    if idx <= 9:
        num = '0'+str(idx)
    else:
        num = str(idx)
    np.savetxt(folder + name + num + '.csv', specArray, delimiter=',')