from django import forms
from .models import Pizza, Topping


class CommentForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ["name"]
        label = {"Comment: ": ""}

        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
