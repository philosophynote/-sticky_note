from django.shortcuts import render, resolve_url, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView
from .models import Card, Category,Tag
from django.urls import reverse_lazy
from .forms import CardForm, LoginForm, SignUpForm, SearchForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


class TopPage(TemplateView):
    template_name = 'mysite/toppage.html'

    def Toppage(request):
        return render(request,'mysite/toppage.html,{}')



class Index(TemplateView):
    template_name = 'mysite/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        card_list = Card.objects.all().order_by('-created_at')[:6]
        context = {
            'card_list': card_list,
        }
        return context


class CardCreate(CreateView):
    template_name = 'mysite/card_create.html'  # どこのページに適用するかを明記する

    model = Card
    form_class = CardForm
    success_url = reverse_lazy('learning:index')

    def get_success_url(self):
        messages.success(self.request, 'CARDを登録しました。')
        return resolve_url('learning:index')


class CardDetail(DetailView):
    template_name = 'mysite/card_detail.html'

    model = Card

    def get_context_data(self, **kwargs):
        detail_data = Card.objects.get(id=self.kwargs['pk'])
        category_posts = Card.objects.filter(
            category=detail_data.category).order_by('-created_at')[:5]
        params = {
            'object': detail_data,
            'category_posts': category_posts,
        }
        return params


class CardUpdate(UpdateView):
    template_name = 'mysite/card_update.html'

    model = Card
    form_class = CardForm

    def get_success_url(self):
        messages.info(self.request, 'CARDを更新しました。')
        return resolve_url('learning:index', pk=self.kwargs['pk'])


class CardDelete(DeleteView):
    template_name = 'mysite/card_confirm_delete.html'

    model = Card

    def get_success_url(self):
        messages.info(self.request, 'CARDを削除しました。')
        return resolve_url('learning:index')


class CardList(ListView):
    template_name = 'mysite/card_list.html'

    model = Card
    paginate_by = 5

    def get_queryset(self):
        return Card.objects.all().order_by('-created_at')


class Login(LoginView):
    form_class = LoginForm
    template_name = 'mysite/login.html'

    def get_success_url(self):
        messages.info(self.request, 'ログインしました。')
        return resolve_url('learning:index')


class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'mysite/logout.html'

    def get_success_url(self):
        messages.info(self.request, 'ログアウトしました。')
        return resolve_url('learning:toppage')


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'mysite/signup.html'
    success_url = reverse_lazy('learning:index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user  # userをオブジェクトに入れる
        messages.info(self.request, 'ユーザー登録をしました。')
        return HttpResponseRedirect(self.get_success_url())


class CategoryList(ListView):
    template_name = 'mysite/category_list.html'

    model = Category


class CategoryDetail(DetailView):
    template_name = 'mysite/category_detail.html'

    model = Category
    slug_field = "name_en"
    slug_url_kwarg = "name_en"

    def get_context_data(self, *args, **kargs):
        detail_data = Category.objects.get(name_en=self.kwargs['name_en'])
        category_cards = Card.objects.filter(
            category=detail_data.id).order_by('-created_at')

        params = {
            'object': detail_data,
            'category_cards': category_cards,
        }

        return params


def Search(request):
    if request.method == "POST":
        searchform = SearchForm(request.POST)

        if searchform.is_valid():
            freeword = searchform.cleaned_data["freeword"]
            search_list = Card.objects.filter(
                Q(title__icontains=freeword) | Q(content__icontains=freeword))

        params = {
            'search_list': search_list,
        }
        return render(request, 'mysite/search.html', params)


class TagList(ListView):
    template_name = 'mysite/tag_list.html'

    model = Tag


class TagDetail(DetailView):
    template_name = 'mysite/tag_detail.html'

    model = Tag
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, *args, **kargs):
        detail_data = Tag.objects.get(slug=self.kwargs['slug'])
        tag_cards = Card.objects
        params = {
            'object': detail_data,
            'tag_cards': tag_cards,
        }

        return params
