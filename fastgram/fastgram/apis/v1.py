from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email, ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from contents.models import Content, Image, FollowRelation

@method_decorator(csrf_exempt, name='dispatch')
class BaseView(View):
    @staticmethod
    def response(data={}, message='', status= 200):
        result = {
            'data':data,
            'message':message,
        }
        return JsonResponse(result, status=status)
    
    
class UserCreateView(BaseView):
    #@method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)
    
    def post(self, request):
        username = request.POST.get('username', '')
        if not username:
            return self.response(message='아이디를 입력해주세요', status=400)
        password = request.POST.get('password', '')
        if not password:
            return self.response(message='비밀번호를 입력해주세요', status=400)
        email = request.POST.get('email', '')
        try :
            validate_email(email)
        except ValidationError:
            return self.response(message='올바른 이메일을 입력해주세요', status=400)
        # if not email:
        #     return self.response(message='이메일을 입력해주세요', status=400)

        try :
            user = User.objects.create_user(username, password, email)
        except IntegrityError:
            return self.response(message='이미 존재하는 아아디입니다', status=400)
        return self.response({'user.id':user.id})
    
    
class UserLoginView(BaseView):
    def post(self, request):
        username = request.POST.get('username','')
        if not username:
            return self.response(message='아이디를 입력해주세요',status=400)
        password = request.POST.get('password', '')
        if not password:
            return self.response(message='비밀번호를 입력해주세요', status=400)
        
        user = authenticate(request, username=username,password=password)
        if user is None:
            return self.response(message='입력정보를 확인해주세요', status=400)
        login(request, user)
        return self.response()
    


@method_decorator(login_required, name='dispatch')
class ContentCreateView(BaseView):

    def post(self, request):
        text = request.POST.get('text', '').strip()
        content = Content.objects.create(user=request.user, text=text)
        for idx, file in enumerate(request.FILES.values()):
            Image.objects.create(content=content, image=file, order=idx)
        return self.response({})


@method_decorator(login_required, name='dispatch')
class RelationCreateView(BaseView):

    def post(self, request):
        try:
            user_id = request.POST.get('id', '')
        except ValueError:
            return self.response(message='잘못된 요청입니다.', status=400)

        try:
            relation = FollowRelation.objects.get(follower=request.user)
        except FollowRelation.DoesNotExist:
            relation = FollowRelation.objects.create(follower=request.user)

        try:
            if user_id == request.user.id:
                # 자기 자신은 팔로우 안됨.
                raise IntegrityError
            relation.following.add(user_id)
            relation.save()
        except IntegrityError:
            return self.response(message='잘못된 요청입니다.', status=400)

        return self.response({})


@method_decorator(login_required, name='dispatch')
class RelationDeleteView(BaseView):

    def post(self, request):
        try:
            user_id = request.POST.get('id', '')
        except ValueError:
            return self.response(message='잘못된 요청입니다.', status=400)

        try:
            relation = FollowRelation.objects.get(follower=request.user)
        except FollowRelation.DoesNotExist:
            return self.response(message='잘못된 요청입니다.', status=400)

        try:
            if user_id == request.user.id:
                # 자기 자신은 언팔로우 안됨.
                raise IntegrityError
            relation.following.remove(user_id)
            relation.save()
        except IntegrityError:
            return self.response(message='잘못된 요청입니다.', status=400)

        return self.response({})
    

class UserGetView(BaseView):
    
    def get(self, request):
        username = request.GET.get('username', '').strip()
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            self.response(message='사용자를 찾을 수 없습니다.', status=404)
        return self.response({'username': username, 'email': user.email, 'id': user.id})
    

class UserLogoutView(BaseView):
    def get(self, request):
        logout(request)
        return self.response()