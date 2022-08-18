def segment_predict(str1,str2,int1,int2):
    print('Running setmentation with parameters: \n'+'niftifile: '+str1+'\n output folder: '+ str2+'\nstarting time: '+str(int1)+'\nend time: '+str(int2))

def segment_train(epoks, imageName, folderPath):
    print('\nRunning training for '+ str(epoks)+ ' epochs.'+'\n'+'image: ' + imageName + '\n'+folderPath)