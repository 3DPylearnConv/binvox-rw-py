import subprocess
import os

def run_subprocess(cmd_string):
    print "running: " + cmd_string
    process = subprocess.Popen(cmd_string.split(), stdout = subprocess.PIPE)
    output = process.communicate()[0]
    print output

def generate_binvox_files():
    ip_models_dir = '/srv/data/processed_mesh_models/ycb'
    op_models_dir = '/srv/data/shape_completion_data/ycb'
    model_names = [d for d in os.listdir(ip_models_dir) if os.path.isdir(os.path.join(ip_models_dir, d))]
    selected_models = []

    print
    print "model_names:"
    print
    print model_names

    for model_name in model_names:
        if not os.path.exists(op_models_dir + '/' + model_name + '/models/' + model_name + '.binvox'):
            if not os.path.exists(op_models_dir + '/' + model_name + '/models'):
                os.mkdir(op_models_dir + '/' + model_name + '/models')
            selected_models.append(model_name)
            #ip_model_filepaths.append(ip_models_dir + '/' + model_name + '/optimized_tsdf_texture_mapped_mesh.obj')

    print
    print "files to convert:"
    print
    print selected_models
    print len(selected_models)
    for model_name in selected_models:
        ip_model_filepath = ip_models_dir + '/' + model_name + '/optimized_tsdf_texture_mapped_mesh.obj'
        print
        print "working on:"
        print ip_model_filepath

        subprocess.call(["binvox", ip_model_filepath])
	
	cmd = ""
	cmd += 'mv '
	cmd +=  ip_models_dir + '/' + model_name + '/optimized_tsdf_texture_mapped_mesh.binvox '
	cmd +=  op_models_dir + '/' + model_name + '/models/'
        print cmd
	run_subprocess(cmd)

	cmd = ""
	cmd += 'mv '
	cmd +=  op_models_dir + '/' + model_name + '/models/optimized_tsdf_texture_mapped_mesh.binvox '
	cmd +=  op_models_dir + '/' + model_name + '/models/' + model_name + '.binvox'
        print cmd
	run_subprocess(cmd)

if __name__ == "__main__":
    generate_binvox_files()
