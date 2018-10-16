from django.shortcuts import render
from .forms import note_form
from .database_functions import *



def post_list(request):
    if request.method == 'POST':
        form = note_form(request.POST)
        if form.is_valid():
            append_post(form.cleaned_data["name"],form.cleaned_data["text"])
    form = note_form()
    notes = get_all_posts()
    notes=notes_sorting(notes)
    print(notes)
    return render(request, 'notes/post_list.html',  {'form': form,'posts': notes})

def notes_sorting(notes):
    sorted=[]
    for note in notes:
        amount_of_unique_words_in_note_text=0
        note_text_words_list=note["text"].split()
        unique_words_list=[]
        for word in note_text_words_list:
            if word not in unique_words_list:
                amount_of_unique_words_in_note_text+=1
                unique_words_list.append(word)
        sorted.append([amount_of_unique_words_in_note_text,note])
    sorted.sort()
    for i in range(len(sorted)):
        sorted[i]=sorted[i][1]
    return sorted
        
                
        
