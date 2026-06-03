clear()

def pbaixo():
	if get_pos_y()==(get_world_size()-1):
			for i in range(get_world_size()):
				if get_entity_type()==None:
					if (get_pos_x() + get_pos_y()) %2 == 0:
						plant(Entities.Tree)
					else:
						plant(Entities.Carrot)
					while (get_water()<=0.25):
						use_item(Items.Water,3)
				
				if can_harvest():
					harvest()
					plant(Entities.Carrot)
					while (get_water()<=0.25):
						use_item(Items.Water,3)
				if get_pos_y()==0:
					move(East)
					break
				move(South)
				
def pcima():
	for i in range(get_world_size()):
		if get_entity_type()==None:
			if (get_pos_x() + get_pos_y()) %2 == 0:
						plant(Entities.Tree)
			else:
				plant(Entities.Carrot)
			while (get_water()<=0.25):
				use_item(Items.Water,3)
				
		if can_harvest():
			harvest()
			if (get_pos_x() + get_pos_y()) %2 == 0:
						plant(Entities.Tree)
			else:
				plant(Entities.Carrot)
			while (get_water()<=0.25):
				use_item(Items.Water,3)
		if get_pos_y()==(get_world_size()-1):
			move(East)
			break
		move(North)
iniciou = False
while True:
	if get_pos_y()==(get_world_size()-1):
				for i in range(get_world_size()):
					till()
					if get_pos_y()==0:
						move(East)
						break
					move(South)
	if get_pos_x()==0 and get_pos_y()==0:
		if iniciou:
			break
		else:
			iniciou = True
						
	for i in range(get_world_size()):
			till()
			if get_pos_y()==(get_world_size()-1):
				move(East)
				break
			move(North)

while True:
	pbaixo()
	pcima()