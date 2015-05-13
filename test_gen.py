import sys
import copy
import rospy
import StringIO
from std_msgs.msg import String
from std_msgs.msg import Header
from std_msgs.msg import Int64
from StringIO import StringIO

import moveit_commander
import moveit_msgs.msg
from moveit_msgs.msg import PositionIKRequest, RobotState, Constraints, OrientationConstraint
from moveit_msgs.srv import GetPositionIK, GetPositionIKRequest

import geometry_msgs.msg
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion

from sensor_msgs.msg import JointState
from goal_pos_generate import generate_goal_points

def Save_traj(bin_num,traj_property,plan):
	file_name = "Traj/bin_"+ str(bin_num) +"/"+ str(traj_property);		
	print "saving bin.",bin_num,"trajectory to file",file_name;
	buf = StringIO();
	plan.serialize(buf);				
	f = open(file_name,"w");
	f.write(buf.getvalue());
	f.close();


if __name__ == '__main__':
	try:

		if len(sys.argv)>1:
			X_pos = float(sys.argv[1])
			Y_pos = float(sys.argv[2])
			Z_pos = float(sys.argv[3])
		else:
			print "No distance assigned, using default parameters"
			X_pos = 1.32
			Y_pos = 0
			Z_pos = 0

		goal_points = generate_goal_points( Shelf_x = X_pos, Shelf_y = Y_pos, Shelf_z = Z_pos)

		print ">>>>>>>>>> Initializing... <<<<<<<<<<"
		moveit_commander.roscpp_initialize(sys.argv)
		rospy.init_node('IK_test', anonymous = True)

		robot = moveit_commander.RobotCommander()
		scene = moveit_commander.PlanningSceneInterface()

		display_trajectory_publisher = rospy.Publisher(
                                    '/move_group/display_planned_path',
                                    moveit_msgs.msg.DisplayTrajectory)

		arm_right_group = moveit_commander.MoveGroupCommander("arm_right_torso")
		arm_right_group.set_planner_id("RRTstarkConfigDefault")
		arm_right_group.set_planning_time(10)

		bin_pose = PoseStamped();
		bin_pose.pose.position.x = 1.0;
		bin_pose.pose.position.y = 0;
		bin_pose.pose.position.z = 0;
	
		bin_pose.pose.orientation.x = 0.5;	
		bin_pose.pose.orientation.y = 0.5;	
		bin_pose.pose.orientation.z = 0.5;	
		bin_pose.pose.orientation.w = 0.5;
		
		# collision_object = moveit_msgs.msg.CollisionObject()

		# # scene.addCollisionObjects(collision_object)

		scene.attach_mesh(link = "base_link", 
					  name = "order_bin", 
					  pose = bin_pose,
					  filename = "Model/bin.stl");

		print ">>>>>>>>>> Waiting for service 'compute_ik' <<<<<<<<<<"
		rospy.wait_for_service('compute_ik')
		ik = rospy.ServiceProxy("compute_ik", GetPositionIK)

		# goal_points = generate_goal_points(X_pos,Y_pos,Z_pos)

		# group_variable_values = arm_right_group.get_current_joint_values()
		# group_variable_values[0] = 0
		# group_variable_values[1] = -0.27125427199145014
		# group_variable_values[2] = -1.1498847117494644
		# group_variable_values[3] = -1.2408312987225103
		# group_variable_values[4] =  1.6936065617174285
		# group_variable_values[5] = -2.5951005253646096
		# group_variable_values[6] = -1.217012615492259
		# group_variable_values[7] = -1.9341596127994072
		# arm_right_group.set_joint_value_target(group_variable_values)

		# plan1 = arm_right_group.plan()
		# arm_right_group.execute(plan1)

		print ">>>>>>>>>> Testing <<<<<<<<<<"
		path = []

		# start = geometry_msgs.msg.Pose()
		# start.position.x =  0.359592
		# start.position.y =  -0.519298
		# start.position.z =  0.624757
		# start.orientation.x =  0.429311
		# start.orientation.y =  -0.418094
		# start.orientation.z = -0.558991
		# start.orientation.w =  0.573078		

		start = geometry_msgs.msg.Pose()
		start.position.x =  0.32127
		start.position.y =  -0.443647
		start.position.z =  0.627921
		start.orientation.x =  0.496218
		start.orientation.y =  -0.124756
		start.orientation.z = -0.165146
		start.orientation.w =  0.843167


		start1 = geometry_msgs.msg.Pose()
		start1.position.x =  0.317953
		start1.position.y =  -0.434752
		start1.position.z =  0.641989
		start1.orientation.x =  0.538331
		start1.orientation.y =  -0.117649
		start1.orientation.z = -0.149793
		start1.orientation.w =  0.820927

		start2 = geometry_msgs.msg.Pose()
		start2.position.x =  0.307791
		start2.position.y =  -0.419551
		start2.position.z =  0.678059
		start2.orientation.x =  0.633326
		start2.orientation.y =  -0.0994578
		start2.orientation.z = -0.112856
		start2.orientation.w =  0.759125

		start3 = geometry_msgs.msg.Pose()
		start3.position.x =  0.321292
		start3.position.y =  -0.443657
		start3.position.z =  0.627932
		start3.orientation.x =  0.696192
		start3.orientation.y =  -0.0956158
		start3.orientation.z = -0.0942283
		start3.orientation.w =  0.705191

#Working!!
		# start = geometry_msgs.msg.Pose()
		# start.position.x =  0.126969
		# start.position.y =  -0.265004
		# start.position.z =  0.796843
		# start.orientation.x =  0.46273205788363436
		# start.orientation.y = -0.4688770373099473
		# start.orientation.z = -0.5269554127154963
		# start.orientation.w =  0.5369835747023032	

		mid = geometry_msgs.msg.Pose()
		mid.position.x =  0.36
		mid.position.y = -0.405748
		mid.position.z =  0.619773
		mid.orientation.x =  0.50395
		mid.orientation.y =  -0.485432
		mid.orientation.z =  -0.510118
		mid.orientation.w =  0.50017

		mid1 = geometry_msgs.msg.Pose()
		mid1.position.x =  0.36
		mid1.position.y =  -0.275
		mid1.position.z =  1.6435 - 0.08
		mid1.orientation.x =  0.50395
		mid1.orientation.y =  -0.485432
		mid1.orientation.z =  -0.510118
		mid1.orientation.w =  0.50017

		mid2 = geometry_msgs.msg.Pose()
		mid2.position.x =  0.36
		mid2.position.y =  0.275
		mid2.position.z =  1.6435 - 0.08
		mid2.orientation.x =  0.50395
		mid2.orientation.y =  -0.485432
		mid2.orientation.z =  -0.510118
		mid2.orientation.w =  0.50017

		mid3 = geometry_msgs.msg.Pose()
		mid3.position.x =  0.80
		mid3.position.y =  0.275
		mid3.position.z =  1.6435 - 0.10
		mid3.orientation.x =  0.50395
		mid3.orientation.y =  -0.485432
		mid3.orientation.z =  -0.510118
		mid3.orientation.w =  0.50017


		mid4 = geometry_msgs.msg.Pose()
		mid4.position.x =  0.126969
		mid4.position.y =  -0.45
		mid4.position.z =  0.796843
		mid4.orientation.x =  0.46273205788363436
		mid4.orientation.y =  -0.4688770373099473
		mid4.orientation.z =  -0.5269554127154963
		mid4.orientation.w =  0.5369835747023032

		mid5 = geometry_msgs.msg.Pose()
		mid5.position.x =  0.47498
		mid5.position.y =  -0.277006
		mid5.position.z =  0.737571
		mid5.orientation.x =  0.707326
		mid5.orientation.y =  0.00194324
		mid5.orientation.z =  0.00189404
		mid5.orientation.w =  0.706882

		# ocm = OrientationConstraint()
		# ocm.link_name = "arm_right_link_7_t"
		# ocm.header.frame_id = "base_link"
		# ocm.orientation.x = 0.46273205788363436
		# ocm.orientation.y = -0.4688770373099473
		# ocm.orientation.z = -0.5269554127154963
		# ocm.orientation.w = 0.5369835747023032
		# ocm.absolute_x_axis_tolerance = 0.1
		# ocm.absolute_y_axis_tolerance = 0.1
		# ocm.absolute_z_axis_tolerance = 0.1
		# ocm.weight = 1.0

		# ocm1 = OrientationConstraint()
		# ocm1.link_name = "arm_right_link_7_t"
		# ocm1.header.frame_id = "base_link"
		# ocm1.orientation.x = 0.463315
		# ocm1.orientation.y = 0.475989
		# ocm1.orientation.z = -0.521358
		# ocm1.orientation.w = 0.535687
		# ocm1.absolute_x_axis_tolerance = 0.1
		# ocm1.absolute_y_axis_tolerance = 0.1
		# ocm1.absolute_z_axis_tolerance = 0.1
		# ocm1.weight = 1.0

		# test_constraints = Constraints()
		# test_constraints.orientation_constraints.append(ocm);
		# # test_constraints.orientation_constraints.append(ocm1);
		# arm_right_group.set_path_constraints(test_constraints);

		# mid1 = geometry_msgs.msg.Pose()
		# mid1.position.x =  0.40
		# mid1.position.y =  0.275
		# mid1.position.z =  1.3985
		# mid1.orientation.x =  0.506527
		# mid1.orientation.y =  -0.493362
		# mid1.orientation.z = -0.49387
		# mid1.orientation.w =  0.50608

		# mid2 = geometry_msgs.msg.Pose()
		# mid2.position.x =  0.40	
		# mid2.position.y =  0.0
		# mid2.position.z =  1.3985
		# mid2.orientation.x =  0.689549
		# mid2.orientation.y =  -0.141975
		# mid2.orientation.z = 0.137415
		# mid2.orientation.w =  0.696766

		# mid21 = geometry_msgs.msg.Pose()
		# mid21.position.x =  0.40	
		# mid21.position.y =  0.0
		# mid21.position.z =  1.3985
		# mid21.orientation.x =  0.506527
		# mid21.orientation.y =  -0.493362
		# mid21.orientation.z = -0.49387
		# mid21.orientation.w =  0.50608

		# mid3 = geometry_msgs.msg.Pose()
		# mid3.position.x =  0.83
		# mid3.position.y =  0.0
		# mid3.position.z =  1.3985
		# mid3.orientation.x =  0.506527
		# mid3.orientation.y =  -0.493362
		# mid3.orientation.z = -0.49387
		# mid3.orientation.w =  0.50608

		# mid3 = geometry_msgs.msg.Pose()
		# mid3.position.x =  0.29
		# mid3.position.y =  0.275
		# mid3.position.z =  1.6435
		# mid3.orientation.x =  0.704678
		# mid3.orientation.y =  0.00853603
		# mid3.orientation.z = -0.0223218
		# mid3.orientation.w =  0.709124

#		mid = geometry_msgs.msg.Pose()
#		mid.position.x =  0.245513
#		mid.position.y = -0.434602
#		mid.position.z =  0.568589
#		mid.orientation.x =  0.490285
#		mid.orientation.y = -0.492092
#		mid.orientation.z = -0.515267
#		mid.orientation.w =  0.501962

#		end = geometry_msgs.msg.Pose()
#		end.position.x =  0.29
#		end.position.y =  0
#		end.position.z =  1.6435
#		end.orientation.x =  0.701623
#		end.orientation.y =  0.00404495
#		end.orientation.z = -0.00479594
#		end.orientation.w =  0.712521

		path.append(copy.deepcopy(start))
		path.append(copy.deepcopy(start1))
		path.append(copy.deepcopy(start2))
		path.append(copy.deepcopy(start3))
		path.append(copy.deepcopy(mid))
		path.append(copy.deepcopy(mid1))
		# path.append(copy.deepcopy(mid))
		path.append(copy.deepcopy(mid2))
		# path.append(copy.deepcopy(mid1))
		# path.append(copy.deepcopy(mid))
		# path.append(copy.deepcopy(start))
		# path.append(copy.deepcopy(mid1))
		# path.append(copy.deepcopy(mid21))
		# path.append(copy.deepcopy(mid3))
#		path.append(copy.deepcopy(end))
		
		# arm_right_group.set_pose_target(mid1)
		# arm_right_group.plan()


		(plan, fraction) = arm_right_group.compute_cartesian_path(
                             path,   # waypoints to follow
                             0.01,        # eef_step
                             0.0)         # jump_threshold

		# arm_right_group.execute(plan)
		Save_traj("1","Pick",plan)

		print "============ Waiting while RVIZ displays plan..."
		rospy.sleep(10)
		# print plan.joint_trajectory.points[2].positions

		plan1 = copy.deepcopy(plan)
		# print plan1.joint_trajectory.points 
		print "******************************"
		a = len(plan.joint_trajectory.points)
		# print a
		for i in range(1,a+1):
			# print i-1, "   ", a-i
			# print plan1.joint_trajectory.points[i-1].positions
			# print plan.joint_trajectory.points[i-1].positions
			# print " ************************************"
			plan1.joint_trajectory.points[a-i].positions = copy.deepcopy(plan.joint_trajectory.points[i-1].positions)
			# print plan1.joint_trajectory.points[i-1].positions
			# print plan.joint_trajectory.points[i-1].positions
			# print " %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"

		# print plan1.joint_trajectory.points

		# plan2 = plan.positions.reverse()

		print "============ Visualizing plan1"
		display_trajectory = moveit_msgs.msg.DisplayTrajectory()

		display_trajectory.trajectory_start = robot.get_current_state()
		display_trajectory.trajectory.append(plan1)
		display_trajectory_publisher.publish(display_trajectory);

		Save_traj("1","Drop",plan1)

		rospy.sleep(10)

		# arm_right_group.execute(plan1)

		print "********** Test End **********"
		moveit_commander.roscpp_shutdown()

	except rospy.ROSInterruptException:
		pass