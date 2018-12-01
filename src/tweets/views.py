from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Tweet
from .forms import TweetModelForm
from django.views.generic import DetailView,ListView,CreateView,UpdateView,DeleteView
from .mixins import  FormUserNeededMixin,UserOwnerMixin
from django import  forms,http
from django.forms.utils import ErrorList
from django.urls import reverse_lazy
from django.db.models import Q
# Create your views here.


class TweetCreateView(FormUserNeededMixin,CreateView):
    # queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    # success_url = '/tweet/create/'
    # login_url = '/admin/'



class TweetUpdateView(LoginRequiredMixin,UserOwnerMixin,UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    # success_url = '/tweet/'

class  TweetDeleteView(LoginRequiredMixin,UserOwnerMixin,DeleteView):
    model = Tweet
    # form_class = TweetModelForm
    template_name = 'tweets/delete_confirm.html'
    success_url = reverse_lazy('tweet:create')

    def delete(self, request, *args, **kwargs):
        # the Post object
        self.object = self.get_object()
        if self.object.user == request.user:
            success_url = self.get_success_url()
            self.object.delete()
            return http.HttpResponseRedirect(success_url)
        else:
            # form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["not authorized"])
            return http.HttpResponseForbidden("Cannot delete other's tweet")


class TweetDetailView(DetailView):

    template_name = 'tweets/detail_view.html'
    queryset = Tweet.objects.all()

    # def get_object(self):

    #     id = self.kwargs.get('id')
    #     return Tweet.objects.filter(pk=id).first()


class TweetListView(ListView):

    template_name = 'tweets/list_view.html'
    # queryset = Tweet.objects.all()
    def get_queryset(self,*args,**kwargs):
        data = Tweet.objects.all()
        serach_tweet = self.request.GET.get('q',None)
        if serach_tweet is not None:
            data = data.filter(
                Q(content__icontains =serach_tweet)|
                Q(user__username =serach_tweet)
            )
        return data 


    def get_context_data(self,*args,**kwargs):
        context = super(TweetListView,self).get_context_data(*args,**kwargs)
        return context



def tweet_create_view(request):
    form = TweetModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
    context = {
        'form':form
    }
    return render(request,'tweets/create_view.html',context)

def tweet_detail_view(request,pk):

    tweet = Tweet.objects.filter(pk=pk).first()
    context = {
        'object' : tweet,
        # 'hello ': 'harsh'
    } 
    return render(request,'tweets/detail_view.html',context)

def tweet_list_view(request):

    tweet = Tweet.objects.filter()
    context = {
        'object_list' : tweet
    } 
    return render(request,'tweets/list_view.html',context)