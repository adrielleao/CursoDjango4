from django.shortcuts import render

# Create your views here.
def example_view(request):
    # my_app/templates/my_app/example.html
    return render(request, 'my_app/example.html')

def variable_view(request):
    # my_app/templates/my_app/variable.html

    my_var ={'first_name':'RosaLind', 'last_name':'Franklin',
             'some_list':[1,2,3], 'user_logged_in':False,'some_dict':{'inside_key':'inside_var'}}

    return render(request, 'my_app/variable.html', context=my_var)