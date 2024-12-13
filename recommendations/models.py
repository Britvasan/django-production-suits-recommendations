from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import RegexValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils import timezone

# Custom User Model
class ClientUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="clientuser_groups",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="clientuser_permissions",
        blank=True,
    )

    def __str__(self):
        return self.username


# Model for Client Order Data
class Clientdata(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100, blank=False, null=False)
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Enter a valid phone number")],
        blank=False, null=False
    )
    email = models.EmailField(max_length=50, blank=False, null=False)
    orders = models.CharField(max_length=100, blank=False, null=False)  # Example: "fireman suit"
    order_type = models.CharField(max_length=100, blank=False, null=False)  # Example: "asbestos"
    customization = models.CharField(max_length=50, blank=True, null=True)  # Example: "fire-proof"
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        default=1
    )  # Example: 2
    pickup_date = models.DateField(blank=True, null=True)  # Example: "2024-10-26"
    status = models.CharField(max_length=50, default="pending", blank=False, null=False)  # Example: "in_progress"
    recommended_product = models.CharField(max_length=100, null=True, blank=True)  # Predicted product name, e.g., "ABC suits"


    def clean(self):
        if self.pickup_date and self.pickup_date < timezone.now().date():
            raise ValidationError("Pickup date cannot be in the past.")
        
    def __str__(self):
        return f"Order for {self.client_name} - {self.orders} ({self.order_type})"

from django.db import models

class RecommendationData(models.Model):
    orders = models.CharField(max_length=255)
    order_type = models.CharField(max_length=255)
    customization = models.CharField(max_length=255)
    recommended_product = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.orders} - {self.recommended_product}'








# from django.db import models
# from django.contrib.auth.models import AbstractUser, Group, Permission
# from django.core.validators import MinValueValidator, RegexValidator
# from django.core.exceptions import ValidationError
# from django.conf import settings
# from django.utils import timezone

# # Custom User Model
# class ClientUser(AbstractUser):
#     # Additional fields can be added here if necessary
#     groups = models.ManyToManyField(
#         Group,
#         related_name="clientuser_groups",
#         blank=True,
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         related_name="clientuser_permissions",
#         blank=True,
#     )

# # Create your models here.
# from django.db import models
# from django.core.validators import RegexValidator, MinValueValidator
# from django.conf import settings
# from django.utils import timezone
# from django.core.exceptions import ValidationError

# class Clientdata(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
#     client_name = models.CharField(max_length=100, blank=False, null=True)  # Stores names like "Arun"
#     phone_number = models.CharField(
#         max_length=15,
#         validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')],
#         blank=False, null=False
#     )
#     email = models.EmailField(max_length=50, blank=False, null=False)
#     order = models.CharField(max_length=100, blank=False, null=False)  # Example: "fireman suit"
#     order_type = models.CharField(max_length=100, blank=False, null=False)  # Example: "asbestos"
#     customization = models.CharField(max_length=50, blank=True, null=True)  # Example: "fire-proof"
#     quantity = models.PositiveIntegerField(
#         validators=[MinValueValidator(1)],
#         default=1
#     )  # Example: 2
#     pickup_date = models.DateField(blank=True, null=True)  # Example: "2024-10-26"
#     status = models.CharField(max_length=50, default="pending", blank=False, null=False)  # Example: "in_progress"

#     def clean(self):
#         if self.pickup_date and self.pickup_date < timezone.now().date():
#             raise ValidationError("Pickup date cannot be in the past.")

#     def __str__(self):
#         return f"{self.client_name} ({self.user.username})"

