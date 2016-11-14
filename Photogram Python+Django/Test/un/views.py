import datetime
from django.contrib.auth.models import User
from un.models import Album, Photo
from django.core.context_processors import csrf
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .forms import UploadFileForm

def handle_uploaded_file(f, name):
    with open('media/images/'+name+'.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def albums(request):
    return render_to_response('albums.html', {'albums': Album.objects.all(), 'username': auth.get_user(request).username})

def album(request, album_id=1):
    if request.method == 'POST':
        photo_form = UploadFileForm(request.POST, request.FILES)
        photoname = photo_form.data['name']
        photoname = photoname.replace('/', '')
        photoname = photoname.replace('\\', '')
        #photoname = ''.join(photoname.split())
        handle_uploaded_file(request.FILES['file'], photoname)
        path = "images/"+photoname+".jpg"
        usname = request.user.username
        alb = Album.objects.get(id=album_id)
        z=Photo(photo_album = Album.objects.get(album_name=alb.album_name), photo_date=datetime.datetime.now(), photo_name=photoname, photo_image=path, photo_user=User.objects.get(username=usname))
        z.save()
        return HttpResponseRedirect('/albums/get/'+album_id)
    else:
        photo_form =  UploadFileForm()
        args = {}
        args.update(csrf(request))
        args['album'] = Album.objects.get(id=album_id)
        args['photos'] = Photo.objects.filter(photo_album_id=album_id)
        args['form'] = photo_form
        args['username'] = auth.get_user(request).username
        return render_to_response('album.html', args)



