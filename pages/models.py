from pytils.translit import slugify
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill




class AboutPageClients(models.Model):
    image = models.ImageField('О нас - Изображения секция 2', upload_to='about_images', blank=False)
    image_small = ImageSpecField(source='image', processors=[ResizeToFill(270, 220)], format='JPEG', options={'quality':80})
    is_active = models.BooleanField('Показывать на странице?', default=True)

    def __str__(self):
        return 'Избражение клиента'

    class Meta:
        verbose_name = "Избражение клиента"
        verbose_name_plural = "Избражения клиентов"

class AboutPageWork(models.Model):
    image = models.ImageField('О нас - Изображения секция 3', upload_to='about_images', blank=False)
    image_small = ImageSpecField(source='image', processors=[ResizeToFill(270, 220)], format='JPEG', options={'quality':80})
    is_active = models.BooleanField('Показывать на странице?', default=True)

    def __str__(self):
        return 'Избражение продукции'

    class Meta:
        verbose_name = "Избражение продукции"
        verbose_name_plural = "Избражения продукции"


class AboutSlider(models.Model):
    image = models.ImageField('О нас - Изображения для слайдера', upload_to='about_images', blank=False)
    is_active = models.BooleanField('Показывать на странице?', default=True)

    def __str__(self):
        return 'Избражение в слайдере'

    class Meta:
        verbose_name = "Избражение в слайдер"
        verbose_name_plural = "Избражения в слайдере"


class Services(models.Model):
    header = models.CharField('Услуги - Заголовок ', max_length=30, blank=False,
                                                default='Услуги')
    text = RichTextUploadingField('Услуги - Текст ', blank=False,
                                                     default='')
    def __str__(self):
        return 'Услуга'

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Page(models.Model):
    about_header_section1 = models.CharField('О нас - Заголовок секция 1', max_length=30, blank=False, default='О НАС')
    about_text1_section1 = RichTextUploadingField('О нас - Текст 1 секция 1', blank=False, default='Текст 1 секция 1')
    about_text2_section1 = RichTextUploadingField('О нас - Текст 2 секция 1', blank=False, default='Текст 2 секция 1')
    about_header_section2 = models.CharField('О нас - Заголовок секция 1', max_length=30, blank=False, default='НАШИ КЛИЕНТЫ')
    about_text1_section2 = RichTextUploadingField('О нас - Текст 1 секция 2', blank=False, default='Текст 1 секция 2')
    about_header_section3 = models.CharField('О нас - Заголовок секция 3', max_length=30, blank=False, default='НАШЕ ПРОИЗВОДСТВО')
    about_title = models.CharField('О нас - Title страницы', max_length=30, blank=False, default='О НАС')
    about_description = models.CharField('О нас - Description страницы', max_length=30, blank=False, default='О НАС')
    about_keywords = models.CharField('О нас - Keywords страницы', max_length=30, blank=False, default='О НАС')

    contact_header_section1 = models.CharField('Контакты - Заголовок секция 1', max_length=30, blank=False, default='КОНТАКТЫ')
    contact_text1_section1 = RichTextUploadingField('Контакты - Текст 1 секция 1', blank=False, default='Текст 1 секция 1')
    contact_header_section2 = models.CharField('Контакты - Заголовок секция 2', max_length=30, blank=False,default='РЕКВИЗИТЫ')
    contact_text1_section2 = RichTextUploadingField('Контакты - Текст 1 секция 2', blank=False, default='Текст 1 секция 2')


    contact_title = models.CharField('Контакты - Title страницы', max_length=30, blank=False, default='КОНТАКТЫ')
    contact_description = models.CharField('Контакты - Description страницы', max_length=30, blank=False, default='КОНТАКТЫ')
    contact_keywords = models.CharField('Контакты - Keywords страницы', max_length=30, blank=False, default='КОНТАКТЫ')

    category_main_title = models.CharField('Портфолио  - Title страницы', max_length=30, blank=False, default='Портфолио')
    category_main_description = models.CharField('Портфолио  - Description страницы', max_length=30, blank=False,
                                           default='Портфолио')
    category_main_keywords = models.CharField('Портфолио  - Keywords страницы', max_length=30, blank=False,
                                         default='Портфолио')  
 
    services_header_section1 = models.CharField('Услуги - Заголовок секция 1', max_length=30, blank=False, default='Услуги')
    services_text1_section1 = RichTextUploadingField('Услуги - Текст 1 секция 1', blank=False, default='Текст 1 секция 1')
    services_item_title = models.CharField('Услуги - Title страницы', max_length=30, blank=False,
                                            default='Услуги')
    services_item_description = models.CharField('Услуги - Description страницы', max_length=30, blank=False,
                                                 default='Услуги')
    services_item_keywords = models.CharField('Услуги - Keywords страницы', max_length=30, blank=False,
                                               default='Услуги')

    index_title = models.CharField('Главная - Title страницы', max_length=30, blank=False, default='Главная')
    index_description = models.CharField('Главная - Description страницы', max_length=30, blank=False,
                                          default='Главная')
    index_keywords = models.CharField('Главная - Keywords страницы', max_length=30, blank=False, default='Главная')


class Category(models.Model):
    name = models.CharField('Название категории', max_length=30, blank=False, default='НАЗВАНИЕ КАТЕГОРИИ')
    name_slug = models.CharField( max_length=30, blank=True)
    image = models.ImageField('Картинка категории', upload_to='category_images', blank=False)
    image_small = ImageSpecField(source='image', processors=[ResizeToFill(230, 290)], format='JPEG',
                                 options={'quality': 80})
    title = models.CharField('Title ', max_length=30, blank=False,
                                            default='Категория')
    description = models.CharField('Description ', max_length=30, blank=False,
                                                 default='Категория')
    keywords = models.CharField('Keywords ', max_length=30, blank=False,
                                               default='Категория')
    is_active = models.BooleanField('Показывать на странице?', default=True)
    views = models.IntegerField('Просмотров категории', default=0, blank=False)

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return 'Категория {}'.format(self.name)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Item(models.Model):
    category = models.ForeignKey(Category,blank=True,null=True, on_delete=models.SET_NULL,verbose_name='Товар в категории')
    name = models.CharField('Название товара', max_length=30, blank=False, default='')
    name_slug = models.CharField(max_length=30, blank=True)
    item_description = RichTextUploadingField('Описание товара', blank=False, default='')
    min_order = models.IntegerField('Минимальный заказ', default=0, blank=False)
    min_price = models.IntegerField('Минимальная стоимость', default=0, blank=False)
    max_price = models.IntegerField('Максимальная стоимость', default=0, blank=False)
    title = models.CharField('Title', max_length=30, blank=False,
                                           default='Портфолио')
    description = models.CharField('Description', max_length=30, blank=False,
                                                default='Портфолио')
    keywords = models.CharField('Keywords', max_length=30, blank=False,
                                              default='Портфолио')
    is_active = models.BooleanField('Показывать на странице?', default=True)
    views = models.IntegerField('Просмотров товара', default=0, blank=False)

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        if self.category.name:
            return 'Товар {} в категория {}'.format(self.name, self.category.name)
        else:
            return 'Товар {} не в категории '.format(self.name)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class ItemImage(models.Model):
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Изображение для товара')
    image = models.ImageField('Изображение товара', upload_to='item_images', blank=False)
    image_small = ImageSpecField(source='image', processors=[ResizeToFill(230, 290)], format='JPEG',
                                 options={'quality': 80})

    def __str__(self):
        if self.item:
            return 'Изображение не связано с товаром : {}'.format(self.item.name)
        else:
            return 'Изображение не связано с товаром '

    class Meta:
        verbose_name = "Изображение для товара"
        verbose_name_plural = "Изображения для товаров"


class Forms(models.Model):
    name = models.CharField('Поле - Ваше имя',max_length=255, blank=False, default='Нет данных')
    phone = models.CharField('Поле - Телефон', max_length=255, blank=False, default='Нет данных')
    email = models.EmailField('Поле - Email', max_length=255, blank=True, default='Нет данных')
    file = models.FileField('Загруженный файл', upload_to='form_files',blank=True)