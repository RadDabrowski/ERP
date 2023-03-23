from django.urls import reverse
from django.views.generic import ListView, CreateView

from products.forms import SegmentForm, CategoryForm, SubCategoryForm
from products.models import Segment, Category, SubCategory


class SegmentListView(ListView):
    model = Segment


class NewSegmentView(CreateView):
    model = Segment
    form_class = SegmentForm

    def get_success_url(self):
        return reverse('segment-list')


class CategoryListView(ListView):
    model = Category


class NewCategoryView(CreateView):
    model = Category
    form_class = CategoryForm

    def get_success_url(self):
        return reverse('category-list')


class SubCategoryListView(ListView):
    model = SubCategory


class NewSubCategoryView(CreateView):
    model = SubCategory
    form_class = SubCategoryForm

    def get_success_url(self):
        return reverse('subcategory-list')