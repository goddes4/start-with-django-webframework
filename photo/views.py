from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from photo.forms import PhotoEditForm


def single_photo(request, photo_id):

    photo = get_object_or_404(Photo, pk=photo_id)
    return HttpResponse('{}번 사진을 보여주세요.<img src="{}"/>'.format(photo_id, photo.image_file.url))


def new_photo(request):
    if request.method == 'GET':
        edit_form = PhotoEditForm()
    elif request.method == 'POST':
        edit_form = PhotoEditForm(request.POST, request.FILES)

        if edit_form.is_valid():
            new_photo = edit_form.save()

            return redirect(new_photo.get_absolute_url())

    return render(request, 'new_photo.html', {'form': edit_form})