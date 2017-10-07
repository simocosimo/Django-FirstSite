from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from merch.models import Merch


# Relationship codes/choices
RELATIONSHIP_FOLLOWING = 1
RELATIONSHIP_BLOCKED = 2
RELATIONSHIP_STATUS = (
    (RELATIONSHIP_FOLLOWING, 'Following'),
    (RELATIONSHIP_BLOCKED, 'Blocked'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    relationships = models.ManyToManyField('self', through='Relationship',
                                           symmetrical=False,
                                           related_name='related_to')

    def __str__(self):
        return self.user.get_username()

    # Relatationship functions
    def add_relationship(self, person, status):
        relationship, created = Relationship.objects.get_or_create(
            from_person=self,
            to_person=person,
            status=status)
        return relationship

    def remove_relationship(self, person, status):
        Relationship.objects.filter(
            from_person=self,
            to_person=person,
            status=status).delete()
        return

    def get_relationships(self, status):
        return self.relationships.filter(
            to_people__status=status,
            to_people__from_person=self)

    def get_related_to(self, status):
        return self.related_to.filter(
            from_people__status=status,
            from_people__to_person=self)

    def get_following(self):
        return self.get_relationships(RELATIONSHIP_FOLLOWING)

    def get_followers(self):
        return self.get_related_to(RELATIONSHIP_FOLLOWING)

    # Merch functions
    def add_merchPossession(self, m):
        MerchPossession.objects.get_or_create(
            user = self,
            merch = m)
        return

    def remove_merchPossession(self, m):
        MerchPossession.objects.filter(
            user = self,
            merch = m).delete()
        return

    def get_merchPossession(self):
        return MerchPossession.objects.filter(
            user=self)


# this triggers when a new user is created by User model
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# This update the profile field of the user when updated via User model
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Relationship(models.Model):
    from_person = models.ForeignKey(Profile, related_name='from_people')
    to_person = models.ForeignKey(Profile, related_name='to_people')
    status = models.IntegerField(choices=RELATIONSHIP_STATUS)
    rel_date = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return '%s now following %s' % (self.from_person.user.get_username(),
                                        self.to_person.user.get_username())


class MerchPossession(models.Model):
    user = models.ForeignKey(Profile, related_name='user_possessing')
    merch = models.ForeignKey(Merch, related_name='merch_possessed')
    linked_date = models.DateField(default=timezone.now, blank=False)

    def __str__(self):
        return '%s now possess %s' % (self.user.user.get_username(),
                                      self.merch.name)
