from rest_framework import serializers
from .models import Colours, Fonts, Header, ElementMenu, Offers, MainBlock, OurServices, Stack, Frameworks, Feedbacks, Feedback, Interview, Keyses, CooperationFormats, DecidesOnFooter, Footer, ServisesLeadForm, LeadForm, Site
from drf_yasg.utils import swagger_serializer_method


class ColoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colours
        fields = ('code',)


class FontsSerializer(serializers.ModelSerializer):
    file = serializers.FileField(use_url=False)

    class Meta:
        model = Fonts
        fields = ('name', 'file')


class ElementMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementMenu
        fields = ('title', 'link')


class HeaderSerializer(serializers.ModelSerializer):
    menu = serializers.SerializerMethodField()

    class Meta:
        model = Header
        fields = '__all__'

    def get_menu(self, obj):
            header_menu_query = ElementMenu.objects.all()
            serializer = ElementMenuSerializer(header_menu_query, many=True)
    
            return serializer.data


class OffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offers
        fields = '__all__'


class MainBlockSerializer(serializers.ModelSerializer):
    background_mobile = serializers.FileField(use_url=False)
    background_desktop = serializers.FileField(use_url=False)
    buttoncolour = ColoursSerializer(source='button_colour')
    
    class Meta:
        model = MainBlock
        fields = '__all__'


class OurServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurServices
        fields = '__all__'


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = '__all__'


class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = ('language',)


class FrameworksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frameworks
        fields = ('framework',)


class KeysesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=False)
    stack = StackSerializer(many=True)
    frameworks = FrameworksSerializer(many=True)

    class Meta:
        model = Keyses
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    screenshot = serializers.ImageField(use_url=False)
    mail = serializers.ImageField(use_url=False)
    class Meta:
        model = Feedback
        fields = '__all__'


class FeedbacksSerializer(serializers.ModelSerializer):
    feedbacks = serializers.SerializerMethodField()

    class Meta:
        model = Feedbacks
        fields = '__all__'

    def get_feedbacks(self, obj):
            feedbacks_query = Feedback.objects.all()
            serializer = FeedbackSerializer(feedbacks_query, many=True)
    
            return serializer.data


class CooperationFormatsSerializer(serializers.ModelSerializer):
    button_colour = ColoursSerializer()

    class Meta:
        model = CooperationFormats
        fields = '__all__'


class ServisesLeadFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServisesLeadForm
        fields = '__all__'


class LeadFormSerializer(serializers.ModelSerializer):
    button_colour = ColoursSerializer()
    servises = serializers.SerializerMethodField()

    class Meta:
        model = LeadForm
        fields = '__all__'

    def get_servises(self, obj):
            servises_query = ServisesLeadForm.objects.all()
            serializer = ServisesLeadFormSerializer(servises_query, many=True)
    
            return serializer.data


class DecidesOnFooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DecidesOnFooter
        fields = ('name',)


class FooterSerializer(serializers.ModelSerializer):
    decides = serializers.SerializerMethodField()
    stack = serializers.SerializerMethodField()
    frameworks = serializers.SerializerMethodField()

    class Meta:
        model = Footer
        fields = '__all__'

    def get_decides(self, obj):
            decides_query = DecidesOnFooter.objects.all()
            serializer = DecidesOnFooterSerializer(decides_query, many=True)
    
            return serializer.data
    
    def get_stack(self, obj):
            stack_query = Stack.objects.all()
            serializer = StackSerializer(stack_query, many=True)
    
            return serializer.data

    def get_frameworks(self, obj):
            frameworks_query = Frameworks.objects.all()
            serializer = FrameworksSerializer(frameworks_query, many=True)
    
            return serializer.data


class SiteSerializer(serializers.ModelSerializer):
    font = FontsSerializer()
    colour_of_background = ColoursSerializer()
    header = serializers.SerializerMethodField()
    mainblock = serializers.SerializerMethodField()
    ourservices = OurServicesSerializer(source='ourservices_set', many=True)
    interview = serializers.SerializerMethodField()
    keyses = KeysesSerializer(source='keyses_set', many=True)
    feedbacks = serializers.SerializerMethodField()
    cooperationformats = CooperationFormatsSerializer(source='cooperationformats_set', many=True)
    leadform = serializers.SerializerMethodField()
    footer = serializers.SerializerMethodField()

    class Meta:
        model = Site
        fields = '__all__'

    @swagger_serializer_method(serializer_or_field=HeaderSerializer)
    def get_header(self, obj):
        return HeaderSerializer(Header.objects.all().first()).data

    @swagger_serializer_method(serializer_or_field=MainBlockSerializer)
    def get_mainblock(self, obj):
        return MainBlockSerializer(MainBlock.objects.all().first()).data

    @swagger_serializer_method(serializer_or_field=OurServicesSerializer)
    def get_ourservices(self, obj):
        return OurServicesSerializer(OurServices.objects.all()).data

    @swagger_serializer_method(serializer_or_field=InterviewSerializer)
    def get_interview(self, obj):
        return InterviewSerializer(Interview.objects.all().first()).data

    @swagger_serializer_method(serializer_or_field=KeysesSerializer)
    def get_keyses(self, obj):
        return KeysesSerializer(Keyses.objects.all()).data

    @swagger_serializer_method(serializer_or_field=FeedbacksSerializer)
    def get_feedbacks(self, obj):
        return FeedbacksSerializer(Feedbacks.objects.all().first()).data

    @swagger_serializer_method(serializer_or_field=CooperationFormatsSerializer)
    def get_cooperationformats(self, obj):
        return CooperationFormatsSerializer(CooperationFormats.objects.all()).data

    @swagger_serializer_method(serializer_or_field=LeadFormSerializer)
    def get_leadform(self, obj):
        return LeadFormSerializer(LeadForm.objects.all().first()).data

    @swagger_serializer_method(serializer_or_field=FooterSerializer)
    def get_footer(self, obj):
        return FooterSerializer(Footer.objects.all().first()).data