# Generated by Django 2.2.2 on 2022-03-16 18:26
import datetime
import os
import random
import shutil

from django.db import migrations


def init_manager(apps, args):
    Manager = apps.get_model('app', 'Manager')
    Manager(
        account="admin",
        pwd="123456",
        name="admin",
        gender=1,
        phone="15611112222",
    ).save()


def init_providers(apps, args):
    provider = apps.get_model('app', 'Provider')
    for i in range(3):
        p = provider()
        p.name = "供应商%d" % i
        p.address = "(%s)地球村中国镇3号" % p.name
        p.phone = "1551234567%d" % i
        p.save()


def init_goods(apps, args):
    category_map = {
        0: "零食饮料",
        1: "生鲜果蔬",
        2: "粮油副食",
        3: "清洁用品",
        4: "家居家电",
    }

    # 循环 /static/media/resources/goods/*
    current_path = os.path.dirname(os.path.abspath(__file__))
    current_path = current_path.replace("app\\migrations", "")
    resource_img_dir = "%s\\static\\media\\resources\\goods" % current_path
    upload_img_dir = "%s\\static\\media\\goods_img" % current_path
    files = [f for f in os.listdir(resource_img_dir) if os.path.isfile(os.path.join(resource_img_dir, f))]
    print(files)

    # 复制+改名 成 /static/media/goods_img/{category_num}_{good_id}.jpg
    date_now = datetime.datetime.utcnow()
    good = apps.get_model('app', 'Goods')
    record = apps.get_model('app', 'Record')
    for index, f in enumerate(files):
        category_id = random.randrange(0, 5)
        provider_id = random.randrange(1, 4)
        cost_price = random.randrange(5, 100)
        sale_price = cost_price + random.randrange(5, 20)

        produce_date = date_now - datetime.timedelta(days=(category_id + 1) * 365)
        limit_date = date_now + datetime.timedelta(days=(category_id + 1) * 365)
        purchase_date = produce_date + datetime.timedelta(days=cost_price)
        sale_date = purchase_date + datetime.timedelta(days=sale_price)

        # total = good.objects.count()
        # 随机造数据
        g = good(
            name=category_map[category_id] + str(index),
            sort=category_id,
            cost_price=float(cost_price),
            sale_price=float(sale_price),
            produce_date=produce_date,
            limit_date=limit_date,
            weight=float(sale_price + cost_price),
            provider_id=provider_id,
        )
        # g.id = total+1
        g.save()

        image_path = "%s\\%d_%d.png" % (upload_img_dir, category_id, g.id)
        shutil.copyfile("%s\\%s" % (resource_img_dir, f), image_path)

        location_id = random.randrange(0, 8)
        record(
            location=location_id,
            purchase_num=sale_price * cost_price,
            goods_id=g.id,
            date=purchase_date,
        ).save()
        record(
            location=location_id,
            goods_id=g.id,
            date=sale_date,
            sale_num=sale_price * cost_price / (location_id + 1),
        ).save()


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(init_providers),
        migrations.RunPython(init_goods),
        migrations.RunPython(init_manager),
    ]
