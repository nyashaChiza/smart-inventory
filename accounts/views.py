from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, CustomUserUpdateForm
from django.contrib.auth.views import PasswordResetView
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password

from django.urls import reverse
from django.views.generic.edit import UpdateView
from .forms import LoginForm


class LoginUserView(FormView):
    template_name = "registration/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            messages.success(
                self.request, f"You have successfully logged in as: {user.username}"
            )
            return super().form_valid(form)
        else:
            messages.warning(
                self.request, "Please check your credentials and try again"
            )
            return redirect("login")

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)


class UserListView(ListView):
    model = User
    template_name = "registration/index.html"


def register_user(request):
    if request.method == "GET":
        return render(
            request, "registration/create.html", {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, ("User created successfully"))
        return redirect("users-index")
    else:
        messages.success(request, ("Something went wrong please try again"))
        return redirect("register-user")


class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    template_name = "registration/update.html"
    form_class = CustomUserUpdateForm
    success_message = "User updated successfully"

    def get_success_url(self):
        return reverse("users-index")

    def form_valid(self, form):
        # Encrypt the password before saving
        password = form.cleaned_data.get("password")
        if password:
            form.instance.password = make_password(password)

        response = super().form_valid(form)
        return response


class UserDeleteView(DeleteView):
    model = User
    success_message = "User deleted successfully"

    def get_success_url(self):
        return reverse("users-index")


# Custom email reset


class CustomPasswordResetView(PasswordResetView):
    email_template_name = "account/password_reset_email.html"
    html_email_template_name = "account/password_reset_email.html"

    def send_mail(
        self,
        subject_template_name,
        email_template_name,
        context,
        from_email,
        to_email,
        html_email_template_name=None,
    ):
        html_email = render_to_string(html_email_template_name, context)
        email_message = EmailMessage(
            subject_template_name,
            html_email,
            from_email,
            [to_email],
        )

        email_message.content_subtype = "html"
        email_message.send()


def logout_view(request):
    # Use the logout() function to log the user out

    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")