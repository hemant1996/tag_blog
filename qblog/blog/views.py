from django.shortcuts import render,render_to_response
from django.views import generic
from . import models
from django.template.context import RequestContext

class BlogIndex(generic.ListView):
	queryset=models.Entry.objects.published()
	template_name="home.html"
	paginate_by=2
class BlogDetail(generic.DetailView):
	model=models.Entry
	template_name="post.html"
def home(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('thirdauth/home.html',
                             context_instance=context)
# Create your views here.
