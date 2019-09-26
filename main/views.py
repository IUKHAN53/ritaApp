from django.shortcuts import render
import threading
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import UserGooglePasswordAddForm, UserFacebookPasswordAddForm
from users.models import FacebookFile
from scrappers.facebook_get_data import run
from django.contrib.auth import get_user_model
User_auth = get_user_model()
# run('sdf', 'sda', '/Users/comerade/Downloads')


def home(request):
    return render(request, 'main/home.html')


@login_required
def getdata(request):
    if request.method == 'POST':
        form_google = UserGooglePasswordAddForm(request.POST)
        form_facebook = UserFacebookPasswordAddForm(request.POST)

        if form_google.is_valid():
            messages.error(request, 'Unable to retrieve data from Google!')
            GoogleCred = form_google.save(commit=False)
            GoogleCred.user = request.user  # Set the user object here
            GoogleCred.save()  # Now you can send it to DB

        if form_facebook.is_valid():
            messages.success(request, 'Your request to get your data was succesfully passed!')
            messages.info(request, 'It may take anywhere from 2 mins to many hours to retrieve your data')
            facebookcred = form_facebook.save(commit=False)
            facebookcred.user = request.user  # Set the user object here
            facebookcred.save()
            fb_username_phone = facebookcred.facebook_email_phone
            fb_pass = facebookcred.facebook_password
            t = threading.Thread(target=run, args=[fb_username_phone, fb_pass, '/Users/comerade/Downloads', request.user])
            t.start()

    else:
        form_google = UserGooglePasswordAddForm()
        form_facebook = UserFacebookPasswordAddForm()
    return render(request, 'main/getdata.html', {'form_google': form_google, 'form_facebook': form_facebook})


@login_required
def your_data(request):
    all_user_file_objects = FacebookFile.objects.filter(user=request.user.pk)
    availible_stat_topass = False

    # all_user_file_objects[0].availible_stat
    # print(request.user.facebookfile.availible_stat)
    return render(request, 'main/yourdata.html', {'facebook_files': all_user_file_objects})
