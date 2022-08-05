from django.shortcuts import render

from django.http import HttpResponse

class Finch:
    def __init__(self, commonName, species, description, iocSequence):
        self.commonName = commonName
        self.species = species
        self.description = description
        self.iocSequence = iocSequence

finches = [
    Finch('Common chaffinch', 'Fringilla coelebs', 'Common and widespread bird in the finch family.', 1),
    Finch('Brambling', 'Fringilla montifringilla', 'Also known as the "cock of the north".', 4),
    Finch('Pine grosbeak', 'Pinicola enucleator', 'Found in coniferous woods, name translating directly to "bird that lives in the pines and shells the seeds".', 14),
    Finch('Scarlet finch', 'Carpodacus sipahi', 'Found in hte Himalayas and across Nepal stretching as far south as Thailand.', 38),
    Finch('Palila', 'Loxioides bailleui', 'Critically endangered. Golden-yellow head and breast with a light belly, gray back, and greenish wings and tail.', 72),
]
# Define the home view
def home(request):
    return HttpResponse('<h1>Welcome to the Finch Collection!</h1>')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', { 'finches': finches })
