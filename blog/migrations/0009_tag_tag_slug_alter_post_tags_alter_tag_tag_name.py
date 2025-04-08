# Generated by Django 5.1.3 on 2025-04-07 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_post_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="tag",
            name="tag_slug",
            field=models.SlugField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(to="blog.tag"),
        ),
        migrations.AlterField(
            model_name="tag",
            name="tag_name",
            field=models.CharField(max_length=20),
        ),
    ]
