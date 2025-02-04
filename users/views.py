from django.shortcuts import render, get_object_or_404, reverse
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import UserProfileForm


# Create your views here.
@login_required
def user_profile(request, id):
    """
    Display an individual :model:`users.User`.

    **Context**
        ``profile_user``
            An instance of :model:`users.User`.
        ``user_profile_form``
            An instance of :form:`users.UserProfileForm`.
    
    **Template**
        :template:`users/profile.html`
    """
    if request.user.id != id:
        raise Http404("User does not have access to this page")
    
    profile_user = User.objects.get(pk=id)    

    user_profile_form = UserProfileForm(instance=profile_user)

    return render(
        request,
        'users/profile.html',
        {
            'profile_user': profile_user,
            'user_profile_form': user_profile_form,
        }
    )

@login_required
def user_update(request, id):
    """
    Update details for the given :model:`users.User` in the database

    If the request method is not POST or if the user submitting the change
    is not the owner of the profile, user receives a 404
    """
    
    if request.method == "POST":
        if request.user.id == id:
            profile_user = get_object_or_404(User, pk=id)
            user_profile_form = UserProfileForm(data=request.POST, instance=profile_user)

            if user_profile_form.is_valid():
                updated_user = user_profile_form.save()
                messages.add_message(
                    request, messages.SUCCESS, 'Profile updated'
                )
            else:
                messages.add_message(
                    request, messages.ERROR, 'Error updating profile'
                )
            
            return HttpResponseRedirect(reverse('profile', args=[id]))
        else:
            raise Http404("You don't have access to this page")
    else:
        raise Http404("Bad request")

@login_required
def user_delete(request, id):
    """
    Delete a user from the database.

    Ensures that the user submitting the action is the user to be deleted.
    Returns user to the home page with a message to notify success
    """

    profile_user = get_object_or_404(User, pk=id)
    if profile_user != request.user:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own account'
        )
        raise Http404("You don't have acces to this page")
    
    profile_user.delete()
    messages.add_message(
        request, messages.SUCCESS, "Account deleted"
    )

    return HttpResponseRedirect(reverse('home'))
