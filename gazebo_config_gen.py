

import os
from off_utils.off_handler import OffHandler

sub_dirs  = os.listdir('.')

off_handler = OffHandler()

for sub_dir in sub_dirs:
    if "D0" not in sub_dir:
        continue
    print sub_dir
    off_file = sub_dir + '/' + sub_dir + '.off'
    off_handler.read(off_file)
    scale = off_handler.get_scale_factor()
    #print sub_dir

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
    model_sdf += '          <ixx>0.00058</ixx>\n'
    model_sdf += '         <ixy>0</ixy>\n'
    model_sdf += '          <ixz>0</ixz>\n'
    model_sdf += '          <iyy>0.00058</iyy>\n'
    model_sdf += '          <iyz>0</iyz>\n'
    model_sdf += '          <izz>0.00019</izz>\n'
    model_sdf += '        </inertia>\n'
    model_sdf += '      </inertial>\n'
    model_sdf += '      <collision name="collision">\n'
    model_sdf += '        <pose>0 0 0 0 0 0</pose>\n'
    model_sdf += '        <geometry>\n'
    model_sdf += '          <mesh>\n'
    model_sdf += '            <uri>model://' + sub_dir + '/' + sub_dir +'.dae</uri>\n'
    model_sdf += '            <scale>' + str(scale) + ' ' + str(scale) + ' ' + str(scale) + ' </scale>\n'
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
    model_sdf += '            <uri>model://' + sub_dir + '/' + sub_dir +'.dae</uri>\n'
    model_sdf += '            <scale>' + str(scale) + ' ' + str(scale) + ' ' + str(scale) + ' </scale>\n'
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