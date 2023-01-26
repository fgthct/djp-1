"""
def my_decorator_func(func):
    def wrapper_func():
        # Do something before the function.
        func()
        # Do something after the function.
    return wrapper_func
"""

from django.shortcuts import redirect 

def user_not_authenticated(function=None, redirect_url='/'):
    """
    Decoratore per le viste che verifica che l'utente NON sia loggato, 
    reindirizzandolo alla home page se necessario per impostazione predefinita.
    Qui stiamo creando un decoratore per verificare se l'utente è 
    autenticato o meno. Useremo questo decoratore dove crediamo che 
    gli utenti che hanno effettuato l'accesso non dovrebbero essere 
    in grado di accedervi. Creiamo una funzione all'interno di una funzione 
    che chiamiamo decorator, e per accedere a una request Django, 
    creiamo ancora un'altra funzione specifica che chiamiamo " _wrapped_view". 
    Qui controlliamo se un utente è autenticato; se lo è, restituiamo una 
    funzione di reindirizzamento. In caso contrario, reindirizzeremo la 
    funzione originale a cui l'utente sta tentando di accedere.
    """
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_url)
                
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    if function:
        return decorator(function)

    return decorator