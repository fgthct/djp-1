from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm, UserUpdateForm
from django.contrib import messages
from .decorators import user_not_authenticated

# Create your views here.
@user_not_authenticated
def register(request):
    '''Se l'utente è registrato non fa niente e va alla home page'''
    #if request.user.is_authenticated:
    #    return redirect('/')

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)    # fa login con i dati registrati in user
            messages.success(request, f"Nuovo account creato: {user.username}")
            return redirect('/')

        else:                       # se qualcosa va storto, stampa la lista degli errori
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:                           # se il form è GET mi propone il form vuoto
        form = UserRegistrationForm()

    return render(
        # un altro modo per rendere i dati nel template
        request=request,
        template_name = "accounts/register.html",
        context={"form": form}
    )

# le due viste custom, sovrascrivono le viste standard login e logout

@login_required
def custom_logout(request):
    '''Chiamo la funzione importata 'logout' che fa la magia '''
    logout(request)
    messages.info(request, "Sei stato disconnesso!")
    return redirect("home")


@user_not_authenticated
def custom_login(request):
    '''Se l'utente è autenticato non fa niente e va alla HomePage'''
    #if request.user.is_authenticated:
    #    return redirect('home')

    if request.method == 'POST':
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Bentornato <b>{user.username}</b>! Sei operativo!")
                return redirect('home')

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'Questo campo è obbligatorio.':
                    messages.error(request, "Devi passare il reCAPTCHA test")
                    continue
                messages.error(request, error) 

    # form = AuthenticationForm()
    form = UserLoginForm() 

    
    return render(
        request=request,
        template_name="accounts/login.html", 
        context={'form': form}
        )

def profile(request, username):
    if request.method == 'POST':
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()

            messages.success(request, f'{user_form}, Il tuo profilo è stato aggiornato')
            return redirect('profile', user_form.username)
        for error in list(form.errors.values()):
            messages.error(request, error)

    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        form.fields['description'].widget.attrs = {'rows': 1}
        return render(request, 'accounts/profile.html', context={'form': form})

    return redirect('home')


def home(request):
    return render(request, 'home.html')
    # return HttpResponse('HomePage')


    
