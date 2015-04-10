


from subprocess import call
import os
import binvox_rw

models_dir = '/srv/3d_conv_data/ModelNet10'
categories = [d for d in os.listdir(models_dir) if os.path.isdir(os.path.join(models_dir, d))]
model_filepaths = []

for category in categories:
    for file_name in os.listdir(models_dir + '/' + category + '/test/'):
        if ".binvox" in file_name:
            model_filepaths.append(models_dir + '/' + category + '/test/' + file_name)
    for file_name in os.listdir(models_dir + '/' + category + '/train/'):
        if ".binvox" in file_name:
            model_filepaths.append(models_dir + '/' + category + '/train/' + file_name)

for model_filepath in model_filepaths:

    with open(model_filepath, 'r') as f:
        model = binvox_rw.read_as_3d_array(f).data
        if model.max() == 0:
            print "fixing" + str(model_filepath)
            #call(['rm', model_filepath])
            #call(["binvox", model_filepath[:-6] + 'off'])

