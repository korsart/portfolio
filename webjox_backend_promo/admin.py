from django.contrib import admin
from .models import Colours, Feedback, Feedbacks, Fonts, ElementMenu, Stack, Frameworks, Header, Offers, MainBlock, OurServices, Interview, Keyses, Feedback, Feedbacks, CooperationFormats, ServisesLeadForm, LeadForm, Footer, DecidesOnFooter, Site
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from django import forms


class ColoursAdmin(admin.ModelAdmin):
    model = Colours
    list_display = ('name', 'code')
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['code'].widget.attrs['placeholder'] = "#000000"
        return form


class FontsAdmin(admin.ModelAdmin):
    model = Fonts
    max_num = 10
    list_display = ('name', 'file')


class ElementMenuAdmin(NestedStackedInline):
    max_num = 10
    model = ElementMenu
    fk_name = 'header'


class StackAdmin(admin.ModelAdmin):
    max_num = 10
    model = Stack


class FrameworksAdmin(admin.ModelAdmin):
    max_num = 10
    model = Frameworks


class HeaderAdmin(NestedStackedInline):
    model = Header
    max_num = 1
    list_display = ('logo',)
    inlines = (ElementMenuAdmin,)


class OffersAdmin(NestedStackedInline):
    max_num = 5
    model = Offers
    fk_name = 'mainblock'


class MainBlockAdmin(NestedStackedInline):
    max_num = 1
    model = MainBlock


class OurServicesAdmin(NestedStackedInline):
    max_num = 10
    model = OurServices


class InterviewAdmin(NestedStackedInline):
    max_num = 1
    model = Interview


class KeysesAdmin(NestedStackedInline):
    max_num = 10
    model = Keyses


class FeedbackAdmin(NestedStackedInline):
    max_num = 10
    extra = 0
    model = Feedback
    fk_name = 'feedbacks'


class FeedbacksAdmin(NestedStackedInline):
    max_num = 1
    model = Feedbacks
    inlines = (FeedbackAdmin,)


class CooperationFormatsAdmin(NestedStackedInline):
    extra = 2
    max_num = 3
    model = CooperationFormats


class ServisesLeadFormAdmin(NestedStackedInline):
    max_num = 10
    extra = 0
    model = ServisesLeadForm
    fk_name = 'leadform'


class LeadFormAdmin(NestedStackedInline):
    max_num = 1
    model = LeadForm
    inlines = (ServisesLeadFormAdmin,)


class DecidesOnFooterAdmin(NestedStackedInline):
    max_num = 10
    extra = 0
    model = DecidesOnFooter


class FooterAdmin(NestedStackedInline):
    max_num = 1
    model = Footer
    fk_name = 'site'
    inlines = (DecidesOnFooterAdmin,)


class SiteAdmin(NestedModelAdmin):

    def has_add_permission(self, request):
        return not Site.objects.exists()

    model = Site
    inlines = (HeaderAdmin, MainBlockAdmin, OurServicesAdmin, InterviewAdmin,
               KeysesAdmin, FeedbacksAdmin, CooperationFormatsAdmin, LeadFormAdmin, FooterAdmin)


admin.site.register(Fonts, FontsAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(Colours, ColoursAdmin)
admin.site.register(Stack, StackAdmin)
admin.site.register(Frameworks, FrameworksAdmin)