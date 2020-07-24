from django.db import models

# Create your models here.
class Projectmanager(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        permissions = (
            ("can_createtask", "can create task"),
            ("can_invite", "can invite project members"),
            ("can_removemember", "can remove members"),
            ("can_removetask", "can remove task"),
            ("can_deleteproject", "can delete project"),

        )

class project_member (models.Model):
    name = models.CharField(max_length=50)
    # project = models.ForeignKey(project)
    task_assigned = models.TextField()
    task_accepted = models.BooleanField()
    tasked_finished = models.BooleanField()

    class Meta:
        permissions = (
            ("can_mark", "can mark task as complete")
        )

class Task(models.Model):
    name = models.CharField()
    description = models.TextField()
    Assigned_to = models.ForeignKey(project_member)
    taken = models.BooleanField()
    taken_by = models.ForeignKey(project_member)
    finished = models.BooleanField()
    finished_by = models.ForeignKey(project_member)
    created_date = models.DateField()
    assigned_date =models.DateTimeField()
    deadline_date = models.DateTimeField()

class project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    project_manager = models.ForeignKey(Projectmanager)
    team_members = models.ManyToManyField(project_member)
    tasks = models.ManyToManyField(Task)
    start_date = models.DateField()
    end_date = models.DateField()
    github_link = models.URLField()

