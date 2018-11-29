from django.shortcuts import render
from .models import Tweet
from .forms import TweetModelForm
from django.views.generic import DetailView,ListView,CreateView
# Create your views here.


class TweetCreateView(CreateView):
    # queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = '/tweet/create/'
    def form_valid(self,form):
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super(TweetCreateView,self).form_valid(form)
        else:
            return self.form_invalid(form)

class TweetDetailView(DetailView):

    template_name = 'tweets/detail_view.html'
    queryset = Tweet.objects.all()
    # def get_object(self):

    #     id = self.kwargs.get('id')
    #     return Tweet.objects.filter(pk=id).first()


class TweetListView(ListView):

    template_name = 'tweets/list_view.html'
    queryset = Tweet.objects.all()
    # print('queryset ', queryset.content)

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