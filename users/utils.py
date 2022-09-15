from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def _create_user(
        self,
        full_name,
        email,
        password,
        profile_picture,
        **extra_fields,
    ):
        email = self.normalize_email(email)

        user = self.model(
            full_name=full_name,
            email=email,
            profile_picture=profile_picture,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self, full_name, email, password, profile_picture, **extra_fields
    ):
        return self._create_user(
            full_name,
            email,
            password,
            profile_picture,
            **extra_fields,
        )
