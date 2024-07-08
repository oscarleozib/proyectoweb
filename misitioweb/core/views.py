from urllib import request
from django.shortcuts import render, HttpResponse

# Create your views here.
# def home(request):
#     return HttpResponse("<h1>Mi Mi sitio web</h1><h2>Portada</h2>")

# def about(request):
#     return HttpResponse("""
#         <h1>Mi Web Personal</h1>
#         <h2>Acerca de</h2>
#         <p>Me llamo OSKAR y esto es Django!</p>
#     """)

# html_base = """
#     <h1>Mi Web Personal</h1>
#     <ul>
#         <li><a href="/">Portada</a></li>
#         <li><a href="/about/">Acerca de</a></li>
#         <li><a href="/portfolio/">Portfolio</a></li>
#         <li><a href="/contact/">Contacto</a></li>
#     </ul>
# """

# def home(request):
#     return HttpResponse(html_base + """
#         <h2>Bienvenidos</h2>
#         <p>Esto es la portada.</p>
#     """)

# def about(request):
#     return HttpResponse("""
#         <h2>Acerca de</h2>
#         <p>Me llamo OSKAR y esto es Django</p>
#     """)

# def portfolio(request):
#     return HttpResponse("""
#         <h2>Portfolio</h2>
#         <p>Trabajo con ANGULAR y quiero aprender PYTHON</p>
#     """)

# def contact(request):
#     return HttpResponse("""
#         <h2>Contacto</h2>
#         <p>VIVO EN MADRID!!!!</p>
#     """)

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def portfolio(request):
    return render(request, "core/portfolio.html")
