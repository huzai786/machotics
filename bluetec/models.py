from django.db import models

#  SERVICE PAGE

class GetStarted(models.Model):
    name = models.CharField(max_length=200, null=False, blank=True)
    phone_no = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField()
    description = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Service page Get started Form (SERVICE PAGE)'
        verbose_name_plural = 'Service page Get started Form (SERVICE PAGE)'

class OurServiceFront(models.Model):
    heading = models.CharField(max_length=300, null=True, blank=True)
    sub_heading = models.CharField(max_length=300, null=True, blank=True)
    short_detail = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'Service page Front text (SERVICE PAGE)'
        verbose_name_plural = 'Service page Front text (SERVICE PAGE)'
    

class WhatDoWeOffer(models.Model):
    heading = models.CharField(max_length=300, null=True, blank=True)
    short_detail = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.heading


    class Meta:
        verbose_name = 'What do we offer text (SERVICE PAGE)'
        verbose_name_plural = 'What do we offer text (SERVICE PAGE)'
    

class ServiceCard(models.Model):
    card_heading = models.CharField(max_length=300, null=True, blank=True)
    card_pic = models.ImageField( null=True, blank=True)
    card_detail = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.card_heading

    class Meta:
        verbose_name = 'Service cards slide data (SERVICE PAGE)'
        verbose_name_plural = 'Service cards slide data (SERVICE PAGE)'

class HowDoWeWork(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    short_detail = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'How do we work (SERVICE PAGE)'
        verbose_name_plural = 'How do we work (SERVICE PAGE)'


class OurWorkSlide(models.Model):
    card_heading = models.CharField(max_length=300, null=True, blank=True)
    card_detail = models.CharField(max_length=300, null=True, blank=True)


    def __str__(self):
        return self.card_heading

    class Meta:
        verbose_name = 'Our Work Slide (SERVICE PAGE)'
        verbose_name_plural = 'Our Work Slide (SERVICE PAGE)'

class DataSecuritySection(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    detail = models.CharField(max_length=300, null=True, blank=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Data Security Section (SERVICE PAGE)'
        verbose_name_plural = 'Data Security Section (SERVICE PAGE)'

class TechnologiesIcons(models.Model):
    icons = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.icons

    class Meta:
        verbose_name = 'Technologies icon (SERVICE PAGE)'
        verbose_name_plural = 'Technologies icon (SERVICE PAGE)'


class Testimonials(models.Model):
    testimonial = models.CharField(max_length=300, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.testimonial

    class Meta:
        verbose_name = 'Testimonials section (SERVICE PAGE)'
        verbose_name_plural = 'Testimonials section (SERVICE PAGE)'


class CompanyStat(models.Model):
    achievement_name = models.CharField(max_length=300, null=True, blank=True)
    max_num_to_reach = models.IntegerField(default=0)

    def __str__(self):
        return self.achievement_name

    class Meta:
        verbose_name = 'company stats (SERVICE PAGE)'
        verbose_name_plural = 'company stats (SERVICE PAGE)'

#  HOME PAGE
class HomePageFront(models.Model):
    front_data = models.CharField(max_length=300, null=True, blank=True)
    sub_detail = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.front_data

    class Meta:
        verbose_name = 'home page front section (HOME PAGE)'
        verbose_name_plural = 'home page front section (HOME PAGE)'

class HowDoesItWorkHome(models.Model):
    heading = models.CharField(max_length=300, null=True, blank=True)
    short_intro = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.heading


    class Meta:
        verbose_name = 'how does it work for home page (HOME PAGE)'
        verbose_name_plural = 'how does it work for home page (HOME PAGE)'

# rest are same as service page last 4 models


# ABOUT US
class AboutUsStarting(models.Model):
    heading = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'Starting text for About us page (ABOUT US PAGE)'
        verbose_name_plural = 'Starting text for About us page (ABOUT US PAGE)'


class WhatMakeUsDifferent1(models.Model):
    heading = models.CharField(max_length=300, null=True, blank=True)
    para1 = models.CharField(max_length=300, null=True, blank=True)
    para2 = models.CharField(max_length=300, null=True, blank=True) 

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'What makes us different (first) (ABOUT US PAGE)'
        verbose_name_plural = 'What makes us different (first) (ABOUT US PAGE)'

class TopTeamMembers(models.Model):
    member_pic = models.ImageField()
    member_name = models.CharField(max_length=300, null=True, blank=True)
    member_role = models.CharField(max_length=300, null=True, blank=True)
    gmail = models.CharField(max_length=300, null=True, blank=True)
    facebook = models.CharField(max_length=300, null=True, blank=True)
    twitter = models.CharField(max_length=300, null=True, blank=True)
    linkdin = models.CharField(max_length=300, null=True, blank=True)


    def __str__(self):
        return self.member_name

    class Meta:
        verbose_name = 'Top Team Member details (ABOUT US PAGE)'
        verbose_name_plural = 'Top Team Member details (ABOUT US PAGE)'

class WhatMakeUsDifferent2(models.Model):
    heading = models.CharField(max_length=300, null=True, blank=True)
    para1 = models.CharField(max_length=300, null=True, blank=True)
    para2 = models.CharField(max_length=300, null=True, blank=True) 

    def __str__(self):
        return self.heading


    class Meta:
        verbose_name = 'What makes us different (second) (ABOUT US PAGE)'
        verbose_name_plural = 'What makes us different (second) (ABOUT US PAGE)'
# 6th class of service page i.e TechnologiesIcons

class LetsDoIt(models.Model):
    ready_text = models.CharField(max_length=300, null=True, blank=True)
    ready_btn = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.ready_text


    class Meta:
        verbose_name = 'Contact us section (ABOUT US PAGE)'
        verbose_name_plural = 'Contact us section (ABOUT US PAGE)'

#  TEAM PAGE
class OurTeamIntro(models.Model):
    intro = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.intro

    class Meta:
        verbose_name = 'Our Team Introduction (TEAM PAGE)'
        verbose_name_plural = 'Our Team Introduction (TEAM PAGE)'

class MembersDetailnPic(models.Model):
    member_pic = models.ImageField()
    member_name = models.CharField(max_length=300, null=True, blank=True)
    member_role = models.CharField(max_length=300, null=True, blank=True)
    gmail = models.CharField(max_length=300, null=True, blank=True)
    facebook = models.CharField(max_length=300, null=True, blank=True)
    twitter = models.CharField(max_length=300, null=True, blank=True)
    linkdin = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.member_name


    class Meta:
        verbose_name = 'Team Members details and pictures (TEAM PAGE)'
        verbose_name_plural = 'Team Members details and pictures (TEAM PAGE)'

#  FOOTER DATA
class FooterData(models.Model):
    footer_data = models.CharField(max_length=300, null=True, blank=True)
    copy_right = models.CharField(max_length=300, null=True, blank=True) 

    def __str__(self):
        return self.footer_data

    class Meta:
        verbose_name = 'Footer Section (FOOTER PAGE)'
        verbose_name_plural = 'Footer Section (FOOTER PAGE)'
