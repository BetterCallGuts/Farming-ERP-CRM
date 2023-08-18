from django.shortcuts import render




def index(req):
    
    
    return render (req, "home.html")




def CowApp(req):
    

    return render(req, 'app/cows.html')