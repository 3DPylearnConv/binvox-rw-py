

from subprocess import call
import os

models_dir = '/home/jvarley/.gazebo/models'
# import IPython
# IPython.embed()
subdirs = [d for d in os.listdir(models_dir) if os.path.isdir(models_dir + "/" + d)]
model_filepaths = []

print
print "subdirs:"
print
print subdirs

for subdir in subdirs:
    in_file = models_dir + '/' + subdir + "/" + subdir + '.off'
    out_file = models_dir + '/' + subdir + "/" + subdir + '.binvox'
    if not os.path.exists(out_file):
        #print model_name_without_ext
        model_filepaths.append(in_file)
        #print models_dir + '/' + model_name

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
