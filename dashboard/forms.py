from django import forms
from product.models import Product, Category, Brand, Type, BannerImage, Cart, ProductSpecification, ProductImage, SuperImage, OfferImage, SpecificationTitle, SpecificationContent
from django.forms.models import inlineformset_factory
from PIL import Image


class ProductForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())
    
    class Meta:
        model = Product 
        fields = ['name', 'description', 'previous_price', 'new_price', 'category', 'brand', 'product_type', 'super_deals', 'offer', 'availability', 'main_image', 'x', 'y', 'width', 'height']
    
    def save(self):
        photo = super(ProductForm, self).save()
        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')
        # if x is not None and y is not None:
        image = Image.open(photo.main_image)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((265, 290), Image.ANTIALIAS)
        resized_image.save(photo.main_image.path)
        
        return photo


class CategoryForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Category
        fields = ['name', 'category_image', 'x', 'y', 'width', 'height']
    
    def save(self):
        photo = super(CategoryForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')
        # if x is not None and y is not None:
        image = Image.open(photo.category_image)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((410, 281), Image.ANTIALIAS)
        resized_image.save(photo.category_image.path)


class BrandForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Brand
        fields = ['category', 'name', 'brand_image', 'x', 'y', 'width', 'height']
    
    def save(self):
        photo = super(BrandForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')
        # if x is not None and y is not None:
        image = Image.open(photo.brand_image)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((193, 115), Image.ANTIALIAS)
        resized_image.save(photo.brand_image.path)


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['brand', 'brand_type']


class BannerImageForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = BannerImage
        fields = ['image', 'x', 'y', 'width', 'height']

    def save(self):
        photo = super(BannerImageForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')
        # if x is not None and y is not None:
        image = Image.open(photo.image)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((1280, 435), Image.ANTIALIAS)
        resized_image.save(photo.image.path)


class ProductSpecificationForm(forms.ModelForm):
    class Meta:
        model = ProductSpecification
        fields = ['title', 'content']


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['big_image', 'thumbnail_image']


ProductImageFormset = inlineformset_factory(Product, ProductImage, form=ProductImageForm, fields=['big_image', 'thumbnail_image'], extra=1, max_num=10)
ProductSpecificationFormset = inlineformset_factory(Product, ProductSpecification, form=ProductSpecificationForm, fields=['title', 'content'], extra=1, max_num=20)


class SuperImageForm(forms.ModelForm):
    class Meta:
        model = SuperImage
        fields = ['name', 'super_image']


class OfferImageForm(forms.ModelForm):
    class Meta:
        model = OfferImage
        fields = ['name', 'offer_image']


class SpecificationTitleForm(forms.ModelForm):
    class Meta:
        model = SpecificationTitle
        fields = ['title']


class SpecificationContentForm(forms.ModelForm):
    class Meta:
        model = SpecificationContent
        fields = ['title', 'content']

SpecificationContentFormset = inlineformset_factory(SpecificationTitle, SpecificationContent, form=SpecificationContentForm, fields=['title', 'content'], extra=1, max_num=20)
