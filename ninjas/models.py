from django.db import models


class Village(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return str(self.name)


class Academy(models.Model):
    cover = models.ImageField()
    village = models.OneToOneField(
        "ninjas.Village", on_delete=models.CASCADE, related_name="academies"
    )
    curriculum = models.TextField(default="", blank=True)
    founded = models.DateField()

    def __str__(self) -> str:
        return f"{self.village}'s Ninja Academy"


class Cohort(models.Model):
    academy = models.ForeignKey(
        "ninjas.Academy", on_delete=models.CASCADE, related_name="cohorts"
    )
    start_at = models.DateField()
    end_at = models.DateField()

    def __str__(self) -> str:
        return f"{self.academy}'s Cohort"


class Sensei(models.Model):
    name = models.CharField(max_length=30)
    cohorts = models.ManyToManyField("ninjas.Cohort", related_name="senseis")

    def __str__(self) -> str:
        return str(self.name)


class Ninja(models.Model):
    name = models.CharField(max_length=30)
    cohorts = models.ManyToManyField("ninjas.Cohort", related_name="ninjas")
    graduated_at = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name)
