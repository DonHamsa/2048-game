import pygame 
import random
import time

pygame.init()
window_height=900
window_length=900
tiles_in_row=4
tiles_in_column=4
tile_length=int(window_length/tiles_in_row)
tile_width=int(window_height/tiles_in_column)
background_fill=(204, 192, 179)
rec_color=(187, 173, 160)
tile_number_color=(119, 110, 101)
ii=pygame.time.Clock()
boarder=5
line_thickeness=boarder
font=pygame.font.Font(size=60)
font_end_game=pygame.font.Font(size=90)
delay=0.2
animation_speed=60
window=pygame.display.set_mode((window_length,window_height))
game_name=pygame.display.set_caption('2048')
window.fill(background_fill)

total_columns_rec=[]

num_in_tile={}

occupied_tile_dic={} 

row_1_tile_rect=[]
row_2_tile_rect=[]
row_3_tile_rect=[]
row_4_tile_rect=[]

tiles_color={'2':(238, 228, 218),
         '4':(237, 224, 200),
         '8':(242, 177, 121),
         '16':(245, 149, 99),
         '32':(246, 124, 95),
         '64':(246, 94, 59),
         '128':(237, 207, 114),
         '256':(237, 204, 97),
         '512':(237, 200, 80),
         '1024':(237, 197, 63),
         '2048':(237, 194, 46)}


pygame.draw.rect(window,rec_color,(0,0,window_length,window_height),line_thickeness)

for index, vertical_line in enumerate(range(tile_length,window_length,tile_length), start=1):
    pygame.draw.line(window,rec_color,(vertical_line,0),(vertical_line, window_height),line_thickeness)
   
for horizontal_line in range(tile_width,window_height,tile_width):
    pygame.draw.line(window,rec_color,(boarder,horizontal_line),(window_length, horizontal_line),line_thickeness)


for colors in range(0,tiles_in_row):
    if tiles_in_row==1:
        multiply=2
        second_multiply=2
    else:
        multiply=1.5
        second_multiply=1.5

    if colors!=0 and colors!=tiles_in_row-1:
        i=pygame.Rect(tile_length*colors+0.5*boarder,boarder,tile_length-boarder,tile_width-boarder*multiply)
        row_1_tile_rect.append(i)
        num_in_tile[str(i)]=0
    if colors==0:
        i=pygame.Rect(boarder,boarder,tile_length-second_multiply*boarder,tile_width-boarder*multiply)
        row_1_tile_rect.append(i)
        num_in_tile[str(i)]=0
    if colors==tiles_in_row-1:
        i=pygame.Rect(tile_length*colors+0.5*boarder,boarder,tile_length-1.5*boarder,tile_width-boarder*multiply)
        row_1_tile_rect.append(i)
        num_in_tile[str(i)]=0
        
        
for colors in range(0,tiles_in_row):
    if tiles_in_row==2:
        multiply=1.5
    else:
        multiply=1

    if colors!=0 and colors!=tiles_in_row-1:
        i=pygame.Rect(tile_length*colors+0.5*boarder,tile_width+0.5*boarder,tile_length-boarder,tile_width-multiply*boarder)
        row_2_tile_rect.append(i)
        num_in_tile[str(i)]=0
    if colors==0:
        i=pygame.Rect(tile_length*colors+boarder,tile_width+0.5*boarder,tile_length-1.5*boarder,tile_width-multiply*boarder)
        row_2_tile_rect.append(i)
        num_in_tile[str(i)]=0
    if colors==tiles_in_row-1:
        i=pygame.Rect(tile_length*colors+0.5*boarder,tile_width+0.5*boarder,tile_length-1.5*boarder,tile_width-multiply*boarder)
        row_2_tile_rect.append(i)
        num_in_tile[str(i)]=0
        



for colors in range(0,tiles_in_row):
        if tiles_in_row==3:
            multiply=1.5
        else:
            multiply=1

        if colors!=0 and colors!=tiles_in_row-1:
            i=pygame.Rect(tile_length*colors+0.5*boarder,2*tile_width+0.5*boarder,tile_length-boarder,tile_width-multiply*boarder)
            row_3_tile_rect.append(i)
            num_in_tile[str(i)]=0
        if colors==0:
            i=pygame.Rect(tile_length*colors+boarder,2*tile_width+0.5*boarder,tile_length-1.5*boarder,tile_width-multiply*boarder)
            row_3_tile_rect.append(i)
            num_in_tile[str(i)]=0
        if colors==tiles_in_row-1:
            i=pygame.Rect(tile_length*colors+0.5*boarder,2*tile_width+0.5*boarder,tile_length-1.5*boarder,tile_width-multiply*boarder)
            row_3_tile_rect.append(i)
            num_in_tile[str(i)]=0
            

for colors in range(0,tiles_in_row):
        if colors!=0 and colors!=tiles_in_row-1:
            i=pygame.Rect(tile_length*colors+0.5*boarder,3*tile_width+0.5*boarder,tile_length-boarder,tile_width-1.5*boarder)
            row_4_tile_rect.append(i)
            num_in_tile[str(i)]=0
        if colors==0:
            i=pygame.Rect(tile_length*colors+boarder,3*tile_width+0.5*boarder,tile_length-1.5*boarder,tile_width-1.5*boarder)
            row_4_tile_rect.append(i)
            num_in_tile[str(i)]=0
        if colors==tiles_in_row-1:
            i=pygame.Rect(tile_length*colors+0.5*boarder,3*tile_width+0.5*boarder,tile_length-1.5*boarder,tile_width-1.5*boarder)
            row_4_tile_rect.append(i)
            num_in_tile[str(i)]=0


total_rows_rec=[]
total_rows_rec.append(row_1_tile_rect)
total_rows_rec.append(row_2_tile_rect)
total_rows_rec.append(row_3_tile_rect)
total_rows_rec.append(row_4_tile_rect)


def are_all_tiles_occupied():

    all_occupied_tile=True

    for dic_key in occupied_tile_dic:
        key_value=occupied_tile_dic[dic_key]
        if key_value==0:
            all_occupied_tile=False
        
    if all_occupied_tile==True:
            return True 


def create_lines_for_grid():
    for number_for_line in range(1,tiles_in_row):
        vertical=pygame.draw.rect(window,rec_color,(number_for_line*tile_length-0.5*boarder, 0, boarder, window_height))
        horizontal=pygame.draw.rect(window,rec_color,(0, number_for_line*tile_width-0.5*boarder, window_length,boarder))
    pygame.display.update()       
create_lines_for_grid()


pygame.display.update() 


def creating_transition_right(old_rect,new_rect,color,num_old_tile):
     
     x=old_rect.x
     y=old_rect.y
     width=old_rect.width
     height=old_rect.height 

     new_x=new_rect.x
     
     updating_x=x

     difference=new_x-x
     increment=difference/animation_speed
     _=0
     
     while updating_x!=new_x:
        if _ ==1:
            new=pygame.draw.rect(window,background_fill,increment_rect)

        increment_rect=pygame.Rect(updating_x,y,width-0.5*boarder,height)
        i=pygame.draw.rect(window,color,increment_rect)
        create_lines_for_grid()
        pygame.display.update()
        
        _=1
        font_display=font.render(num_old_tile,True, tile_number_color)
        dest=font_display.get_rect(center=increment_rect.center)
        window.blit(font_display,(dest)) 

        updating_x+=increment

        if updating_x+1>new_x:
             new=pygame.draw.rect(window,background_fill,increment_rect)
   
             increment_rect=new_rect
             i=pygame.draw.rect(window,color,new_rect)
             

             font_display=font.render(num_old_tile,True, tile_number_color)
             dest=font_display.get_rect(center=increment_rect.center)
             window.blit(font_display,(dest)) 
       
             create_lines_for_grid()
             pygame.display.update()
             updating_x=new_x
             break 


def creating_transition_left(old_rect,new_rect,color,num_old_tile):
     
     x=old_rect.x
     y=old_rect.y
     width=old_rect.width
     height=old_rect.height 

     new_x=new_rect.x
    

     updating_x=x

     difference=x-new_x
     increment=difference/animation_speed
     _=0
     
     while updating_x!=new_x:
        if _ ==1:
            new=pygame.draw.rect(window,background_fill,increment_rect)

        increment_rect=pygame.Rect(updating_x,y,width,height)
        i=pygame.draw.rect(window,color,increment_rect)
        create_lines_for_grid()
        pygame.display.update()
        
        _=1
        font_display=font.render(num_old_tile,True, tile_number_color)
        dest=font_display.get_rect(center=increment_rect.center)
        window.blit(font_display,(dest)) 

        updating_x-=increment

        if updating_x-1<new_x:
             create_lines_for_grid()
             new=pygame.draw.rect(window,background_fill,increment_rect)
             increment_rect=new_rect
             i=pygame.draw.rect(window,color,new_rect)

             font_display=font.render(num_old_tile,True, tile_number_color)
             dest=font_display.get_rect(center=increment_rect.center)
             window.blit(font_display,(dest)) 
             create_lines_for_grid()

             pygame.display.update()
             updating_x=new_x
             break 


def creating_transition_up(old_rect,new_rect,color,num_old_tile):
     old_x=old_rect.x
     old_y=old_rect.y
     width=old_rect.width
     height=old_rect.height 

     new_y=new_rect.y
    

     updating_y=old_y

     difference=old_y-new_y
     increment=difference/animation_speed
     _=0
     
     while updating_y!=new_y:
        if _ ==1:
            new=pygame.draw.rect(window,background_fill,increment_rect)

        increment_rect=pygame.Rect(old_x,updating_y,width,height)
        i=pygame.draw.rect(window,color,increment_rect)
        create_lines_for_grid()
        pygame.display.update()
        
        _=1
        font_display=font.render(num_old_tile,True, tile_number_color)
        dest=font_display.get_rect(center=increment_rect.center)
        window.blit(font_display,(dest)) 

        updating_y-=increment

        if updating_y-1<new_y:
             create_lines_for_grid()
             new=pygame.draw.rect(window,background_fill,increment_rect)
             increment_rect=new_rect
             i=pygame.draw.rect(window,color,new_rect)

             font_display=font.render(num_old_tile,True, tile_number_color)
             dest=font_display.get_rect(center=increment_rect.center)
             window.blit(font_display,(dest)) 
             create_lines_for_grid()

             pygame.display.update()
             updating_y=new_y
             break 


def creating_transition_down(old_rect,new_rect,color,num_old_tile):
     old_x=old_rect.x
     old_y=old_rect.y
     width=old_rect.width
     height=old_rect.height 

     new_y=new_rect.y
    

     updating_y=old_y

     difference=new_y-old_y
     increment=difference/animation_speed
     _=0
     
     while updating_y!=new_y:
        if _ ==1:
            new=pygame.draw.rect(window,background_fill,increment_rect)

        increment_rect=pygame.Rect(old_x,updating_y,width,height-boarder)
        i=pygame.draw.rect(window,color,increment_rect)
        create_lines_for_grid()
        pygame.display.update()
        
        _=1
        font_display=font.render(num_old_tile,True, tile_number_color)
        dest=font_display.get_rect(center=increment_rect.center)
        window.blit(font_display,(dest)) 

        updating_y+=increment

        if updating_y+2>new_y:
             create_lines_for_grid()
             new=pygame.draw.rect(window,background_fill,increment_rect)
             increment_rect=new_rect
             i=pygame.draw.rect(window,color,new_rect)

             font_display=font.render(num_old_tile,True, tile_number_color)
             dest=font_display.get_rect(center=increment_rect.center)
             window.blit(font_display,(dest)) 
             create_lines_for_grid()

             pygame.display.update()
             updating_y=new_y
             break 


def create_the_tracking_dic():
    for row in total_rows_rec:
        for rect_value in row:
            occupied_tile_dic[str(rect_value)]=0
create_the_tracking_dic()


def total_column_list():
    for index in range(tiles_in_column):
        columns_rec=[]
        for list in total_rows_rec:
            columns_rec.append(list[index])
            
        total_columns_rec.append(columns_rec)
total_column_list()


def random_tile_num_generator():
    numbers=['2','4']
    ran_num_generator=random.choice(numbers)
    return ran_num_generator


def random_index():
    random_num_index=[]
    for index in range(tiles_in_row):
        random_num_index.append(index)

    random_index=random.choice(random_num_index)
    return random_index

def random_tile_generator():
    
    new_tile=False

    while new_tile==False:

        if are_all_tiles_occupied()==True:
            return None 
        
        random_index_one=random_index()
        random_index_two=random_index()
        return_random_tile_generator=random_tile_num_generator()
        
        rect_value=total_rows_rec[random_index_one][random_index_two]


        if occupied_tile_dic[str(rect_value)]!=1:
            new_tile=True


    num_in_tile[str(rect_value)]=return_random_tile_generator
    occupied_tile_dic[str(rect_value)]=1
    
    random_draw=pygame.draw.rect(window,tiles_color[return_random_tile_generator],rect_value)

    font_display=font.render(return_random_tile_generator,True, tile_number_color)
    dest=font_display.get_rect(center=total_rows_rec[random_index_one][random_index_two].center)
    window.blit(font_display,(dest))
    
    time.sleep(delay)
    pygame.display.update()
    
    return random_draw,return_random_tile_generator


def rect_and_randnum():

    i=random_tile_generator()
    return i



def move_all_right_key(Boolean):

    total_score=0
    
    for row,tiles in enumerate(total_rows_rec):
        
        for index in range(tiles_in_row-1,-1,-1):
                tile_index=index
                rows_index=row

                if tile_index!=tiles_in_row-1:
                    for tile_position in range(tile_index+1,tiles_in_row):
                        if occupied_tile_dic[str(total_rows_rec[rows_index][tile_position])]==1:
                            new_tile_index=tile_position-1
                            break
                        elif occupied_tile_dic[str(total_rows_rec[rows_index][tiles_in_row-1])]==0:
                            new_tile_index=tiles_in_row-1
                        

                else:
                    new_tile_index=tile_index
                
                
                old_rect=total_rows_rec[rows_index][tile_index]
                new_rect=total_rows_rec[rows_index][new_tile_index]
                num_old_tile=num_in_tile[str(old_rect)]


                if num_old_tile!=0:
                    if tile_index!=tiles_in_row-1:
                        if occupied_tile_dic[str(new_rect)]==0:

                            creating_transition_right(old_rect,new_rect,tiles_color[num_old_tile],num_old_tile)
                                
                            occupied_tile_dic[str(new_rect)]=1
                            num_in_tile[str(new_rect)]=str(num_old_tile)

                            occupied_tile_dic[str(old_rect)]=0
                            num_in_tile[str(old_rect)]=0
                    
   
    if Boolean==True:
        for list in total_rows_rec: 
            
                    if tiles_in_row==4:
                     if num_in_tile[str(list[3])]!=0 and num_in_tile[str(list[2])]!=0:

                        if num_in_tile[str(list[3])]==num_in_tile[str(list[2])]:
                                

                            number_in_tile=int(num_in_tile[str(list[3])])

                            creating_transition_right(list[2],list[3],tiles_color[str(number_in_tile*2)],str(number_in_tile*2))

                            num_in_tile[str(list[2])]=0
                            num_in_tile[str(list[3])]=str(number_in_tile*2)

                            occupied_tile_dic[str(list[2])]=0
                            occupied_tile_dic[str(list[3])]=1

                            total_score+=number_in_tile*2

            
                    if num_in_tile[str(list[2])]!=0 and num_in_tile[str(list[1])]!=0:

                        if num_in_tile[str(list[2])]==num_in_tile[str(list[1])]:
                                
                            number_in_tile=int(num_in_tile[str(list[1])])

                            creating_transition_right(list[1],list[2],tiles_color[str(number_in_tile*2)],str(number_in_tile*2))
                            
                            num_in_tile[str(list[1])]=0
                            num_in_tile[str(list[2])]=str(number_in_tile*2)

                            occupied_tile_dic[str(list[1])]=0
                            occupied_tile_dic[str(list[2])]=1

                            total_score+=number_in_tile*2

                    
                    if num_in_tile[str(list[1])]!=0 and num_in_tile[str(list[0])]!=0:

                        if num_in_tile[str(list[1])]==num_in_tile[str(list[0])]:

                            number_in_tile=int(num_in_tile[str(list[1])])

                            creating_transition_right(list[0],list[1],tiles_color[str(number_in_tile*2)],str(number_in_tile*2))

                            num_in_tile[str(list[0])]=0
                            num_in_tile[str(list[1])]=str(number_in_tile*2)

                            occupied_tile_dic[str(list[0])]=0
                            occupied_tile_dic[str(list[1])]=1

                            total_score+=number_in_tile*2

    pygame.display.update()
    
    return total_score


def move_all_left_key(Boolean): 

    total_score=0

    for row,tiles in enumerate(total_rows_rec):
        
        for index in range(0,tiles_in_row ):
                tile_index=index
                rows_index=row

            
                if tile_index!=0:
                    for tile_position in range(0,index+1):
                        if occupied_tile_dic[str(total_rows_rec[rows_index][tile_position])]==0 :
                            new_tile_index=tile_position
                            break
                        
                else:
                    new_tile_index=tile_index
                
                
                old_rect=total_rows_rec[rows_index][tile_index]
                new_rect=total_rows_rec[rows_index][new_tile_index]
                num_old_tile=num_in_tile[str(old_rect)]


                if num_old_tile!=0:
                    if tile_index!=0:
                        if occupied_tile_dic[str(new_rect)]==0:
                               
                            creating_transition_left(old_rect,new_rect,tiles_color[num_old_tile],num_old_tile)

                            occupied_tile_dic[str(new_rect)]=1
                            num_in_tile[str(new_rect)]=str(num_old_tile)

                            occupied_tile_dic[str(old_rect)]=0
                            num_in_tile[str(old_rect)]=0

                           
    if Boolean==True:
        for list in total_rows_rec: 
                                
                            if num_in_tile[str(list[1])]!=0 and num_in_tile[str(list[0])]!=0:

                                if num_in_tile[str(list[1])]==num_in_tile[str(list[0])]:

                                    number_in_tile=int(num_in_tile[str(list[1])])

                                    creating_transition_left(list[1],list[0],tiles_color[str(number_in_tile*2)],str(number_in_tile*2))

                                    num_in_tile[str(list[1])]=0
                                    num_in_tile[str(list[0])]=str(number_in_tile*2)

                                    occupied_tile_dic[str(list[1])]=0
                                    occupied_tile_dic[str(list[0])]=1

                                    total_score+=number_in_tile*2

            
                                if num_in_tile[str(list[2])]!=0 and num_in_tile[str(list[1])]!=0:

                                    if num_in_tile[str(list[2])]==num_in_tile[str(list[1])]:
                                            
                                        number_in_tile=int(num_in_tile[str(list[1])])

                                        creating_transition_left(list[2],list[1],tiles_color[str(number_in_tile*2)],str(number_in_tile*2))

                                        num_in_tile[str(list[2])]=0
                                        num_in_tile[str(list[1])]=str(number_in_tile*2)

                                        occupied_tile_dic[str(list[2])]=0
                                        occupied_tile_dic[str(list[1])]=1

                                        total_score+=number_in_tile*2

                                if tiles_in_row==4:
                                 if num_in_tile[str(list[3])]!=0 and num_in_tile[str(list[2])]!=0:

                                    if num_in_tile[str(list[3])]==num_in_tile[str(list[2])]:
                                            
                                        number_in_tile=int(num_in_tile[str(list[3])])

                                        creating_transition_left(list[3],list[2],tiles_color[str(number_in_tile*2)],str(number_in_tile*2))

                                        num_in_tile[str(list[3])]=0
                                        num_in_tile[str(list[2])]=str(number_in_tile*2)

                                        occupied_tile_dic[str(list[3])]=0
                                        occupied_tile_dic[str(list[2])]=1

                                        total_score+=number_in_tile*2
                        
    pygame.display.update()
    return total_score


def move_all_keys_up(Boolean):

    total_score=0

    for row,tiles in enumerate(total_rows_rec):
        
        for index in range(0,tiles_in_row ):
                tile_index=index
                rows_index=row
                

                if row!=0:
                    for tile_position in range(0,rows_index+1):
                        if occupied_tile_dic[str(total_rows_rec[tile_position][tile_index])]==0 :
                            updated_row_index=tile_position
                            break
                        
                else:
                    updated_row_index=rows_index
                
                
                old_rect=total_rows_rec[rows_index][tile_index]
                new_rect=total_rows_rec[updated_row_index][tile_index]
                num_old_tile=num_in_tile[str(old_rect)]


                if num_old_tile!=0:
                    if row!=0:
                        if occupied_tile_dic[str(new_rect)]==0:
                               

                            creating_transition_up(old_rect,new_rect,tiles_color[num_old_tile],num_old_tile)

                            occupied_tile_dic[str(new_rect)]=1
                            num_in_tile[str(new_rect)]=str(num_old_tile)


                            occupied_tile_dic[str(old_rect)]=0
                            num_in_tile[str(old_rect)]=0

    
    if Boolean==True:
        for column_list in total_columns_rec: 
            
                    if num_in_tile[str(column_list[1])]!=0 and num_in_tile[str(column_list[0])]!=0:

                        if num_in_tile[str(column_list[1])]==num_in_tile[str(column_list[0])]:

                            number_in_tile=int(num_in_tile[str(column_list[1])])

                            creating_transition_up(column_list[1],column_list[0],tiles_color[str(number_in_tile*2)],str(number_in_tile*2))

                            num_in_tile[str(column_list[1])]=0
                            num_in_tile[str(column_list[0])]=str(number_in_tile*2)

                            occupied_tile_dic[str(column_list[1])]=0
                            occupied_tile_dic[str(column_list[0])]=1

                            total_score+=number_in_tile*2


                    if num_in_tile[str(column_list[2])]!=0 and num_in_tile[str(column_list[1])]!=0:

                        if num_in_tile[str(column_list[2])]==num_in_tile[str(column_list[1])]: 
                                
                            number_in_tile=int(num_in_tile[str(column_list[1])])
                            
                            creating_transition_up(column_list[2],column_list[1],tiles_color[str(number_in_tile*2)],str(number_in_tile*2))

                            num_in_tile[str(column_list[2])]=0
                            num_in_tile[str(column_list[1])]=str(number_in_tile*2)

                            occupied_tile_dic[str(column_list[2])]=0
                            occupied_tile_dic[str(column_list[1])]=1

                            total_score+=number_in_tile*2

                        
                    if tiles_in_row==4:
                     if num_in_tile[str(column_list[3])]!=0 and num_in_tile[str(column_list[2])]!=0:

                        if num_in_tile[str(column_list[3])]==num_in_tile[str(column_list[2])]: 
                                
                            number_in_tile=int(num_in_tile[str(column_list[3])])

                            creating_transition_up(column_list[3],column_list[2],tiles_color[str(number_in_tile*2)],str(number_in_tile*2))

                            num_in_tile[str(column_list[3])]=0
                            num_in_tile[str(column_list[2])]=str(number_in_tile*2)

                            occupied_tile_dic[str(column_list[3])]=0
                            occupied_tile_dic[str(column_list[2])]=1

                            total_score+=number_in_tile*2

    pygame.display.update()
    return total_score 
   

def move_all_keys_down(Boolean):

    total_score=0

    for row,tiles in enumerate(total_columns_rec):
        
        for index in range(tiles_in_column-1,-1,-1):
                tile_index=index
                rows_index=row
                

                if tile_index!=tiles_in_column-1:
                    for tile_position in range(tiles_in_column-1,tile_index-1,-1):
                        if occupied_tile_dic[str(total_columns_rec[row][tile_position])]==0 :
                            updated_row_index=tile_position 
                            break
                        
                else:
                    updated_row_index=tile_index
                
                
                old_rect=total_columns_rec[row][tile_index]
                new_rect=total_columns_rec[row][updated_row_index]
                num_old_tile=num_in_tile[str(old_rect)]


                if num_old_tile!=0:
                    if tile_index!=tiles_in_column-1:
                        if occupied_tile_dic[str(new_rect)]==0:
                               
                            creating_transition_down(old_rect,new_rect,tiles_color[num_old_tile],num_old_tile)   

                            occupied_tile_dic[str(new_rect)]=1
                            num_in_tile[str(new_rect)]=str(num_old_tile)

                            occupied_tile_dic[str(old_rect)]=0
                            num_in_tile[str(old_rect)]=0

    
    if Boolean==True:
        for column_list in total_columns_rec: 
                        
                    if tiles_in_row==4:
                     if num_in_tile[str(column_list[3])]!=0 and num_in_tile[str(column_list[2])]!=0:

                        if num_in_tile[str(column_list[3])]==num_in_tile[str(column_list[2])]:

                            number_in_tile=int(num_in_tile[str(column_list[3])])

                            creating_transition_down(column_list[2],column_list[3],tiles_color[str(number_in_tile*2)],str(number_in_tile*2))

                            num_in_tile[str(column_list[2])]=0
                            num_in_tile[str(column_list[3])]=str(number_in_tile*2)

                            occupied_tile_dic[str(column_list[2])]=0
                            occupied_tile_dic[str(column_list[3])]=1

                            total_score+=number_in_tile*2


                    if num_in_tile[str(column_list[1])]!=0 and num_in_tile[str(column_list[2])]!=0:

                        if num_in_tile[str(column_list[1])]==num_in_tile[str(column_list[2])]: 
                                
                            number_in_tile=int(num_in_tile[str(column_list[2])])

                            creating_transition_down(column_list[1],column_list[2],tiles_color[str(number_in_tile*2)],str(number_in_tile*2))

                            num_in_tile[str(column_list[1])]=0
                            num_in_tile[str(column_list[2])]=str(number_in_tile*2)

                            occupied_tile_dic[str(column_list[1])]=0
                            occupied_tile_dic[str(column_list[2])]=1

                            total_score+=number_in_tile*2

                    
                    if num_in_tile[str(column_list[0])]!=0 and num_in_tile[str(column_list[1])]!=0:

                        if num_in_tile[str(column_list[0])]==num_in_tile[str(column_list[1])]: 
                                
                            number_in_tile=int(num_in_tile[str(column_list[1])])
                            
                            creating_transition_down(column_list[0],column_list[1],tiles_color[str(number_in_tile*2)],str(number_in_tile*2))

                            num_in_tile[str(column_list[0])]=0
                            num_in_tile[str(column_list[1])]=str(number_in_tile*2)

                            occupied_tile_dic[str(column_list[0])]=0
                            occupied_tile_dic[str(column_list[1])]=1

                            total_score+=number_in_tile*2
    
    pygame.display.update()
    return total_score 
      

def game():

    
    run=True
    fps=ii.tick(60)
    rect_and_randnum()
    rect_and_randnum()
    total_score=0
    has_it_run_once=False

    while run==True:
        game_over=True

        for event in pygame.event.get():
            if event.type==pygame.QUIT:        
                run=False
                break 


            try:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        accumulating_score=move_all_right_key(True)
                        total_score+=accumulating_score
                        move_all_right_key(False)
                        rect_and_randnum()
                        pygame.display.update()
                        continue
            except:
                continue
                
            try:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        accumulating_score_two=move_all_left_key(True)
                        total_score+=accumulating_score_two
                        move_all_left_key(False)
                        rect_and_randnum()
                        pygame.display.update()
                        continue
            except:
                continue

            try:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        accumulating_score_three=move_all_keys_up(True)
                        total_score+=accumulating_score_three
                        move_all_keys_up(False)
                        rect_and_randnum()
                        pygame.display.update()
                        continue
            except:
                continue

            try:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_DOWN:
                        accumulating_score_four=move_all_keys_down(True)
                        total_score+=accumulating_score_four
                        move_all_keys_down(False)
                        rect_and_randnum()
                        pygame.display.update()
                        continue
            except:
                continue

            
            if are_all_tiles_occupied()==True:
              

                for list in total_rows_rec:
                    for index,number in enumerate(range(1,tiles_in_row)):
                        rect=str(list[index])
                        rect_2=str(list[number])
                        if num_in_tile[rect]==num_in_tile[rect_2]:
                            game_over=False 
                            break
                    if game_over==False:
                        run=True
                        break

                for list in total_columns_rec:
                    for index,number in enumerate(range(1,tiles_in_column)):
                        rect=str(list[index])
                        rect_2=str(list[number])
                        if num_in_tile[rect]==num_in_tile[rect_2]:
                            game_over=False 
                            break
                    if game_over==False:
                        run=True
                        break
                
                
                if has_it_run_once==False:
                    if game_over==True:

                       
                        end_game_surface=pygame.Surface((window_length,window_height))
                        transparency=end_game_surface.set_alpha(150)
                        end_game_surface.fill((255,0,0))
                        window.blit(end_game_surface, (0,0))

                        font_display=font_end_game.render(f'Your score is: {total_score} ',True, (255,255,255))
                        rect=pygame.rect.Rect(0,0,window_length,window_height)
                        rect_2=font_display.get_rect(center=rect.center)
                        window.blit(font_display, rect_2)
                        
                        has_it_run_once=True

                        pygame.display.update()
                
game()






















