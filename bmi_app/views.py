from django.shortcuts import render


def bmi_view(request):
    context = {}
    if request.method == 'POST':
        try:
            gewicht = float(request.POST['gewicht'])
            lengte = float(request.POST['lengte'])
            lengte_m = lengte / 100
            bmi = gewicht / (lengte_m ** 2)

            if bmi < 18.5:
                categorie = 'Ondergewicht'
            elif bmi < 25:
                categorie = 'Normaal gewicht'
            elif bmi < 30:
                categorie = 'Overgewicht'
            else:
                categorie = 'Obesitas'

            context = {
                'bmi': round(bmi, 1),
                'categorie': categorie,
                'gewicht': gewicht,
                'lengte': lengte,
            }
        except (ValueError, ZeroDivisionError):
            context['fout'] = 'Voer geldige waarden in.'

    return render(request, 'bmi_app/index.html', context)
