from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from gallery import forms
from gallery.models import Image


@login_required
def index(request):
    form = forms.FilesUploadForm()
    if request.method == "POST":
        form = forms.FilesUploadForm(request.POST, request.FILES)
        if form.is_valid:
            for uploaded_file in request.FILES.getlist("files"):
                # uploaded_file is of type UploadedFile
                if uploaded_file.content_type.startswith("image"):
                    image = Image.objects.create(user=request.user, file=uploaded_file)
    return render(request, "index.html", {"form": form})
