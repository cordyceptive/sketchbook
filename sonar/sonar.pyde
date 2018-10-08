# import contact: click on chart to draw a contact that gets pinged by sonar

colors = {'GRN':color(51, 255, 0), 'RED':color(193, 49, 36), 'BLK':color(10)}

def setup():
    size(480, 480)
    background(colors['BLK'])
    fill(colors['RED'])
    ellipse(240, 240, 430, 430)
    fill(10)
    ellipse(240, 240, 420, 420)

def draw():
    stroke(colors['GRN'])
    
    if mousePressed:
        fill(colors['GRN'])
        ellipse(mouseX, mouseY, 10, 10)
