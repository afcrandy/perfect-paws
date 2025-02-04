from django.shortcuts import render, get_object_or_404, reverse
from .models import User
from .forms import UserProfileForm
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def user_profile(request, id):
    """
    Display an individual :model:`users.User`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comments``
        All approved comments related to the post.
    ``comment_count``
        A count of approved comments related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`.
    
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

    **Context**
    ``post``
        An instance of :model:`blog.Post`
    ``comment``
        A single comment related to the post
    ``comment_form``
        An instance of :form:`blog.CommentForm`
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
    Delete an user

    **Context**
    ``post``
        An instance of :model:`blog.Post`
    ``comment``
        A single comment related to the post
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
