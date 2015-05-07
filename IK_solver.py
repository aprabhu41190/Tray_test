import sys
import copy
import rospy
from std_msgs.msg import String
from std_msgs.msg import Header

import moveit_commander
import moveit_msgs.msg
from moveit_msgs.msg import PositionIKRequest, RobotState
from moveit_msgs.srv import GetPositionIK, GetPositionIKRequest

import geometry_msgs.msg
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion

from sensor_msgs.msg import JointState
from goal_pos_generate import generate_goal_points

def get_current_state(group):
	return JointState(
		name = group.get_joints()[:8],
		position = group.get_current_joint_values()
		)

def find_IK(ik, target, seed, group_name):
	    response = ik( GetPositionIKRequest(ik_request = PositionIKRequest( group_name = group_name,
																		pose_stamped = PoseStamped( header = Header(frame_id=""),
																									pose = target),
																		robot_state = RobotState(joint_state=seed))
										) )	 
	    return response

def copy_joint_value(group_name, joint_values):
	count =  0 
	target_joint_value = []

	target_joint_value.append(copy.deepcopy(joint_values[26]))

	for count in range(1,27):
		if group_name == "arm_left_torso":
			if count > 1 and count < 9:
				target_joint_value.append(copy.deepcopy(joint_values[count-1]))
		elif group_name == "arm_right_torso":		
			if count > 19 and count < 27:
				target_joint_value.append(copy.deepcopy(joint_values[count-1]))

#	for num in range(1,12):
#		target_joint_value.append(0.0)
#	for value in joint_values:
#		if group_name == "arm_left_torso":
#			if count == 0:
#				target_joint_value.append(copy.deepcopy(value))
#			elif count > 1 and count < 10:
#				target_joint_value.append(copy.deepcopy(value))
#		elif group_name == "arm_right_torso":
#			if count > 19 and count < 28:
#				target_joint_value.append(copy.deepcopy(value))
#		count += 1
#	print target_joint_value

	return target_joint_value

def position_test(pose_targets, group, IK_handle, animate = False):

	test_number = len(pose_targets)
	print "**********Reference Frame: %s **********" % group.get_end_effector_link()

	if IK_handle != None:
		IK = IK_handle
	else:
		print "No IK solver assigned. Exit!"
		return False

	if len(pose_targets):
		count = 0
		success = 0 
		for pose in pose_targets:
			count += 1

			target = geometry_msgs.msg.Pose()
			
			target.orientation.x =  0.0112
			target.orientation.y =  0.7072
			target.orientation.z = -0.7068
			target.orientation.w = -0.0031

			target.position.x = pose.x
			target.position.y = pose.y
			target.position.z = pose.z

			print target.position
			current_state = get_current_state(group)
#			print "************************************************"
#			print current_state
			result = find_IK(IK, target, current_state, group.get_name())

#			print "************************************************"	
#			print result.solution.joint_state 

			if result.error_code.val != 1:
#				if count%4 != 1:
				print "Bin ", count/3 , "test failed!"
			else:
				success += 1
				target_joint = copy_joint_value(group.get_name(), result.solution.joint_state.position)

				if animate:
					print "********** Displaying Trajectory ", count, "**********"
					if len(target_joint):
						group.set_joint_value_target(target_joint)
						plan = group.plan()
						rospy.sleep(5)
						print "********** Executing Trajectory **********"
						group.go()
						rospy.sleep(5)

		if success == test_number:
			print "Solution available for all positions!"
			return True
		else:
			print "Can't find solution for all positions!"
			print "Success ratio: ", success, "/", test_number
			return False
	else:
		print "No target assigned. Exit!"
		return False

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

		arm_right_group = moveit_commander.MoveGroupCommander("arm_right_torso")
		arm_right_group.set_planner_id("RRTstarkConfigDefault")
		arm_right_group.set_planning_time(60)

		print ">>>>>>>>>> Waiting for service 'compute_ik' <<<<<<<<<<"
		rospy.wait_for_service('compute_ik')
		ik = rospy.ServiceProxy("compute_ik", GetPositionIK)

		print ">>>>>>>>>> Testing <<<<<<<<<<"
		position_test(goal_points, arm_right_group, ik, animate = True)

		print "********** Test End **********"
		moveit_commander.roscpp_shutdown()

	except rospy.ROSInterruptException:
		pass