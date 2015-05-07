
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
from moveit_msgs.msg import PositionIKRequest, RobotState
from moveit_msgs.msg import RobotTrajectory
from moveit_msgs.srv import GetPositionIK, GetPositionIKRequest

import geometry_msgs.msg
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion

from sensor_msgs.msg import JointState
from goal_pos_generate import generate_goal_points, generate_goal_joints


def Get_current_state(group):
	return	JointState(
        name=group.get_joints()[:7],
        position=group.get_current_joint_values(),
    );
    
def find_IK_solution(ik, target, seed, group_name):
    response = ik( GetPositionIKRequest(ik_request = PositionIKRequest( group_name = group_name,
																		pose_stamped = PoseStamped( header = Header(frame_id="/base_link"),
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

	return target_joint_value

def plan_trajectory(group_handle,pose_target):
		
	ArmJointValue = [];
	target = geometry_msgs.msg.Pose();
	target.position.x = pose_target.x;
	target.position.y = pose_target.y;
	target.position.z = pose_target.z;
	target.orientation.x = pose_target.qx;
	target.orientation.y = pose_target.qy;
	target.orientation.z = pose_target.qz;
	target.orientation.w = pose_target.qw;
	print "EE Target position: ";
	print target;
	
	if pose_target.property is "init_pos":
		print ">>>>>> Go to bin", pose_target.bin_num, "start pos >>>>>>"
		ArmJointValue = left_arm_init_joint_value;
		
	else:
		if pose_target.property is "test_pos":
			print ">>>>>> Go to bin", pose_target.bin_num, "test pos >>>>>>"
		else:
			print ">>>>>> Go to bin", pose_target.bin_num, "drop pos >>>>>>"
				
		current_state = Get_current_state(group_handle);
		
		result = find_IK_solution(ik, target, current_state, group_handle.get_name());
					
		if result.error_code.val != 1:
			attempt = 0;
			Success = False;
			
			while attempt < 100:
				attempt += 1;
				result = find_IK_solution(ik, target, current_state, group_handle.get_name());
				if result.error_code.val == 1:
					Success = True;
					break;
			
			if Success is not True:
				print "Can't find IK solution for Bin ", pose_target.bin_num, pose_target.pnt_property;
				return 1;
		
		ArmJointValue = Copy_joint_value(group_handle.get_name(),result.solution.joint_state.position);
	
	group_handle.set_start_state_to_current_state();
	group_handle.set_joint_value_target(ArmJointValue);
	plan = group_handle.plan();
	# Plan is valid, Save trajectory to file
	if len(plan.joint_trajectory.points):																		
		Save_traj(pose_target,plan);
		print "Executing trajectory";
		group_handle.go();
		rospy.sleep(5);
		return 0;
	else:
		print "Planning failed!";
		return 1;


def pos_test(pose_targets, group_handle, IK_handle, animate_result = False):
  
  test_number = len(pose_targets);
  group = group_handle;  
  if IK_handle is not None:
	 ik = IK_handle;	 
  else:
	  print "No IK solver assigned! Exit!";
	  return False;
  # We have valid targets assigned
  if len(pose_targets):
	count = 1;
	success_number = 0;
	for pose_target in pose_targets:
		
		
		if plan_trajectory(group, pose_target):
			print "--------------- Attempts on bin ", pose_target.bin_num," failed---------------";
			#group = moveit_commander.MoveGroupCommander("arm_left");
			#group.set_planner_id("RRTConnectkConfigDefault");
			#group.allow_replanning(True);
			#group.set_planning_time(20);			
			#print "Attempts 2 on bin", pose_target.bin_num;
			#if plan_trajectory(group, pose_target):				
			#	print "Test on bin", pose_target.bin_num, "failed!";
			#	group = moveit_commander.MoveGroupCommander("arm_left_with_torso");
			#	group.set_planner_id("RRTConnectkConfigDefault");
			#	group.allow_replanning(True);
			#	group.set_planning_time(20);
		else:
			success_number += 1;			
		
								
	if success_number == test_number:
		print "Available for all position!";
		return True;
	else:
		print "Can't find IK solution for all target position!"
		print "Success ratio:", success_number, "/",test_number;
		return False;
  else:
	  print "No target Assigned, Exit!";
	  return False;

def goal_jnt_val_test(goal_jnt_value_set, group_handle, animate_result = False):
	
	success_num = 0;
	for goal_jnt_value in goal_jnt_value_set:
		if len(goal_jnt_value.value):
			
			group_handle.set_start_state_to_current_state();
			group_handle.set_joint_value_target(goal_jnt_value.value);			
			plan = group_handle.plan();
			count  = 0;
			while len(plan.joint_trajectory.points) == 0:
				plan = group_handle.plan();
				count += 1;
				if count > 100:
					break;
			if len(plan.joint_trajectory.points):			
				print "Executing trajectory",goal_jnt_value.bin_num;
				group_handle.execute(plan);
				#for point in plan.joint_trajectory.points:
				#	point.velocities = [0]*len(point.velocities);
				#	point.accelerations = [0]*len(point.accelerations);										
				#Save_traj(goal_jnt_value,plan);
				rospy.sleep(5);
				success_num += 1;
			else:
				print "Planning failed!";
		else:
			print "Joint value is empty!";
	
	print "Success number:", success_num;


if __name__=='__main__':
  try:
	
	print ">>>> Initializing... >>>>"
	moveit_commander.roscpp_initialize(sys.argv);
	rospy.init_node('IK_Solution_Test', anonymous=True);  
	#robot = moveit_commander.RobotCommander();
	
	scene = moveit_commander.PlanningSceneInterface();	
	print ">>>> Import Bin model, Generate Testing Targets >>>>"
	if len(sys.argv)>1:
	  X_pos = float(sys.argv[1]);
	  Y_pos = float(sys.argv[2]);
	  Z_pos = float(sys.argv[3]);	  
	else:
	  print "No distance assigned, using default parameters"
	  X_pos = 1.35;
	  Y_pos = 0;
	  Z_pos = 0;
	  
	#Goal_points = generate_goal_points(Bin_base_x = X_pos, Bin_base_y = Y_pos, Bin_base_z = Z_pos);
	#print "Total", len(Goal_points), "targets need to be test";
	
	Goal_jnt_val_set = generate_goal_joints()
	print "Total", len(Goal_jnt_val_set), "traj need to be test";
	
	bin_pose = PoseStamped();
	bin_pose.pose.position.x = X_pos;
	bin_pose.pose.position.y = Y_pos;
	bin_pose.pose.position.z = Z_pos;
	
	bin_pose.pose.orientation.x = 0.5;	
	bin_pose.pose.orientation.y = 0.5;	
	bin_pose.pose.orientation.z = 0.5;	
	bin_pose.pose.orientation.w = 0.5;
		
	scene.attach_mesh(link = "base_link", 
					  name = "kiva_pod", 
					  pose = bin_pose,
					  filename = "Model/pod_lowres.stl");
	
	print ">>>> Set Init Position >>>>"
	arm_left_group = moveit_commander.MoveGroupCommander("arm_left");	
	#arm_left_group.set_planner_id("RRTstarkConfigDefault");	
	arm_left_group.set_planner_id("RRTConnectkConfigDefault");	
	#arm_left_group.set_planner_id("RRTkConfigDefault");	
	arm_left_group.allow_replanning(True);
	arm_left_group.set_planning_time(30);

	arm_right_group = moveit_commander.MoveGroupCommander("arm_right_torso"); 
	#arm_right_group.set_planner_id("RRTstarkConfigDefault");	
	arm_right_group.set_planner_id("RRTConnectkConfigDefault");
	#arm_right_group.set_planner_id("RRTkConfigDefault");
	arm_right_group.allow_replanning(True);
	arm_right_group.set_planning_time(30);
	

#	pos_init(arm_left_group, arm_right_group);
	
	print ">>>> Waiting for service `compute_ik` >>>>";
	rospy.wait_for_service('compute_ik');
	ik = rospy.ServiceProxy("compute_ik", GetPositionIK);
					  
	print ">>>> Start Testing >>>>"
	#pos_test(Goal_points,arm_left_group, ik, animate_result = True)
	goal_jnt_val_test(Goal_jnt_val_set,arm_right_group, animate_result = True)

	print "**** Test End ****"
	moveit_commander.roscpp_shutdown()
    
  except rospy.ROSInterruptException:
    pass