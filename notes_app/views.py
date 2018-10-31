from django.shortcuts import render
from .forms import note_form
import 



def post_list(request):
    games = get_games()
    return render(request, 'notes/post_list.html',  {'games': games})


                
        
