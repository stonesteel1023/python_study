from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from contents.models import Content, FollowRelation

@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    # def dispatch(self, request, *args, **kwargs):
    #     return super(TemplateView, self).dispatch(request, *args, **kwargs)
    template_name = 'home.htm'
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        user = self.request.user
        following = FollowRelation.objects.filter(follower=user).values_list('following__id', flat=True)
        lookup_user_ids=[user.id] + list(following)
        context['contents'] = Content.objects.select_related('user').prefetch_related('image_set').filter(
            user__id__in = lookup_user_ids
        )
        
        return context
    

# @login_required
    # def login(request):
    #     pass
    

# class LoginView(View):
#     @method_decorator(login_required)
#     def dispatch(self, view):
#         pass
    
#     def get(self, request):
#         return self.response()

@method_decorator(login_required, name='dispatch')
class RelationView(TemplateView):

    template_name = 'relation.html'

    def get_context_data(self, **kwargs):
        context = super(RelationView, self).get_context_data(**kwargs)

        user = self.request.user

        # 내가 팔로우하는 사람들
        try:
            followers = FollowRelation.objects.get(follower=user).following.all()
            context['following'] = followers
            context['following_ids'] = list(followers.values_list('id', flat=True))
            
        except FollowRelation.DoesNotExist:
            pass

        context['followers'] = FollowRelation.objects.select_related('follower').filter(following__in=[user])
        
        return context
