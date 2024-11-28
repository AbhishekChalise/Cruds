from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from .forms import Main_User_Form  

# Create your views here.
def register(request):
    print("Request Method:", request.method)  # Debugging
    
    if request.method == "POST":
        form = Main_User_Form(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user to the database
            #login(request, user)  # Log the user in after successful registration
            print("User registered and logged in successfully")
            return redirect('register')  # Redirect to another page (URL name should match your `urls.py`)
        else:
            print("Form is not valid:", form.errors)  # Debugging invalid form
            #messages.error(request,'Values given are not correct!!!')
            return redirect('register')

    else:
        form = Main_User_Form()
    return render(request, 'registration.html', {'form': form})


