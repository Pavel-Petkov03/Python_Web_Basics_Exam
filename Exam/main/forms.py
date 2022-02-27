from django import forms

from Exam.main.models import Profile, Album


class CreateProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['age'].widget.attrs['min'] = 0

    widgets = {
        "username": forms.TextInput(attrs={
            "type": "text", "name": "username", "id": "first_name",
            "placeholder": "Username"
        }),
        "email": forms.EmailInput(attrs={
            "type": "text", "name": "email", "id": "email",
            "placeholder": "Email"
        }),

        "age": forms.NumberInput(attrs={
            "type": "number", "name": "age", "id": "age",
            "placeholder": "Age", "min": "0"
        })
    }

    labels = {
        "username": "Username:",
        "email": "Email:",
        "age": "Age:"
    }

    class Meta:
        model = Profile
        fields = ("username", "email", "age")


class CreateAlbumForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['price'].widget.attrs['min'] = 0

    class Meta:
        model = Album
        fields = "__all__"

    widgets = {
        "name": forms.TextInput(attrs={
            "type": "text", "name": "name", "required": True,
            "placeholder": "Album Name"
        }),
        "artist": forms.TextInput(attrs={
            "type": "text", "id": "artist",
            "placeholder": "Artist", "required": True
        }),

        "genre": forms.TextInput(attrs={
            "name": "genre", "id": "genre",
        }),
        "description": forms.Textarea(attrs={
            "name": "genre", "id": "description", "Description": "Album Name"
        }),
        "image_url": forms.URLInput(attrs={
            "type": "url", "placeholder": "Image URL", "required": True, "id": "imgUrl"
        }),
        "price": forms.NumberInput(attrs={
            "id": "price", "type": "number", "placeholder": "price", "required": True, "min": "0"
        })
    }

    labels = {
        "name": "Artist:",
        "genre": "Genre:",
        "description": "Description:",
        "image_url": "Image URL:",
        "price": "Price:"
    }


class EditAlbumForm(CreateAlbumForm):
    pass


class DeleteAlbumForm(CreateAlbumForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_fields()

    def disable_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs["disabled"] = True
            field.widget.attrs["readonly"] = True
