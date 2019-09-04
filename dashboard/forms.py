from django import forms
from product.models import Product, Category, Brand, Type, BannerImage, Cart, ProductSpecification, ProductImage, SuperImage, OfferImage
from django.forms.models import inlineformset_factory


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product 
        fields = ['name', 'description', 'previous_price', 'new_price', 'category', 'brand', 'product_type', 'super_deals', 'offer', 'offer_tag', 'availability', 'main_image', 'color']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["color"].widget.attrs.update({'class': 'multi-select'})


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'category_image']


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['category', 'name', 'brand_image', 'brand_small_image']


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['brand', 'brand_type', 'type_image']


class BannerImageForm(forms.ModelForm):
    class Meta:
        model = BannerImage
        fields = ['image']


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