from typing import Any, Optional

from django.contrib import admin
from django.db.models import QuerySet
from django.utils import timezone

from ninjas import models


@admin.register(models.Village)
class VillageAdmin(admin.ModelAdmin[models.Village]):
    list_display = ("id", "name", "ninja_count")
    list_display_links = ("id", "name")

    @admin.display(description="Ninja Count")
    def ninja_count(self, instance: models.Village) -> int:
        return models.Ninja.objects.filter(
            cohorts__academy__village=instance,
            cohorts__end_at__gt=timezone.now().date(),
            graduated_at=None,
        ).count()


class CohortInlineAdmin(admin.TabularInline):
    model = models.Cohort
    extra = 1


@admin.register(models.Academy)
class AcademyAdmin(admin.ModelAdmin[models.Academy]):
    list_display = ("id", "village", "founded")
    list_display_links = ("id", "village")
    inlines = [CohortInlineAdmin]


@admin.register(models.Cohort)
class CohortAdmin(admin.ModelAdmin[models.Cohort]):
    list_display = ("id", "start_at", "end_at", "sensei_count", "ninja_count")
    list_display_links = ("id", "start_at", "end_at")
    list_filter = ("senseis__name",)

    @admin.display(description="Sensei Count")
    def sensei_count(self, obj: models.Cohort) -> int:
        return obj.senseis.all().count()

    @admin.display(description="Ninja Count")
    def ninja_count(self, obj: models.Cohort) -> int:
        return obj.ninjas.all().count()


@admin.register(models.Sensei)
class SenseiAdmin(admin.ModelAdmin[models.Sensei]):
    list_display = ("id", "name", "cohort_count")
    list_display_links = ("id", "name")

    @admin.display(description="Cohort Count")
    def cohort_count(self, obj: models.Sensei) -> int:
        return obj.cohorts.all().count()


class GraduatedListFilter(admin.SimpleListFilter):
    title: str = "has_graduated"
    parameter_name: str = "has_graduated"

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        return [(True, "Yes"), (False, "No")]

    def queryset(
        self, request: Any, queryset: QuerySet[models.Ninja]
    ) -> Optional[QuerySet[models.Ninja]]:
        value = self.value()
        if value is None:
            return queryset

        if value == "True":
            return queryset.exclude(graduated_at=None)

        return queryset.filter(graduated_at=None)


@admin.action(description="Mark selected ninjas as graduated")
def mark_as_graduated(
    modeladmin: admin.ModelAdmin[models.Ninja],
    request: Any,
    queryset: QuerySet[models.Ninja],
) -> None:
    queryset.update(graduated_at=timezone.now().date())


@admin.register(models.Ninja)
class NinjaAdmin(admin.ModelAdmin[models.Ninja]):
    list_display = ("id", "name", "graduated")
    list_display_links = ("id", "name")
    list_filter = (GraduatedListFilter,)
    actions = (mark_as_graduated,)

    @admin.display(description="Has Graduated", boolean=True)
    def graduated(self, obj: models.Ninja) -> bool:
        return bool(
            obj.graduated_at and obj.graduated_at <= timezone.now().date()
        )
