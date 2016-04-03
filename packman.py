import sys
import pygame
from pygame.locals import *
from math import floor
import random





def init_window():
    pygame.init()
    pygame.display.set_mode((cell_size*feild_size_x,cell_size*feild_size_y),FULLSCREEN)
    pygame.display.set_caption('Packman from Gravity Falls',)




def draw_background(screen, image=None):
    if image:
        screen.blit(image,(0,0))
    else:
        background=pygame.Surface(screen.get_size())
        background.fill((0,0,0))
        screen.blit(background,(0,0))
        
        
        
        
class GameObject(pygame.sprite.Sprite):



    # x,y - координаты персонажа на поле.
    # self.feild_x,self.field_y - координаты персонажа непосредственно на поле
    # self.image - изображение персонажа
    # self.feild_size_y - размер игрового поля(в клетках) по горизонтали
    # self.feild_size_x - размер игрового поля(в клетках) по вертикали
    # self.cell_size - размер одной клетки(в пикселях, клетка квадратная)
    # self.tick - время жизни персонажа в условных внутриигровых единицах



    def __init__(self,x,y,feild_size_x,feild_size_y,cell_size):
    
        self.x=0
        self.y=0
        self.screen_rect=None
        self.feild_size_x=feild_size_x
        self.feild_size_y=feild_size_y
        self.cell_size=cell_size
        self.tick=0
        self.set_coord(x,y)


    def set_coord(self,x,y):
        self.x=x
        self.y=y
        self.screen_rect=Rect(floor(x)*self.cell_size,floor(y)*self.cell_size,self.feild_size_x,self.feild_size_y)

    def game_tick(self):
        self.tick+=1

    def draw(self,screen,image):
        screen.blit(image,(self.screen_rect.x,self.screen_rect.y))






class Ghost(GameObject):
    
    def __init__(self,x,y,image,feild_size_x,feild_size_y,cell_size):
        GameObject.__init__(self,x,y,feild_size_x,feild_size_y,cell_size)
        self.image=image
        self.image_with_direction=image['right']
        self.direction=None
        self.speed=4.0/10.0
    
    def game_tick(self):
    
        super(Ghost,self).game_tick()
        
        if self.tick%10==0 or self.direction==None:
            self.direction=random.choice(['up','right','left','down']) 
            
        if self.direction=='up':
            self.y-=self.speed
            if self.y<0 or map.get(floor(self.x),floor(self.y))=='W' or map.get(floor(self.x),floor(self.y))=='B' or map.get(floor(self.x),floor(self.y))=='U':
                self.y+=self.speed
                self.direction=random.choice(['up','right','left','down'])
            self.image_with_direction=self.image[self.direction]
        
        elif self.direction=='right':
            self.x+=self.speed
            if self.x>feild_size_x or map.get(floor(self.x),floor(self.y))=='W' or map.get(floor(self.x),floor(self.y))=='B' or map.get(floor(self.x),floor(self.y))=='U':
                self.x-=self.speed
                self.direction=random.choice(['up','right','left','down'])
            self.image_with_direction=self.image[self.direction]
        
        elif self.direction=='down':
            self.y+=self.speed
            if self.y>feild_size_y or map.get(floor(self.x),floor(self.y))=='W' or map.get(floor(self.x),floor(self.y))=='B' or map.get(floor(self.x),floor(self.y))=='U':
                self.y-=self.speed
                self.direction=random.choice(['up','right','left','down'])
            self.image_with_direction=self.image[self.direction]
        
        elif self.direction=='left':
            self.x-=self.speed
            if self.x<0 or map.get(floor(self.x),floor(self.y))=='W' or map.get(floor(self.x),floor(self.y))=='B' or map.get(floor(self.x),floor(self.y))=='U':
                self.x+=self.speed
                self.direction=random.choice(['up','right','left','down'])
            self.image_with_direction=self.image[self.direction]
                
        self.set_coord(self.x,self.y)
        
        
        
def is_wall(x,y):
        if map.get(floor(x),floor(y))=='W' or map.get(floor(x),floor(y))=='B'or map.get(floor(x),floor(y))=='U':
            return True
        return False
    
    
        
        
        
class CleverGhost(Ghost):

    def __init__(self,x,y,image,image_for_packman,feild_size_x,feild_size_y,cell_size):
        Ghost.__init__(self,x,y,image,feild_size_x,feild_size_y,cell_size)  
        self.image=image
        self.image_for_packman=image_for_packman
        self.image_with_direction=self.image['right']
        self.direction=None
        self.speed=4.0/10.0
        self.flag='free'
        self.run_for_packman_coord_x=[]
        self.run_for_packman_coord_y=[]
        self.image_direction_of_packman=[]
        self.running_time=0
    
           
        
    def check_flag(self):
        if self.flag=='free':
            if self.direction=='up':                
                if floor(self.y)-7<=floor(packman.y) and floor(packman.y)<=floor(self.y) and floor(self.x)==floor(packman.x):
                    flagger=True
                    for i in range(floor(packman.y),floor(self.y)):
                        if is_wall(self.x,i):
                            flagger=False
                    if flagger:        
                        self.flag='up'
                        self.run_for_packman_coord_x.append(self.x)
                        self.run_for_packman_coord_x.append(self.x)
                        self.run_for_packman_coord_x.append(self.x)
                        self.run_for_packman_coord_x.append(self.x)
                        self.run_for_packman_coord_x.append(self.x)
                        self.run_for_packman_coord_x.append(self.x)
                        self.run_for_packman_coord_x.append(self.x)
                        self.run_for_packman_coord_x.append(self.x)
                        self.run_for_packman_coord_y.append(self.y-1)
                        self.run_for_packman_coord_y.append(self.y-1)
                        self.run_for_packman_coord_y.append(self.y-2)
                        self.run_for_packman_coord_y.append(self.y-2)
                        self.run_for_packman_coord_y.append(self.y-3)
                        self.run_for_packman_coord_y.append(self.y-3)
                        self.run_for_packman_coord_y.append(self.y-4)
                        self.run_for_packman_coord_y.append(self.y-4)
                        self.image_direction_of_packman.append('up')
                        self.image_direction_of_packman.append('up')
                        self.image_direction_of_packman.append('up')
                        self.image_direction_of_packman.append('up')
                        self.image_direction_of_packman.append('up')
                        self.image_direction_of_packman.append('up')
                        self.image_direction_of_packman.append('up')
                        self.image_direction_of_packman.append('up')               
                
            elif self.direction=='down':
                flagger=True
                for i in range(floor(self.y),):
                    if is_wall(self.x,i):
                        flagger=False
                if floor(self.y)<=floor(packman.y) and floor(packman.y)<=floor(self.y)+7 and floor(self.x)==floor(packman.x):
                    flagger=True
                    for i in range(floor(self.y),floor(packman.y)):
                        if is_wall(self.x,i):
                            flagger=False
                    if flagger:
                        self.flag='down'
                        self.run_for_packman_coord_x.append(self.x)
                        self.run_for_packman_coord_x.append(self.x)
                        self.run_for_packman_coord_x.append(self.x)
                        self.run_for_packman_coord_x.append(self.x)
                        self.run_for_packman_coord_x.append(self.x)
                        self.run_for_packman_coord_x.append(self.x)
                        self.run_for_packman_coord_x.append(self.x)
                        self.run_for_packman_coord_x.append(self.x)
                        self.run_for_packman_coord_y.append(self.y+1)
                        self.run_for_packman_coord_y.append(self.y+1)
                        self.run_for_packman_coord_y.append(self.y+2)
                        self.run_for_packman_coord_y.append(self.y+2)
                        self.run_for_packman_coord_y.append(self.y+3)
                        self.run_for_packman_coord_y.append(self.y+3)
                        self.run_for_packman_coord_y.append(self.y+4)
                        self.run_for_packman_coord_y.append(self.y+4)
                        self.image_direction_of_packman.append('down')
                        self.image_direction_of_packman.append('down')
                        self.image_direction_of_packman.append('down')
                        self.image_direction_of_packman.append('down')
                        self.image_direction_of_packman.append('down')
                        self.image_direction_of_packman.append('down')
                        self.image_direction_of_packman.append('down')
                        self.image_direction_of_packman.append('down')
                
            elif self.direction=='right':                
                if self.x<=floor(packman.x) and floor(packman.x)<=self.x+5 and floor(self.y)==floor(packman.y):
                    flagger=True
                    for i in range(floor(self.x),floor(packman.x)):
                        if is_wall(i,self.y):
                            flagger=False
                    if flagger:
                        self.flag='right'
                        self.run_for_packman_coord_x.append(self.x+1)
                        self.run_for_packman_coord_x.append(self.x+1)
                        self.run_for_packman_coord_x.append(self.x+2)
                        self.run_for_packman_coord_x.append(self.x+2)
                        self.run_for_packman_coord_x.append(self.x+3)
                        self.run_for_packman_coord_x.append(self.x+3)
                        self.run_for_packman_coord_x.append(self.x+4)
                        self.run_for_packman_coord_x.append(self.x+4)
                        self.run_for_packman_coord_y.append(self.y)
                        self.run_for_packman_coord_y.append(self.y)
                        self.run_for_packman_coord_y.append(self.y)
                        self.run_for_packman_coord_y.append(self.y)
                        self.run_for_packman_coord_y.append(self.y)
                        self.run_for_packman_coord_y.append(self.y)
                        self.run_for_packman_coord_y.append(self.y)
                        self.run_for_packman_coord_y.append(self.y)
                        self.image_direction_of_packman.append('right')
                        self.image_direction_of_packman.append('right')
                        self.image_direction_of_packman.append('right')
                        self.image_direction_of_packman.append('right')
                        self.image_direction_of_packman.append('right')
                        self.image_direction_of_packman.append('right')
                        self.image_direction_of_packman.append('right')
                        self.image_direction_of_packman.append('right')
                
            elif self.direction=='left':                
                if floor(self.x)-5<floor(packman.x) and floor(packman.x)<floor(self.x) and floor(self.y)==floor(packman.y):
                    flagger=True
                    for i in range(floor(packman.x),floor(self.x)):
                        if is_wall(i,self.y):
                            flagger=False
                    if flagger:
                        self.flag='left'
                        self.run_for_packman_coord_x.append(self.x-1)
                        self.run_for_packman_coord_x.append(self.x-1)
                        self.run_for_packman_coord_x.append(self.x-2)
                        self.run_for_packman_coord_x.append(self.x-2)
                        self.run_for_packman_coord_x.append(self.x-3)
                        self.run_for_packman_coord_x.append(self.x-3)
                        self.run_for_packman_coord_x.append(self.x-4)
                        self.run_for_packman_coord_x.append(self.x-4)
                        self.run_for_packman_coord_y.append(self.y)
                        self.run_for_packman_coord_y.append(self.y)
                        self.run_for_packman_coord_y.append(self.y)
                        self.run_for_packman_coord_y.append(self.y)
                        self.run_for_packman_coord_y.append(self.y)
                        self.run_for_packman_coord_y.append(self.y)
                        self.run_for_packman_coord_y.append(self.y)
                        self.run_for_packman_coord_y.append(self.y)
                        self.image_direction_of_packman.append('left')
                        self.image_direction_of_packman.append('left')
                        self.image_direction_of_packman.append('left')
                        self.image_direction_of_packman.append('left')
                        self.image_direction_of_packman.append('left')
                        self.image_direction_of_packman.append('left')
                        self.image_direction_of_packman.append('left')
                        self.image_direction_of_packman.append('left')
            
        
    def game_tick(self): 
        self.check_flag()   
        if self.flag=='free':
            Ghost.game_tick(self)
        else:
            
            self.run_for_packman_coord_x.append(packman.x)
            self.run_for_packman_coord_y.append(packman.y)
            self.image_direction_of_packman.append(packman.direction)
            self.set_coord(self.run_for_packman_coord_x[self.running_time],self.run_for_packman_coord_y[self.running_time])
            self.image_with_direction=self.image_for_packman[self.image_direction_of_packman[self.running_time]]
            self.running_time+=1        
            
                           
                
                
class Packman(GameObject):
    
    def __init__(self,x,y,image,feild_size_x,feild_size_y,cell_size):
        GameObject.__init__(self,x,y,feild_size_x,feild_size_y,cell_size)
        self.image=image
        self.direction='stop'
        self.speed=4.0/10.0
        self.image_with_direction=self.image['right']
    
    def game_tick(self):
    
        super(Packman,self).game_tick()        
                 
        if self.direction=='up':
            self.y-=self.speed
            if self.y<0 :
                self.y+=self.speed 
            elif map.get(floor(self.x),floor(self.y))=='W':
                self.direction='stop'
                self.y+=self.speed
            self.image_with_direction=self.image['up']            
        
        elif self.direction=='right':
            self.x+=self.speed
            if self.x>feild_size_x:
                self.x-=self.speed 
            elif map.get(floor(self.x),floor(self.y))=='W':
                self.direction='stop'
                self.x-=self.speed 
            self.image_with_direction=self.image['right']                
        
        elif self.direction=='down':
            self.y+=self.speed
            if self.y>feild_size_y:
                self.y-=self.speed
            elif map.get(floor(self.x),floor(self.y))=='W':
                self.direction='stop'
                self.y-=self.speed
            self.image_with_direction=self.image['down']                 
        
        elif self.direction=='left':
            self.x-=self.speed
            if self.x<0:
                self.x+=self.speed
            elif map.get(floor(self.x),floor(self.y))=='W':
                self.direction='stop'
                self.x+=self.speed
            self.image_with_direction=self.image['left']                 
                
        self.set_coord(self.x,self.y)




class Map():
    
    def __init__(self,feild_size_x,feild_size_y,mapfile):
        
        self.map=[['']*feild_size_x for i in range(feild_size_y)]
        self.mapfile=open(mapfile,'r')  
        for y in range(feild_size_y):
            for x in range(0,feild_size_x+1):
                symbol=self.mapfile.read(1)
                if symbol=='\n':
                    pass
                else:
                    self.map[y][x]=symbol
            
        
    def get(self,x,y):
        return self.map[y][x]



class Wall(GameObject):
    
    def __init__(self,x,y,image,feild_size_x,feild_size_y,cell_size):
        GameObject.__init__(self,x,y,feild_size_x,feild_size_y,cell_size)
        self.image=pygame.image.load(image) 
           
class Boom_Wall(GameObject):
    
    def __init__(self,x,y,image,feild_size_x,feild_size_y,cell_size):
        GameObject.__init__(self,x,y,feild_size_x,feild_size_y,cell_size)
        self.image=pygame.image.load(image)



class Food(GameObject):

    def __init__(self,x,y,image,feild_size_x,feild_size_y,cell_size):
        GameObject.__init__(self,x,y,feild_size_x,feild_size_y,cell_size)
        self.image=pygame.image.load(image)
    
        


def process_events(events):
    
    for event in events:
        if (event.type==QUIT) or (event.type==KEYDOWN and event.key==K_ESCAPE):
            sys.exit(0)
        elif event.type==KEYDOWN:
            if event.key==K_UP:
                packman.direction='up'
            elif event.key==K_RIGHT:
                packman.direction='right'
            elif event.key==K_DOWN:
                packman.direction='down'
            elif event.key==K_LEFT:
                packman.direction='left'
            elif event.key==K_SPACE or event.key==K_RSHIFT:
                packman.direction='stop'



map_general_file='./resources/maps/easy_map.txt'

def menu():
    menu_sound=pygame.mixer.Sound('./resources/music/music_menu.wav')
    menu_sound.play(loops=1000)
    flag='work'
    screen=pygame.display.get_surface()
    menu=Rect(13*cell_size,2*cell_size,feild_size_x,feild_size_y)                                                       
    play=Rect(14*cell_size,6*cell_size,feild_size_x,feild_size_y)                                                           
    choose_the_map=Rect(14*cell_size,10*cell_size,feild_size_x,feild_size_y)                                                
    quit=Rect(14*cell_size,14*cell_size,feild_size_x,feild_size_y)                                                          
    map1=Rect(14*cell_size,6*cell_size,feild_size_x,feild_size_y)                                                           
    map2=Rect(14*cell_size,10*cell_size,feild_size_x,feild_size_y)
    map_bill=Rect(14*cell_size,14*cell_size,feild_size_x,feild_size_y) 
    back=Rect(14*cell_size,18*cell_size,feild_size_x,feild_size_y)
    menu_image=pygame.image.load('./resources/images/menu.png')
    play_image=pygame.image.load('./resources/images/play.png')
    play_image_pressed=pygame.image.load('./resources/images/play_pressed.png')
    choose_the_map_image=pygame.image.load('./resources/images/choose_the_map.png')
    choose_the_map_image_pressed=pygame.image.load('./resources/images/choose_the_map_pressed.png')
    quit_image=pygame.image.load('./resources/images/quit.png')
    quit_image_pressed=pygame.image.load('./resources/images/quit_pressed.png')
    map1_image=pygame.image.load('./resources/images/map_1.png')
    map1_image_pressed=pygame.image.load('./resources/images/map_1_pressed.png')
    map2_image=pygame.image.load('./resources/images/map_2.png')
    map2_image_pressed=pygame.image.load('./resources/images/map_2_pressed.png')
    map_bill_image=pygame.image.load('./resources/images/map_bill_chiefer.png')
    map_bill_image_pressed=pygame.image.load('./resources/images/map_bill_chiefer_pressed.png')
    back_image=pygame.image.load('./resources/images/back.png')
    back_image_pressed=pygame.image.load('./resources/images/back_pressed.png')
    background=pygame.image.load('./resources/images/background_for_menu.png')
    draw_background(screen,background)
    map_general_file='./resources/maps/easy_map.txt'
    k=0
    image_play=play_image
    image_quit=quit_image
    image_choose=choose_the_map_image
    pygame.display.flip()
    image_map1=map1_image
    image_map2=map2_image
    image_back=back_image
    image_map_bill=map_bill_image
    
    while flag=='work':
        draw_background(screen,background)
        screen.blit(menu_image,(menu.x,menu.y))
        screen.blit(image_play,(play.x,play.y))
        screen.blit(image_choose,(choose_the_map.x,choose_the_map.y))
        screen.blit(image_quit,(quit.x,quit.y))
        pygame.display.flip()
     
     
        for event in pygame.event.get():
            if (event.type==QUIT) or (event.type==KEYDOWN and event.key==K_ESCAPE):
                sys.exit(0)
            if event.type==KEYDOWN: 
               if event.key==K_DOWN:
                   k+=1
               if event.key==K_UP:
                   k-=1
               if k%3==1:
                   image_play=play_image_pressed
                   image_choose=choose_the_map_image
                   image_quit=quit_image
                   if event.key==K_RETURN:
                       flag='stop_work'
               elif k%3==2:
                   image_play=play_image
                   image_choose=choose_the_map_image_pressed
                   image_quit=quit_image
                   if event.key==K_RETURN:
                       flagger='work'
                       l=0
                       while flagger=='work':
                           draw_background(screen,background)
                           screen.blit(menu_image,(menu.x,menu.y))
                           screen.blit(image_map1,(map1.x,map1.y))
                           screen.blit(image_map2,(map2.x,map2.y))
                           screen.blit(image_map_bill,(map_bill.x,map_bill.y))
                           screen.blit(image_back,(back.x,back.y))
                           pygame.display.flip()
                           for event in pygame.event.get():
                               if (event.type==QUIT) or (event.type==KEYDOWN and event.key==K_ESCAPE):
                                   sys.exit(0)
                               if event.type==KEYDOWN: 
                                   if event.key==K_DOWN:
                                       l+=1
                                   if event.key==K_UP:
                                       l-=1
                                   if l%4==1:
                                       image_map1=map1_image_pressed
                                       image_map2=map2_image
                                       image_back=back_image
                                       image_map_bill=map_bill_image
                                       if event.key==K_RETURN:
                                           map_general_file='./resources/maps/easy_map.txt'                                     
                                           flagger='stop_work'
                                           flag='stop_work'
                                   if l%4==2:                                                            
                                       image_map1=map1_image                                             
                                       image_map2=map2_image_pressed
                                       image_back=back_image
                                       image_map_bill=map_bill_image
                                       if event.key==K_RETURN:
                                           map_general_file='./resources/maps/hard_map.txt'
                                           flagger='stop_work'
                                           flag='stop_work'
                                   if l%4==3:                                                            
                                       image_map1=map1_image                                             
                                       image_map2=map2_image
                                       image_back=back_image
                                       image_map_bill=map_bill_image_pressed
                                       if event.key==K_RETURN:
                                           map_general_file='./resources/maps/map_bill_chiefer.txt'
                                           flagger='stop_work'
                                           flag='stop_work'
                                   if l%4==0:
                                       image_map1=map1_image
                                       image_map2=map2_image
                                       image_back=back_image_pressed
                                       image_map_bill=map_bill_image
                                       if event.key==K_RETURN:
                                           flagger='stop_work'        
                                             
               elif k%3==0:
                   image_play=play_image
                   image_choose=choose_the_map_image
                   image_quit=quit_image_pressed
                   if event.key==K_RETURN:
                       sys.exit(0)
    menu_sound.stop()
    return map_general_file
            
     


if __name__=='__main__':


    
    cell_size=50    
    feild_size_x=38
    feild_size_y=21
    init_window()
    clever_ghost=[]
    ghost=[]
    wall=[]
    boom_wall=[]
    food=[]
    pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
    pygame.init()
    sound=pygame.mixer.Sound('./resources/music/music.wav')
    bill_sound=pygame.mixer.Sound('./resources/music/music_bill.wav')
    menu_sound=pygame.mixer.Sound('./resources/music/music_menu.wav')
    map_general_file=menu()
    if map_general_file=='./resources/maps/map_bill_chiefer.txt':
        bill_sound.play(loops=100)
    else:
        sound.play(loops=100)
    loser=pygame.mixer.Sound('./resources/music/Loser.wav')
    win=pygame.mixer.Sound('./resources/music/win.wav')
    map=Map(feild_size_x,feild_size_y,map_general_file)
    
    packman_images={
                        'up': pygame.image.load('./resources/images/packman_up.png'),
                        'right': pygame.image.load('./resources/images/packman_right.png'),
                        'down': pygame.image.load('./resources/images/packman_down.png'),
                        'left': pygame.image.load('./resources/images/packman_left.png') 
                   }
    
    ghost_1_images={
                        'up': pygame.image.load('./resources/images/ghost_1_up.png'),
                        'right': pygame.image.load('./resources/images/ghost_1_right_and_left.png'),
                        'down': pygame.image.load('./resources/images/ghost_1_down.png'),
                        'left': pygame.image.load('./resources/images/ghost_1_right_and_left.png') 
                   }
    
    ghost_2_images={
                        'up': pygame.image.load('./resources/images/ghost_2_up.png'),
                        'right': pygame.image.load('./resources/images/ghost_2_right_and_left.png'),
                        'down': pygame.image.load('./resources/images/ghost_2_down.png'),
                        'left': pygame.image.load('./resources/images/ghost_2_right_and_left.png') 
                   }
    
    ghost_saw_packman_images={
                        'stop':pygame.image.load('./resources/images/ghost_saw_packman_right.png'),
                        'up': pygame.image.load('./resources/images/ghost_saw_packman_up.png'),
                        'right': pygame.image.load('./resources/images/ghost_saw_packman_right.png'),
                        'down': pygame.image.load('./resources/images/ghost_saw_packman_down.png'),
                        'left': pygame.image.load('./resources/images/ghost_saw_packman_left.png') 
                   }
                  
                  
    for y in range(feild_size_y):
        for x in range(feild_size_x):
            if map.get(x,y)=='C':
                clever_ghost.append(CleverGhost(x,y,random.choice([ghost_1_images,ghost_2_images]),ghost_saw_packman_images,feild_size_x,feild_size_y,cell_size))
            if map.get(x,y)=='G':
                ghost.append(Ghost(x,y,random.choice([ghost_1_images,ghost_2_images]),feild_size_x,feild_size_y,cell_size))
            if map.get(x,y)=='P':
                packman=Packman(x,y,packman_images,feild_size_x,feild_size_y,cell_size,)
            if map.get(x,y)=='F':
                food.append(Food(x,y,'./resources/images/food.png',feild_size_x,feild_size_y,cell_size))
            if map.get(x,y)=='W':
                wall.append(Wall(x,y,'./resources/images/wall_undestroy.png',feild_size_x,feild_size_y,cell_size))
            if map.get(x,y)=='B':
                boom_wall.append(Boom_Wall(x,y,'./resources/images/wall_destroy.png',feild_size_x,feild_size_y,cell_size))
            if map.get(x,y)=='U':
                boom_wall.append(Boom_Wall(x,y,'./resources/images/wall_undestroy.png',feild_size_x,feild_size_y,cell_size))
    
         
    
    background=pygame.image.load('./resources/images/background.png')
    screen=pygame.display.get_surface()
    k=len(food)
    while 1:
        sovp=False
        for i in range(len(ghost)):
            if (floor(packman.x)==floor(ghost[i].x) and floor(packman.y)==floor(ghost[i].y)) or k<=0:
                sovp=True
                break
        for i in range(len(clever_ghost)):
            if (floor(packman.x)==floor(clever_ghost[i].x) and floor(packman.y)==floor(clever_ghost[i].y)):
                sovp=True
                break
        if sovp:
            if k>0:
                CameOver_screen_rect=Rect(50,200,feild_size_x,feild_size_y)
                screen.blit(pygame.image.load('./resources/images/WASTED.png'),(CameOver_screen_rect.x,CameOver_screen_rect.y))  
                loser.play()        
            else:
                CameOver_screen_rect=Rect(0,0,feild_size_x,feild_size_y)
                screen.blit(pygame.image.load('./resources/images/WINNER.png'),(CameOver_screen_rect.x,CameOver_screen_rect.y))
                win.play()
            sound.stop()
            bill_sound.stop()
            pygame.display.flip()
            pygame.time.wait(4000)
            menu_sound.play(loops=1000)
            while 1:
                process_events(pygame.event.get())
                quit_1=Rect(14*cell_size,17*cell_size,feild_size_x,feild_size_y)
                screen.blit(pygame.image.load('./resources/images/quit?.png'),(quit_1.x,quit_1.y))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type==KEYDOWN:
                        if event.key==K_RETURN:
                            sys.exit(0)
        else:
            
                        
            for i in range(len(boom_wall)):
                if floor(packman.x)==floor(boom_wall[i].x) and floor(packman.y)==floor(boom_wall[i].y):
                    map.map[boom_wall[i].y][boom_wall[i].x]=' '
                    boom_wall[i].set_coord(-1,-1)
                    
            for i in range(len(food)):
                if floor(packman.x)==floor(food[i].x) and floor(packman.y)==floor(food[i].y):
                    food[i].set_coord(-1,-1)
                    k-=1
                    
            process_events(pygame.event.get())
            pygame.time.delay(100)
            packman.game_tick()
            for i in range(len(ghost)):
                ghost[i].game_tick()
            for i in range(len(clever_ghost)):
                clever_ghost[i].game_tick()
            for i in range(len(wall)):
                wall[i].game_tick()   
            for i in range(len(boom_wall)):
                boom_wall[i].game_tick()   
            for i in range(len(food)):
                food[i].game_tick()           
            draw_background(screen,background)
            for i in range(len(wall)):
                wall[i].draw(screen,wall[i].image)
            for i in range(len(boom_wall)):
                boom_wall[i].draw(screen,boom_wall[i].image)
            for i in range(len(food)):
                food[i].draw(screen,food[i].image)
            for i in range(len(ghost)):
                ghost[i].draw(screen,ghost[i].image_with_direction)
            for i in range(len(clever_ghost)):
                clever_ghost[i].draw(screen,clever_ghost[i].image_with_direction)
            packman.draw(screen,packman.image_with_direction)
            pygame.display.flip()

