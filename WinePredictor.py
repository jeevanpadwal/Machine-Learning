
from sys import *
import os
import smtplib
import pandas as pd
import matplotlib.pyplot as plt
from email.mime.multipart import *
from email.mime.text import *
from email.mime.base import *
from email import encoders   

def GraphFig(Graph_name):
    excel_file = 'WinePredictor.xlsx'

    data = pd.read_excel(excel_file)

    x = list(data['Alcohol'])

    y = list(data['Ash'])

    plt.figure(figsize=(10,10))
    plt.style.use('seaborn')
    plt.scatter(x,y)
    plt.title("Alcohol Vs Ash")
    plt.savefig(Graph_name)
    plt.show()

    return Graph_name

def Mail_Send(Sender_Mail,Dir_Name):
   
    
    fromaddr = "supercoin2002@gmail.com"
    toaddr = Sender_Mail
    
    msg = MIMEMultipart()
    
    msg['From'] = fromaddr
    
    msg['To'] = toaddr
    msg['Subject'] = "mail cheak"
    
    body = "Graph Of Wine Predictor"
    
    msg.attach(MIMEText(body, 'plain'))

    file_path = os.path.join(Dir_Name)
        
    attachment = open(file_path, "rb")
          
    p = MIMEBase('application', 'octet-stream')
            
    p.set_payload((attachment).read())
                
    encoders.encode_base64(p)
                
    p.add_header('Content-Disposition', "attachment; filename= %s"%Dir_Name)
                
    msg.attach(p)
  
    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()
                
    s.login(fromaddr, "qvbitgkjtejhifdt")
                
    text = msg.as_string()

    s.sendmail(fromaddr, toaddr, text)

    s.quit()
    print("Mail send")

def main():
    print("This script use for ploting graph of wine predictor")

    if(len(argv) != 3):
        print("Error :Invalid number of arguments")
        print("Enter -H : For the help")
        print("Enter -U: For the Usage of the program")
        exit()

    if((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage : This script use to send mail of grapthical reprasantion of wine predictor")
        exit()

    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("Application_Name Grapth_name Sender_Mail")
        exit()
    else:

        Graph_name = GraphFig(argv[1])

        Mail_Send(argv[2],Graph_name)

    


if __name__ =="__main__":
    main()