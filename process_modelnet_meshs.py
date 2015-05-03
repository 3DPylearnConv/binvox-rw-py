

import os
import shutil
from off_utils.off_handler import OffHandler

from subprocess import call
import os

models_dir = '.'


def generate_centered_scaled_meshes():
    off_mesh_files = [fi for fi in os.listdir(models_dir) if os.path.isfile(fi) and ".off" in fi]

    off_handler = OffHandler()

    for off_mesh_file in off_mesh_files:
        filename_root = off_mesh_file[:-4]
        off_handler.read(off_mesh_file)
        offset, scale = off_handler.scale_and_center(desired_largest_side=.25)

        off_handler.write(filename_root + "_scaled_centered.off")
        f = open(filename_root + "_offset_and_scale.txt", 'w')
        offset_and_scale = str(offset[0]) + " " + str(offset[1]) + " " + str(offset[2]) + " " + str(scale) + "/n"
        f.write(offset_and_scale)
        f.close()


def generate_dae_files():

    file_names = [d for d in os.listdir(models_dir) if "_scaled_centered.off" in d]
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


def move_files_to_gazebo_subdirs():
    file_names = [d for d in os.listdir(models_dir) if ".off" in d and not "_scaled_centered" in d]
    print
    print "model_names:"
    print
    print file_names

    file_extensions = ["_scaled_centered.off", ".off", "_scaled_centered.dae", "_offset_and_scale.txt", ".binvox"]
    for model_name in file_names:
        model_name_without_ext = model_name[:-4]
        os.mkdir(model_name_without_ext)
        for file_extension in file_extensions:
            shutil.move(model_name_without_ext + file_extension,
                        model_name_without_ext + "/" + model_name_without_ext + file_extension )


def generate_gazebo_config():

    sub_dirs = [sub_dir for sub_dir in os.listdir(models_dir) if os.path.isdir(sub_dir) and "D0" in sub_dir]

    for sub_dir in sub_dirs:

        ################################
        # write the model.config
        ################################
        model_config = ""
        model_config += '<?xml version="1.0"?>\n'
        model_config += '  <model>\n'
        model_config += '    <name>' + sub_dir + '</name>\n'
        model_config += '    <version>1.0</version>\n'
        model_config += '    <sdf version="1.2">model-1_2.sdf</sdf>\n'
        model_config += '    <sdf version="1.3">model-1_3.sdf</sdf>\n'
        model_config += '    <sdf version="1.4">model-1_4.sdf</sdf>\n'
        model_config += '    <sdf version="1.5">model.sdf</sdf>\n'
        model_config += '  </model>'

        f = open(sub_dir + "/model.config", 'w')
        f.write(model_config)
        f.close()


        ################################
        # write the model.sdf
        ################################
        model_sdf = ""
        model_sdf += '<?xml version="1.0" ?>\n'
        model_sdf += '<sdf version="1.5">\n'
        model_sdf += '  <model name="' + sub_dir + '">\n'
        model_sdf += '    <link name="link">\n'
        model_sdf += '      <inertial>\n'
        model_sdf += '        <pose>0 0 0 0 0 0</pose>\n'
        model_sdf += '        <mass>0.390</mass>\n'
        model_sdf += '       <inertia>\n'
        model_sdf += '          <ixx>0</ixx>\n'
        model_sdf += '          <ixy>0</ixy>\n'
        model_sdf += '          <ixz>0</ixz>\n'
        model_sdf += '          <iyy>0</iyy>\n'
        model_sdf += '          <iyz>0</iyz>\n'
        model_sdf += '          <izz>0</izz>\n'
        model_sdf += '        </inertia>\n'
        model_sdf += '      </inertial>\n'
        model_sdf += '      <collision name="collision">\n'
        model_sdf += '        <pose>0 0 0 0 0 0</pose>\n'
        model_sdf += '        <geometry>\n'
        model_sdf += '          <mesh>\n'
        model_sdf += '            <uri>model://' + sub_dir + '/' + sub_dir +'_scaled_centered.dae</uri>\n'
        model_sdf += '          </mesh>\n'
        model_sdf += '        </geometry>\n'
        model_sdf += '        <surface>\n'
        model_sdf += '          <friction>\n'
        model_sdf += '            <ode>\n'
        model_sdf += '              <mu>1.0</mu>\n'
        model_sdf += '              <mu2>1.0</mu2>\n'
        model_sdf += '            </ode>\n'
        model_sdf += '         </friction>\n'
        model_sdf += '          <contact>\n'
        model_sdf += '            <ode>\n'
        model_sdf += '              <kp>10000000.0</kp>\n'
        model_sdf += '              <kd>1.0</kd>\n'
        model_sdf += '              <min_depth>0.001</min_depth>\n'
        model_sdf += '              <max_vel>0.1</max_vel>\n'
        model_sdf += '            </ode>\n'
        model_sdf += '          </contact>\n'
        model_sdf += '        </surface>\n'
        model_sdf += '      </collision>\n'
        model_sdf += '      <visual name="visual">\n'
        model_sdf += '        <pose>0 0 0 0 0 0</pose>\n'
        model_sdf += '        <geometry>\n'
        model_sdf += '          <mesh>\n'
        model_sdf += '            <uri>model://' + sub_dir + '/' + sub_dir +'_scaled_centered.dae</uri>\n'
        model_sdf += '          </mesh>\n'
        model_sdf += '        </geometry>\n'
        model_sdf += '      </visual>\n'
        model_sdf += '    </link>\n'
        model_sdf += '  </model>\n'
        model_sdf += '</sdf>\n'

        f = open(sub_dir + "/model.sdf",'w')
        f.write(model_sdf)
        f.close()

        f = open(sub_dir + "/model-1_4.sdf",'w')
        f.write(model_sdf)
        f.close()


if __name__ == "__main__":
    generate_centered_scaled_meshes()
    generate_dae_files()
    move_files_to_gazebo_subdirs()
    generate_gazebo_config()