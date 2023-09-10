from django.shortcuts import render
import datetime
# Create your views here.

def app1(req):
    message = "Hi "
    dateTime = datetime.datetime.now()
    hour = int(dateTime.strftime("%H"))
    if hour<12:
        message+="Good Morning"
    else:
        message+="Good Night"

    content = {"name":"Balaji","dateTime":dateTime,"HOUR":hour}
    content["greet"]=message
    return render(req,'APP1/app1_index.html',context=content)
    