from django.shortcuts import render, redirect
from .models import Category, Photo


# Create your views here.
def gallery(request):
    category = request.GET.get('category')
    if category is None:
        photos = Photo.objects.all()

    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()

    return render(request, 'photos/gallery.html', {
        'categories': categories,
        'photos': photos,
    })


def view_photo(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {
        'photo': photo
    })


def add_photo(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None
        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image
            )

        return redirect('gallery')

    return render(request, 'photos/add.html',{
        'categories': categories
    })
