from django.shortcuts import render, redirect
from pytube import *

# Create your views here.
def app(request):
	if request.method == 'POST':
		url = request.POST['url']
		yt = YouTube(url)
		stream = yt.streams.get_lowest_resolution()
		thumbnail = yt.thumbnail_url
		stream.download()
		return render(request, 'app/app.html', context = {'thumbnail_img': thumbnail})
	return render(request, 'app/app.html')