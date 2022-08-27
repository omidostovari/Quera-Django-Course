from django.http import HttpResponse


def make_sad(request, name):
    final_str = f"Nobody likes you, {name}!"
    return HttpResponse(final_str)


def make_happy(request, name, times):
    the_str = f"You are great, {name} :)\n"
    final_str = ""
    for i in range(times):
        final_str += the_str
    return HttpResponse(final_str)
