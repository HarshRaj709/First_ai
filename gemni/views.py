from django.shortcuts import render, redirect, HttpResponse
from .forms import InfoForm
from .ai_client import GoogleAIClient
from .services import generate_travel_suggestions, format_response
from ai.settings import api_key

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
    return render(request, "gemni/forms.html", {'form': form})

def result(request):
    form_data = request.session.get('form_data')

    if form_data:
        # Dependency Injection
        ai_client = GoogleAIClient(api_key=api_key)
        response_text = generate_travel_suggestions(form_data, ai_client)
        formatted_response = format_response(response_text)
        return render(request, 'gemni/result.html', {
            'form_data': form_data,
            'response_text': formatted_response
        })
    else:
        return HttpResponse("No data found in session.")