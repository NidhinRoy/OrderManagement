from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from order.models import Order
from .models import Order, CompletedOrders
def home(request):
    return render(request,'home.html')



def final(request):
    # Fetch all orders from the database
    orders = Order.objects.all()

    if request.method == 'POST':
        # Get order ID from the submitted form
        order_id = request.POST.get('order_id')
        # Fetch the specific order object
        order = Order.objects.get(id=order_id)

        # Create a new completed order with relevant data
        completed_order = CompletedOrders(
            customer_name=order.customer_name,
            model_no=order.model_no,
            copy=order.copy,
            date=order.date,
            franchise_name=order.franchise_name
        )
        # Save the completed order to the database
        completed_order.save()

        # Optionally, you can delete the order after saving to the completed orders
        # order.delete()  # Uncomment this line if you want to remove the order after proceeding

        # Redirect back to the same page or another page if needed
        return redirect('final')  # Assuming 'final' is the URL name of this view

    # Render the 'final.html' template and pass the orders context
    return render(request, 'final.html', {'orders': orders})



# def final(request):
#     # Fetch all orders from the database
#     orders = Order.objects.all()
#     # Render the 'final.html' template and pass the orders context
#     return render(request, 'final.html', {'orders': orders})




from django.shortcuts import render, redirect
from .models import CompletedOrders

def delivery(request):
    # Check if the form has been submitted
    if request.method == 'POST':
        # Retrieve the order ID from the submitted form
        order_id = request.POST.get('order_id')
        # Try to get the specific order and delete it
        try:
            order = CompletedOrders.objects.get(id=order_id)
            order.delete()
        except CompletedOrders.DoesNotExist:
            pass  # Handle the case where the order does not exist if needed

        # Redirect back to the delivery page after deletion
        return redirect('delivery')  # Replace 'delivery' with the correct URL name if different

    # Fetch all completed orders from the database
    completed_orders = CompletedOrders.objects.all()
    
    # Render the 'delivery.html' template and pass the completed orders to the context
    return render(request, 'delivery.html', {'completed_orders': completed_orders})


def order(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customerName')
        model_no = request.POST.get('modelNo')
        copy = request.POST.get('copy')
        date = request.POST.get('date')
        per_copy_rate = request.POST.get('perCopyRate')
        mob = request.POST.get('mob')
        franchise_name = request.POST.get('franchiseName')
        advance = request.POST.get('advance')
        balance = request.POST.get('balance')
        remarks = request.POST.get('remarks')
        order=Order.objects.create(customer_name=customer_name,
                                   model_no=model_no,
                                   copy=copy,
                                   date=date,
                                   per_copy_rate=per_copy_rate,
                                   mob=mob,
                                   franchise_name=franchise_name,
                                   advance=advance,
                                   balance=balance,
                                   remarks=remarks
                                   )
        order.save()
    return render(request,'order.html')

def index(request):
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials")
           
    return render(request,'index.html')

