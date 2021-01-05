ball = PVector(200, 250)
pipes = random(30, 470)
pipe_x1 = 1500
pipe_x2 = 1200
pipe_x3 = 900
pipe_x4 = 600
pipe_space1 = random(50, 325)
pipe_space2 = random(50, 325)
pipe_space3 = random(50, 325)
pipe_space4 = random(50, 325)
movement = False
points = 0


def pipe_setup(pipe_x, pipe_space):
    global pipe_x1
    global pipe_x2
    global pipe_x3
    global pipe_x4
    global pipe_space1
    global pipe_space2
    global pipe_space3
    global pipe_space4
    global movement
    global points
    
    # pipes
    fill(255, 131, 87)
    rect(pipe_x, 0, 75, height)
    fill(226, 91, 69)
    rect(pipe_x + 50, 0, 25, height)
    
    # pipe space
    fill(206, 241, 235)
    rect(pipe_x, pipe_space, 75, 125)
    
    # points
    if ball.x -18 <= pipe_x + 75/2 <= ball.x - 16: points += 1
    
    # collision
    if ((pipe_x - 15 <= 200 and pipe_x + 75 >= 200 and
        (ball.y - 15 <= pipe_space or ball.y + 15 >= pipe_space + 125)) or
        ball.y + 15 >= height):
            movement = False
            if keyPressed == True:
                if key == ' ':
                    pipe_x1 = 1500
                    pipe_x2 = 1200
                    pipe_x3 = 900
                    pipe_x4 = 600
                    ball.y = 250
                    movement = True
                    points = 0


def setup():
    size(1000, 500)
    
    
def draw():
    global ball
    global pipes
    global pipe_x1
    global pipe_x2
    global pipe_x3
    global pipe_x4
    global pipe_space1
    global pipe_space2
    global pipe_space3
    global pipe_space4
    global movement
    global points
    
    # background
    background(206, 241, 235)
    noStroke()
    
    fill(173, 201, 101)
    rect(0, 450, 1000, 50)
    
    if keyPressed == True:
            if key  == ' ':
                movement = True
    
    # pipes
    if pipe_x1 <= -200: pipe_x1 = 1000
    if pipe_x2 <= -200: pipe_x2 = 1000
    if pipe_x3 <= -200: pipe_x3 = 1000
    if pipe_x4 <= -200: pipe_x4 = 1000
    
    if pipe_x1 == 1000: pipe_space1 = random(50, 325)
    if pipe_x2 == 1000: pipe_space2 = random(50, 325)
    if pipe_x3 == 1000: pipe_space3 = random(50, 325)
    if pipe_x4 == 1000: pipe_space4 = random(50, 325)
                
    pipe_setup(pipe_x1, pipe_space1)
    pipe_setup(pipe_x2, pipe_space2)
    pipe_setup(pipe_x3, pipe_space3)
    pipe_setup(pipe_x4, pipe_space4)
    
    textSize(45)
    fill(255)
    textAlign(CENTER)
    text(str(points), 500, 100)
        
    # ball
    if movement == True:
        ball.y += 4
        pipe_x1 -= 2
        pipe_x2 -= 2
        pipe_x3 -= 2
        pipe_x4 -= 2
        if keyPressed == True:
            if key  == ' ':
                for x in range(3, 0, -1):
                    ball.y -= (x**2)/1.25
    else:
        textAlign(CENTER)
        text("PRESS SPACE TO START", 500, 250)

    fill(250, 210, 114)
    ellipse(ball.x, ball.y, 30, 30)
    fill(250, 193, 114)
    arc(ball.x, ball.y, 30, 30, -HALF_PI, HALF_PI)
    