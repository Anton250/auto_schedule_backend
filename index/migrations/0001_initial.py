# Generated by Django 2.0.5 on 2020-02-27 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('prof_type', models.CharField(choices=[('S', 'Обычная'), ('C', 'Компьютерная'), ('D', 'Дизайн'), ('L', 'Лаборатория'), ('M', 'Мастерская')], default='S', max_length=1)),
                ('need_projector', models.BooleanField(default=False)),
                ('need_big_blackboard', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='EducationPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('L', 'Лекция'), ('P', 'Практика'), ('LB', 'Лаб. работа')], default='L', max_length=2)),
                ('hours', models.IntegerField()),
                ('constraints', models.TextField(null=True)),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='index.Discipline')),
            ],
        ),
        migrations.CreateModel(
            name='Flow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=7)),
                ('count_of_students', models.IntegerField()),
                ('constraints', models.TextField(default='{"MO": [true, true, true, true, true, true, true], "TU": [true, true, true, true, true, true, true], "WE": [true, true, true, true, true, true, true], "TH": [true, true, true, true, true, true, true], "FR": [true, true, true, true, true, true, true], "SA": [true, true, true, true, true, true, true]}')),
                ('flow', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='index.Flow')),
            ],
        ),
        migrations.CreateModel(
            name='LectureHall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spaciousness', models.IntegerField()),
                ('code', models.CharField(max_length=10)),
                ('building', models.CharField(choices=[('V', 'ул. Павла Корчагина'), ('A', 'ул. Автозаводская'), ('E', 'ул. Большая Семеновская'), ('P', 'ул. Прянишникова'), ('S', 'ул. Садовая-Спасская')], default='E', max_length=1)),
                ('prof_type', models.CharField(choices=[('S', 'Обычная'), ('C', 'Компьютерная'), ('D', 'Дизайн'), ('L', 'Лаборатория'), ('M', 'Мастерская')], default='S', max_length=1)),
                ('has_projector', models.BooleanField(default=False)),
                ('has_big_blackboard', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.IntegerField(choices=[(1, 'Первая пара'), (2, 'Вторая пара'), (3, 'Третья пара'), (4, 'Четвёртая пара'), (5, 'Пятая пара'), (6, 'Шестая пара'), (7, 'Седьмая пара')], default=1)),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='index.EducationPlan')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='index.Group')),
                ('lecture_hall', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='index.LectureHall')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('constraints', models.TextField(default='{"buildings_priority": ["E", "A", "V", "S", "P"], "day_constraints": {"MO": [true, true, true, true, true, true, true], "TU": [true, true, true, true, true, true, true], "WE": [true, true, true, true, true, true, true], "TH": [true, true, true, true, true, true, true], "FR": [true, true, true, true, true, true, true], "SA": [true, true, true, true, true, true, true]}}')),
                ('total_hours', models.IntegerField()),
                ('disciplines', models.ManyToManyField(to='index.Discipline')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingDirection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('B', 'Бакалавриат'), ('S', 'Специалитет'), ('M', 'Магистратура')], default='B', max_length=1)),
                ('constraints', models.TextField(default='["E", "A", "P", "V", "S"]', verbose_name='Ограничения направления')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='index.Teacher'),
        ),
        migrations.AddField(
            model_name='group',
            name='training_direction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='index.TrainingDirection'),
        ),
        migrations.AddField(
            model_name='educationplan',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='index.Group'),
        ),
    ]
