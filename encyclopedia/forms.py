from django import forms

# class SearchBarForm(forms.Form):
#     search = forms.CharField(max_length=30, label="Search",widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Search'}),strip=True,)

class NewPageForm(forms.Form):
    title = forms.CharField(max_length=30, required=True, label="Title",
    widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Title'}),strip=True,)
    content = forms.CharField(max_length=5000, required=True, label="Content",
    widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Page content'}), strip=True)
