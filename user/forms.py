from django.contrib.auth.forms import UserCreationForm

class NewUser(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)