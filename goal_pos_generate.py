import copy

class point:
	def __init__(self):
		self.x = 0 
		self.y = 0
		self.z = 0
		self.orx =  0.0112
		self.ory =  0.7072
		self.orz = -0.7068
		self.orw = -0.0031
		""" Function doc """

class Joint:
	def __init__(self):
		self.bin_num = 0
		self.property = "test pos"
		self.value = []

def generate_goal_points( Shelf_x, Shelf_y, Shelf_z ):
	
	goal_pos = [] 
	goal_joints = []
	bin_values = []

	TrayLength = 0.5
	### Bin Dimensions ###
	Bin_depth = 0.430
	Start_gap = 0.100

	LeftBinWidth = 0.240
	CenterBinWidth = 0.300
	RightBinWidth = 0.240

	BaseHeight = 0.835
	BottomLayer = 0.225
	SecondLayer = 0.190
	ThirdLayer = 0.190
	TopLayer = 0.225

	LeftShift = CenterBinWidth/2 + LeftBinWidth/2 
	RightShift = CenterBinWidth/2 + RightBinWidth/2 

	Level4 = BaseHeight + BottomLayer + SecondLayer + ThirdLayer + TopLayer/2
	Level3 = BaseHeight + BottomLayer + SecondLayer + ThirdLayer/2
	Level2 = BaseHeight + BottomLayer + SecondLayer/2
	Level1 = BaseHeight + BottomLayer/2

	Entry_X = Shelf_x - Bin_depth - Start_gap - TrayLength

	# Setting Configuration:
	
	#	1		2		3
	#	4		5		6
	#	7		8		9
	#	10		11		12
	#		   Base


	bin1 = point() 
	bin1.x = Entry_X 
	bin1.y = Shelf_y + LeftShift
	bin1.z = Shelf_z + Level4
	bin_values.append(bin1)

	bin2 = point() 
	bin2.x = Entry_X 
	bin2.y = Shelf_y
	bin2.z = Shelf_z + Level4
	bin_values.append(bin2)

	bin3 = point() 
	bin3.x = Entry_X 
	bin3.y = Shelf_y + RightShift
	bin3.z = Shelf_z + Level4
	bin_values.append(bin3)

	bin4 = point() 
	bin4.x = Entry_X 
	bin4.y = Shelf_y + LeftShift
	bin4.z = Shelf_z + Level3
	bin_values.append(bin4)

	bin5 = point() 
	bin5.x = Entry_X 
	bin5.y = Shelf_y
	bin5.z = Shelf_z + Level3
	bin_values.append(bin5)

	bin6 = point() 
	bin6.x = Entry_X 
	bin6.y = Shelf_y + RightShift
	bin6.z = Shelf_z + Level3
	bin_values.append(bin6)

	bin7 = point() 
	bin7.x = Entry_X 
	bin7.y = Shelf_y + LeftShift
	bin7.z = Shelf_z + Level2
	bin_values.append(bin7)

	bin8 = point() 
	bin8.x = Entry_X 
	bin8.y = Shelf_y
	bin8.z = Shelf_z + Level2
	bin_values.append(bin8)

	bin9 = point() 
	bin9.x = Entry_X 
	bin9.y = Shelf_y + RightShift
	bin9.z = Shelf_z + Level2
	bin_values.append(bin9)

	bin10 = point() 
	bin10.x = Entry_X 
	bin10.y = Shelf_y + LeftShift
	bin10.z = Shelf_z + Level1
	bin_values.append(bin10)

	bin11 = point() 
	bin11.x = Entry_X 
	bin11.y = Shelf_y
	bin11.z = Shelf_z + Level1
	bin_values.append(bin11)

	bin12 = point() 
	bin12.x = Entry_X 
	bin12.y = Shelf_y + RightShift
	bin12.z = Shelf_z + Level1
	bin_values.append(bin12)

#	goal_pos.append(start)

	for bin_num in range(1,13):

		if(bin_num != 8 and bin_num != 9):
			mid = bin_values[bin_num-1]

			point1 = copy.deepcopy(mid)
			point2 = copy.deepcopy(mid) 

			point2.x = point2.x + 0.43

			goal_pos.append(point1)
			goal_pos.append(point2)
			goal_pos.append(point1)
#			goal_pos.append(start)

	return goal_pos

def generate_goal_joints():
	goal_joints = []

	dropOff = Joint()
	dropOff.bin_num = 0
	dropOff.property = "drop_pos"
	dropOff.value = [-0.12815605217058476, 2.047191452103053, 1.3336219224862689, -1.6851435010120746, -0.7074364583590782, 2.9981334643481152, 1.3309577575283984, 1.8640779712799922]
	goal_joints.append(dropOff)

	goal1 = Joint()
	goal1.bin_num = 1
	goal1.value = [0.5605544223647795, 1.4468192489631677, -1.2520338152755075, -2.7420670452220106, -1.4705573745202156, 2.7463702325777475, 0.47302033652079034, -1.187097175706295]
	goal_joints.append(goal1)
	goal_joints.append(dropOff)

	goal2 = Joint()
	goal2.bin_num = 2
	goal2.value = [0.4007363789983349, 1.3464256049565888, -0.7016436110873807, -2.884175231248668, -1.6316827498855255, 2.837026002740442, 0.859137962055642, -1.3075977453544478]
	goal_joints.append(goal2)
	goal_joints.append(dropOff)


	goal3 = Joint()
	goal3.bin_num = 3
	goal3.value = [0.23893966211950973, 1.3320441013901965, -0.39265033633686397, -2.9353981824848816, -1.2912302243981104, 2.9683857360093273, 1.4801404656269932, -1.472376993803517]
	goal_joints.append(goal3)
	goal_joints.append(dropOff)


	goal4 = Joint()
	goal4.bin_num = 4
	goal4.value = [0.3558507862997257, 1.3996852105133917, -1.343463922685873, -2.656393601810547, -2.1443475760680353, 2.746107799932468, -0.3220410117180552, -1.109863380474208]
	goal_joints.append(goal4)
	goal_joints.append(dropOff)

	goal5 = Joint()
	goal5.bin_num = 5
	goal5.value = [-0.1355332640137606, 0.16611311070155316, 1.8604975028078834, 1.6419992785071942, 2.3588316536910234, -1.7123865110905483, 1.6452079253195488, -0.9123621709396166]
	goal_joints.append(goal5)
	goal_joints.append(dropOff)

	goal6 = Joint()
	goal6.bin_num = 6
	goal6.value = [-0.39527201411446516, 0.26743355138728686, 1.5514025085094274, 1.12386597937404, 1.9777160026666385, -0.9730812751467105, 1.875350590881393, -1.2143660267357368]
	goal_joints.append(goal6)
	goal_joints.append(dropOff)

	goal7 = Joint()
	goal7.bin_num = 7
	#goal7.value = [-0.39527201411446516, 0.26743355138728686, 1.5514025085094274, 1.12386597937404, 1.9777160026666385, -0.9730812751467105, 1.875350590881393, -1.2143660267357368]

	goal8 = Joint()
	goal8.bin_num = 8
	#goal8.value = [0.4007363789983349, 1.3464256049565888, -0.7016436110873807, -2.884175231248668, -1.6316827498855255, 2.837026002740442, 0.859137962055642, -1.3075977453544478]

	goal9 = Joint()
	goal9.bin_num = 9
	goal9.value = [-0.3690700106733874, 1.3881227320678913, 1.1438914613236006, 1.1268430083849734, 2.2751900545476853, -0.6654174886127295, 1.7916819524811831, -2.075182890851764]
	goal_joints.append(goal9)
	goal_joints.append(dropOff)

	goal10 = Joint()
	goal10.bin_num = 10
	goal10.value = [0.04283233672774618, 0.944848411606495, 1.3818002598749366, -2.94298364076123, 1.9692811721284933, 2.3655047489075525, 0.291100765932598, -0.19402933426659907]
	goal_joints.append(goal10)
	goal_joints.append(dropOff)

	goal11 = Joint()
	goal11.bin_num = 11
	goal11.value = [-0.4832982741948308, -2.685050710553354, -0.9346841521896815, -2.68620664856921, -2.1236463471970146, -3.0826088823020537, 0.4793467861821847, 2.3173471353072914]
	goal_joints.append(goal11)
	goal_joints.append(dropOff)


	goal12 = Joint()
	goal12.bin_num = 12
	goal12.value = [-0.3973955466520441, 0.04721802344092341, 0.42551193342876537, 0.8968209067699624, -1.868818931722396, -3.122566961428589, 1.23416817834455, 2.2288337763154145]
	goal_joints.append(goal12)
	goal_joints.append(dropOff)

	return goal_joints