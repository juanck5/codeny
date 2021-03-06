
from email.mime import text
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.views.decorators.csrf import csrf_protect
# from tkinter import *
from django.http import HttpResponse
import smtplib

# Create your views here.


# PAGES
def index(request):
    nombre = "roberto"
    user = "asjchjdsch"
    return render(request, 'web/index.html' , {'nombre' : nombre, 'nombre2' : user})

def boardAdmin(request):
    return render(request, 'dashboards/dashboard.html')

def login(request):
   return render(request, 'dashboards/login.html')

def profile(request):
   return render(request, 'dashboards/profile.html') 
 
def tables(request):
   return render(request, 'dashboards/tables.html') 

def billing(request):
   return render(request, 'dashboards/billing.html')   


def funcion(request):
   print("fui presionado")



# REQUESTS
@csrf_protect
def login_user(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponse("correcto")
        else:
            #  Retornar a una pagina de error
            try:
                user = User.objects.get(username=username)
                # si lo encuentra quiere decir que el problema está en la contraseña
                return HttpResponse("contraseñaIncorrecta")
            except User.DoesNotExist:
                # no está registrado
                return HttpResponse("usuarioNoExiste")
        
    return render(request, 'web/index.html')
   
def contactForm(request):

    print(request.POST)
    nameL = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    print(nameL)

    me = "codeny.contact@gmail.com"
    my_password = "ewjhsrfnsdthacem"
    you = "codeny.developers@gmail.com"

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Alguien te está contactando"
    msg['From'] = me
    msg['To'] = you

    html = '<!DOCTYPE html> <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office"> <head> <meta charset="utf-8"> <meta name="viewport" content="width=device-width,initial-scale=1"> <meta name="x-apple-disable-message-reformatting"> <title>Contácto</title> <!--[if mso]> <style> table {border-collapse:collapse;border-spacing:0;border:none;margin:0;} div, td {padding:0;} div {margin:0 !important;} </style> <noscript> <xml> <o:OfficeDocumentSettings> <o:PixelsPerInch>96</o:PixelsPerInch> </o:OfficeDocumentSettings> </xml> </noscript> <![endif]--> <style> table, td, div, h1, p { font-family: Arial, sans-serif; }@media screen and (max-width: 530px) { .unsub { display: block; padding: 8px; margin-top: 14px; border-radius: 6px; background-color: #555555; text-decoration: none !important; font-weight: bold; }.col-lge { max-width: 100% !important; } }@media screen and (min-width: 531px) { .col-sml { max-width: 27% !important; }.col-lge { max-width: 73% !important; } } </style> </head><body style="margin:0;padding:0;word-spacing:normal;background-color:#939297;"> <div role="article" aria-roledescription="email" lang="en" style="text-size-adjust:100%;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;background-color:#939297;"> <table role="presentation" style="width:100%;border:none;border-spacing:0;"> <tr> <td align="center" style="padding:0;"> <!--[if mso]> <table role="presentation" align="center" style="width:600px;"> <tr> <td> <![endif]--> <table role="presentation" style="width:94%;max-width:600px;border:none;border-spacing:0;text-align:left;font-family:Arial,sans-serif;font-size:16px;line-height:22px;color:#363636;"> <tr> <td style="padding:40px 30px 30px 30px;text-align:center;font-size:24px;font-weight:bold;"> <a href="http://www.example.com/" style="text-decoration:none;"><img src="https://assets.codepen.io/210284/logo.png" width="165" alt="Logo" style="width:80%;max-width:165px;height:auto;border:none;text-decoration:none;color:#ffffff;"></a> </td> </tr> <tr> <td style="padding:30px;background-color:#ffffff;"> <h1 style="margin-top:0;margin-bottom:16px;font-size:26px;line-height:32px;font-weight:bold;letter-spacing:-0.02em;">Hey hola, alguien nos está contactando</h1> <p style="margin:0;"> nombre: ' + nameL + '<br> email:' + email + '</p> </td> </tr> <tr> <td style="padding:0;font-size:24px;line-height:28px;font-weight:bold;"> <a href="http://www.example.com/" style="text-decoration:none;"><img src="https://assets.codepen.io/210284/1200x800-2.png" width="600" alt="" style="width:100%;height:auto;display:block;border:none;text-decoration:none;color:#363636;"></a> </td> </tr> <tr> <td style="padding:35px 30px 11px 30px;font-size:0;background-color:#ffffff;border-bottom:1px solid #f0f0f5;border-color:rgba(201,201,207,.35);"> <!--[if mso]> <table role="presentation" width="100%"> <tr> <td style="width:145px;" align="left" valign="top"> <![endif]--> <div class="col-sml" style="display:inline-block;width:100%;max-width:145px;vertical-align:top;text-align:left;font-family:Arial,sans-serif;font-size:14px;color:#363636;"> <img src="https://assets.codepen.io/210284/icon.png" width="115" alt="" style="width:80%;max-width:115px;margin-bottom:20px;"> </div> <!--[if mso]> </td> <td style="width:395px;padding-bottom:20px;" valign="top"> <![endif]--> <div class="col-lge" style="display:inline-block;width:100%;max-width:395px;vertical-align:top;padding-bottom:20px;font-family:Arial,sans-serif;font-size:16px;line-height:22px;color:#363636;"> <p style="margin-top:0;margin-bottom:12px;">'+ message +'</p> <p style="margin:0;"><a href="https://example.com/" style="background: #ff3884; text-decoration: none; padding: 10px 25px; color: #ffffff; border-radius: 4px; display:inline-block; mso-padding-alt:0;text-underline-color:#ff3884"> <!--[if mso]><i style="letter-spacing: 25px;mso-font-width:-100%;mso-text-raise:20pt">&nbsp;</i><![endif]--><span style="mso-text-raise:10pt;font-weight:bold;">Ir a la web</span> <!--[if mso]><i style="letter-spacing: 25px;mso-font-width:-100%">&nbsp;</i><![endif]--> </a></p> </div> <!--[if mso]> </td> </tr> </table> <![endif]--> </td> </tr><td style="padding:30px;background-color:#ffffff;"> <p style="margin:0;">Ánimo, vamos a atender tdas las peticiones!</p> </td> </tr> <tr> <td style="padding:30px;text-align:center;font-size:12px;background-color:#404040;color:#cccccc;"> <p style="margin:0 0 8px 0;"><a href="https://www.facebook.com/CodenyOficial" style="text-decoration:none;"><img src="https://assets.codepen.io/210284/facebook_1.png" width="40" height="40" alt="f" style="display:inline-block;color:#cccccc;"></a> <a href="http://www.twitter.com/" style="text-decoration:none;"><img src="https://assets.codepen.io/210284/twitter_1.png" width="40" height="40" alt="t" style="display:inline-block;color:#cccccc;"></a></p> <p style="margin:0;font-size:14px;line-height:20px;">&reg; Codeny, copyrigth 2021<br><a class="unsub" href="http://www.example.com/" style="color:#cccccc;text-decoration:underline;">Unsubscribe instantly</a></p> </td> </tr> </table> <!--[if mso]> </td> </tr> </table> <![endif]--> </td> </tr> </table> </div> </body></html>'
    part2 = MIMEText(html, 'html')

    msg.attach(part2)

    # Send the message via gmail's regular server, over SSL - passwords are being sent, afterall
    s = smtplib.SMTP_SSL('smtp.gmail.com')
    # uncomment if interested in the actual smtp conversation
    # s.set_debuglevel(1)
    # do the smtp auth; sends ehlo if it hasn't been sent already
    s.login(me, my_password)

    s.sendmail(me, you, msg.as_string())
    s.quit()

    return HttpResponse("success")