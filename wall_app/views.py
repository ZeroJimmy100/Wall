from django.shortcuts import render, redirect, HttpResponse
from .models import User, Message, Comment, UserManager
from django.contrib import messages
import bcrypt


# Create your views here.

def index(request):
    users = User.objects.all()
    context = {
        "all_users": users
    }
    return render(request, "index.html", context)

def successDisplay(request, user_Val):
    users = User.objects.get(id = user_Val)
    messages = Message.objects.all()
    comments = Comment.objects.all()
    
    # give_me_messages()
    # myMessages = Message.objects.get(id= user_Val)
    if "user" not in request.session:
        return redirect("/")
    context = {
        "create_user": users,
        "go_message": messages,
        "go_comment": comments,
    }
    return render(request, "success.html", context)

def create_user(request):
    errors = User.objects.basic_validator(request.POST)
    password = request.POST['type_password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
    print(pw_hash) 
    
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        # print("*"*50, "\n", errors)
        return redirect("/")
    else:
        newUser = User.objects.create(first_name = request.POST["type_first_name"], 
        last_name = request.POST["type_last_name"], email = request.POST["type_email"],
        password = pw_hash)

        request.session['user'] = newUser.id
        return redirect(f"/success/{newUser.id}")
    
def validate_login(request):
    user = User.objects.filter(email=request.POST['type_login_email']) 
    print(user)
    if user:
        logged_user = user[0]

        if bcrypt.checkpw(request.POST['type_login_password'].encode(), logged_user.password.encode()):
            request.session["user"] = logged_user.id
            print("password match")
            return redirect("/success/{}".format(logged_user.id))
        else:
            print("failed password")
            messages.error(request, "Invalid password")
            return redirect("/")
    messages.error(request, "No account associated to email")
    print ("No account associated to email")
    return redirect("/")

def logout(request):
    request.session.flush()
    return redirect("/")

def give_me_messages(request):
    Create_Msg = Message.objects.create(message = request.POST["get_message"], users = User.objects.get(id= request.session["user"]))
    uid = request.session['user']
    return redirect(f"/success/{uid}")

def give_me_comments(request, val):
    Create_Cm = Comment.objects.create(
        comment = request.POST["get_comment"], 
        messages = Message.objects.get(id = val), 
        users = User.objects.get(id= request.session["user"]))
    Create_Cm.save()
    this_the_id = request.session['user']
    return redirect(f"/success/{this_the_id}")

def deleteMessage(request, got_Val):
    print("Going to delete a message!")
    delMessage = Message.objects.get(id = got_Val)
    print("Found the message!")
    delMessage.delete()
    print("Deleted the message!")
    goBack = request.session['user']
    print(goBack,"is our user? User ID?")
    return redirect(f"/success/{goBack}")

def deleteComment(request, this_val):
    print("Going to delete a comment!")
    delComment = Comment.objects.get(id = this_val)
    print("Found comment!")
    delComment.delete()
    print("Deleted the comment!")
    plsGoBack = request.session['user']
    print(plsGoBack,"is our user? User ID?")
    return redirect(f"/success/{plsGoBack}")
