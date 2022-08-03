report_x=0
report_y=0
report_f=""

def move():
    global report_x
    global report_y
    global report_f
    if report_f == "NORTH":
        report_y+=1
    elif report_f == "EAST":
        report_x+=1
    elif report_f == "SOUTH":
        report_y-=1
    elif report_f == "WEST":
        report_x-=1
    if report_x < 0 or report_y < 0 or report_x > 5 or report_y > 5:
        raise Exception('Your robot will Fall.')
        
def convert_facing_to_int(facing):
    if facing == "NORTH":
        return 0
    if facing == "EAST":
        return 90
    if facing == "SOUTH":
        return 180
    if facing == "WEST":
        return 270
        
def convert_int_to_facing(value):
    if value == 0:
        return "NORTH"
    if value == 90:
        return "EAST"
    if value == 180:
        return "SOUTH"
    if value == 270:
        return "WEST"
        
def left():
    global report_f
    report_f = convert_int_to_facing((convert_facing_to_int(report_f)-90)%360)

def right():
    global report_f
    report_f = convert_int_to_facing((convert_facing_to_int(report_f)+90)%360)
    
def report():
    global report_x
    global report_y
    global report_f
    print(str(report_x)+", "+str(report_y)+", "+str(report_f))

def compute(x):
    global report_x
    global report_y
    global report_f
    actions = x.split(" ")
    place = actions[0].split(",")
    del actions[0]

    report_x=int(place[0])
    report_y=int(place[1])
    report_f=place[2]

    for action in actions:
        if action=="MOVE":
            move()
        elif action=="LEFT":
            left()
        elif action=="RIGHT":
            right()
        elif action=="REPORT":
            report()

