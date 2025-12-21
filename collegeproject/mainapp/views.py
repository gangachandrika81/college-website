

from django.shortcuts import render

def home(request):
    return render(request, 'mainapp/home.html')

def colleges(request):
    return render(request, 'mainapp/colleges.html')

def svecw1(request):
    return render(request, 'mainapp/svecw1.html')

def vit(request):
    return render(request, 'mainapp/vit.html')

def bvrit(request):
    return render(request, 'mainapp/bvrit.html')

def infrastructure(request):
    infra_list = [
        {'name': 'Library', 'image': 'mainapp/images/library.jpg'},
        {'name': 'Computer Lab', 'image': 'mainapp/images/computerlab.jpg'},
        {'name': 'Hostel', 'image': 'mainapp/images/hostel.webp'},
        {'name': 'Sports Ground', 'image': 'mainapp/images/sports.jpg'},
        {'name': 'temple', 'image': 'mainapp/images/temple.jpg'},
        {'name': 'mess', 'image': 'mainapp/images/mess.jpeg'},
    ]
    return render(request, 'mainapp/infrastructure.html', {'infra': infra_list})

def placements(request):
    place_list = [
        {'image': 'mainapp/images/place1.jpg'},
        {'image': 'mainapp/images/place2.jpg'},
        {'image': 'mainapp/images/place3.jpg'},
        {'image': 'mainapp/images/place4.jpg'},
        {'image': 'mainapp/images/place5.jpg'},
        {'image': 'mainapp/images/place6.jpg'},
    ]
    return render(request, 'mainapp/placements.html', {'place': place_list})
    

