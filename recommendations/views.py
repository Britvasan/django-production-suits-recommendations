from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Clientdata
from .forms import ClientdataForm
from .utils import train_recommendation_model, predict_recommended_product 
import pandas as pd

# Homepage view
def homepage(request):
    return render(request, "homepage.html")

# Client login view
def clientlogin(request):
    next_url = request.GET.get('next', '/index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next_url)
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "clientlogin.html")

# Logout view
def logout_view(request):
    logout(request)
    return redirect('clientlogin')

# Client data submission view
def index(request):
    if request.method == "POST":
        form = ClientdataForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.user = request.user 
            new_entry.save()
            return redirect("/result")
    else:
        form = ClientdataForm()
    return render(request, "index.html", {'form': form})

# Client list view
def client_list(request):
    clients = Clientdata.objects.filter(user=request.user)
    return render(request, 'cli_req.html', {'value': clients})

# View to update order status
def update_status(request, client_id):
    client = get_object_or_404(Clientdata, id=client_id)
    if request.method == 'POST':
        client.status = request.POST.get('status')
        client.save()
        return redirect('client_list')
    return render(request, 'update_status.html', {'client': client})

def delete_client(request, client_id):
    client = get_object_or_404(Clientdata, id=client_id)
    if request.method == 'POST':
        client.delete() 
        return redirect('client_list')  
    return render(request, 'delete_client.html', {'client': client})


def result_view(request):
    # Train the model
    model, encoders, accuracy = train_recommendation_model()

    # Get user input from form submission
    orders = request.POST.get("orders")
    order_type = request.POST.get("order_type")
    customization = request.POST.get("customization")

    print("Received orders:", orders)
    print("Received order_type:", order_type)
    print("Received customization:", customization)

    # Check for missing input
    if not orders or not order_type or not customization:
        recommended_product = "Please submit all order details."
    else:
        # Predict based on user input
        recommended_product = predict_recommended_product(model, encoders, orders, order_type, customization)

    return render(request, "result.html", {
        "accuracy": accuracy,
        "recommended_product": recommended_product
        
    })
    






