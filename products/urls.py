from django.urls import path

from products.views import SegmentListView, NewSegmentView

urlpatterns = [
    path('segment/', SegmentListView.as_view(), name='segment-list'),
    path('segment-new/', NewSegmentView.as_view(), name='new-segment'),
    path('category/', SegmentListView.as_view(), name='category-list'),
    path('category-new/', NewSegmentView.as_view(), name='new-category'),
    path('subcategory/', SegmentListView.as_view(), name='subcategory-list'),
    path('subcategory-new/', NewSegmentView.as_view(), name='new-subcategory'),
]