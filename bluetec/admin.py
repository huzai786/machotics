from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib import admin
from .models import (
GetStarted,
OurServiceFront,
WhatDoWeOffer,
ServiceCard,
HowDoWeWork,
OurWorkSlide,
DataSecuritySection,
TechnologiesIcons,
Testimonials,
HomePageFront,
CompanyStat,
HowDoesItWorkHome,
AboutUsStarting,
WhatMakeUsDifferent1,
TopTeamMembers,
WhatMakeUsDifferent2,
LetsDoIt,
OurTeamIntro,
FooterData,
CareerIntro,
CareerDesc

)

admin.site.register(GetStarted)
admin.site.register(OurServiceFront)
admin.site.register(WhatDoWeOffer)
admin.site.register(ServiceCard)
admin.site.register(HowDoWeWork)
admin.site.register(OurWorkSlide)
admin.site.register(DataSecuritySection)
admin.site.register(TechnologiesIcons)
admin.site.register(Testimonials)
admin.site.register(HomePageFront)
admin.site.register(CompanyStat)
admin.site.register(HowDoesItWorkHome)
admin.site.register(AboutUsStarting)
admin.site.register(WhatMakeUsDifferent1)
admin.site.register(TopTeamMembers)
admin.site.register(WhatMakeUsDifferent2)
admin.site.register(OurTeamIntro)
admin.site.register(LetsDoIt)
admin.site.register(FooterData)
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(CareerDesc)
admin.site.register(CareerIntro)





admin.site.site_header = 'Machotics CMS'                    
admin.site.index_title = 'Content Management System for Machotics'                
admin.site.site_title = 'Content Management System for Machotics'
