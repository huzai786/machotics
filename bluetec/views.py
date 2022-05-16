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
    ServiceCard
)


def home(request):

    context = {}
    return render(request, 'bluetec/home.html', context)

def about_us(request):

    context = {}
    return render(request, 'bluetec/about-us.html', context)

def team(request):
    
    context = {}
    return render(request, 'bluetec/team.html', context)

def career(request):

    context = {}
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
