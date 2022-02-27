from django.urls import path

from Exam.main.views import HomePage, CreateAlbumView, DeleteAlbumView, EditAlbumView, DetailsAlbumView, \
    ProfileDetailsView, DeleteProfileView

urlpatterns = [
    path("", HomePage.as_view(), name="home-page"),
    path("album/add", CreateAlbumView.as_view(), name="create-album"),
    path("album/delete/<int:pk>", DeleteAlbumView.as_view(), name="delete-album"),
    path("album/edit/<int:pk>", EditAlbumView.as_view(), name="edit-album"),
    path("album/details/<int:pk>", DetailsAlbumView.as_view(), name="album-details"),
    path("profile/details", ProfileDetailsView.as_view(), name="profile-details"),
    path("profile/delete", DeleteProfileView.as_view(), name="profile-delete"),
]
