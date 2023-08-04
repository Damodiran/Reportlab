from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def margin(obj):
    obj.line(30,30,580,30)#top
    obj.line(30,30,30,758)#left
    obj.line(30,758,580,758)#bottom
    obj.line(580,758,580,30)#right
    
    
def para_1(obj,img,fonts):
    obj.setFont("Courier-Bold",20)
    obj.drawString(230,720,"Story Time")
    obj.drawString(150,690,"(Turtle and Rabbit Story)")
    obj.rect(60, 550, 100, 100, stroke=1, fill=0)
    obj.drawImage(img, 65, 555, width=90, height=90)
    obj.setFont("Times-Roman",20)
    obj.drawString(170,630,"Once upon a time there was a Rabbit and Turtle" )
    obj.drawString(170,590,"Then they planned to go for a race , so they ")
    obj.drawString(172,550,"organized race.")

def para_2(obj,img_2,fonts):
    obj.rect(435, 425, 100, 100, stroke=1, fill=0)
    obj.drawImage(img_2, 440, 430, width=90, height=90)
    obj.setFont("Times-Roman",20)
    obj.drawString(65,510,"Both of them started the race from starting")
    obj.drawString(65,472,"point , The rabbit ran faster than turtle in ")
    obj.drawString(65,437,"race and the turtle puts full efforts in race. ")

def para_3(obj,img_3,fonts):
    obj.rect(65,295 , 100, 100, stroke=1, fill=0)
    obj.drawImage(img_3, 70, 300, width=90, height=90)
    obj.setFont("Times-Roman",20)
    obj.drawString(176,380,"After a while in a race the rabbit thinks in a way ")
    obj.drawString(176,343,"that turtle is not a competitor to rabbit and takes ")
    obj.drawString(176,308,"rest under the tree , on that time turtle crossed.")

def para_4(obj,img_3,fonts):
    obj.rect(435, 150, 100, 100, stroke=1, fill=0)
    obj.drawImage(img_4, 440, 155, width=90, height=90)
    obj.setFont("Times-Roman",20)
    obj.drawString(65,230,"The turtle puts consistent efforts in a race")
    obj.drawString(65,195,"and at the same time the rabbit comes to  ")
    obj.drawString(65,158,"know that turtle in end line and turtle wins. ")

def moral(obj,img_climax,fonts):
    obj.setFont("Times-Roman-Bold",30)
    obj.rect(236, 620, 124, 124, stroke=1, fill=0)
    obj.drawImage(img_climax, 243, 627, width=110, height=110)
    obj.drawString(50,580,"The moral of the story is that the rabbit")
    obj.drawString(50,530,"thinks in a way like the turtle is not faster")
    obj.drawString(50,480,"than rabbit and it felt lethargic because of") 
    obj.drawString(48,430,"that it takes rest in between the race , so that")
    obj.drawString(50,380,"the rabbit loss a race but due to the ")
    obj.drawString(50,330,"consistent effort of turtleit pays for it and")
    obj.drawString(50,280,"the rabbit had learned his lesson...!!")
    obj.setFont("Helvetica-Bold",30)
    obj.drawString(90,210,"'''Slow Steady Wins The Race'''")
if __name__ == "__main__":
    obj = canvas.Canvas("exp_pdf.pdf",pagesize=letter)
    fonts = obj.getAvailableFonts()
    img = "start.jfif"
    img_2 = "started.jfif"
    img_3 = "turtle_crosses_rabbit.jfif"
    img_4 = "turtle_win.jfif"
    img_climax = "Quote.jfif"
    print("PDF Created")
    margin(obj)
    para_1(obj,img,fonts)
    para_2(obj,img_2,fonts)
    para_3(obj,img_3,fonts)
    para_4(obj,img_4,fonts)
    obj.showPage()
    margin(obj)
    moral(obj,img_climax,fonts)
    obj.save()
