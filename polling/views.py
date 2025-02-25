from django.shortcuts import render, get_object_or_404, redirect
from .models import Party, Vote
from .forms import VoteForm

def home(request):
    parties = Party.objects.all()
    return render(request, 'polling/home.html', {'parties': parties})

def party_detail(request, party_id):
    party = get_object_or_404(Party, id=party_id)
    return render(request, 'polling/party_detail.html', {'party': party})

def vote(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VoteForm()
    return render(request, 'polling/vote.html', {'form': form})

def results(request):
    parties = Party.objects.all()
    return render(request, 'polling/results.html', {'parties': parties})