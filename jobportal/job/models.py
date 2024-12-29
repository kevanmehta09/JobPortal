from django.db import models
from django.contrib.auth.models import AbstractUser


#CustomUserModel
class CustomUser(AbstractUser):
    contact_number = models.CharField(max_length=10)

    groups = models.ManyToManyField(
        'auth.Group', related_name='customuser_set', blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='customuser_permissions_set', blank=True
    )

    def __str__(self):
        return self.username

# CompanyModel
class Company(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='company')
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name

# Job Model
class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=255)
    description = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.CharField(max_length=255, blank=True, help_text="Comma-separated tags")

    def get_tags(self):
        # Return the tags as a list (splitting by commas)
        return [tag.strip() for tag in self.tags.split(',')] if self.tags else []

    def set_tags(self, tag_list):
        # Set tags by passing a list of tags
        self.tags = ', '.join(tag_list)

    def __str__(self):
        return self.title
