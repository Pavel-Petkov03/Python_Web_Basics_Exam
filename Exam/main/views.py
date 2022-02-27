from django.shortcuts import render, redirect
from django.views import View

from Exam.main.forms import CreateProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm
from Exam.main.models import Profile, Album


class HomePage(View):
    def get(self, req):
        if Profile.objects.exists():
            albums = Album.objects.all()
            return render(req, "home-with-profile.html", {
                "albums": albums
            })
        else:
            return render(req, "home-no-profile.html", {
                "form": CreateProfileForm()
            })

    def post(self, req):
        form = CreateProfileForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("home-page")
        return render(req, "home-no-profile.html", {
            "form": form
        })


class CreateAlbumView(View):
    def get(self, req):
        return render(req, "add-album.html", {
            "form": CreateAlbumForm()
        })

    def post(self, req):
        form = CreateAlbumForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("home-page")
        return render(req, "add-album.html", {
            "form": form
        })


class EditAlbumView(View):
    def get(self, req, pk):
        form = EditAlbumForm(instance=Album.objects.get(id=pk))
        return render(req, "edit-album.html", {
            "form": form,
        })

    def post(self, req, pk):
        form = EditAlbumForm(req.POST, instance=Album.objects.get(id=pk))
        if form.is_valid():
            form.save()
            return redirect("home-page")
        return render(req, "edit-album.html", {
            "form": form,
        })


class DeleteAlbumView(View):

    def get(self, req, pk):
        form = DeleteAlbumForm(instance=Album.objects.get(id=pk))
        return render(req, "delete-album.html", {
            "form": form,
        })

    def post(self, req, pk):
        Album.objects.get(id=pk).delete()
        return redirect("home-page")


class DetailsAlbumView(View):
    def get(self, req, pk):
        return render(req, "album-details.html", {
            "album": Album.objects.get(id=pk)
        })


class ProfileDetailsView(View):
    def get(self, req):
        return render(req, "profile-details.html", {
            "profile": Profile.objects.first(),
            "all_albums": Album.objects.all().__len__()
        })


class DeleteProfileView(View):
    def get(self, req):
        return render(req, "profile-delete.html")

    def post(self, req):
        Profile.objects.first().delete()
        Album.objects.all().delete()
        return redirect("home-page")
