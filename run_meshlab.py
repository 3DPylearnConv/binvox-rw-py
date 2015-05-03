from subprocess import call
import os

models_dir = '.' #'/home/jvarley/SHREC2012_Generic'
file_names = [d for d in os.listdir(models_dir) if ".off" in d]
model_filepaths = []

print
print "model_names:"
print
print file_names

for model_name in file_names:
    model_name_without_ext = model_name[:-4]
    if not os.path.exists(models_dir + '/' + model_name_without_ext + '.dae'):
        #print model_name_without_ext
        infile = model_name
        outfile = model_name_without_ext + ".dae"
        model_filepaths.append([infile, outfile])
        #print models_dir + '/' + model_name

print
print "files to convert:"
print
print model_filepaths
print len(model_filepaths)
for example in model_filepaths:
    infile, outfile = example
    print
    print "working on:"
    print infile
    print outfile
    argument = " -i " + str(infile)+ " -o " + str(outfile)
    print argument

    call(["meshlabserver" , "-i", infile, "-o", outfile])