from product.models import AboutITeam

def base_processor(request):
    if request.user.is_authenticated:
        about = AboutITeam.objects.last()
        return {'about': about}
    else:
        return {}
