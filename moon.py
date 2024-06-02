row_centre_dest_1=[]
row_centre_dest_2=[]
row_centre_dest_3=[]
row_centre_dest_4=[]
row_centre_dest_5=[]
row_centre_dest_6=[]


for _ in range(4):
    i=pygame.Rect((tile_length/4 + tile_length*(_), tile_width/4, tile_length/2,tile_width/2))
    row_centre_dest_1.append(i)

for _ in range(4):
    i=pygame.Rect((tile_length/4 + tile_length*(_), tile_width+ tile_width/4, tile_length/2,tile_width/2))
    row_centre_dest_2.append(i)

for _ in range(4):
    i=pygame.Rect((tile_length/4 + tile_length*(_), 2*tile_width+ tile_width/4, tile_length/2,tile_width/2))
    row_centre_dest_3.append(i)

for _ in range(4):
    i=pygame.Rect((tile_length/4 + tile_length*(_), 3*tile_width+ tile_width/4, tile_length/2,tile_width/2))
    row_centre_dest_4.append(i)
