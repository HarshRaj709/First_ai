from django.shortcuts import render, redirect, HttpResponse
from .forms import InfoForm, LoginForms,RegisterForm
from .ai_client import GoogleAIClient
from .models import UserHistory
from django.contrib.auth import authenticate,login,logout
from .services import generate_travel_suggestions, format_response
from ai.settings import api_key
from django.contrib.auth.models import User
from django.contrib import messages



def UserRegister(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'gemni/register.html', {'form': form})



def UserLogin(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'gemni/login.html', {'error': 'Invalid username or password'})
        else:
            print(form.errors)
            return render(request, 'gemni/login.html')
    else:
        form = LoginForms()
       
        return render(request, 'gemni/login.html')


def form(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            request.session['form_data'] = form.cleaned_data
            print('Data valid')
            return redirect('result')
        else:
            print('Something went wrong')
    else:
        form = InfoForm()
        history = UserHistory.objects.filter(user = request.user).order_by('-created_at')[:10]
    return render(request, "gemni/forms.html", {'form': form, 'history':history})

def result(request):
    form_data = request.session.get('form_data')

    if form_data:
        ai_client = GoogleAIClient(api_key=api_key)
        response_text = generate_travel_suggestions(form_data, ai_client)
        formatted_response = format_response(response_text)

        if request.user.is_authenticated:
                UserHistory.objects.create(
                    user=request.user,
                    visitor_type=form_data["visitor_type"],
                    interest=form_data["interest"],
                    time=form_data["time"],
                    budget=form_data["budget"],
                    transport=form_data["transport"],
                    duration=form_data["duration"],
                    ai_suggestion=formatted_response,
                )

        return render(request, 'gemni/result.html', {
            'form_data': form_data,
            'response_text': formatted_response
        })
    else:
        return HttpResponse("No data found in session.")