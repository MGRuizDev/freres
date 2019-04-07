from django.db.models import Q
from django.shortcuts import render
from .models import Wine

# Create your views here.
def home(request):
    context={}
    return render(request, 'wineList/home.html', context)

def grapes(request, slug):
    wine =["Cabernet is king in the U.S. and in many other parts of the world. We crave its bold tannins and fruit and it certainly pairs well with many of the dishes we as Americans love: including beef But Cabernet Savignon has a softer side, and goes well with some cheeses and even lavender.", "cabernet.jpg",
         "Merlot is a dark blue-colored wine grape variety, that is used as both a blending grape and for varietal wines. The name Merlot is thought to be a diminutive of merle, the French name for the blackbird, probably a reference to the color of the grape. Its softness, combined with its earlier ripening, makes Merlot a popular grape for blending with the sterner, later-ripening Cabernet Sauvignon, which tends to be higher in tannin", "merlot.jpg",
         "Pinot noir is a red wine grape variety of the species Vitis vinifera. The name may also refer to wines created predominantly from pinot noir grapes. The name is derived from the French words for pine and black. The word pine alludes to the grape variety having tightly clustered, pine cone-shaped bunches of fruit.", "pinot_noir.jpg",
         "Sauvignon blanc is a green-skinned grape variety that originates from the Bordeaux region of France. The grape most likely gets its name from the French words sauvage and blanc due to its early origins as an indigenous grape in South West France. It is possibly a descendant of Savagnin. Sauvignon blanc is planted in many of the world's wine regions, producing a crisp, dry, and refreshing white varietal wine. The grape is also a component of the famous desser wines from Sauternes and Barsac. Sauvignon blanc is widely cultivated in France, Chile, Romania, Canada, Australia, New Zealand, South Africa, the states of Washington and California in the US. Some New World Sauvignon blancs, particularly from California.", "sauvignon_blanc.jpg",
         "Chardonnay is a green-skinned grape variety used in the production of white wine. The variety originated in the Burgundy wine region of eastern France, but is now grown wherever wine is produced, from England to New Zealand. For new and developing wine regions, growing Chardonnay is seen as an easy entry into the international wine market.", "chardonay.jpg", ]
    if slug == 'cabernet':
        context={
            'definition': wine[0],
            'image': wine[1],
        }
    elif slug == 'merlot':
        context={
            'definition': wine[2],
            'image': wine[3],
        }
    elif slug == 'pinotNoir':
        context={
            'definition': wine[4],
            'image': wine[5],
        }
    elif slug == 'sauvignon':
        context={
            'definition': wine[6],
            'image': wine[7],
        }
    elif slug == 'chardonay':
        context={
            'definition': wine[8],
            'image': wine[9],
        }
    return render(request, 'wineList/grapes.html', context)

def about(request):
    context={}
    return render(request, 'wineList/about.html', context)

def contact(request):
    context={}
    return render(request, 'wineList/contact.html', context)

def store(request):
    list_all = Wine.objects.order_by('variety')
    red = list_all.filter( Q(variety='Agiorgitiko') | Q(variety='Aglianico') | Q(variety='Alicante Bouschet') | Q(variety='Alvarinho') | Q(variety='Aragonês') | Q(variety='Baga') | Q(variety='Barbera') | Q(variety='Blauburgunder') | Q(variety='Blaufränkisch') | Q(variety='Bordeaux-style Red Blend') | Q(variety='Cabernet Franc') | Q(variety='Cabernet Sauvignon') | Q(variety='Carignane') | Q(variety='Charbono') | Q(variety='Frappato') | Q(variety='Früburgunder') | Q(variety='G-S-M') | Q(variety='Gamay') | Q(variety='Grenache') | Q(variety='Grenache-Syrah') | Q(variety='Kekfrankos') | Q(variety='Lemberger') | Q(variety='Malbec') | Q(variety='Malbec-Cabernet') | Q(variety='Malbec-Merlot') | Q(variety='Mavrud') | Q(variety='Mencía') | Q(variety='Meritage') | Q(variety='Merlot') | Q(variety='Merlot-Malbec') | Q(variety='Monastrell') | Q(variety='Mourvèdre') | Q(variety='Nebbiolo') | Q(variety='Negrette') | Q(variety="Nero d'Avola") | Q(variety='Petit Verdot') | Q(variety='Petite Sirah') | Q(variety='Pinot Nero') | Q(variety='Pinot Noir') | Q(variety='Pinot Noir-Gamay') | Q(variety='Portuguese Red') | Q(variety='Primitivo') | Q(variety='Provence red blend') | Q(variety='Red Blend') | Q(variety='Rhône-style Red Blend') | Q(variety='Sangiovese') | Q(variety='Syrah') | Q(variety='Syrah-Grenache') | Q(variety='Tannat') | Q(variety='Tannat-Cabernet') | Q(variety='Tempranillo') | Q(variety='Tempranillo Blend') | Q(variety='Tinta de Toro') | Q(variety='Touriga Nacional') | Q(variety='Zinfandel') | Q(variety='St\. Laurent') )
    white = list_all.filter( Q(variety='Alsace white blend') | Q(variety='Assyrtiko') | Q(variety='Bordeaux-style White Blend') | Q(variety='Chardonnay') | Q(variety='Chasselas') | Q(variety='Chenin Blanc-Chardonnay') | Q(variety='Friulano') | Q(variety='Furmint') | Q(variety='Garganega') | Q(variety='Glera') | Q(variety='Godello') | Q(variety='Greco') | Q(variety='Gros Manseng') | Q(variety='Grüner Veltliner') | Q(variety='Malagouzia') | Q(variety='Malvasia Bianca') | Q(variety='Moscato') | Q(variety='Muscat') | Q(variety='Palomino') | Q(variety='Picpoul') | Q(variety='Pinot Bianco') | Q(variety='Pinot Blanc') | Q(variety='Pinot Grigio') | Q(variety='Pinot Gris') | Q(variety='Portuguese White') | Q(variety='Prié Blanc') | Q(variety='Rhône-style White Blend') | Q(variety='Ribolla Gialla') | Q(variety='Riesling') | Q(variety='Sauvignon') | Q(variety='Sauvignon Blanc') | Q(variety='Scheurebe') | Q(variety='Semillon-Sauvignon Blanc') | Q(variety='Silvaner') | Q(variety='Sylvaner') | Q(variety='Torrontés') | Q(variety='Ugni Blanc') | Q(variety='Ugni Blanc-Colombard') | Q(variety='Vermentino') | Q(variety='Viognier') | Q(variety='White Blend'))
    rose = list_all.filter( Q(variety='Gewürztraminer') | Q(variety='Portuguese Rosé') | Q(variety='Rosé'))
    sparkling = list_all.filter( variety='Sparkling Blend')
    fortified = list_all.filter( variety='Sherry')
    list_count = list_all.count()
    red_count = red.count()
    white_count = white.count()
    rose_count = rose.count()
    sparkling_count = sparkling.count()
    fortified_count = fortified.count()
    return render(request, 'wineList/store.html', context = {'list_all': list_all, 'list_count': list_count, 'red': red, 'white': white, 'rose': rose, 'sparkling': sparkling, 'fortified': fortified, 'red_count': red_count, 'white_count': white_count, 'rose_count': rose_count, 'sparkling_count': sparkling_count, 'fortified_count': fortified_count},)

def listWine(request, slug):
    list_all = Wine.objects.order_by('variety')
    red = list_all.filter( Q(variety='Agiorgitiko') | Q(variety='Aglianico') | Q(variety='Alicante Bouschet') | Q(variety='Alvarinho') | Q(variety='Aragonês') | Q(variety='Baga') | Q(variety='Barbera') | Q(variety='Blauburgunder') | Q(variety='Blaufränkisch') | Q(variety='Bordeaux-style Red Blend') | Q(variety='Cabernet Franc') | Q(variety='Cabernet Sauvignon') | Q(variety='Carignane') | Q(variety='Charbono') | Q(variety='Frappato') | Q(variety='Früburgunder') | Q(variety='G-S-M') | Q(variety='Gamay') | Q(variety='Grenache') | Q(variety='Grenache-Syrah') | Q(variety='Kekfrankos') | Q(variety='Lemberger') | Q(variety='Malbec') | Q(variety='Malbec-Cabernet') | Q(variety='Malbec-Merlot') | Q(variety='Mavrud') | Q(variety='Mencía') | Q(variety='Meritage') | Q(variety='Merlot') | Q(variety='Merlot-Malbec') | Q(variety='Monastrell') | Q(variety='Mourvèdre') | Q(variety='Nebbiolo') | Q(variety='Negrette') | Q(variety="Nero d'Avola") | Q(variety='Petit Verdot') | Q(variety='Petite Sirah') | Q(variety='Pinot Nero') | Q(variety='Pinot Noir') | Q(variety='Pinot Noir-Gamay') | Q(variety='Portuguese Red') | Q(variety='Primitivo') | Q(variety='Provence red blend') | Q(variety='Red Blend') | Q(variety='Rhône-style Red Blend') | Q(variety='Sangiovese') | Q(variety='Syrah') | Q(variety='Syrah-Grenache') | Q(variety='Tannat') | Q(variety='Tannat-Cabernet') | Q(variety='Tempranillo') | Q(variety='Tempranillo Blend') | Q(variety='Tinta de Toro') | Q(variety='Touriga Nacional') | Q(variety='Zinfandel') | Q(variety='St\. Laurent') )
    white = list_all.filter( Q(variety='Alsace white blend') | Q(variety='Assyrtiko') | Q(variety='Bordeaux-style White Blend') | Q(variety='Chardonnay') | Q(variety='Chasselas') | Q(variety='Chenin Blanc-Chardonnay') | Q(variety='Friulano') | Q(variety='Furmint') | Q(variety='Garganega') | Q(variety='Glera') | Q(variety='Godello') | Q(variety='Greco') | Q(variety='Gros Manseng') | Q(variety='Grüner Veltliner') | Q(variety='Malagouzia') | Q(variety='Malvasia Bianca') | Q(variety='Moscato') | Q(variety='Muscat') | Q(variety='Palomino') | Q(variety='Picpoul') | Q(variety='Pinot Bianco') | Q(variety='Pinot Blanc') | Q(variety='Pinot Grigio') | Q(variety='Pinot Gris') | Q(variety='Portuguese White') | Q(variety='Prié Blanc') | Q(variety='Rhône-style White Blend') | Q(variety='Ribolla Gialla') | Q(variety='Riesling') | Q(variety='Sauvignon') | Q(variety='Sauvignon Blanc') | Q(variety='Scheurebe') | Q(variety='Semillon-Sauvignon Blanc') | Q(variety='Silvaner') | Q(variety='Sylvaner') | Q(variety='Torrontés') | Q(variety='Ugni Blanc') | Q(variety='Ugni Blanc-Colombard') | Q(variety='Vermentino') | Q(variety='Viognier') | Q(variety='White Blend'))
    rose = list_all.filter( Q(variety='Gewürztraminer') | Q(variety='Portuguese Rosé') | Q(variety='Rosé'))
    sparkling = list_all.filter( variety='Sparkling Blend')
    fortified = list_all.filter( variety='Sherry')
    if slug == 'red':
        context={'wine': red, 'type': slug}
    elif slug == 'white':
        context={'wine': white, 'type': slug}
    elif slug == 'rose':
        context={'wine': rose, 'type': slug}
    elif slug == 'sparkling':
        context={'wine': sparkling, 'type': slug}
    elif slug == 'fortified':
        context={'wine': fortified, 'type': slug}
    return render(request, 'wineList/listWine.html', context,)
