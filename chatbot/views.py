# chatbot/views.py
from django.http import JsonResponse
# import ollama  # 确保已安装 ollama 库: pip install ollama

def chatbot_response(request):
    if request.method == 'POST':
        user_query = request.POST.get('query')
        print("user question: ",user_query)
        if user_query:
            try:
                # # 与 Ollama 模型交互
                # response = ollama.chat(
                #     model='llama2',  #  指定要使用的 Ollama 模型名称 (例如 llama2, mistral, etc.)
                #     messages=[
                #         {
                #             'role': 'user',
                #             'content': user_query,
                #         },
                #     ]
                # )
                # chatbot_reply = response['message']['content']
                # return JsonResponse({'reply': chatbot_reply})
                return JsonResponse({'reply': "这是一条测试信息返回, this is a test message return"})
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500) # 返回错误信息, 状态码 500 (服务器错误)
        else:
            return JsonResponse({'error': 'Query cannot be empty'}, status=400) # 返回错误信息, 状态码 400 (客户端错误 - 请求错误)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405) # 返回错误信息, 状态码 405 (方法不允许)