

from subprocess import call
import os

models_dir = '/srv/3d_conv_data/ModelNet10'
categories = [d for d in os.listdir(models_dir) if os.path.isdir(os.path.join(models_dir, d))]
model_filepaths = []

print
print "Categories:"
print
print categories

for category in categories:
    for file_name in os.listdir(models_dir + '/' + category + '/test/'):
        if ".off" in file_name and  not os.path.exists(models_dir + '/' + category + '/test/' + file_name[:-3] + "binvox"):
            model_filepaths.append(models_dir + '/' + category + '/test/' + file_name)
    for file_name in os.listdir(models_dir + '/' + category + '/train/'):
        if ".off" in file_name and not os.path.exists(models_dir + '/' + category + '/train/' + file_name[:-3] + "binvox"):
            model_filepaths.append(models_dir + '/' + category + '/train/' + file_name)

print
print "files to convert:"
print
print model_filepaths
print len(model_filepaths)
for model_filepath in model_filepaths:

    print
    print "working on:"
    print model_filepath

    call(["binvox", model_filepath])
