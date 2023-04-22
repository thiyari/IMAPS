import imaplib
from django.shortcuts import render, redirect
from django.contrib import messages
from IMAPMailsProcessing.Delete import DeleteSearch
from IMAPMailsProcessing.FetchDate import FetchDateSearch
from IMAPMailsProcessing.FetchFromSearch import FetchingFromSearch
from IMAPMailsProcessing.FetchingMails import Fetching
from IMAPMailsProcessing.Fromaddr import FromaddrSearch
from IMAPMailsProcessing.Subject import FetchSubject
from IMAPMailsProcessing.body import BodySearch
import re 
#import email
#import mailparser

# Create your views here.

def index(request):
        return render(request,'IMAPMailsProcessing/index.html')

def login(request):
    if request.method == 'POST':
        request.session['username'] = request.POST['username']
        request.session['password'] = request.POST['password']  

    if request.session.has_key('username') and request.session.has_key('password'):
        userid = request.session['username']
        passwd = request.session['password']
    #connect to host using SSL
    imap = imaplib.IMAP4_SSL('imap.gmail.com')

    #login to server
    try:
        connection = imap.login(userid,passwd)
        print("Connected: Login Successful")
        return redirect('home')
    except Exception as e:
        print("AUTHENTICATION FAILED!",e)
        return render(request,'IMAPMailsProcessing/index.html')

def home(request):
    return render(request, 'IMAPMailsProcessing/home.html')

def mails(request):
    userid = request.session['username']
    passwd = request.session['password']
    checkmails=Fetching(userid,passwd)
    result = checkmails.MailProcess()
    return render(request, 'IMAPMailsProcessing/mails.html',{"records":result})

def subject(request):
    userid = request.session['username']
    passwd = request.session['password']
    request.session['subject'] = request.POST['subject']
    subject = request.session['subject'] 
    checkmails=FetchSubject(userid,passwd,subject)
    result = checkmails.SubjectProcess()
    return render(request, 'IMAPMailsProcessing/mails.html',{"records":result})

def date(request):
    userid = request.session['username']
    passwd = request.session['password']
    request.session['date'] = request.POST['date']
    date = request.session['date'] 
    checkmails=FetchDateSearch(userid,passwd,date)
    result = checkmails.DateProcess()
    return render(request, 'IMAPMailsProcessing/mails.html',{"records":result})

def fromaddr(request):
    userid = request.session['username']
    passwd = request.session['password']
    request.session['from'] = request.POST['from']
    fromaddr = request.session['from'] 
    checkmails=FetchingFromSearch(userid,passwd,fromaddr)
    result = checkmails.FromAddrProcess()
    return render(request, 'IMAPMailsProcessing/mails.html',{"records":result})

def body(request):
    userid = request.session['username']
    passwd = request.session['password']
    request.session['body'] = request.POST['body']
    body = request.session['body'] 
    checkmails=BodySearch(userid,passwd,body)
    result = checkmails.BodyProcess()
    return render(request, 'IMAPMailsProcessing/mails.html',{"records":result})

def SelectMailsDeletion(request):
    userid = request.session['username']
    passwd = request.session['password']
    checkmails = FromaddrSearch(userid,passwd)
    result = checkmails.FromProcess()
    return render(request, 'IMAPMailsProcessing/SelectMailsDeletion.html',{"fromaddr":result})

def delete(request):
    userid = request.session['username']
    passwd = request.session['password']
    fromaddr = request.POST.getlist('from[]')
    for fromaddress in fromaddr:
        #Regular Expression for searching the email address from list
        match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', fromaddress)
        #match.group(0) retrieves only email address from the match
        from_addr = match.group(0)
        checkmails = DeleteSearch(userid,passwd,from_addr)
        checkmails.DeleteProcess()
    return redirect('SelectMailsDeletion')

def FromSearchForm(request):
    return render(request, 'IMAPMailsProcessing/FromSearchForm.html')

def BodySearchForm(request):
    return render(request, 'IMAPMailsProcessing/BodySearchForm.html')

def SinceDateForm(request):
    return render(request, 'IMAPMailsProcessing/SinceDateForm.html')

def logout(request):
    try:
        del request.session['username'],
        del request.session['password'],
        del request.session['subject'],
        del request.session['from'],
        del request.session['date'],
        del request.session['body']
    except KeyError:
        pass 
    return render(request,'IMAPMailsProcessing/index.html')