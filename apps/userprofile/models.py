from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE, verbose_name=_('user'))
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('address'))
    zipcode = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('zipcode'))
    place = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('place'))
    phone = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('phone'))

    def __str__(self):
        return '%s' % self.user.username

User.userprofile = property(lambda u:Userprofile.objects.get_or_create(user=u)[0])