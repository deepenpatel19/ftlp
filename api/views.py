from __future__ import unicode_literals
import json
from django.db import IntegrityError
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, HostTournament, Ground
from django.forms.models import model_to_dict


class Signup(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Signup, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        try:
            data = json.loads(request.body.decode("UTF-8"))
            print(data)
            user = User.objects.create(**data)

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
                                                                              'profile',
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
        return super(Ground, self).dispatch(request, *args, **kwargs)

    # Fetch Ground details
    # def get(self, request):

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