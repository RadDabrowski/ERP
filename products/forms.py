from django.forms import ModelForm

from products.models import Segment, Category, SubCategory


class SegmentForm(ModelForm):
    class Meta:
        model = Segment
        fields = '__all__'


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategoryForm(ModelForm):
    class Meta:
        model = SubCategory
        fields = '__all__'

