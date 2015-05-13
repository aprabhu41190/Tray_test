import copy

import geometry_msgs.msg
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion


class waypoint:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.z = 0 
		self.qx =  0.50395
		self.qy = -0.485432
		self.qz = -0.510118
		self.qw =  0.50017

def generate_waypoints( Shelf_X, Shelf_Y, Shelf_Z, bin_num):

	waypoints = []

	TrayLength = 0.5
	Bin_depth = 0.430
	Start_gap = 0.13
	offsetX = 0.001527
	offsetY = 0.036179
	offsetZ = 0.01364

	LeftBinWidth = 0.250
	CenterBinWidth = 0.300
	RightBinWith = 0.250

	BaseHeight = 0.835
	BottomLayer = 0.225
	SecondLayer = 0.225
	ThirdLayer = 0.227
	TopLayer = 0.263

	LeftShift = CenterBinWidth/2 + LeftBinWidth/2 + offsetY
	RightShift = CenterBinWidth/2 + RightBinWith/2 + offsetY

	Level4 = BaseHeight + BottomLayer + SecondLayer + ThirdLayer + TopLayer/2 + offsetZ
	Level3 = BaseHeight + BottomLayer + SecondLayer + ThirdLayer/2 + offsetZ
	Level2 = BaseHeight + BottomLayer + SecondLayer/2 + offsetZ
	Level1 = BaseHeight + BottomLayer/2 + offsetZ

	Entry_X = Shelf_X - Bin_depth - Start_gap - TrayLength + offsetX

	# Setting Configuration:
	
	#	1		2		3
	#	4		5		6
	#	7		8		9
	#	10		11		12
	#		   Base

	# start = geometry_msgs.msg.Pose()
	# start.position.x =  0.32127
	# start.position.y = -0.443647
	# start.position.z =  0.627921
	# start.orientation.x =  0.496218
	# start.orientation.y = -0.124756
	# start.orientation.z = -0.165146
	# start.orientation.w =  0.843167


	# tilt1 = geometry_msgs.msg.Pose()
	# tilt1.position.x =  0.317953
	# tilt1.position.y = -0.434752
	# tilt1.position.z =  0.641989
	# tilt1.orientation.x =  0.538331
	# tilt1.orientation.y = -0.117649
	# tilt1.orientation.z = -0.149793
	# tilt1.orientation.w =  0.820927

	# tilt2 = geometry_msgs.msg.Pose()
	# tilt2.position.x =  0.307791
	# tilt2.position.y = -0.419551
	# tilt2.position.z =  0.678059
	# tilt2.orientation.x =  0.633326
	# tilt2.orientation.y = -0.0994578
	# tilt2.orientation.z = -0.112856
	# tilt2.orientation.w =  0.759125

	# tilt3 = geometry_msgs.msg.Pose()
	# tilt3.position.x =  0.321292
	# tilt3.position.y = -0.443657
	# tilt3.position.z =  0.627932
	# tilt3.orientation.x =  0.696192
	# tilt3.orientation.y = -0.0956158
	# tilt3.orientation.z = -0.0942283
	# tilt3.orientation.w =  0.705191

	# fwd = geometry_msgs.msg.Pose()
	# fwd.position.x =  0.36
	# fwd.position.y = -0.405748 - Shelf_Y
	# fwd.position.z =  0.619773
	# fwd.orientation.x =  0.50395
	# fwd.orientation.y = -0.485432
	# fwd.orientation.z = -0.510118
	# fwd.orientation.w =  0.50017

	start = geometry_msgs.msg.Pose()
	start.position.x =  0.327324
	start.position.y = -0.446507
	start.position.z =  0.62792
	start.orientation.x =  0.0163016
	start.orientation.y = -0.507649
	start.orientation.z =  0.764183
	start.orientation.w =  0.397556


	tilt1 = geometry_msgs.msg.Pose()
	tilt1.position.x =  0.326629
	tilt1.position.y = -0.446425
	tilt1.position.z =  0.627745
	tilt1.orientation.x =  0.000715694
	tilt1.orientation.y = -0.560974
	tilt1.orientation.z =  0.737628
	tilt1.orientation.w =  0.375783

	tilt2 = geometry_msgs.msg.Pose()
	tilt2.position.x =  0.32673
	tilt2.position.y = -0.446473
	tilt2.position.z =  0.627771
	tilt2.orientation.x =  0.00239386
	tilt2.orientation.y = -0.627858
	tilt2.orientation.z =  0.692506
	tilt2.orientation.w =  0.35528

	tilt3 = geometry_msgs.msg.Pose()
	tilt3.position.x =  0.326721
	tilt3.position.y = -0.446537
	tilt3.position.z =  0.627769
	tilt3.orientation.x = -0.00895653
	tilt3.orientation.y =  0.694375
	tilt3.orientation.z = -0.639786
	tilt3.orientation.w = -0.329299

	fwd0 = geometry_msgs.msg.Pose()
	fwd0.position.x =  0.326721
	fwd0.position.y = -0.446537
	fwd0.position.z =  0.627769
	fwd0.orientation.x =  0.50395
	fwd0.orientation.y = -0.485432
	fwd0.orientation.z = -0.510118
	fwd0.orientation.w =  0.50017

	fwd = geometry_msgs.msg.Pose()
	fwd.position.x =  0.36
	fwd.position.y = -0.405748 - Shelf_Y
	fwd.position.z =  0.619773
	fwd.orientation.x =  0.50395
	fwd.orientation.y = -0.485432
	fwd.orientation.z = -0.510118
	fwd.orientation.w =  0.50017


	bin1 = geometry_msgs.msg.Pose()
	bin1.position.x = Entry_X
	bin1.position.y = Shelf_Y + LeftShift
	bin1.position.z = Shelf_Z + Level4
	bin1.orientation.x =  0.50395
	bin1.orientation.y = -0.485432
	bin1.orientation.z = -0.510118
	bin1.orientation.w =  0.50017

	bin1t = geometry_msgs.msg.Pose()
	bin1t.position.x = Entry_X
	bin1t.position.y = Shelf_Y + LeftShift
	bin1t.position.z = Shelf_Z + Level4
	bin1t.orientation.x = -0.254063
	bin1t.orientation.y = -0.473887
	bin1t.orientation.z =  0.420963
	bin1t.orientation.w =  0.730529


	bin2 = geometry_msgs.msg.Pose()
	bin2.position.x = Entry_X
	bin2.position.y = Shelf_Y
	bin2.position.z = Shelf_Z + Level4
	bin2.orientation.x =  0.50395
	bin2.orientation.y = -0.485432
	bin2.orientation.z = -0.510118
	bin2.orientation.w =  0.50017

	bin3 = geometry_msgs.msg.Pose()
	bin3.position.x = Entry_X
	bin3.position.y = Shelf_Y - RightShift
	bin3.position.z = Shelf_Z + Level4	
	bin3.orientation.x =  0.50395
	bin3.orientation.y = -0.485432
	bin3.orientation.z = -0.510118
	bin3.orientation.w =  0.50017

	bin4 = geometry_msgs.msg.Pose()
	bin4.position.x = Entry_X
	bin4.position.y = Shelf_Y + LeftShift
	bin4.position.z = Shelf_Z + Level3
	bin4.orientation.x =  0.50395
	bin4.orientation.y = -0.485432
	bin4.orientation.z = -0.510118
	bin4.orientation.w =  0.50017

	bin5 = geometry_msgs.msg.Pose()
	bin5.position.x = Entry_X
	bin5.position.y = Shelf_Y 
	bin5.position.z = Shelf_Z + Level3
	bin5.orientation.x =  0.50395
	bin5.orientation.y = -0.485432
	bin5.orientation.z = -0.510118
	bin5.orientation.w =  0.50017

	bin6 = geometry_msgs.msg.Pose()
	bin6.position.x = Entry_X
	bin6.position.y = Shelf_Y - RightShift
	bin6.position.z = Shelf_Z + Level3
	bin6.orientation.x =  0.50395
	bin6.orientation.y = -0.485432
	bin6.orientation.z = -0.510118
	bin6.orientation.w =  0.50017

	bin7 = geometry_msgs.msg.Pose()
	bin7.position.x = Entry_X
	bin7.position.y = Shelf_Y + LeftShift
	bin7.position.z = Shelf_Z + Level2
	bin7.orientation.x =  0.50395
	bin7.orientation.y = -0.485432
	bin7.orientation.z = -0.510118
	bin7.orientation.w =  0.50017

	bin8 = geometry_msgs.msg.Pose()
	bin8.position.x = Entry_X
	bin8.position.y = Shelf_Y 
	bin8.position.z = Shelf_Z + Level2
	bin8.orientation.x =  0.50395
	bin8.orientation.y = -0.485432
	bin8.orientation.z = -0.510118
	bin8.orientation.w =  0.50017

	bin9 = geometry_msgs.msg.Pose()
	bin9.position.x = Entry_X
	bin9.position.y = Shelf_Y - RightShift
	bin9.position.z = Shelf_Z + Level2
	bin9.orientation.x =  0.50395
	bin9.orientation.y = -0.485432
	bin9.orientation.z = -0.510118
	bin9.orientation.w =  0.50017

	bin10 = geometry_msgs.msg.Pose()
	bin10.position.x = Entry_X
	bin10.position.y = Shelf_Y + LeftShift
	bin10.position.z = Shelf_Z + Level1
	bin10.orientation.x =  0.50395
	bin10.orientation.y = -0.485432
	bin10.orientation.z = -0.510118
	bin10.orientation.w =  0.50017

	bin11 = geometry_msgs.msg.Pose()
	bin11.position.x = Entry_X
	bin11.position.y = Shelf_Y 
	bin11.position.z = Shelf_Z + Level1
	bin11.orientation.x =  0.50395
	bin11.orientation.y = -0.485432
	bin11.orientation.z = -0.510118
	bin11.orientation.w =  0.50017

	bin12 = geometry_msgs.msg.Pose()
	bin12.position.x = Entry_X
	bin12.position.y = Shelf_Y - RightShift
	bin12.position.z = Shelf_Z + Level1
	bin12.orientation.x =  0.50395
	bin12.orientation.y = -0.485432
	bin12.orientation.z = -0.510118
	bin12.orientation.w =  0.50017

	waypoints.append(start)
	waypoints.append(tilt1)
	waypoints.append(tilt2)
	waypoints.append(tilt3)
	waypoints.append(fwd0)
	waypoints.append(fwd)
		

	# if( bin_num == 1 ):
	# 	waypoints.append(bin3)
	# 	waypoints.append(bin1)
	# 	waypoints.append(bin1t)
	# elif( bin_num == 2):
	# 	waypoints.append(bin3)
	# 	waypoints.append(bin2)
	# elif( bin_num == 3):
	# 	waypoints.append(bin3)
	# elif( bin_num == 4):
	# 	waypoints.append(bin3)
	# 	waypoints.append(bin4)
	# elif( bin_num == 5):
	# 	waypoints.append(bin3)
	# 	waypoints.append(bin5)
	# elif( bin_num == 6):
	# 	waypoints.append(bin3)
	# 	waypoints.append(bin6)
	# elif( bin_num == 7):
	# 	waypoints.append(bin9)
	# 	waypoints.append(bin7)
	# elif( bin_num == 8):
	# 	waypoints.append(bin9)
	# 	waypoints.append(bin8)
	# elif( bin_num == 9):
	# 	waypoints.append(bin3)
	# 	waypoints.append(bin9)
	# elif( bin_num == 10):
	# 	waypoints.append(bin10)
	# elif( bin_num == 11):
	# 	waypoints.append(bin12)
	# 	waypoints.append(bin11)
	# else:
	# 	waypoints.append(bin12)

	return waypoints
