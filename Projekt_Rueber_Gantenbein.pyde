#Listen definieren
listeX = [] 
listeY = [] 
listeZ = [] 
listeP1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] 
listeP2 = ["A'","B'","C'", "D'", "E'", "F'","G'","H'", "I'", "J'", "K'","L'", "M'", "N'", "O'", "P'", "Q'", "R'","S'","T'", "U'", "V'", "W'","X'", "Y'", "Z'"] 
counter = []

#Platzierung Button
x = 1350
y = 880

#Arbeitsfläche definieren
def setup():
    size(1800, 1000) 
    background(202, 225, 255) 
    fill(16,78,139)
    textSize(50) 
    text("Achsenspiegelung",30,50)
    strokeWeight(6) 
    stroke(0, 0, 0) 
    line(900,0,900,1800) 
    gitternetz()

#Gitternetz definieren    
def gitternetz():
    strokeWeight(1)
    stroke(0, 0, 0) 
    for x in range (1,30): 
        line(x*60, 1000, x*60, 0) 
    for y in range (1, 20): 
        line(0,y*60, 1800, y*60) 
            

def draw():           
#Button (Quelle: Hefti und Schlegel)       
        if mousePressed == True and mouseX >= x and mouseX <= x + 400 and mouseY >= y and mouseY <= y + 100:
            clearScreen() #Bein Anklicken des Buttons wird clearscreen aufgerufen, somit wird das gezeichnete überschrieben
           
        else:
            textSize(50)#Textgrösse
            fill (255,255,255) #Grundfarbe Schrift
            text("Reset", x + 130, y + 70)
        
        fill(0,0,0,51) #Grundfarbe Button, 51 = durchschimmern
        rect(x, y, 400, 100)
            
def clearScreen(): 
    background(202, 225, 255) 
    fill(16,78,139) 
    textSize(50) 
    text("Achsenspiegelung",30,50)
    strokeWeight(6) 
    stroke(0, 0, 0) 
    line(900,0,900,1800) 
    gitternetz() 
    
    for i in range(len(listeX)): 
        listeX.pop(-1) 
        listeY.pop(-1)
        listeZ.pop(-1) 
    for i in range(len(counter)):
        counter.pop(-1)
        
#Punkte
def mousePressed():
    if len(listeX) > 1 and abs(listeX[0]-mouseX) < 30 and abs(listeY[0]-mouseY) < 30:
        circle(listeX[0],listeY[0], 20)
        circle(1800-listeX[0],listeY[0], 20)
        line(listeX[-1], listeY[-1], listeX[0], listeY[0])
        line(listeZ[-1], listeY[-1], 1800-listeX[0], listeY[0])
        counter.append(1)
    
    elif mouseX <= 900 and mouseY <= 1000 and len(counter) == 0:
        fill(139, 35, 35) 
        #Linke Punkte
        circle(mouseX, mouseY, 20) 
        textSize(30)
        a = len(listeX) 
        text(listeP1[a], mouseX, mouseY - 15) 
        #Rechte Punkte (Spiegelung)
        circle(1800 - mouseX, mouseY, 20) 
        textSize(30)
        text(listeP2[a], 1800 - mouseX, mouseY - 15)
        
#Koordinaten den jeweiligen Listen hinzufügen
        listeX.append(mouseX) 
        listeY.append(mouseY)
        listeZ.append(1800 - mouseX)
        
#Verbindung der Punkte mit einer Linie
    if len(listeX) > 1: 
        stroke (0,0,0) 
        line(listeX[-2], listeY[-2], listeX[-1], listeY[-1])
        line(listeZ[-2], listeY[-2], listeZ[-1], listeY[-1])
