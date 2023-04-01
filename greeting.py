import time 

a= input("enter your name: ")
timestamp= time.strftime('%H:%M:%S')
print (timestamp)

hour= int(time.strftime('%H'))
if 4 <= hour <12:
    print("Good morning", a)

elif 12<= hour <17:
    print("Good aftenoon", a)
    
elif 17<= hour <21:
    print("Good evening", a)
    
else:
    print("good night", a)            
    