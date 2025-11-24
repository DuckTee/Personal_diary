from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

class UserRegisterForm(forms.ModelForm):
    """
    Форма регистрации пользователя
    """

    password1 = forms.CharField(
        label=_("Пароль"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("Введите надёжный пароль (минимум 8 символов)."),
    )
    password2 = forms.CharField(
        label=_("Подтвердите пароль"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("Повторите пароль для подтверждения."),
    )

    class Meta:
        model = get_user_model()
        fields = ("email", "first_name", "last_name")
        widgets = {
            "email": forms.EmailInput(attrs={"placeholder": _("example@example.com")}),
        }
        labels = {
            "email": _("Email"),
            "first_name": _("Имя"),
            "last_name": _("Фамилия"),
        }

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        if password and len(password) < 8:
            raise forms.ValidationError(_("Пароль должен быть не менее 8 символов."))
        return password

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError(_("Этот email уже зарегистрирован."))
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Пароли не совпадают."))
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
