import tkinter as tk
def menu():
        def game():
            mainn.destroy()
            import pygame,sys,random

            pygame.init()
            WIDTH=900
            HEIGHT=500
            black=(0,0,0)
            white=(255,255,255)
            screen = pygame.display.set_mode((WIDTH,HEIGHT))
            pygame.display.set_caption('Pong Game')

            #classes

            class Ball:
                def _init_(self,screen,color,posX,posY,radius):
                    self.screen=screen
                    self.color=color
                    self.posX=posX
                    self.posY=posY
                    self.radius=radius
                    self.dx=0
                    self.dy=0
                    self.show()

                def show(self):
                    pygame.draw.circle(self.screen,self.color,(self.posX,self.posY),self.radius)

                def start(self):
                    self.dx=15
                    self.dy=5

                def move_ball(self):
                    self.posX += self.dx
                    self.posY += self.dy

                def paddle_collision(self):
                    self.dx = -self.dx

                def wall_collision(self):
                    self.dy = -self.dy
            
                def restart_pos(self):
                    self.posX = WIDTH//2
                    self.posY = HEIGHT//2
                    self.dx = 0
                    self.dy = 0
                    self.show()

            class Paddle:
                def _init_(self,screen,color,posX,posY,width,height):
                    self.screen=screen
                    self.color=color
                    self.posX=posX
                    self.posY=posY
                    self.width=width
                    self.height=height
                    self.state='stopped'
                    self.show()

                def show(self):
                    pygame.draw.rect(self.screen,self.color,(self.posX,self.posY,self.width,self.height))

                def move_paddle(self):
                    if self.state == 'up':
                        self.posY-=10
                    elif self.state == 'down':
                        self.posY+=10

                def edge(self):
                    if self.posY<=0:
                        self.posY=10
                    if self.posY>=HEIGHT-self.height:
                        self.posY=HEIGHT-self.height-10

            class CollisionManager():
                def ball_and_paddle1(self,ball,paddle1):
                    if ball.posY + ball.radius > paddle1.posY and ball.posY - ball.radius < paddle1.posY + paddle1.height:
                        if ball.posX - ball.radius <= paddle1.posX + paddle1.width:
                            return True
                    return False

                def ball_and_paddle2(self,ball,paddle2):
                    if ball.posY + ball.radius > paddle2.posY and ball.posY - ball.radius < paddle2.posY + paddle2.height:
                        if ball.posX + ball.radius >= paddle2.posX:
                            return True
                    return False

                def ball_and_wall(self,ball):
                    #top
                    if ball.posY-ball.radius<=0:
                        return True
                    #bottom
                    if ball.posY+ball.radius>=HEIGHT:
                        return True

                    return False

                def between_ball_and_goal1(self, ball):
                    return ball.posX + ball.radius <= 0

                def between_ball_and_goal2(self, ball):
                    return ball.posX - ball.radius >= WIDTH

            class PlayerScore:
                def _init_(self, screen, points, posX, posY):
                    self.screen = screen
                    self.points = points
                    self.posX = posX
                    self.posY = posY
                    self.font = pygame.font.SysFont("monospace", 80, bold=True)
                    self.label = self.font.render(self.points, 0, white)
                    self.show()

                def show(self):
                    self.screen.blit(self.label, (self.posX - self.label.get_rect().width // 2, self.posY))

                def increase(self):
                    points = int(self.points) + 1
                    self.points = str(points)
                    self.label = self.font.render(self.points, 0, white)
                    
            #functions

            def paint_back():
                screen.fill(black)
                pygame.draw.line(screen,white,(WIDTH//2,0),(WIDTH//2,HEIGHT),6)

            paint_back()

            #objects
            ball=Ball(screen,white,WIDTH//2,HEIGHT//2,12)
            paddle1=Paddle(screen,white,15,HEIGHT//2-60,20,120)
            paddle2=Paddle(screen,white,WIDTH-20-15,HEIGHT//2-60,20,120)
            collision=CollisionManager()
            score1 = PlayerScore( screen, '0', WIDTH//4, 15 )
            score2 = PlayerScore( screen, '0', WIDTH - WIDTH//4, 15 )

            #varibles
            playing=False

            #main loop

            while True:
                pygame.time.delay(40)
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        sys.exit()
                    if event.type==pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            ball.start()
                            playing=True
                        if event.key == pygame.K_w:
                            paddle1.state = 'up'
                        if event.key == pygame.K_s:
                            paddle1.state = 'down'
                        if event.key == pygame.K_UP:
                            paddle2.state = 'up'
                        if event.key == pygame.K_DOWN:
                            paddle2.state = 'down'

                    if event.type==pygame.KEYUP:
                        paddle1.state='stopped'
                        paddle2.state='stopped'

                if playing:
                    paint_back()
                    # ball
                    ball.move_ball()
                    ball.show()
                    #paddle1
                    paddle1.move_paddle()
                    paddle1.edge()
                    paddle1.show()
                    #paddle2
                    paddle2.move_paddle()
                    paddle2.edge()
                    paddle2.show()
                    #collision
                    if collision.ball_and_paddle1(ball,paddle1):
                        ball.paddle_collision()
                    if collision.ball_and_paddle2(ball,paddle2):
                        ball.paddle_collision()
                    if collision.ball_and_wall(ball):
                        ball.wall_collision()
                    if collision.between_ball_and_goal2(ball):
                        score1.increase()
                        ball.restart_pos()
                    if collision.between_ball_and_goal1(ball):
                        score2.increase()
                        ball.restart_pos()

                score1.show()
                score2.show()

                pygame.display.update()        







        def help_button():
            mainn.destroy()
            hp=tk.Tk()
            hp.title('HELP')
            hp.geometry('800x600')
            hp.resizable(False,False)

            imag=tk.PhotoImage(file='C:\\Users\\MENNA\\Downloads\\fade.png')
            label1=tk.Label(hp,image=imag)
            label1.place(x=0,y=0)

            lb1=tk.Label(hp, text="1. To start playing press       key. ",font=('Bernard MT Condensed',21),fg='#082448')
            lb1.place(x=30,y=100)
            lb2=tk.Label(hp, text="2. Player 1 with left paddle can move using      and      keys. ",font=('Bernard MT Condensed',21),fg='#082448')
            lb2.place(x=30,y=150)
            lb3=tk.Label(hp, text="-       key for moving up ",font=('Bernard MT Condensed',21),fg='#082448')
            lb3.place(x=100,y=190)
            lb4=tk.Label(hp, text="-       key for moving down ",font=('Bernard MT Condensed',21),fg='#082448')
            lb4.place(x=100,y=230)
            lb5=tk.Label(hp, text="3. Player 2 with right paddle can move using      and      keys. ",font=('Bernard MT Condensed',21),fg='#082448')
            lb5.place(x=30,y=280)
            lb6=tk.Label(hp, text="-       key for moving up ",font=('Bernard MT Condensed',21),fg='#082448')
            lb6.place(x=100,y=320)
            lb7=tk.Label(hp, text="-       key for moving down ",font=('Bernard MT Condensed',21),fg='#082448')
            lb7.place(x=100,y=360)

            i1=tk.PhotoImage(file='C:\\Users\\MENNA\\Downloads\\wkey1.png')
            label2=tk.Label(hp,image=i1)
            label2.place(x=510,y=150)
            i2=tk.PhotoImage(file='C:\\Users\\MENNA\\Downloads\\skey1.png')
            label3=tk.Label(hp,image=i2)
            label3.place(x=595,y=150)
            i3=tk.PhotoImage(file='C:\\Users\\MENNA\\Downloads\\wkey1.png')
            label4=tk.Label(hp,image=i3)
            label4.place(x=118,y=190)
            i4=tk.PhotoImage(file='C:\\Users\\MENNA\\Downloads\\skey1.png')
            label5=tk.Label(hp,image=i4)
            label5.place(x=118,y=230)
            i5=tk.PhotoImage(file='C:\\Users\\MENNA\\Downloads\\upkey1.png')
            label6=tk.Label(hp,image=i5)
            label6.place(x=530,y=280)
            i6=tk.PhotoImage(file='C:\\Users\\MENNA\\Downloads\\downkey1.png')
            label7=tk.Label(hp,image=i6)
            label7.place(x=615,y=280)
            i7=tk.PhotoImage(file='C:\\Users\\MENNA\\Downloads\\upkey1.png')
            label8=tk.Label(hp,image=i7)
            label8.place(x=118,y=320)
            i8=tk.PhotoImage(file='C:\\Users\\MENNA\\Downloads\\downkey1.png')
            label9=tk.Label(hp,image=i8)
            label9.place(x=118,y=360)
            i9=tk.PhotoImage(file='C:\\Users\\MENNA\\Downloads\\pkey1.png')
            label10=tk.Label(hp,image=i9)
            label10.place(x=295,y=100)
            
            def back():
                hp.destroy()
                menu()
            button_back=tk.Button(hp,text="Back to menu",font=('Bernard MT Condensed',20),fg='#17202A',bg='#F7E2C5',activebackground='#A39076',command=back,width='14',height='1',cursor="dot")
            button_back.place(x=300, y=450)
                
            hp.mainloop() 

        mainn=tk.Tk()
        mainn.title('PONG GAME')
        mainn.geometry('800x600')
        mainn.resizable(False,False)

        img=tk.PhotoImage(file='C:\\Users\\MENNA\\Downloads\\pingpo.png')
        label=tk.Label(mainn,image=img)
        label.place(x=0,y=0)

        button_play=tk.Button(mainn,text="Play",font=('Bernard MT Condensed',20),fg='#17202A',bg='#F7E2C5',activebackground='#A39076',command=game,width='14',height='1',cursor="dot")
        button_help=tk.Button(mainn,text="Help",font=('Bernard MT Condensed',20),fg='#17202A',bg='#F7E2C5',activebackground='#A39076',command=help_button,width='14',height='1',cursor="dot")
        button_quit=tk.Button(mainn,text="quit",font=('Bernard MT Condensed',20),fg='#17202A',bg='#F7E2C5',activebackground='#A39076',command=quit,width='14',height='1',cursor="dot")

        button_play.place(x=80, y=350)
        button_help.place(x=80, y=420)
        button_quit.place(x=80, y=490)
        
        mainn.mainloop()


menu()
