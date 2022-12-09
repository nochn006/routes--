from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect, HttpResponseNotFound, JsonResponse

def index(request):
    return HttpResponse("hello")

def login(request, login, password):
    return HttpResponse(f"""
    <p>Log in: {login}</p>
    <p>Password: {password}</p>
    """)

def posts(request):
    return HttpResponse('post')

def products(request):
    return HttpResponse("Products")

def new(request):
    return HttpResponse("new")

def top(request):
    return HttpResponse("top")

def products2(request, id=27):
    return HttpResponse(f"Товар: {id}")

def comments(request, id=27):
    return HttpResponse(f"Комментарии о товаре: {id}")

def likes(request, id=27, like=106):
    return HttpResponse(f"Поставлено лайков: {like} на товар: {id} ")

def about(requst):
    return HttpResponse("About")

def redirect_about(request):
    return HttpResponseRedirect("/about")

def permanent_redirect_about(request):
    return HttpResponsePermanentRedirect("/contacts")

def not_found(request):
    return HttpResponseNotFound("Ошибка", status=404)

def access(request, login, password):
    if login == "admin" and password == "admin":
        return HttpResponse("Все норм")
    return HttpResponse(f"""
    <p>Log in: {login}</p>
    <p>Password: {password}</p>
    """)

def json(request):
    return JsonResponse(request.GET)

def get(request):
    return HttpResponse(request.COOKIES[request.GET['key']])

def set(request):
    key = request.GET.get("key", "Undefined")
    value = request.GET.get("value", "Undefined")
    response = HttpResponse(f"Hello {key} : {value}")
    response.set_cookie(key, value)
    return response