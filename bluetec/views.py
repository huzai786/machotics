from django.shortcuts import redirect, render
from .forms import GetStartedForm
from django.contrib import messages
from django.core.mail import send_mail 
from .models import (TechnologiesIcons,
    Testimonials, 
    WhatDoWeOffer, 
    HowDoWeWork, 
    OurWorkSlide, 
    DataSecuritySection, 
    CompanyStat,
    FooterData,
    OurServiceFront,
    ServiceCard,
    AboutUsStarting,
    LetsDoIt,
    WhatMakeUsDifferent1,
    WhatMakeUsDifferent2,
    TopTeamMembers,
    OurTeamIntro,
    HomePageFront,
    HowDoesItWorkHome,
    CareerIntro,
    CareerDesc
)


def home(request):
    data_security = DataSecuritySection.objects.all().first()
    work_slides = OurWorkSlide.objects.all()
    technologies = TechnologiesIcons.objects.all()
    how_does_it_work = HowDoesItWorkHome.objects.all().first()
    home_front = HomePageFront.objects.all().first()
    testimonials = Testimonials.objects.all()
    company_stat = CompanyStat.objects.all() 
    context = {'company_stats': company_stat, 'testimonials': testimonials, 'home_front': home_front, 
    'how_does_it_work': how_does_it_work, 'work_slides': work_slides, 'data_security': data_security, 
    'technologies':technologies}
    return render(request, 'bluetec/home.html', context)

def about_us(request):
    top_team_member = TopTeamMembers.objects.all()[:4]
    Different1 = WhatMakeUsDifferent1.objects.all().first()
    Different2 = WhatMakeUsDifferent2.objects.all().first()
    about_us = AboutUsStarting.objects.all().first()
    technologies = TechnologiesIcons.objects.all()
    Footer = FooterData.objects.all().first()
    lets_do = LetsDoIt.objects.all().first()
    context = {'about_us': about_us, 'lets_do': lets_do, 'Footer': Footer, 'technologies':technologies, 
                'Different1': Different1, 'Different2': Different2, 'top_team_member': top_team_member}
    return render(request, 'bluetec/about-us.html', context)

def team(request):
    top_team_member = TopTeamMembers.objects.all()
    lets_do = LetsDoIt.objects.all().first()
    Footer = FooterData.objects.all().first()
    intro = OurTeamIntro.objects.all().first()
    context = {'intro': intro, 'Footer': Footer, 'lets_do': lets_do, 'top_team_member': top_team_member}
    return render(request, 'bluetec/team.html', context)

def career(request):
    career_selects = CareerDesc.objects.all()
    intro = CareerIntro.objects.all().first()
    lets_do = LetsDoIt.objects.all().first()
    Footer = FooterData.objects.all().first()
    context = {'Footer':Footer, 'lets_do': lets_do, 'intro': intro, 'career_selects': career_selects}
    return render(request, 'bluetec/career.html', context)

def service(request):
    service_card = ServiceCard.objects.all()
    service_front = OurServiceFront.objects.all().first()
    Footer = FooterData.objects.all().first()
    company_stat = CompanyStat.objects.all() 
    technologies = TechnologiesIcons.objects.all()
    what_do_we_offer = WhatDoWeOffer.objects.all().first()
    how_we_work = HowDoWeWork.objects.all().first()
    testimonials = Testimonials.objects.all()
    data_security = DataSecuritySection.objects.all().first()
    work_slides = OurWorkSlide.objects.all()
    form = GetStartedForm()
    if request.method == 'POST':
        form = GetStartedForm(request.POST)
        if form.is_valid():
            client_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            description = form.cleaned_data['description']
            send_mail(
                'Sent by ' + client_name,
                description,
                sender_email,
                ['muhammadhuzaifagamer123@gmail.com']
            )
            form.save()
            messages.info(request, 'Thanks ' + client_name + '! We have recieved your email and will contact you shortly..')
            context = {'form': form, 'client_name': client_name,}
            return redirect('home')
    context = {'form': form, 'technologies': technologies, 'testimonials': testimonials,
     'what_do_we_offer': what_do_we_offer, 'how_we_work': how_we_work, 'work_slides': work_slides,
      'data_security': data_security, 'company_stats': company_stat, 'Footer': Footer, 
      'service_front':service_front, 'service_cards': service_card}

    return render(request, 'bluetec/service.html', context)


def case_studies(request):
    context = {}
    return render(request, 'bluetec/case-studies.html', context)

def contact_us(request):
    context = {}
    return render(request, 'bluetec/contact_us.html', context)

def portfolio(request):
    context = {}
    return render(request, 'bluetec/portfolio.html', context)
