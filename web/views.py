from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from . engine import run_in_docker

def index(request):
    context = {}
    return render(request, 'web/index.html', context)

def execute(request):
    code = request.body.decode() + "\n"
    
    input_name = settings.INPUT_FILE_PATH
    output_name = settings.OUTPUT_FILE_PATH
    shell_script = settings.RUN_IN_DOCKER_SH_PATH
    
    # run in docker
    result = run_in_docker(input_name, code, shell_script, output_name)
    # enable pretty html formatting and obfuscate input file name with 'source'
    result = result.replace('\n', "<br>").replace(input_name, "source")

    return JsonResponse({'result':result})
