from __future__ import unicode_literals
import json
from django.db import IntegrityError
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, HostTournament, Ground
from django.forms.models import model_to_dict
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from .serializers import UserSerializers
from rest_framework import mixins, generics


class Signup(mixins.ListModelMixin,
             mixins.CreateModelMixin,
             generics.GenericAPIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser, )
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# class Signup(View):
#
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super(Signup, self).dispatch(request, *args, **kwargs)
#
#     def post(self, request):
#         try:
#             # data = json.loads(request.body.decode("UTF-8"))
#             # print(data)
#             user = User.objects.create(**request.body)
#
#             response = {
#                 'status': 200,
#                 'type': '+OK',
#                 'message': 'Successfully Signed Up',
#             }
#         except IntegrityError as e:
#             print(e)
#             response = {
#                 'status': 501,
#                 'type': '-ERR',
#                 'message': 'Same Username or Email',
#             }
#         except Exception as e:
#             print(e)
#             response = {
#                 'status': 500,
#                 'type': '-ERR',
#                 'message': 'Internal Server Error',
#             }
#         return JsonResponse(response)


# class Login(mixins.ListModelMixin,
#             mixins.RetrieveModelMixin,
#             mixins.UpdateModelMixin,
#             generics.GenericAPIView):
#     parser_classes = (JSONParser, MultiPartParser, FormParser, )
#     queryset = User.objects.all()
#     serializer_class = UserSerializers
#
#     def get(self, request, *args, **kwargs):
#         new_query = User.objects.filter(email=request.query_params.get('email'),
#                                         password=request.query_params.get('password')).values('name',
#                                                                                               'email',
#                                                                                               'password',
#                                                                                               'phone_no',
#                                                                                               'dob',
#                                                                                               'address',
#                                                                                               'special_skill',
#                                                                                               'fav_game',
#                                                                                               'profile',
#                                                                                               )
#         # print(new_query)
#         user_data = None
#         for u in new_query:
#             user_data = u
#         print(user_data)
#         if user_data.get('profile'):
#             user_data['profile'] = "https://ftlp-api.herokuapp.com/media/" + user_data['profile']
#         response = {
#                             'status': 200,
#                             'type': '+OK',
#                             'user_data': user_data,
#                             'message': 'Successfully Login',
#                         }
#         return JsonResponse(response)
#
#     # def post(self, request, *args, **kwargs):
#     #     return self.create(request, *args, **kwargs)


class Login(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Login, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        try:
            data = json.loads(request.body.decode("UTF-8"))
            email = data.get('email', None)
            password = data.get('password', None)

            user = User.objects.filter(email=email, password=password).values('name',
                                                                              'email',
                                                                              'password',
                                                                              'phone_no',
                                                                              'dob',
                                                                              'address',
                                                                              'special_skill',
                                                                              'fav_game',
                                                                              # 'profile',
                                                                              )
            user_data = None
            for u in user:
                user_data = u

            if user:
                response = {
                    'status': 200,
                    'type': '+OK',
                    'user_data': user_data,
                    'message': 'Successfully Login',
                }
            else:
                response = {
                    'status': 501,
                    'type': '+OK',
                    'message': 'Login Failed',
                }

        except Exception as e:
            print(e)
            response = {
                'status': 500,
                'type': '-ERR',
                'message': 'Internal Server Error',
            }
        return JsonResponse(response)


class UserView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserView, self).dispatch(request, *args, **kwargs)

    # Fetch tournament details
    def get(self, request):
        quaryset = User.objects.all()
        user_list = list()
        for i in quaryset:
            user_list.append(model_to_dict(i))

        print(user_list)
        return JsonResponse(user_list, safe=False)


class TournamentView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(TournamentView, self).dispatch(request, *args, **kwargs)

    # Fetch tournament details
    def get(self, request):
        quaryset = HostTournament.objects.all()
        tournament = list()
        for i in quaryset:
            tournament.append(model_to_dict(i))

        print(tournament)
        return JsonResponse(tournament, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body.decode("UTF-8"))
            print(data)
            tournament = HostTournament.objects.create(**data)

            response = {
                'status': 200,
                'type': '+OK',
                'message': 'Successfully Signed Up',
            }
        except IntegrityError as e:
            print(e)
            response = {
                'status': 501,
                'type': '-ERR',
                'message': 'Same Username or Email',
            }
        except Exception as e:
            print(e)
            response = {
                'status': 500,
                'type': '-ERR',
                'message': 'Internal Server Error',
            }
        return JsonResponse(response)


class GroundView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(GroundView, self).dispatch(request, *args, **kwargs)

    # Fetch Ground details
    def get(self, request):
        quaryset = Ground.objects.all()
        ground_list = list()
        for i in quaryset:
            ground_list.append(model_to_dict(i))

        print(ground_list)
        return JsonResponse(ground_list, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body.decode("UTF-8"))
            print(data)
            ground = Ground.objects.create(**data)

            response = {
                'status': 200,
                'type': '+OK',
                'message': 'Successfully Signed Up',
            }
        except IntegrityError as e:
            print(e)
            response = {
                'status': 501,
                'type': '-ERR',
                'message': 'Same Username or Email',
            }
        except Exception as e:
            print(e)
            response = {
                'status': 500,
                'type': '-ERR',
                'message': 'Internal Server Error',
            }
        return JsonResponse(response)
