from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from . import forms
from .models import User_details
from .models import user_requests
from django.core.exceptions import ObjectDoesNotExist

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('Project_Allotment_Portal:home')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            try:
                temp = User_details.objects.get(user_user=user)
                request.session['gamer_data_verified'] = temp.data_verified
                request.session['gamer_authority'] = temp.authority
            except ObjectDoesNotExist:
                pass
            login(request,user)
            return redirect('Project_Allotment_Portal:home')
    else :
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('Project_Allotment_Portal:home')

def user_profile(request):
    update(request)
    if request.method == 'POST':
        form = forms.ProfileDetails(request.POST, request.FILES)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user_user = request.user
            temp.data_verified = 1
            temp.save()
            return redirect('Project_Allotment_Portal:home')
    else:
        form = forms.ProfileDetails()

        # try:
        #     form = forms.ProfileDetails()
        #     temp_ = User_details.objects.get(user_user=request.user)
        #     verification_status = temp_.data_verified
        # except ObjectDoesNotExist:
        #     form = forms.ProfileDetails()
        #     verification_status = 0

        # if 'gamer' in request.session:
        #     return render(request, 'accounts/test.html')
        #     #form = forms.ProfileDetails(instance=User_details.objects.get(user_reg_no=request.session['gamer']));
        # else:
        #     form = forms.ProfileDetails()
    return render(request, 'accounts/profile.html', {'form':form} )


def team(request):

    if request.method == 'POST':
        data = request.POST.copy()
        reg = data.get('reg')
        req = user_requests()
        req.user_from = request.user
        req.user_to = User_details.objects.get(user_reg_no = reg ).user_user
        req.save()
    update(request)
    mem1 = User_details.objects.filter(authority=1)
    mem2 = User_details.objects.filter(authority=2)
    mem3 = User_details.objects.filter(authority=3)
    mem4 = User_details.objects.filter(authority=4)
    mem5 = user_requests.objects.filter(user_from=request.user)
    mem1_ = User_details.objects.none()
    mem2_ = User_details.objects.none()
    mem3_ = User_details.objects.none()
    mem4_ = User_details.objects.none()

    # f=1
    # while f == 1 :
    #     f=0
    for j in mem1:
        f=0
        for i in mem5 :
            if j.user_user == i.user_to:
                # mem1.exclude(user_user = i.user_user )
                f=1
                break
        if f==0:
            mem1_ |= User_details.objects.filter(user_user = j.user_user)
    for j in mem2:
        f=0
        for i in mem5 :
            if j.user_user == i.user_to:
                # mem1.exclude(user_user = i.user_user )
                f=1
                break
        if f==0:
            mem2_ |= User_details.objects.filter(user_user = j.user_user)
    for j in mem3:
        f=0
        for i in mem5 :
            if j.user_user == i.user_to:
                # mem1.exclude(user_user = i.user_user )
                f=1
                break
        if f==0:
            mem3_ |= User_details.objects.filter(user_user = j.user_user)
    for j in mem4:
        f=0
        for i in mem5 :
            if j.user_user == i.user_to:
                # mem1.exclude(user_user = i.user_user )
                f=1
                break
        if f==0:
            mem4_ |= User_details.objects.filter(user_user = j.user_user)

    # for j in mem5:
    #     for i in mem2 :
    #         if i.user_user == j.user_to:
    #             mem1.exclude(user_user = i.user_user )
    # for j in mem5:
    #     for i in mem3 :
    #         if i.user_user == j.user_to:
    #             mem1.exclude(user_user = i.user_user )
    # for j in mem5:
    #     for i in mem4 :
    #         if i.user_user == j.user_to:
    #             mem1.exclude(user_user = i.user_user )


    return render(request, 'accounts/team.html', {'mem1':mem1_, 'mem2':mem2_, 'mem3':mem3_, 'mem4':mem4_, 'mem5':mem5})

def validate(request):
    update(request)
    return render(request, 'accounts/validate.html')

def requests(request):
    update(request)
    return render(request, 'accounts/requests.html')

def update(request):
    try:
        if request.user.is_authenticated:
            temp = User_details.objects.get(user_user=request.user)
            request.session['gamer_data_verified'] = temp.data_verified
            request.session['gamer_authority'] = temp.authority
        else :
            request.session['gamer_data_verified'] = 0
            request.session['gamer_authority'] = 0
    except ObjectDoesNotExist:
        request.session['gamer_data_verified'] = 0
        request.session['gamer_authority'] = 0


