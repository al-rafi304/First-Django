from django import forms
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404

from person.form import PersonForm, RawPersonForm

from .models import Person

# Create your views here.
def person_detail_dynamic_view(request, id):

    # Getting object and checking if it exist
    # Raise 404 error if not found
    obj = get_object_or_404(Person, id=id)

    # Another way of catching 404 error
    # try:
    #     obj = Person.objects.get(id=id)
    # except Person.DoesNotExist:
    #     raise Http404

    #Deleting object
    if request.method == "POST":
        obj.delete()
        return redirect('../../') #Redirects to previous page after deleting


    my_context = {
        'object': obj
    }

    return render(request, 'person/detail.html', my_context)


# Creating a form using froms.ModelForm
def person_create_view(request):

    #Getting values from the form
    #To update existing data, add another parameter 'instance'='reference of the object'
    my_form = PersonForm(request.POST or None)

    if my_form.is_valid():
        my_form.save()
        my_form = PersonForm()
        return redirect('../../')

    my_context = {
        'form': my_form
    }

    #
    
    return render(request, 'person/person_create.html', my_context)

def person_update_view(request, id):

    obj = get_object_or_404(Person, id=id)
    my_form = PersonForm(request.POST or None, instance=obj)
    if my_form.is_valid():
        my_form.save()
        return redirect(f'../..{obj.get_absolute_url()}')

    my_context = {
        'form': my_form,
        'object': obj
    }
    return render(request, 'person/person_update.html', my_context)

# ******** Creating a from using forms.Form ********

# def person_create_view(request):
#     my_form = RawPersonForm()

#     #Gets form data if request method in post
#     if request.method == 'POST':
#         my_form = RawPersonForm(request.POST)

#         #Saves data in database if data is valid
#         if my_form.is_valid():
#             data = my_form.cleaned_data
#             print(data)
#             Person.objects.create(**data)
    
#     my_context = {
#         'form': my_form
#     }
#     return render(request, 'person/person_create.html', my_context)