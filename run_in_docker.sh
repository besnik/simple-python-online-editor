
# run image as container named "py", mount code to tmp dir from host to container, execute, output content to file on host
echo "running python image and code"
docker run --name py -v /tmp/code.py:/tmp/code.py python:3.5.2-alpine python /tmp/code.py > /tmp/code.out 2>&1

# make sure there is no container with name "py"
echo "removing container so we can run it next time"
docker rm py > /dev/null 2>&1

echo "done"

# > file redirects stdout to file
# 2>&1 redirect stderr to stdout - we want this to get also error messages of compiler

