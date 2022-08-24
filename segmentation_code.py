def segment_predict(modelName, imageName, outputLocation, startTime, endTime):
    print(
        'Running setmentation with parameters: \n' + 'niftifile: ' + imageName + '\n output folder: ' + outputLocation + '\nstarting time: ' + str(
            startTime) + '\nend time: ' + str(endTime) + '\nModel Name: ' + modelName)


def segment_train(model, epochs, gt_path, output_path):
    print('\nRunning training for ' + str(
        epochs) + ' epochs.' + '\n' + 'Weights: ' + gt_path + '\n Output Folder ' + output_path + '\nModel: ' + model)


def tracking(str1, str2, str3, int1, int2, int3, int4, str4, str5):
    print("Running with:  image                                seg folder                                   track folder              st et ost kdf alfja")
    print(str1, str2, str3, int1, int2, int3, int4, str4, str5)
