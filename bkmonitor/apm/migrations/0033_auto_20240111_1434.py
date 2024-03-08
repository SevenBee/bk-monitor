# Generated by Django 3.2.15 on 2024-01-11 06:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apm", "0032_auto_20231017_1646"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProfileService",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("bk_biz_id", models.IntegerField(db_index=True, verbose_name="业务id")),
                ("app_name", models.CharField(db_index=True, max_length=255, verbose_name="应用名称")),
                ("name", models.CharField(db_index=True, max_length=528, verbose_name="服务名称")),
                ("period", models.CharField(max_length=128, null=True, verbose_name="采样周期")),
                ("period_type", models.CharField(max_length=128, null=True, verbose_name="周期类型")),
                ("frequency", models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name="采样频率")),
                ("data_type", models.CharField(max_length=128, null=True, verbose_name="数据类型")),
                ("last_check_time", models.DateTimeField(verbose_name="最近检查时间")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="创建时间")),
                ("updated_at", models.DateTimeField(auto_now=True, null=True, verbose_name="更新时间")),
            ],
            options={
                "verbose_name": "Profile服务实例表",
            },
        ),
        migrations.AddField(
            model_name="profiledatasource",
            name="retention",
            field=models.IntegerField(default=30, verbose_name="过期时间"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="normaltypevalueconfig",
            name="type",
            field=models.CharField(
                choices=[
                    ("metrics_batch_size", "每批Metric发送大小"),
                    ("traces_batch_size", "每批Trace发送大小"),
                    ("logs_batch_size", "每批Log发送大小"),
                    ("db_slow_command_config", "db慢命令配置"),
                    ("db_config", "db配置"),
                ],
                max_length=32,
                verbose_name="配置类型",
            ),
        ),
    ]
