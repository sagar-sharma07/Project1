from django.shortcuts import redirect, render
from myapp import models
from django.core.mail import send_mail
from resturant import settings

# Create your views here.

def test(request):
    return render(request,'test.html')

def home(request):
    return render(request,'home.html')

def getdirections(request):
    return render(request,'getdirections.html')    

def blogs(request):
    blgs=models.blogs.objects.all()
    print(blgs)
    return render(request,'blogs.html',{'blogs':blgs})

def contactus(request):
    if request.method == 'POST':
        print('Form submitted')
        name = request.POST.get('username')
        email = request.POST.get('user_email')
        message = request.POST.get('message')
        
        c = models.enquiry() 
        c.username = name
        c.email = email
        c.message = message
        c.save()
        res=1
        return render(request,'contactus.html',{'response':res})

    return render(request,'contactus.html') 

def gallery(request):
    efg=models.gallery.objects.all()
    print(efg)
    return render(request,'gallery.html',{'gallery':efg})

def login(request):
    if request.method == 'POST':
        
        email = request.POST.get('user_email')
        password = request.POST.get('user_password')

        if models.registeruser.objects.filter(email=email, password=password).exists():
            user=models.registeruser.objects.get(email=email)
            request.session['userid'] = user.id
            print('Sucessful Login')

            return redirect('myprofile')

            
        else:
            print('Invalid Credentials')
            res = 1

            return render(request,'login.html',{'response':res})
    return render(request,'login.html')  

def register(request):
    if request.method == 'POST':
        print('Form submitted')
        name = request.POST.get('username')
        email = request.POST.get('user_email')
        password = request.POST.get('user_password')
        confirmpassword = request.POST.get('cpassword')

        if password == confirmpassword :
            print('Password matched')
            if models.registeruser.objects.filter(email=email).exists():
                print('Email id already exists')
                res=2
                return render(request,'register.html',{ 'response':res})


            else:
                print('Email id does not exists')
                u= models.registeruser()
                u.name=name
                u.email=email
                u.password=password
                u.save()
                

                return redirect('login')




        else:
            res=1
            print('password does not match')
            return render(request,'register.html',{ 'response':res})


        # r = models.registeruser()
        # r.name = name
        # r.email = email
        # r.password = password
        # r.save()
        
        return render(request,'register.html',{ 'response':abc})

    return render(request,'register.html')

def inquery(request):
    abc=models.enquiry.objects.all()
    print(abc)
    return render(request,'inquery.html',{'inquery':abc})
    
def fullblogs(request,blogid):
    blogs = models.blogs.objects.get(id = blogid)
    print(blogs)

    return render(request,'fullblogs.html',{'abc':blogs})

def changepassword(request):
    
    user = models.registeruser.objects.get(id = request.session.get('userid') ) 
    print(user)

    if request.method == 'POST':
        print('Form Submitted')
        oldpassword = request.POST.get('user_password')
        newpassowrd = request.POST.get('npassword')
        confirmpassword = request.POST.get('cpassword')

        if newpassowrd == confirmpassword:
            print('Password matched')
            if oldpassword == user.password:
                print('old password matches')
                user.password = newpassowrd
                user.save()
                res=3
                print('Password changed successfully')            
                return render(request,'changepassword.html',{'response':res})



            else:
                res=2
                print('old password does not matched')            
                return render(request,'changepassword.html',{'response':res})

            


        else:
            res=1
            print('password does not matched')            
            return render(request,'changepassword.html',{'response':res})
    return render(request,'changepassword.html')

def myprofile(request):
    user = models.registeruser.objects.get(id = request.session.get('userid'))
    print(user)
    return render(request,'myprofile.html',{'myprofile':user})

def forgetpasssword(request):
    if request.method == 'POST':
        email=request.POST.get('user_email')
        print(email)
        if models.registeruser.objects.filter(email=email).exists():
            print('EMail exists')
            user=models.registeruser.objects.get(email=email)
            ####send mail

            subject='Your Forgotten Password'
            message='Your Password is: '+user.password
            email_from=settings.EMAIL_HOST_USER
            email_to=[email,]

            send_mail(subject, message,email_from,email_to)

        else:
            print('EMail does not exists')
            res=1
            return render(request,'forgetpassword.html',{'res':res})



        
        

    return render(request,'forgetpassword.html')

def logout(request):
    del request.session['userid']
    return redirect('login')

