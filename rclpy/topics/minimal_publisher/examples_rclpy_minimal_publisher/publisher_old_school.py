# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##%%
from time import sleep
from traceback import print_tb

import rclpy

#from std_msgs.msg import String
from geometry_msgs.msg import Pose

# We do not recommend this style as ROS 2 provides timers for this purpose,
# and it is recommended that all nodes call a variation of spin.
# This example is only included for completeness because it is similar to examples in ROS 1.
# For periodic publication please see the other examples using timers.

target_pose = Pose()
##%%
def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('minimal_publisher')

    publisher = node.create_publisher(Pose, 'topic', 10)

    
    
    while rclpy.ok():
        # target_pose.position = (target_pose.position.x, target_pose.position.y, target_pose.position.z)
        node.get_logger().info('x: "%s"' % target_pose.position.x)
        node.get_logger().info('y: "%s"' % target_pose.position.y)
        node.get_logger().info('z: "%s"' % target_pose.position.z)
        publisher.publish(target_pose)
        #print(target_pose.position.x, target_pose.position.y, target_pose.position.z)
        sleep(0.5)  # seconds

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()

x_coord = -0.5
y_coord = -0.6
z_coord = 0.1

xyz_robot = [x_coord, y_coord, z_coord]
#print(xyz_robot[1])

target_pose.position.x = xyz_robot[0]
target_pose.position.y = xyz_robot[1]
target_pose.position.z = xyz_robot[2]

if __name__ == '__main__':
    main()

## %%
