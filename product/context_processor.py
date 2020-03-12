from .models import Brand, Category, AboutITeam

def header_processor(request):
    if request.user.is_authenticated:
        categories = Category.objects.all()
        brands = Brand.objects.all()
        about = AboutITeam.objects.last()
        context = {
            'menu_brands': brands,
            'menu_categories': categories,
            'about': about
        }
    else:
        categories = Category.objects.all()
        brands = Brand.objects.all()
        about = AboutITeam.objects.last()
        context = {
            'menu_brands': brands,
            'menu_categories': categories,
            'about': about
        }
    return context
