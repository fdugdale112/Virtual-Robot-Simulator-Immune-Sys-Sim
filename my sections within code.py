'''
immune system simulator
creation of border guide 
created with Tkinter
author: William Escobar Parra
'''




    #drawing border, preventing turtle from losing itself
    borderGuide=turtle.Turtle()
    borderGuide.color('white')
    borderGuide.penup()
    borderGuide.setpos(-350,-350)
    borderGuide.pendown()
    borderGuide.pensize(4)

    for x in range (4):
        borderGuide.forward(700)
        borderGuide.left(90)

    borderGuide.hideturtle()





############################################################

     def collisionCheck(tur1,tur2):
        
        x= math.sqrt(math.pow(tur1.xcor()-tur2.xcor(),2))
        y= math.pow(tur1.ycor()-tur2.ycor(),2)
        #pythagoras theorem,change in x coordinate squared
        #plus the change in y squared
        d=x+y
        if d<19:
            return True
        else:
            return False

           
    while userScore < 5:
        user.forward(turtleSpeed)
        

        #setting up x,y coordinates for boundary checking
        if user.xcor()>350 or user.xcor()<-350:
            user.right(180)
            
        if user.ycor()>350 or user.ycor()<-350:
            user.right(180)


###########################################################

        for count in range (maxPathogens):
            turtles[count].forward(2)
                
            #setting up x,y coordinates for boundary checking
            if turtles[count].xcor()>350 or turtles[count].xcor()<-350:
                turtles[count].right(180)
                    
            #boundary checking the y coordinates
            if turtles[count].ycor()>350 or turtles[count].ycor()<-350:
                turtles[count].right(180)


        #if collision occurs, this will take turtle to a random spot
            if collisionCheck(user,turtles[count]):
                if (user.shape() == turtles[count].shape())==True:
                    
                    turtles[count].setposition(random.randint(-350,350),random.randint(-350,350))
                    turtles[count].right(random.randint(0,360))
                    if turtles[count].shape()=="circle":
                        turtles[count].shape("square")
                        turtles[count].color("blue")
                        userScore = userScore + 2
                    elif turtles[count].shape()=="triangle":
                        turtles[count].shape("circle")
                        turtles[count].color("yellow")
                        userScore = userScore + 1
                    elif turtles[count].shape()=="square":
                        turtles[count].shape("triangle")
                        turtles[count].color("purple")
                        userScore = userScore + 3

                    else:
                        userScore= userScore-2


            
