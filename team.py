import pyttsx3
import subprocess as sp
import os 
import webbrowser as wb
from os import system, name 
from colorama import init
init()

from colorama import Fore, Back, Style

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

pyttsx3.speak("Hello guys...hope you are well ...and doing great..")
pyttsx3.speak("Today...I am going to perform... our first task ")
pyttsx3.speak("Welcome to my ...menu driven program")


while(True):
    clear()
    print( "\n\n\n\t\t\t\t\t\t\t\t\tWelcome\n\t\t\t__________________________________________________________________________________________________")
    print(Fore.YELLOW+"\n\n\n\t\t\t\t\t\t\t\t\tMenu\n\t\t\t\t\t\t\t-------------------------------------")
    print("\n\t\t\t\t\t\t\t\t1: Simple commands")    
    print("\n\t\t\t\t\t\t\t\t2: Docker ") 
    print("\n\t\t\t\t\t\t\t\t3: Amazon Web Services (AWS)") 
    print("\n\t\t\t\t\t\t\t\t4: Hadoop")
    print("\n\t\t\t\t\t\t\t\t5: Increase/Decrease the size of HD using LVM")
    print("\n\t\t\t\t\t\t\t\t6: Shut down/Restart") 
    print("\n\t\t\t\t\t\t\t\t7: Exit")
    pyttsx3.speak("Please...Enter your..choice")
    ch=int(input("\n\n\t\t\t\t\t\t\t\tEnter your choice:"))
    
    if(ch==4):
        while(True):
            clear()
            print(Fore.WHITE, "\n\n\n\t\t\t\t\t\t\t\t\tHADOOP\n\t\t\t__________________________________________________________________________________________________")
            print(Fore.GREEN,"\n\t\t\t\t\t\t\t1:Configure  Master node / Namenode ")
            print(Fore.GREEN,"\n\t\t\t\t\t\t\t2:Configure Slave node / Datanode ")
            print(Fore.GREEN,"\n\t\t\t\t\t\t\t3:Check the status of Master or Slave ")
            print("\n\t\t\t\t\t\t\t4:Show dfsAdmin Report")
            print("\n\t\t\t\t\t\t\t5:Show WEB-UI")
            pyttsx3.speak("Please..Enter your..choice")
            ch=int(input("\n\n\t\t\t\t\t\t\t\tEnter your choice:"))
            
            if(ch==1):
                print("\n\t\t\t\t\t\tEnter the ip ",end= ' ')
                ipp=input()
                cmd=r" ssh -l root {} sudo hadoop-daemon.sh start namenode".format(ipp)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Starting the Namenode's Service ")
                    print(Fore.YELLOW,"\n\t\t\t\t\t\t\t\tStarting the Namenode's Service")
                else:
                    pyttsx3.speak("An error occured.........please check")
                    print("\n\t\t\t\t\t\t\t\tAn error occured.........please check")
                out=output[1]
                print("\n\t\t\t\t\t\t\t\t",out)
                print(Fore.RED,"\n\t\t\t\t\t\t\tDo tou want to continue? (y/n): ",end=' ')
                inp=input()
            elif(ch==2):
                print("\n\t\t\t\t\t\tEnter the ip ",end= ' ')
                ipp=input()
                cmd=r" ssh -l root {} sudo hadoop-daemon.sh start datanode".format(ipp)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Starting the Datanode's Service ")
                    print(Fore.YELLOW,"\n\t\t\t\t\t\t\t\tStarting the Datanode's Service")
                else:
                    pyttsx3.speak("An error occured.........please check")
                    print("\n\t\t\t\t\t\t\t\tAn error occured.........please check")
                out=output[1]
                print("\n\t\t\t\t\t\t\t\t",out)
                print(Fore.RED,"\n\t\t\t\t\t\t\tDo tou want to continue? (y/n): ",end=' ')
                inp=input()
            elif(ch==3):
                print("\n\t\t\t\t\t\tEnter the ip ",end= ' ')
                ipp=input()
                cmd=r" ssh -l root {} sudo jps".format(ipp)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Check the service ")
                    print(Fore.YELLOW,"\n\t\t\t\t\t\t\t\tCheck the service")
                else:
                    pyttsx3.speak("An error occured.........please check")
                    print("\n\t\t\t\t\t\t\t\tAn error occured.........please check")
                out=output[1]
                print("\n\t\t\t\t\t\t\t\t",out)
                print(Fore.RED,"\n\t\t\t\t\t\t\tDo tou want to continue? (y/n): ",end=' ')
                inp=input()
            elif(ch==4):
                print("\n\t\t\t\t\t\tEnter the ip ",end= ' ')
                ipp=input()
                cmd=r" ssh -l root {} sudo hadoop dfsadmin -report".format(ipp)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Check the service ")
                    print(Fore.YELLOW,"\n\t\t\t\t\t\t\t\tCheck the service")
                else:
                    pyttsx3.speak("An error occured.........please check")
                    print("\n\t\t\t\t\t\t\t\tAn error occured.........please check")
                out=output[1]
                print("\n\t\t\t\t\t\t\t\t",out)
                print(Fore.RED,"\n\t\t\t\t\t\t\tDo tou want to continue? (y/n): ",end=' ')
                inp=input()
            elif(ch==5):
                wb.open("http://15.206.203.192:50070")
            
            
    if(ch==1):
        while(True):
            clear()
            print(Fore.WHITE, "\n\n\n\t\t\t\t\t\t\t\t\tAWS\n\t\t\t__________________________________________________________________________________________________")
            print(Fore.GREEN,"\n\n\n\n\t\t\t\t\t\t\t1: Date ") 
            print("\n\t\t\t\t\t\t\t2: Calendar ")
            print("\n\t\t\t\t\t\t\t3: ifconfig ")
            print("\n\t\t\t\t\t\t\t4: Available RAM ")
            print("\n\t\t\t\t\t\t\t5: Check software installed or not ")
            print("\n\t\t\t\t\t\t\t6: Install software ")
            print("\n\t\t\t\t\t\t\t7: Return ")
            pyttsx3.speak("\n\n\n\n\t\t\t\t\t\t\tPlease..Enter your..choice")
            ch=int(input("\n\n\t\t\t\t\t\t\t\tEnter your choice:"))
            if(ch==1):
                print("\n\n\n\n\t\t\t\t\t\t\tEnter the ip",end=' ')
                ip=input()
                cmd='ssh -l root {}	sudo date'.format(ip)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Showing todays date")
                    print("\n\t\t\t\t\t\t Showing today's date")
                else:
                    pyttsx3.speak("Someting is wrong....Try again")
                    print("\n\t\t\t\t\t\t Someting is wrong....Try again")
                out=output[1]
                print(out)
                print("\n\t\t\t\t\t\tDo you want to continue?(y/N)",end=' ')
                i=input()
                
            if(ch==2):
                
                cmd='ssh -l root {}	sudo cal'.format(ip)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Showing calendar")
                    print("\n\t\t\t\t\t\t Showing calendar")
                else:
                    pyttsx3.speak("Someting is wrong....Try again")
                    print("\n\t\t\t\t\t\t Someting is wrong....Try again")
                out=output[1]
                print(out)
                print("\n\t\t\t\t\t\tDo you want to continue?(y/N)",end=' ')
                i=input()
                
            if(ch==3):
                
                cmd='ssh -l root {}	sudo ifconfig'.format(ip)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Showing IP")
                    print("\n\t\t\t\t\t\t Showing IPs")
                else:
                    pyttsx3.speak("Someting is wrong....Try again")
                    print("\n\t\t\t\t\t\t Someting is wrong....Try again")
                out=output[1]
                print(out)
                print("\n\t\t\t\t\t\tDo you want to continue?(y/N)",end=' ')
                i=input()
                
            if(ch==4):
                
                cmd='ssh -l root {}	sudo free -m'.format(ip)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Showing available and used RAM")
                    print("\n\t\t\t\t\t\t Showing available and used RAM")
                else:
                    pyttsx3.speak("Someting is wrong....Try again")
                    print("\n\t\t\t\t\t\t Someting is wrong....Try again")
                out=output[1]
                print(out)
                print("\n\t\t\t\t\t\tDo you want to continue?(y/N)",end=' ')
                i=input()
            
            if(ch==5):
                print("\n\n\n\n\t\t\t\t\t\t\tEnter the software name which you are looking for :",end=' ')
                sof=input()
                cmd='ssh -l root {}	sudo rpm -q {}'.format(ip,sof)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Check whether it is installed or not")
                    #print("\n\t\t\t\t\t\t Showing available and used RAM")
                #else:
                    #pyttsx3.speak("Someting is wrong....Try again")
                    #print("\n\t\t\t\t\t\t Someting is wrong....Try again")
                out=output[1]
                print(out)
                print("\n\t\t\t\t\t\tDo you want to continue?(y/N)",end=' ')
                i=input()
                
            if(ch==6):
                print("\n\n\n\n\t\t\t\t\t\t\tEnter the software name which is to be installed :")
                sof=input()
                cmd='ssh -l root {}	sudo yum install {}'.format(ip,sof)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Installing")
                    print("\n\t\t\t\t\t\t Installing....")
                else:
                    pyttsx3.speak("Someting is wrong....Try again")
                    print("\n\t\t\t\t\t\t Someting is wrong....Try again")
                out=output[1]
                print(out)
                print("\n\t\t\t\t\t\tDo you want to continue?(y/N)",end=' ')
                i=input()
                
            
            
            
    if(ch==2):
        while True:
            os.system("cls")
            print("\t\t\tDocker")
            print("---------------------------------------------------")
            print("press 1 : To see status of  docker");
            print("press 2 : To start docker");
            print("press 3 : To launch an OS on docker");
            print("press 4 : To stop an OS ");
            print("press 5 : To see all running OS on docker");
            print("press 6 : To see all running and stopped OS on docker");
            print("press 7 : To run linux commands on docker container");
            print("press 8 : To delete an OS");
            print("press 9 : To delete all OS")
            print("press 10: To Return back")
            ch=int(input("Enter your choice : "))
            if ch==1:
                wb.open("http://192.168.43.237/cgi-bin/dockerstatus.py")
            elif ch==2:
                wb.open("http://192.168.43.237/cgi-bin/dockerrun.py")	
            elif ch==3:
                wb.open("http://192.168.43.237/osrun.html")	
            elif ch==4:
                wb.open("http://192.168.43.237/osstop.html")	
            elif ch==5:
                wb.open("http://192.168.43.237/cgi-bin/running_os.py")	 
            elif ch==6:
                wb.open("http://192.168.43.237/cgi-bin/all_os.py")	 
            elif ch==7:
                wb.open("http://192.168.43.237/command.html")	 
            elif ch==8:
                wb.open("http://192.168.43.237/delete_os.html")	 
            elif ch==9:
                wb.open("http://192.168.43.237/cgi-bin/del_all_os.py")	 
            elif ch==10:
                break
            else:
                print("Wrong choice! please enter the choice again")
            input("Please enter to continue.....")
            
    if(ch==3):
        
        while(True):
            clear()
            print(Fore.WHITE, "\n\n\n\t\t\t\t\t\t\t\t\tAWS\n\t\t\t__________________________________________________________________________________________________")
            print(Fore.GREEN,"\n\n\n\n\t\t\t\t\t\t\t1: Create a key ") 
            print("\n\t\t\t\t\t\t\t2: Create a security group")
            print("\n\t\t\t\t\t\t\t3: Add inbound rules")
            print("\n\t\t\t\t\t\t\t4: Launch instance")
            print("\n\t\t\t\t\t\t\t5: Create a EBS volume")
            print("\n\t\t\t\t\t\t\t6: Attach previously created EBS volume to the running instance")
            print("\n\t\t\t\t\t\t\t7: Create a S3 bucket")
            print("\n\t\t\t\t\t\t\t8: Upload the images in S3")
            print("\n\t\t\t\t\t\t\t9: Create a CloudFront Distribution")
            print("\n\t\t\t\t\t\t\t10: Create a html page of high availability architecture ")
            print("\n\t\t\t\t\t\t\t11: Exit")
            pyttsx3.speak("Please..Enter your..choice")
            ch=int(input("\n\n\t\t\t\t\t\t\t\tEnter your choice:"))
        
            if(ch==1):
                
                print("\n\t\t\t\t\t\tEnter the key name",end= ' ')
                key=input()
                #cmd="aws ec2 create-key-pair  --key-name keytask"
                cmd="aws ec2 create-key-pair  --key-name {}".format(key)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Creating the new key ")
                    print("\n\t\t\t\t\t\tCreating the new key")
                else:
                    pyttsx3.speak("An error occured.........please check")
                    print("\n\t\t\t\t\t\tAn error occured.........please check")
                out=output[1]
                print(out)
                print("\n\t\t\t\t\t\tDo you want to continue?(y/N)",end=' ')
                i=input()
            if(ch==2):
                print("\n\t\t\t\t\t\tEnter the security name",end= ' ')
                sec=input()
                cmd='aws ec2 create-security-group  --description "Task 3 Security Group"     --group-name {}_sg'.format(sec)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Creating the new security group ")
                    print("\n\t\t\t\t\t\tCreating the new security group ")
                else:
                    pyttsx3.speak("An error occured.........please check")
                    print("\n\t\t\t\t\t\t An error occured.........please check")
                out=output[1]
                print(out)
                print("\n\t\t\t\t\t\tDo you want to continue?(y/N)",end=' ')
                i=input()
            if(ch==3):
                print("\n\t\t\t\t\t\tEnter the security name",end= ' ')
                se=input()
                print("\n\t\t\t\t\t\tEnter the ip that you want to add",end= ' ')
                ip=input()
                cmd='aws ec2 authorize-security-group-ingress  --group-name {}_sg   --protocol tcp   --port 22    --cidr {}/32'.format(se,ip)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Sucessfully created ...,new inbound rules")
                    print("\n\t\t\t\t\t\t Sucessfully created new inbound rules")
                else:
                    pyttsx3.speak("An error occured.........please check")
                    print("\n\t\t\t\t\t\t An error occured.........please check")
                out=output[1]
                print(out)
                print("\n\t\t\t\t\t\tDo you want to continue?(y/N)",end=' ')
                i=input()
            if(ch==4):
                print("\n\t\t\t\t\t\tEnter the security group id sg-",end= ' ')
                sg=input()
                print("\n\t\t\t\t\t\tEnter the key name",end= ' ')
                kn=input()
                cmd='aws ec2 run-instances  --image-id ami-0e306788ff2473ccb    --instance-type t2.micro    --count 1   --subnet-id subnet-bfb2b8d7    --security-group-ids sg-08f53c3f9248e7702  --key-name terminal --tag-specifications ResourceType=instance,Tags=[{Key=Name,Value=Task_3_Instance}]'
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("launching an instance ")
                    print("\n\t\t\t\t\t\tVoice Assistant : launching an instance ")
                else:
                    pyttsx3.speak("An error occured.........please check")
                    print("\n\t\t\t\t\t\tVoice Assistant : An error occured.........please check")
                out=output[1]
                print(out)
                print("\n\t\t\t\t\t\tDo you want to continue?(y/N)",end=' ')
                i=input()
            if(ch==5):
                print("\n\t\t\t\t\t\tEnter the size in GB",end= ' ')
                si=input()
                cmd='aws ec2 create-volume --availability-zone ap-south-1a   --size {}'.format(si)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Creating an ebs volume of 1GB")
                    print("\n\t\t\t\t\t\t Creating an ebs volume of 1GB")
                else:
                    pyttsx3.speak("An error occured.........please check")
                    print("\n\t\t\t\t\t\t An error occured.........please check")
                out=output[1]
                print(out)
                print("\n\t\t\t\t\t\tDo you want to continue?(y/N)",end=' ')
                i=input()
            if(ch==6):
                print("\n\t\t\t\t\t\tEnter the instance id ",end= ' ')
                id1=input()
                print("\n\t\t\t\t\t\tEnter the volume id" ,end= ' ')
                vol=input()
                cmd='aws ec2 attach-volume  --device /dev/xvdb  --instance-id {}  --volume-id {}'.format(id1,vol)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Attaching the ebs volume to the ec2 instance")
                    print("\n\t\t\t\t\t\t Attaching the ebs volume to the ec2 instance")
                else:
                    pyttsx3.speak("Someting is wrong....Try again")
                    print("\n\t\t\t\t\t\t Someting is wrong....Try again")
                out=output[1]
                print(out)
                print("\n\t\t\t\t\t\tDo you want to continue?(y/N)",end=' ')
                i=input()
            if(ch==7):
                print("\n\t\t\t\t\t\tEnter the bucket name ",end= ' ')
                s3=input()
                cmd="aws s3 mb s3://{}".format(s3)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Creating the ...S3 bucket ")
                    print(Fore.YELLOW,"\n\t\t\t\t\t\t\t\tCreating the S3 bucket")
                else:
                    pyttsx3.speak("An error occured.........please check")
                    print(Fore.YELLOW,"\n\t\t\t\t\t\t\t\tAn error occured.........please check")
                out=output[1]
                print("\n\t\t\t\t\t\t\t\t",out)
                print(Fore.RED,"\n\t\t\t\t\t\t\tDo tou want to continue? (y/n): ",end=' ')
                i=input()
            if(ch==8):
                print("\n\t\t\t\t\t\tEnter the bucket name ",end= ' ')
                s3=input()
                print("\n\t\t\t\t\t\tEnter the folder path ",end= ' ')
                s=input()
                cmd=r'aws s3 cp  C:\Users\Tejas\Downloads   s3://{}/ --recursive --exclude "*" --include "*.jpg"'.format(s3)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Uploading the image...in S3 bucket  ")
                    print(Fore.YELLOW,"\n\t\t\t\t\t\t\t\tUploading the image in S3 bucket ")
                else:
                    pyttsx3.speak("An error occured.........please check")
                    print("\n\t\t\t\t\t\t\t\tAn error occured.........please check")
                out=output[1]
                print("\n\t\t\t\t\t\t\t\t",out)
                print(Fore.RED,"\n\t\t\t\t\t\t\tDo tou want to continue? (y/n): ",end=' ')
                i=input()
            
            if(ch==9):
                print("\n\t\t\t\t\t\tEnter the bucket name ",end= ' ')
                s3=input()
                cmd="aws cloudfront create-distribution   --origin-domain-name {}.s3.amazonaws.com   --default-root-object index.html".format(s3)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Creating ...CloudFront Distribution ")
                    print(Fore.YELLOW,"\n\t\t\t\t\t\t\t\tCreating CloudFront Distribution")
                else:
                    pyttsx3.speak("An error occured.........please check")
                    print("\n\t\t\t\t\t\t\t\tAn error occured.........please check")
                out=output[1]
                print("\n\t\t\t\t\t\t\t\t",out)
                print(Fore.RED,"\n\t\t\t\t\t\t\tDo tou want to continue? (y/n): ",end=' ')
                i=input()
                    
            if(ch==10):
               
                while(True):
                    clear()
                    print(Fore.WHITE, "\n\n\n\t\t\t\t\t\t\t\t\tHigh Availability Architecture\n\t\t\t__________________________________________________________________________________________________")
                    print(Fore.BLUE,"\n\n\n\n\t\t\t\t\t\t\tSTEPS TO CREATE A WEB-UI OF HIGH AVAILABILITY ARCHITECTURE")
                    print("\n\t\t\t\t\t\t\t\t1: What is CloudFront ") 
                    print("\n\t\t\t\t\t\t\t\t2: launch the ec2 instance ") 
                    print("\n\t\t\t\t\t\t\t\t3: Install  and start the service of httpd ") 
                    print("\n\t\t\t\t\t\t\t\t4: Create a EBS Volume and attach to an instance")
                    print("\n\t\t\t\t\t\t\t\t5: Create a partition in attached ebs volume")
                    print("\n\t\t\t\t\t\t\t\t6: Format the partition")
                    print("\n\t\t\t\t\t\t\t\t7: Mount the partition on /var/www/html")
                    print("\n\t\t\t\t\t\t\t\t8: Create a S3 bucket ")
                    print("\n\t\t\t\t\t\t\t\t9: Upload the image in S3 bucket") 
                    print("\n\t\t\t\t\t\t\t\t10: Create a CloudFront Distribution") 
                    print("\n\t\t\t\t\t\t\t\t11: Upload the html page in /var/www/html folder") 
                    print("\n\t\t\t\t\t\t\t\t12: Return")
                    pyttsx3.speak("Please..Enter your..choice")
                    ch=int(input("\n\n\t\t\t\t\t\t\t\tEnter your choice:"))
                    
                    if(ch==1):
                        clear()
                        print(Fore.RED,"\n\n\n\n\n\t\t\t\t\t\t\tAmazon CloudFront Web Service\n")
                        print(Fore.YELLOW,"\tAmazon CloudFront is a web service that speeds up distribution of your static and dynamic web content, such as .html, .css, .js, and image files, to your users. CloudFront delivers your content through a worldwide network of data centers called edge locations. When a user requests content that you're serving with CloudFront, the user is routed to the edge location that provides the lowest latency (time delay), so that content is delivered with the best possible performance.\n\n\tIf the content is already in the edge location with the lowest latency, CloudFront delivers it immediately.\n\tIf the content is not in that edge location, CloudFront retrieves it from an origin that you've defined—such as an Amazon S3 bucket, a MediaPackage channel, or an HTTP server (for example, a web server) that you have identified as the source for the definitive version of your content.\n\n\tAs an example, suppose that you're serving an image from a traditional web server, not from CloudFront. For example, you might serve an image, sunsetphoto.png, using the URL http://example.com/sunsetphoto.png.\n\tYour users can easily navigate to this URL and see the image. But they probably don't know that their request was routed from one network to another—through the complex collection of interconnected networks that comprise the internet—until the image was found.\n\tCloudFront speeds up the distribution of your content by routing each user request through the AWS backbone network to the edge location that can best serve your content. Typically, this is a CloudFront edge server that provides the fastest delivery to the viewer. Using the AWS network dramatically reduces the number of networks that your users' requests must pass through, which improves performance. Users get lower latency—the time it takes to load the first byte of the file—and higher data transfer rates.\n\tYou also get increased reliability and availability because copies of your files (also known as objects) are now held (or cached) in multiple edge locations around the world.")
                        pyttsx3.speak("Amazon CloudFront...... is a web service...... that speeds up distribution ...of your static ...and dynamic web content, such as .html, .css, .js, and image files, to your users........ CloudFront ......delivers your content ....through a worldwide network .....of data centers called edge locations..................")
                        pyttsx3.speak(" When a user requests content... that you're serving with CloudFront.., the user is routed to the edge location ...that provides the lowest latency ....that is time delay , so that content is delivered ...with the best possible.. performance.")
                        pyttsx3.speak(",For more information.....read ..this...")
                        print(Fore.RED,"\n\t\t\t\t\t\t\tDo tou want to continue? (y/n): ",end='')
                        inp=input()
                    
                    if(ch==2):
                        clear()
                        print(Fore.WHITE, "\n\n\n\t\t\t\t\t\t\t\t\tLaunch EC2 instance\n\t\t\t__________________________________________________________________________________________________")
                        cmd="aws ec2 run-instances --image-id    ami-0e306788ff2473ccb --instance-type    t2.micro --count 1 --subnet-id subnet-bfb2b8d7  --security-group-ids sg-014d3d81c4b81dfcd  --key-name new2"
                        output=sp.getstatusoutput(cmd)
                        status=output[0]
                        if(status==0):
                            pyttsx3.speak("Launching .. an ..instance")
                            
                            print(Fore.YELLOW,"\n\t\t\t\t\t\t\t\tLaunching an instance")
                        else:
                            pyttsx3.speak("An error occured.........please check")
                            print("\n\t\t\t\t\t\t\t\tAn error occured.........please check")
                        out=output[1]
                        print("\n\t\t\t\t\t\t\t\t",out)
                        print(Fore.RED,"\n\t\t\t\t\t\t\tDo tou want to continue? (y/n): ",end=' ')
                        inp=input()
                    
                    
                    elif (ch==3):
                        clear()
                        print(Fore.WHITE, "\n\n\n\t\t\t\t\t\t\t\t\thttpd Service\n\t\t\t__________________________________________________________________________________________________")
                        print("\n\t\t\t\t\t\tEnter the ip of instance ",end= ' ')
                        s3=input()
                        cmd=r"ssh -l ec2-user {}  -i C:\Users\Tejas\Downloads\terminal.pem sudo yum install httpd -y".format(s3)
                        output=sp.getstatusoutput(cmd)
                        status=output[0]
                        if(status==0):
                            pyttsx3.speak("Installing ...httpd ")
                            print(Fore.YELLOW,"\n\t\t\t\t\t\t\t\tInstalling httpd")
                        else:
                            pyttsx3.speak("An error occured.........please check")
                            print("\n\t\t\t\t\t\t\t\tAn error occured.........please check")
                        out=output[1]
                        print("\n\t\t\t\t\t\t\t\t",out)
                        
                        cmd=r"ssh -l ec2-user 52.66.210.147	  -i C:\Users\Tejas\Downloads\terminal.pem sudo systemctl start httpd"
                        output=sp.getstatusoutput(cmd)
                        status=output[0]
                        if(status==0):
                            pyttsx3.speak("Starting system...of ..httpd ")
                            print("\n\t\t\t\t\t\t\t\tStarting system of httpd")
                        else:
                            pyttsx3.speak("An error occured.........please check")
                            print("\n\t\t\t\t\t\t\t\tAn error occured.........please check")
                        out=output[1]
                        print("\n\t\t\t\t\t\t\t\t",out)
                        print(Fore.RED,"\n\t\t\t\t\t\t\tDo tou want to continue? (y/n): ",end=' ')
                        inp=input()
                        
                    elif(ch==4):
                        clear()
                        print(Fore.WHITE, "\n\n\n\t\t\t\t\t\t\t\t\tEBS Volume\n\t\t\t__________________________________________________________________________________________________")
                        
                        print("\n\t\t\t\t\t\tEnter the size in GB",end= ' ')
                        si=input()
                        cmd='aws ec2 create-volume --availability-zone ap-south-1a   --size {}'.format(si)
                        output=sp.getstatusoutput(cmd)
                        status=output[0]
                        if(status==0):
                            pyttsx3.speak("Creating an ebs volume of 1GB")
                            print("\n\t\t\t\t\t\t Creating an ebs volume of 1GB")
                        else:
                            pyttsx3.speak("An error occured.........please check")
                            print("\n\t\t\t\t\t\t An error occured.........please check")
                        out=output[1]
                        print(out)
                        print(Fore.RED,"\n\t\t\t\t\t\tDo you want to continue?(y/N)",end=' ')
                        i=input()
                
                        print("\n\t\t\t\t\t\tEnter the instance id ",end= ' ')
                        id1=input()
                        print("\n\t\t\t\t\t\tEnter the volume id" ,end= ' ')
                        vol=input()
                        cmd='aws ec2 attach-volume  --device /dev/xvdb  --instance-id {}  --volume-id {}'.format(id1,vol)
                        output=sp.getstatusoutput(cmd)
                        status=output[0]
                        if(status==0):
                            pyttsx3.speak("Attaching the ebs volume to the ec2 instance")
                            print("\n\t\t\t\t\t\t Attaching the ebs volume to the ec2 instance")
                        else:
                            pyttsx3.speak("Someting is wrong....Try again")
                            print("\n\t\t\t\t\t\t Someting is wrong....Try again")
                        out=output[1]
                        print(out)
                        print("\n\t\t\t\t\t\tDo you want to continue?(y/N)",end=' ')
                        i=input()
                        
                    elif(ch==5):
                        clear()
                        print(Fore.WHITE, "\n\n\n\t\t\t\t\t\t\t\t\tLinux Partitions\n\t\t\t__________________________________________________________________________________________________")
                        print("\n\t\t\t\t\t\tEnter the ip of instance ",end= ' ')
                        s3=input()
                        cmd=r"ssh -l ec2-user {}  -i C:\Users\Tejas\Downloads\terminal.pem  sudo fdisk -l".format(s3)
                        #cmd=r"ssh  root@13.233.31.13 fdisk /dev/xvdf"
                        output=sp.getstatusoutput(cmd)
                        status=output[0]
                        if(status==0):
                            pyttsx3.speak("Create.. partition ")
                            print(Fore.YELLOW,"\n\t\t\t\t\t\t\t\tCreate partition")
                        else:
                            pyttsx3.speak("An error occured.........please check")
                            print(Fore.YELLOW,"\n\t\t\t\t\t\t\t\tAn error occured.........please check")
                        out=output[1]
                        print("\n\t\t\t\t\t\t\t\t",out)
                        print(Fore.RED,"\n\t\t\t\t\t\t\tDo tou want to continue? (y/n): ",end=' ')
                        inp=input()
                        
                    elif(ch==6):
                        clear()
                        print(Fore.WHITE, "\n\n\n\t\t\t\t\t\t\t\t\tFormat parition\n\t\t\t__________________________________________________________________________________________________")
                        print("\n\t\t\t\t\t\tEnter the ip of instance ",end= ' ')
                        s3=input()
                        cmd=r"ssh -l ec2-user {}	  -i C:\Users\Tejas\Downloads\terminal.pem sudo mkfs.ext4                /dev/xvdf1	".format(s3)
                        output=sp.getstatusoutput(cmd)
                        status=output[0]
                        if(status==0):
                            pyttsx3.speak("Formatting .. the partition  ")
                            print(Fore.YELLOW,"\n\t\t\t\t\t\t\t\tFormatting the partition")
                        else:
                            pyttsx3.speak("An error occured.........please check")
                            print(Fore.YELLOW,"\n\t\t\t\t\t\t\t\tAn error occured.........please check")
                        out=output[1]
                        print("\n\t\t\t\t\t\t\t\t",out)
                        print(Fore.RED,"\n\t\t\t\t\t\t\tDo tou want to continue? (y/n): ",end=' ')
                        inp=input()
                        
                        
                    elif(ch==7):
                        clear()
                        print(Fore.WHITE, "\n\n\n\t\t\t\t\t\t\t\t\tMount partition\n\t\t\t__________________________________________________________________________________________________")
                        print("\n\t\t\t\t\t\tEnter the ip of instance ",end= ' ')
                        s3=input()
                        cmd=r" ssh -l ec2-user {}	  -i C:\Users\Tejas\Downloads\terminal.pem sudo mount /dev/xvdf1    /var/www/html".format(s3)
                        output=sp.getstatusoutput(cmd)
                        status=output[0]
                        if(status==0):
                            pyttsx3.speak("Mounting.. the .. partition..  ")
                            print(Fore.YELLOW,"\n\t\t\t\t\t\t\t\tMounting the partition")
                        else:
                            pyttsx3.speak("An error occured.........please check")
                            print("\n\t\t\t\t\t\t\t\tAn error occured.........please check")
                        out=output[1]
                        print("\n\t\t\t\t\t\t\t\t",out)
                        print(Fore.RED,"\n\t\t\t\t\t\t\tDo tou want to continue? (y/n): ",end=' ')
                        inp=input()
                        
                    elif(ch==8):
                        clear()
                        print(Fore.WHITE, "\n\n\n\t\t\t\t\t\t\t\t\tS3 Bucket\n\t\t\t__________________________________________________________________________________________________")
                        print("\n\t\t\t\t\t\tEnter the bucket name ",end= ' ')
                        s3=input()
                        cmd="aws s3 mb s3://{}".format(s3)
                        output=sp.getstatusoutput(cmd)
                        status=output[0]
                        if(status==0):
                            pyttsx3.speak("Creating the ...S3 bucket ")
                            print(Fore.YELLOW,"\n\t\t\t\t\t\t\t\tCreating the S3 bucket")
                        else:
                            pyttsx3.speak("An error occured.........please check")
                            print(Fore.YELLOW,"\n\t\t\t\t\t\t\t\tAn error occured.........please check")
                        out=output[1]
                        print("\n\t\t\t\t\t\t\t\t",out)
                        print(Fore.RED,"\n\t\t\t\t\t\t\tDo tou want to continue? (y/n): ",end=' ')
                        print("\n\t\t\t\t\t\tDo you want to continue?(y/N)",end=' ')
                        i=input()
                        
                        
                    elif(ch==9):
                        clear()
                        print(Fore.WHITE, "\n\n\n\t\t\t\t\t\t\t\t\tUploading image to s3 bucket\n\t\t\t__________________________________________________________________________________________________")
                        print("\n\t\t\t\t\t\tEnter the bucket name ",end= ' ')
                        s3=input()
                        print("\n\t\t\t\t\t\tEnter the folder path ",end= ' ')
                        s=input()
                        cmd=r'aws s3 cp  C:\Users\Tejas\Downloads   s3://{}/ --recursive --exclude "*" --include "*.jpg"'.format(s3)
                        output=sp.getstatusoutput(cmd)
                        status=output[0]
                        if(status==0):
                            pyttsx3.speak("Uploading the image...in S3 bucket  ")
                            print(Fore.YELLOW,"\n\t\t\t\t\t\t\t\tUploading the image in S3 bucket ")
                        else:
                            pyttsx3.speak("An error occured.........please check")
                            print("\n\t\t\t\t\t\t\t\tAn error occured.........please check")
                        out=output[1]
                        print("\n\t\t\t\t\t\t\t\t",out)
                        print(Fore.RED,"\n\t\t\t\t\t\t\tDo tou want to continue? (y/n): ",end=' ')
                        i=input()
                        
                        
                    elif(ch==10):
                        clear()
                        print(Fore.WHITE, "\n\n\n\t\t\t\t\t\t\t\t\tCreate CloudFront Distribution\n\t\t\t__________________________________________________________________________________________________")
                        print("\n\t\t\t\t\t\tEnter the bucket name ",end= ' ')
                        s3=input()
                        cmd="aws cloudfront create-distribution   --origin-domain-name {}.s3.amazonaws.com   --default-root-object index.html".format(s3)
                        output=sp.getstatusoutput(cmd)
                        status=output[0]
                        if(status==0):
                            pyttsx3.speak("Creating ...CloudFront Distribution ")
                            print(Fore.YELLOW,"\n\t\t\t\t\t\t\t\tCreating CloudFront Distribution")
                        else:
                            pyttsx3.speak("An error occured.........please check")
                            print("\n\t\t\t\t\t\t\t\tAn error occured.........please check")
                        out=output[1]
                        print("\n\t\t\t\t\t\t\t\t",out)
                        print(Fore.RED,"\n\t\t\t\t\t\t\tDo tou want to continue? (y/n): ",end=' ')
                        inp=input()
                        
                        
                    elif(ch==11):
                        clear()
                        print(Fore.WHITE, "\n\n\n\t\t\t\t\t\t\t\t\tUploading the file\n\t\t\t__________________________________________________________________________________________________")
                        cmd=r" ssh -l ec2-user 52.66.210.147	  -i C:\Users\Tejas\Downloads\terminal.pem sudo  echo Hello > rutu.html	"
                        output=sp.getstatusoutput(cmd)
                        status=output[0]
                        if(status==0):
                            #pyttsx3.speak("G ")
                            print(Fore.YELLOW,"\n\t\t\t\t\t\t\t\tGoing to /var/www/html folder")
                        else:
                            #pyttsx3.speak("An error occured.........please check")
                            print("\n\t\t\t\t\t\t\t\tAn error occured.........please check")
                        out=output[1]
                        print("\n\t\t\t\t\t\t\t\t",out)
                        print(Fore.RED,"\n\t\t\t\t\t\t\tDo tou want to continue? (y/n): ",end=' ')
                        inp=input()
                        
                       
                        
                        
                        
                    elif(ch==12):
                        pyttsx3.speak("Returing back ")
                        print(Fore.YELLOW,"\n\t\t\t\t\t\t\t\tReturing back")
                        break
                        
            if(ch==11):
                pyttsx3.speak("Returing back")
                print(Fore.YELLOW,"\n\t\t\t\t\t\t\t\tReturing back")
                break
                        
                
                
               # aws s3 cp  C:\Users\Tejas\Downloads   s3://yooooo/ --recursive --exclude "*" --include "*.jpg 
     


    if(ch==5):
        while(True):
            clear()
            print("\n\t\t\t\t\t\t\t\t1 : Create physical volume")
            print("\n\t\t\t\t\t\t\t\t2 : Create volume group")
            print("\n\t\t\t\t\t\t\t\t3 : Display vg")
            print("\n\t\t\t\t\t\t\t\t4 : Create Logical volume")
            print("\n\t\t\t\t\t\t\t\t5 : Display Logical volume")
            print("\n\t\t\t\t\t\t\t\t6 : Format")
            print("\n\t\t\t\t\t\t\t\t7 : Create the directory and mount")
            print("\n\t\t\t\t\t\t\t\t8 : Extend logical volume")
            print("\n\t\t\t\t\t\t\t\t9 : Format the extended volume")
            print("\n\t\t\t\t\t\t\t\t10 : Return back")
            pyttsx3.speak("Please..Enter your..choice")
            ch=int(input("\n\n\t\t\t\t\t\t\t\tEnter your choice:"))
            
            if(ch==1):
                print("\n\t\t\t\t\t\tEnter the first Hard disk name ",end= ' ')
                hd1=input()
                print("\n\t\t\t\t\t\tEnter the ip ",end= ' ')
                ipp=input()
                cmd='ssh -l root {}	sudo pvcreate {}'.format(ipp,hd1)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Creating physical volume")
                    print("\n\t\t\t\t\t\t Creating physical volume")
                else:
                    pyttsx3.speak("Someting is wrong....Try again")
                    print("\n\t\t\t\t\t\t Someting is wrong....Try again")
                out=output[1]
                print(out)
                
                print("\n\t\t\t\t\t\tEnter the second Hard disk name ",end= ' ')
                hd1=input()
                cmd='ssh -l root {}	sudo pvcreate {}'.format(ipp,hd1)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Creating physical volume")
                    print("\n\t\t\t\t\t\t Creating physical volume")
                else:
                    pyttsx3.speak("Someting is wrong....Try again")
                    print("\n\t\t\t\t\t\t Someting is wrong....Try again")
                out=output[1]
                print(out)
                print("\n\t\t\t\t\t\tDo you want to continue?(y/N)",end=' ')
                i=input()
            if(ch==2):
                print("\n\t\t\t\t\t\tEnter the volume group name ",end= ' ')
                vg=input()
                cmd='ssh -l root {}	sudo vgcreate {}  /dev/sdb    /dev/sdc'.format(ipp,vg)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Creating volume group")
                    print("\n\t\t\t\t\t\t Creating volume group")
                else:
                    pyttsx3.speak("Someting is wrong....Try again")
                    print("\n\t\t\t\t\t\t Someting is wrong....Try again")
                out=output[1]
                print(out)
                print("\n\t\t\t\t\t\tDo you want to continue?(y/N)",end=' ')
                i=input()
            if(ch==3):
                print("\n\t\t\t\t\t\tEnter the volume group name ",end= ' ')
                vg=input()
                cmd='ssh -l root {}	sudo vgdisplay {}'.format(ipp,vg)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Displaying volume group")
                    print("\n\t\t\t\t\t\t Displaying volume group")
                else:
                    pyttsx3.speak("Someting is wrong....Try again")
                    print("\n\t\t\t\t\t\t Someting is wrong....Try again")
                out=output[1]
                print(out)
                print("\n\t\t\t\t\t\tDo you want to continue?(y/N)",end=' ')
                i=input()
            if(ch==4):
                print("\n\t\t\t\t\t\tEnter the logical volume name ",end= ' ')
                lv=input()
                print("\n\t\t\t\t\t\tEnter the logical volume size in GB ",end= ' ')
                size=input()
                print("\n\t\t\t\t\t\tEnter the volume group name ",end= ' ')
                vg=input()
                cmd='ssh -l root {}	sudo lvcreate --size {}G --name {} {}'.format(ipp,size,lv,vg)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Creating logical group")
                    print("\n\t\t\t\t\t\t Creating logical group")
                else:
                    pyttsx3.speak("Someting is wrong....Try again")
                    print("\n\t\t\t\t\t\t Someting is wrong....Try again")
                out=output[1]
                print(out)
                print("\n\t\t\t\t\t\tDo you want to continue?(y/N)",end=' ')
                i=input()
            if(ch==5):
                print("\n\t\t\t\t\t\tEnter the logical volume name ",end= ' ')
                lv=input()
                print("\n\t\t\t\t\t\tEnter the volume group name ",end= ' ')
                vg=input()
                cmd='ssh -l root {}	sudo lvdisplay {} {}'.format(ipp,vg,lv)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Displaying logical group")
                    print("\n\t\t\t\t\t\t Displaying logical group")
                #else:
                    #pyttsx3.speak("Someting is wrong....Try again")
                    #print("\n\t\t\t\t\t\t Someting is wrong....Try again")
                out=output[1]
                print(out)
                print("\n\t\t\t\t\t\tDo you want to continue?(y/N)",end=' ')
                i=input()
            if(ch==6):
                print("\n\t\t\t\t\t\tEnter the logical volume name ",end= ' ')
                lv=input()
                print("\n\t\t\t\t\t\tEnter the volume group name ",end= ' ')
                vg=input()
                cmd='ssh -l root {}	sudo mkfs.ext4  /dev/{}/{}'.format(ipp,vg,lv)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Formatting")
                    print("\n\t\t\t\t\t\t Formatting")
                else:
                    pyttsx3.speak("Someting is wrong....Try again")
                    print("\n\t\t\t\t\t\t Someting is wrong....Try again")
                out=output[1]
                print(out)
                print("\n\t\t\t\t\t\tDo you want to continue?(y/N)",end=' ')
                i=input()
            if(ch==7):
                print("\n\t\t\t\t\t\tEnter the directory name ",end= ' ')
                fil=input()
                cmd='ssh -l root {}	sudo mkdir /{}'.format(ipp,fil)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Creating new directory")
                    print("\n\t\t\t\t\t\t Creating new directory")
                else:
                    pyttsx3.speak("Someting is wrong....Try again")
                    print("\n\t\t\t\t\t\t Someting is wrong....Try again")
                out=output[1]
                print(out)
                
                print("\n\t\t\t\t\t\tEnter the volume group name ",end= ' ')
                vg=input()
                print("\n\t\t\t\t\t\tEnter the logical volume name ",end= ' ')
                lv=input()
                cmd='ssh -l root {}	sudo mount /dev/{}/{}    /{}'.format(ipp,vg,lv,fil)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Mounting")
                    print("\n\t\t\t\t\t\t Mounting.....")
                else:
                    pyttsx3.speak("Someting is wrong....Try again")
                    print("\n\t\t\t\t\t\t Someting is wrong....Try again")
                out=output[1]
                print(out)
                
                print("\n\t\t\t\t\t\tDo you want to continue?(y/N)",end=' ')
                i=input()
                
            if(ch==8):
                print("\n\t\t\t\t\t\tEnter the logical volume name ",end= ' ')
                lv=input()
                print("\n\t\t\t\t\t\tEnter the volume group name ",end= ' ')
                vg=input()
                print("\n\t\t\t\t\t\tEnter the size by which you want to extend LV",end= ' ')
                size=input()
                cmd='ssh -l root {}	sudo lvextend  --size +{}G  /dev/{}/{}'.format(ipp,size,vg,lv)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Extending the Logical volume")
                    print("\n\t\t\t\t\t\t Extending the Logical volume")
                else:
                    pyttsx3.speak("Someting is wrong....Try again")
                    print("\n\t\t\t\t\t\t Someting is wrong....Try again")
                out=output[1]
                print(out)
                print("\n\t\t\t\t\t\tDo you want to continue?(y/N)",end=' ')
                i=input()
            if(ch==9):
                print("\n\t\t\t\t\t\tEnter the logical volume name ",end= ' ')
                lv=input()
                print("\n\t\t\t\t\t\tEnter the volume group name ",end= ' ')
                vg=input()
                
                cmd='ssh -l root {}	sudo resize2fs /dev/{}/{}'.format(ipp,vg,lv)
                output=sp.getstatusoutput(cmd)
                status=output[0]
                if(status==0):
                    pyttsx3.speak("Formatting")
                    print("\n\t\t\t\t\t\t Formatting")
                else:
                    pyttsx3.speak("Someting is wrong....Try again")
                    print("\n\t\t\t\t\t\t Someting is wrong....Try again")
                out=output[1]
                print(out)
                print("\n\t\t\t\t\t\tDo you want to continue?(y/N)",end=' ')
                i=input()
            if(ch==10):
                pyttsx3.speak("Returing back")
                print(Fore.YELLOW,"\n\t\t\t\t\t\t\t\tReturing back")
                break
    
    if(ch==6):
        print(Fore.RED,"\n\t\t\t\t\t\t\t\t1: Shut down")    
        print("\n\t\t\t\t\t\t\t\t2: Restart ") 
        pyttsx3.speak("Please...Enter your..choice")
        ch=int(input("\n\n\t\t\t\t\t\t\t\tEnter your choice:"))
        if(ch==1):
            ipp=int(input("\n\n\t\t\t\t\t\t\t\tEnter your IP:"))
            cmd="ssh -l root {}	sudo init 0".format(ipp)
            output=sp.getstatusoutput(cmd)
            status=output[0]
            if(status==0):
                pyttsx3.speak("Terminating")
                print("\n\t\t\t\t\t\t Terminating....")
            else:
                pyttsx3.speak("Someting is wrong....Try again")
                print("\n\t\t\t\t\t\t Someting is wrong....Try again")
            out=output[1]
            print(out)
            print("\n\t\t\t\t\t\tDo you want to continue?(y/N)",end=' ')
            i=input()
        if(ch==2):
            ipp=int(input("\n\n\t\t\t\t\t\t\t\tEnter your IP:"))
            cmd='ssh -l root {}	sudo init 6'.format(ipp)
            output=sp.getstatusoutput(cmd)
            status=output[0]
            if(status==0):
                pyttsx3.speak("Restarting")
                print("\n\t\t\t\t\t\t Restarting....")
            else:
                pyttsx3.speak("Someting is wrong....Try again")
                print("\n\t\t\t\t\t\t Someting is wrong....Try again")
            out=output[1]
            print(out)
            print("\n\t\t\t\t\t\tDo you want to continue?(y/N)",end=' ')
            i=input()
    if(ch==7):
        pyttsx3.speak("Bye....Have a nice day")
        print(Fore.YELLOW,"\n\t\t\t\t\t\t\t\tBye....Have a nice day :)")
        exit()
        