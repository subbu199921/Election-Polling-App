from django.db import models

class Party(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    logo = models.ImageField(upload_to='party_logos/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    reveal_date = models.DateTimeField()  # Date to reveal results

    def __str__(self):
        return self.name

    def total_votes(self):
        return self.vote_set.count()

    class Meta:
        verbose_name_plural = "Parties"


class Vote(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    voter_id = models.CharField(max_length=100, unique=True)
    voted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.voter_id} voted for {self.party.name}"

    class Meta:
        ordering = ['-voted_at']