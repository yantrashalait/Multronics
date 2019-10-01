from django import forms
from product.models import Product, Category, Brand, Type, BannerImage, Cart, ProductSpecification, \
    ProductImage, SuperImage, OfferImage, SpecificationTitle, SpecificationContent, AboutITeam
from django.forms.models import inlineformset_factory
from PIL import Image
from .widgets import *


class ProductForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height = forms.FloatField(widget=forms.HiddenInput(), required=False)
    brand = forms.ModelChoiceField(Brand.objects, widget=SelectWithPop)
    product_type = forms.ModelChoiceField(Type.objects, widget=SelectWithPop)
    
    class Meta:
        model = Product 
        fields = ['name', 'description', 'previous_price', 'new_price', 'category', 'brand', 'product_type', 'super_deals', 'offer', 'availability', 'main_image', 'visibility', 'x', 'y', 'width', 'height']
    
    def save(self):
        photo = super(ProductForm, self).save()
        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')
        if x is not None and y is not None:
            image = Image.open(photo.main_image)
            cropped_image = image.crop((x, y, w+x, h+y))
            resized_image = cropped_image.resize((265, 290), Image.ANTIALIAS)
            resized_image.save(photo.main_image.path)
        
        return photo


class CategoryForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height = forms.FloatField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ['name', 'category_image', 'x', 'y', 'width', 'height']
    
    def save(self):
        photo = super(CategoryForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')
        if x is not None and y is not None:
            image = Image.open(photo.category_image)
            cropped_image = image.crop((x, y, w+x, h+y))
            resized_image = cropped_image.resize((410, 281), Image.ANTIALIAS)
            resized_image.save(photo.category_image.path)
        return photo


class BrandForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height = forms.FloatField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Brand
        fields = ['category', 'name', 'brand_image', 'x', 'y', 'width', 'height']
    
    
    def save(self):
        photo = super(BrandForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')
        if x is not None and y is not None:
            image = Image.open(photo.brand_image)
            cropped_image = image.crop((x, y, w+x, h+y))
            resized_image = cropped_image.resize((193, 115), Image.ANTIALIAS)
            resized_image.save(photo.brand_image.path)
        return photo


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['brand_type']


class BannerImageForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height = forms.FloatField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = BannerImage
        fields = ['image', 'x', 'y', 'width', 'height']

    def save(self):
        photo = super(BannerImageForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')
        if x is not None and y is not None:
            image = Image.open(photo.image)
            cropped_image = image.crop((x, y, w+x, h+y))
            resized_image = cropped_image.resize((1280, 435), Image.ANTIALIAS)
            resized_image.save(photo.image.path)
        return photo


class ProductSpecificationForm(forms.ModelForm):
    title = forms.ModelChoiceField(SpecificationTitle.objects, widget=SelectWithPop)
    content = forms.ModelChoiceField(SpecificationContent.objects, widget=SelectWithPop)
    
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
    x = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height = forms.FloatField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = SuperImage
        fields = ['name', 'super_image', 'x', 'y', 'width', 'height']

    def save(self):
        photo = super(SuperImageForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')
        if x is not None and y is not None:
            image = Image.open(photo.super_image)
            cropped_image = image.crop((x, y, w+x, h+y))
            resized_image = cropped_image.resize((401, 424), Image.ANTIALIAS)
            resized_image.save(photo.super_image.path)
        return photo


class OfferImageForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height = forms.FloatField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = OfferImage
        fields = ['name', 'offer_image', 'x', 'y', 'width', 'height']

    def save(self):
        photo = super(OfferImageForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')
        if x is not None and y is not None:
            image = Image.open(photo.offer_image)
            cropped_image = image.crop((x, y, w+x, h+y))
            resized_image = cropped_image.resize((401, 424), Image.ANTIALIAS)
            resized_image.save(photo.offer_image.path)
        return photo


class SpecificationTitleForm(forms.ModelForm):
    class Meta:
        model = SpecificationTitle
        fields = ['title']


class SpecificationContentForm(forms.ModelForm):
    class Meta:
        model = SpecificationContent
        fields = ['title', 'content']

SpecificationContentFormset = inlineformset_factory(SpecificationTitle, SpecificationContent, form=SpecificationContentForm, fields=['title', 'content'], extra=1, max_num=20)


class AboutForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height = forms.FloatField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = AboutITeam
        fields = ['contact_number', 'email', 'logo', 'x', 'y', 'height', 'width']

    def save(self):
        photo = super(AboutForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')
        if x is not None and y is not None:
            image = Image.open(photo.logo)
            cropped_image = image.crop((x, y, w+x, h+y))
            resized_image = cropped_image.resize((192, 31), Image.ANTIALIAS)
            resized_image.save(photo.logo.path)
        return photo
    