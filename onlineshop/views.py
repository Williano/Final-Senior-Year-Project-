from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from cart.forms import CartAddProductForm
from .models import Category, Product, Review
from .forms import ReviewForm
from .recommender import Recommender


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        language = request.LANGUAGE_CODE
        category = get_object_or_404(Category, translations__language_code=language,
                                     translations__slug=category_slug)
        products = products.filter(category=category)

    cart_product_form = CartAddProductForm()
    return render(request, 'onlineshop/product/product-list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'cart_product_form': cart_product_form,
                   })


def product_detail(request, id, slug):
    language = request.LANGUAGE_CODE
    product = get_object_or_404(Product, id=id, translations__language_code=language,
                                translations__slug=slug, available=True)
    # List of active comments for this product.
    reviews = product.reviews.filter(active=True)

    if request.method == "POST":
        # A review form was posted.
        review_form = ReviewForm(request.POST)
        print(review_form)
        if review_form.is_valid():
            # Create Review object but do not save to database yet.
            new_review = review_form.save(commit=False)
            # Assign the current product to the review
            new_review.product = product
            # Save the review to the database
            new_review.save()
    else:
        review_form = ReviewForm()

    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 3)
    return render(request, 'onlineshop/product/product-detail.html', {'product': product,
                                                                      'reviews': reviews,
                                                                      'review_form': review_form,
                                                                      'cart_product_form': cart_product_form,
                                                                      'recommended_products': recommended_products})






