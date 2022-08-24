from distutils.command.upload import upload
from django.db import models


class Fonts(models.Model):
    '''Шрифты, которые будут использоваться на сайте'''
    name = models.CharField(max_length=50, verbose_name='Название шрифта')
    file = models.FileField(upload_to='fonts', blank=True,
                            null=True, verbose_name='Файл со шрифтом', default=None)

    class Meta:
        verbose_name = 'Шрифт'
        verbose_name_plural = 'Шрифты'

    def __str__(self):
        return self.name


class Colours(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название цвета')
    code = models.CharField(max_length=10, verbose_name='Код цвета')

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.name


class Site(models.Model):
    '''Общая модель с шрифтом, объединяющая все блоки сайта'''
    font = models.ForeignKey(
        Fonts, blank=True, null=True, verbose_name='Шрифт сайта', on_delete=models.SET_NULL)
    colour_of_background = models.ForeignKey(Colours, blank=True, null=True, verbose_name='Цвет фона сайта',
                                on_delete=models.SET_NULL, default=None, related_name='site_font')

    class Meta:
        verbose_name = 'Сайт'
        verbose_name_plural = 'Сайт'

    def __str__(self):
        return 'Promo'


class Header(models.Model):
    '''Хэдер сайта(главный блок) с кликабельным фоновым изображением и лого'''
    site = models.ForeignKey(
        Site, null=True, on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name = 'Хэдер'
        verbose_name_plural = 'Хэдер'

    def __str__(self):
        return "Шапка сайта"


class ElementMenu(models.Model):
    '''Элементы меню сайта с якорными ссылками'''
    title = models.CharField(
        max_length=100, verbose_name='Название элемента меню')
    link =  models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Якорь', default=None)
    header = models.ForeignKey(Header, null=True, on_delete=models.PROTECT, default=None, related_name='header_menu')

    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'

    def __str__(self):
        return "Элемент меню"


class MainBlock(models.Model):
    background_mobile = models.FileField(upload_to='backgrounds/mobile',
                              blank=True, null=True, verbose_name='Фон для мобилки', default=None)
    background_desktop = models.FileField(upload_to='backgrounds/mobile',
                              blank=True, null=True, verbose_name='Фон для десктопа', default=None)
    main_offer = models.CharField(
        max_length=100, verbose_name='Главный оффер')
    button_text =  models.CharField(
        max_length=50, verbose_name='Текст кнопки')
    button_link =  models.CharField(
        max_length=50, verbose_name='Ссылка кнопки', blank=True, null=True)
    button_colour = models.ForeignKey(Colours, blank=True, null=True, verbose_name='Цвет кнопки',
                                on_delete=models.SET_NULL, default=None, related_name='button_colour')
    site = models.ForeignKey(
        Site, null=True, on_delete=models.CASCADE, default=None)
    separator = models.BooleanField(verbose_name='Разделитель', default=False)

    
    class Meta:
        verbose_name = 'Главный блок'
        verbose_name_plural = 'Главный блок'

    def __str__(self):
        return "Главный блок"

class Offers(models.Model):
    text = models.TextField(verbose_name='Текст оффера')
    mainblock = models.ForeignKey(MainBlock, null=True, on_delete=models.PROTECT, default=None, related_name='offers_mainblock')
    
    class Meta:
        verbose_name = 'Оффер'
        verbose_name_plural = 'Офферы'

    def __str__(self):
        return "Офферы"


class OurServices(models.Model):
    name = models.CharField(
        max_length=50, verbose_name='Название услуги')
    description = models.TextField(
        max_length=200, verbose_name='Описание услуги')
    price = models.IntegerField(verbose_name='Цена')
    site = models.ForeignKey(
        Site, null=True, on_delete=models.CASCADE, default=None)
    separator = models.BooleanField(verbose_name='Разделитель', default=False)

    class Meta:
        verbose_name = 'Наша услуга'
        verbose_name_plural = 'Наши услуги'

    def __str__(self):
        return "Наши услуги"


class Interview(models.Model):
    text = models.TextField(
        verbose_name='Текст')
    signature = models.TextField(
        max_length=100, verbose_name='Подпись')
    photo = models.ImageField(upload_to='images/interview/', verbose_name='Фото')
    site = models.ForeignKey(
        Site, null=True, on_delete=models.CASCADE, default=None)
    separator = models.BooleanField(verbose_name='Разделитель', default=False)
    tg_link = models.CharField(max_length=100, blank=True, null=True,
                              default=None, verbose_name='Ссылка для ТГ')
    wa_link = models.CharField(max_length=100, blank=True, null=True,
                          default=None, verbose_name='Ссылка для Вотсапа')

    class Meta:
        verbose_name = 'Интервьюшка'
        verbose_name_plural = 'Интервьюшка'

    def __str__(self):
        return "Интервьюшка" 


class Stack (models.Model):
    language = models.CharField(max_length=20, verbose_name='Язык программирования')

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    def __str__(self):
        return self.language


class Frameworks (models.Model):
    framework = models.CharField(max_length=20, verbose_name='Фреймворк')

    class Meta:
        verbose_name = 'Фреймворк'
        verbose_name_plural = 'Фреймворки'

    def __str__(self):
        return self.framework


class Keyses(models.Model):
    title = models.CharField(max_length=50, verbose_name='Навзание кейса')
    image = models.ImageField(upload_to='images/keyses/', blank=True, null=True, verbose_name='Обложка кейса')
    description = models.TextField(verbose_name='Описание кейса', blank=True, null=True)
    stack = models.ManyToManyField(Stack, verbose_name='Стек', blank=True)
    frameworks = models.ManyToManyField(Frameworks, verbose_name='Фреймворки', blank=True)
    site = models.ForeignKey(
        Site, null=True, on_delete=models.CASCADE, default=None)
    separator = models.BooleanField(verbose_name='Разделитель', default=False)
    
    class Meta:
        verbose_name = 'Кейс'
        verbose_name_plural = 'Кейсы'

    def __str__(self):
        return "Кейсы"


class Feedbacks (models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок блока')
    text = models.TextField(verbose_name='Текст', blank=True, null=True)
    site = models.ForeignKey(
        Site, null=True, on_delete=models.CASCADE, default=None)
    separator = models.BooleanField(verbose_name='Разделитель', default=False)

    class Meta:
        verbose_name = 'Блок с отзывами'
        verbose_name_plural = 'Блок с отзывами'

    def __str__(self):
        return "Блок с отзывами"


class Feedback (models.Model):
    name = models.CharField(max_length=50, verbose_name='Название проекта', blank=True, null=True)
    screenshot = models.ImageField(upload_to='images/feedbacks/screenshots', verbose_name='Скриншот')
    mail = models.ImageField(upload_to='images/feedbacks/mails', verbose_name='Письмо')
    feedbacks = models.ForeignKey(
        Feedbacks, null=True, on_delete=models.CASCADE, default=None, related_name='every_feedbacks')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return "Отзывы"


class CooperationFormats (models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    discription = models.TextField(verbose_name='Описание', blank=True, null=True)
    button_text = models.CharField(max_length=20, verbose_name='Текст кнопки')
    button_link = models.CharField(max_length=20, verbose_name='Ссылка кнопки', blank=True, null=True)
    button_colour = models.ForeignKey(Colours, blank=True, null=True, verbose_name='Цвет кнопки',
                                on_delete=models.SET_NULL, default=None, related_name='cooperations_button_colour')
    site = models.ForeignKey(
        Site, null=True, on_delete=models.CASCADE, default=None)
    separator = models.BooleanField(verbose_name='Разделитель', default=False)

    class Meta:
        verbose_name = 'Формат сотрудничества'
        verbose_name_plural = 'Форматы сотрудничества'

    def __str__(self):
        return "Форматы сотрудничества"


class LeadForm(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок блока')
    button_text = models.CharField(max_length=30, verbose_name='Текст кнопки')
    button_colour = models.ForeignKey(Colours, blank=True, null=True, verbose_name='Цвет кнопки',
                                on_delete=models.SET_NULL, default=None, related_name='leadform_button_colour')
    site = models.ForeignKey(
        Site, null=True, on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name = 'Форма сбора заявок'
        verbose_name_plural = 'Форма сбора заявок'

    def __str__(self):
        return "Форма сбора заявок"


class ServisesLeadForm (models.Model):
    name = models.CharField(max_length=20, verbose_name='Услуги')
    leadform = models.ForeignKey(
        LeadForm, null=True, on_delete=models.CASCADE, default=None, related_name='services_leadform')

    class Meta:
        verbose_name = 'Услуга в лид-форме'
        verbose_name_plural = 'Услуги в лид-форме'

    def __str__(self):
        return "Услуги в лид-форме"


class Footer(models.Model):
    '''Подвал сайта с контактной информацией'''
    text = models.TextField(
        verbose_name='Текст в футере', blank=True, null=True, default=None)
    phone_number = models.CharField(
        max_length=15, blank=True, null=True, default=None, verbose_name='Телефон')
    tg_link = models.CharField(max_length=100, blank=True, null=True,
                              default=None, verbose_name='Ссылка для ТГ')
    wa_link = models.CharField(max_length=100, blank=True, null=True,
                          default=None, verbose_name='Ссылка для Вотсапа')
    site = models.ForeignKey(
        Site, null=True, on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name = 'Футер'
        verbose_name_plural = 'Футер'

    def __str__(self):
        return "Подвал сайта"


class DecidesOnFooter (models.Model):
    name = models.CharField(max_length=20, verbose_name='Решение')
    footer = models.ForeignKey(
        Footer, null=True, on_delete=models.CASCADE, default=None, related_name='decides_footer')

    class Meta:
        verbose_name = 'Решение'
        verbose_name_plural = 'Решения'

    def __str__(self):
        return "Решения"
