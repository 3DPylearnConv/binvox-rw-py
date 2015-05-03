

from subprocess import call
import os

models_dir = '/home/jvarley/models2'
model_names = [d for d in os.listdir(models_dir) if os.path.isdir(os.path.join(models_dir, d))]
model_filepaths = []

print
print "model_names:"
print
print model_names

for model_name in model_names:
    if not os.path.exists(models_dir + '/' + model_name + '/optimized_tsdf_texture_mapped_mesh.binvox'):
        model_filepaths.append(models_dir + '/' + model_name + '/optimized_tsdf_texture_mapped_mesh.obj')

print
print "files to convert:"
print
print model_filepaths
print len(model_filepaths)
for model_filepath in model_filepaths:

    print
    print "working on:"
    print model_filepath

    #call(["binvox", model_filepath])
