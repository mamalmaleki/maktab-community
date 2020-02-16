from django.db import models
from django.utils.translation import ugettext_lazy as _


class Term(models.Model):
    title = models.CharField(max_length=250)
    code = models.CharField(max_length=50, blank=True)
    short_title = models.CharField(max_length=50, blank=True)

    department = models.ForeignKey(
        "departments.Department",
        verbose_name=_("department"),
        on_delete=models.CASCADE
    )


class Course(models.Model):
    title = models.CharField(max_length=250)
    code = models.CharField(max_length=50, blank=True)
    daily_length = models.TimeField()
    no_of_days = models.IntegerField()
    description = models.TextField(blank=True)
    prerequisites = models.TextField(blank=True)

    department = models.ForeignKey(
        "departments.Department",
        verbose_name=_("department"),
        on_delete=models.CASCADE
    )

    def __str__(self):
        result = self.title
        if self.code is not None:
            result += f' ({self.code})'
        return result


class SelectedCourse(models.Model):
    code = models.CharField(max_length=50, blank=True)
    term = models.ForeignKey(
        "departments.Term",
        verbose_name=_("term"),
        on_delete=models.CASCADE)

    cousre = models.ForeignKey(
        "departments.Course",
        verbose_name=_("course"),
        on_delete=models.CASCADE)

    instructors = models.ManyToManyField(
        "instructors.Instructor",
        verbose_name=_("instructors"))

    class Meta:
        verbose_name = _("Selected Course")
        verbose_name_plural = _("Selected Courses")

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class Room(models.Model):
    code = models.CharField(max_length=50)
    address = models.TextField(blank=True)

    department = models.ForeignKey(
        "departments.Department",
        verbose_name=_("department"),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.code


class Department(models.Model):
    title = models.CharField(max_length=250)
    code = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.title


class DaysOfWeek(models.IntegerChoices):
    SATURDAY = 0, _('Saturday')
    SUNDAY = 1, _('Sunday')
    MONDAY = 2, _('Monday')
    TUESDAY = 3, _('Tuesday')
    WEDNESDAY = 4, _('Wednesday')
    THURSDAY = 5, _('Thursday')
    FRIDAY = 6, _('Friday')

    __empty__ = _('(Unknown)')


class TimeSpans(models.Model):
    day_of_week = models.IntegerField(choices=DaysOfWeek.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        abstract = True


class DepartmentPeriod(TimeSpans):
    department = models.ForeignKey(
        "departments.Department",
        verbose_name=_("department"),
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _("Department Period")
        verbose_name_plural = _("Department Periods")


class Schedule(models.Model):
    department_period = models.ManyToManyField(
        "departments.DepartmentPeriod",
        verbose_name=_("department period")
    )

    selected_course = models.ForeignKey(
        "departments.Course",
        verbose_name=_("course"),
        on_delete=models.CASCADE)

    room = models.ForeignKey(
        "departments.Room",
        verbose_name=_("room"),
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ['selected_course', 'room']
