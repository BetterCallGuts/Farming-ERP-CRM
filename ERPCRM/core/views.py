from django.shortcuts import render




def index(req):
    
    
    return render (req, "home.html")




def CowApp(req,app, page,stat):
        var = {
        "app" : app,
        'slec': stat
    }
        if app == "cow":

                var['main'] = {'f' : "Cows", "s": "bull", "t": "Groups"}

                if stat == 1:
                    return render(req, 'app/staticticsview.html', var)
                
                elif stat == 2:
                    return render(req, 'app/addnew.html', var)
                
                elif stat == 3:
                    return render(req, 'app/staticticsview.html', var)
                    
                elif stat == 4:
                    return render(req, 'app/staticticsview.html', var)
                
                        
                elif stat == 5:
                    return render(req, 'app/staticticsview.html', var)
                
                elif stat == 6:
                    return render(req, 'app/staticticsview.html', var)

                elif stat == 7:
                    return render(req, 'app/staticticsview.html', var)

                elif stat == 8:
                    return render(req, 'app/staticticsview.html', var)
                
                            
                elif stat == 9:
                    return render(req, 'app/staticticsview.html', var)
                
        
        # 
        # 
        elif app == "empolyees" : 
            
            
                if stat == 1:
                    return render(req, 'app/staticticsview.html', var)
                elif stat == 2:
                    return render(req, 'app/addnew.html', var)
                elif stat == 3:
                    return render(req, 'app/staticticsview.html', var)
                elif stat == 4:
                    return render(req, 'app/staticticsview.html', var)
                elif stat == 5:
                    return render(req, 'app/staticticsview.html', var)
                elif stat == 6:
                    return render(req, 'app/staticticsview.html', var)
                elif stat == 7:            
                    return render(req, 'app/staticticsview.html', var)
                elif stat == 8:
                    return render(req, 'app/staticticsview.html', var)
                elif stat == 9:
                    return render(req, 'app/staticticsview.html', var)

        elif app == "milk" : 
            
            
                if stat == 1:
                    return render(req, 'app/staticticsview.html', var)
                
                
                elif stat == 2:
                    return render(req, 'app/addnew.html', var)
                elif stat == 3:
                    return render(req, 'app/staticticsview.html', var)
                    
                elif stat == 4:

                    return render(req, 'app/staticticsview.html', var)
                    
                elif stat == 5:

                    return render(req, 'app/staticticsview.html', var)
                
                elif stat == 6:
                    return render(req, 'app/staticticsview.html', var)
                    
                elif stat == 7:
                    return render(req, 'app/staticticsview.html', var)
                    
                elif stat == 8:
            
                    return render(req, 'app/staticticsview.html', var)
                       
                elif stat == 9:
            
                    return render(req, 'app/staticticsview.html', var)
                
                
                
        elif app == "food" : 

                if stat == 1:
                    return render(req, 'app/staticticsview.html', var)
                elif stat == 2:    
                    return render(req, 'app/addnew.html', var)
                elif stat == 3:
                    return render(req, 'app/staticticsview.html', var)
                elif stat == 4:
                    return render(req, 'app/staticticsview.html', var)
                elif stat == 5:
                    return render(req, 'app/staticticsview.html', var)
                elif stat == 6:
                    return render(req, 'app/staticticsview.html', var)
                elif stat == 7:
                    return render(req, 'app/staticticsview.html', var)
                elif stat == 8:
                    return render(req, 'app/staticticsview.html', var)
                elif stat == 9:
                    return render(req, 'app/staticticsview.html', var)
                
                

        elif app == "logs" : 

                if stat == 1:
                    return render(req, 'app/staticticsview.html', var)
                
                elif stat == 2:    
                    return render(req, 'app/addnew.html', var)
                
                elif stat == 3:
                    return render(req, 'app/staticticsview.html', var)
                    
                elif stat == 4:
                    return render(req, 'app/staticticsview.html', var)
                    
                elif stat == 5:
                    return render(req, 'app/staticticsview.html', var)
                
                elif stat == 6:
                    return render(req, 'app/staticticsview.html', var)
                     
                elif stat == 7:

                    return render(req, 'app/staticticsview.html', var)
                       
                elif stat == 8:
                    return render(req, 'app/staticticsview.html', var)
                       
                elif stat == 9:
                    return render(req, 'app/staticticsview.html', var)
                
                
                