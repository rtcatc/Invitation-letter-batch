#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
    邀请函图片批量生成脚本 V1.0
    作者: Poc Sir    网站: www.hackinn.com
    环境: Python2.X 需安装"pillow"包
    本程序支持缺省模式，原始图片：o.png 名单：invite-list.txt
    font目录下为自带字体，其他请自行选择，注意版权
"""
from PIL import Image, ImageDraw, ImageFont
import os,time


def draw_image(new_img, text, font, font_size, x, y, color):
    text = str(text)
    draw = ImageDraw.Draw(new_img)
    img_size = new_img.size
    try:
        fnt = ImageFont.truetype(font, font_size)
        fnt_size = fnt.getsize(unicode(text,'UTF-8'))
    except:
        print "字体不存在请检查！"
        exit()
    if x == "d":
        x1 = (img_size[0] - fnt_size[0]) / 2
        y1 = (img_size[1] - fnt_size[1]) / 2
    else:
        try:
            x1 = int(x)
            y1 = int(y)
        except:
            print "文字坐标轴输入不正确请检查！"
            exit()
    try:
        draw.text((x1, y1), unicode(text,'UTF-8'), font=fnt, fill=color)
        print TellTime() + text + "的邀请函生成成功！"
    except:
        print TellTime() + text + "的邀请函生成失败请检查！"
    del draw

def new_image(text, name, pic, font, font_size, x, y, color):
    try:
        new_img = Image.open(pic)
    except:
        print "原始图片打开失败请检查！"
    draw_image(new_img, text, font, font_size, x, y, color)
    new_img.save(r'pic/%s-%s.png' % (text, name))
    del new_img

def new_image_with_file(list,name,pic):
    try:
        with open(list) as f:
            font = raw_input("请输入字体文件路径（可留空）:")
            if len(font) == 0:
                font = "font/arial.ttf"
            font_size = int(raw_input("请输入字体大小:"))
            x = raw_input("请输入文字X坐标（留空默认居中）:")
            if len(x) == 0:
                x = "d"
                y = "d"
            else:
                y = raw_input("请输入文字Y坐标:")
            color = raw_input("请输入文字颜色（例如#FFFFFF或red）:")
            for l in f:
                l = l.strip()
                if l:
                    new_image(l, name, pic, font, font_size, x, y, color)
    except IOError:
        print "邀请人名单不存在请检查！"
    except ValueError:
        print "字体大小输入错误请检查！"

def default_file(file):
    file_path = os.getcwd() + os.sep + file
    if os.path.exists(file_path) == True:
        return True

def TellTime():
    localtime = "[" + str(time.strftime('%H:%M:%S',time.localtime(time.time()))) + "] "
    return localtime

if '__main__' == __name__:
    print "+------------------------------------------------------------+"
    print "|欢迎使用邀请函图片批量生成脚本  Coucou, Je Suis Poc-Sir!    |"
    print "|本程序支持缺省模式，若程序目录下存在对应文件则自动使用      |"
    print "|默认缺省原始图片为：o.png  缺省名单：invite-list.txt        |"
    print "|默认字体为font文件夹下arial.ttf字体，请注意商用版权！       |"
    print "|邀请人名单文件内邀请人一行一个分开即可，支持中文            |"
    print "|最终生成格式为\"邀请人-邀请函名称.扩展名\"，在pic目录下       |"
    print "+------------------------------------------------------------+\n"
    if default_file("o.png") == True:
        print TellTime() + "原始图片文件存在自动缺省"
        pic = "o.png"
    else:
        pic = raw_input("请输入原始图片路径:")
    if default_file("invite-list.txt") == True:
        list = "invite-list.txt"
        print TellTime() + "邀请人名单存在自动缺省"
    else:
        list = raw_input("请输入邀请人名单路径:")
    name = raw_input("请输入邀请函名称（留空为“邀请函”）:")
    if len(name) == 0:
        name = "邀请函"
    new_image_with_file(list,name,pic)
