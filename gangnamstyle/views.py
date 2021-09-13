from rest_framework.views import APIView
from django.http import JsonResponse
from .stylegan2_tf import projector as projector_tf
#from .stylegan2 import projector

class Gangnam_Style(APIView):
    def post(self, request):
        # https://www.python2.net/questions-894144.htm  
        # 요거 보고 하려는데 잘 이해가 안됩니다 ㅠ

        # TODO : try except 처리 (status 400)
        jsonData = request.data[0]
        image = jsonData['image']
        gender = jsonData['gender']
        feature = jsonData['feature']

        if feature == 1:
            projector_tf.project(
                network_pkl="gangnamstyle/stylegan2/asian_tf.pkl",
                seed=303,
                outdir="./",
                save_video=False,
                base64str=image,
            )
            """
            projector.run_projection(
                network_pkl="gangnamstyle/stylegan2/asian_tf.pkl",
                seed=303,
                outdir="./",
                num_steps=1000,
                save_video=False,
                base64str=image,
            )
            """


        # TODO : projector.py의 함수 여기에 넣기
        # toonify 코드를 참고하기 (로컬에서 왜 안돌아가니ㅠ)
        data = {
            "image": image,
            "response": 1,#if response==1, status 200
        }
        return JsonResponse(data, status=200)
