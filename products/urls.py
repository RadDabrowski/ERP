from django.urls import path

from products.views import SegmentListView, NewSegmentView, CategoryListView, \
    NewCategoryView, SubCategoryListView, NewSubCategoryView

urlpatterns = [
    path('segment/', SegmentListView.as_view(), name='segment-list'),
    path('segment-new/', NewSegmentView.as_view(), name='new-segment'),
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('category-new/', NewCategoryView.as_view(), name='new-category'),
    path('subcategory/', SubCategoryListView.as_view(), name='subcategory-list'),
    path('subcategory-new/', NewSubCategoryView.as_view(), name='new-subcategory'),
]