from django import forms


class FilesUploadForm(forms.Form):
    files = forms.FileField(
        required=True, widget=forms.ClearableFileInput(attrs={"multiple": True})
    )
