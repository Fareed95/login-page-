from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import CustomUserCreationForm

@csrf_exempt
def api_register(request):
    if request.method == 'POST':
        print('Received POST request to api_register')

        # Assuming you're using a form for user registration
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            response_data = {'status': 'success', 'message': 'Registration successful!'}
        else:
            # Include form errors in the response data
            response_data = {'status': 'error', 'message': 'Registration failed. Please correct the errors.', 'errors': form.errors}
    else:
        response_data = {'status': 'error', 'message': 'Invalid request method.'}

    print('Sending response from api_register:', response_data)
    return JsonResponse(response_data)

@csrf_exempt
def api_login(request):
    if request.method == 'POST':
        print('Received POST request to api_login')

        # Get username and password from request data
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response_data = {'status': 'success', 'message': 'Login successful!'}
        else:
            response_data = {'status': 'error', 'message': 'Invalid username or password. Please try again.'}
    else:
        response_data = {'status': 'error', 'message': 'Invalid request method.'}

    print('Sending response from api_login:', response_data)
    return JsonResponse(response_data)

@login_required
@csrf_exempt
def api_welcome(request):
    if request.method == 'GET':
        print('Received GET request to api_welcome')

        # Your logic for handling the welcome endpoint
        response_data = {'status': 'success', 'message': 'Welcome!'}
        return render(request, 'welcome.html', context=response_data)
    else:
        response_data = {'status': 'error', 'message': 'Invalid request method.'}
        return JsonResponse(response_data)