from django.shortcuts import render


def get_only_one_page(request):
    return render(
        request,
        template_name='grad_cong_page.html'
    )
