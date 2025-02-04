from django.shortcuts import render


# Create your views here.
def home(request):
    """
    Renders the home page of the site.
    
    **Template:**
        :template:`core/home.html`
    """
    return render(
        request,
        'core/home.html',
    )
