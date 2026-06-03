clear()
def pbaixo():
		if get_pos_y()==(get_world_size()-1):
				for i in range(get_world_size()):
					if can_harvest():
						harvest()
						#print(get_world_size(),get_pos_y())
					if get_pos_y()==0:
						move(East)
						break
					move(South)
def pcima():
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			#print(get_world_size(),get_pos_y())
		if get_pos_y()==(get_world_size()-1):
			move(East)
			break
		move(North)
while 1:
	pbaixo()
	pcima()