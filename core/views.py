from typing import List
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ContactForm
from .models import Product, ProductTag
from django.views.generic import FormView, ListView, DetailView, DeleteView

class ContactUsView(FormView):
    template_name = 'contact_form.html'
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)

    def get_form_kwargs(self):
        print('#####')
        print(self.kwargs)
        return super().get_form_kwargs()



# View for listing out the products on the web page
class ProductListView(ListView):
    
    # template_name = 'products_list.html'
    context_object_name = 'products'
    paginate_by = 2
    def get_queryset(self):

        print(self.kwargs)  
        tag = self.kwargs['tag']
        self.tag = None

        if tag != 'all':
            self.tag = get_object_or_404(ProductTag, slug=tag)

        if self.tag:
            products = Product.objects.active().filter(
                tags = self.tag
            )
        else:
            products = Product.objects.active()


        return products

class ProductDetailView(DetailView):
    model = Product