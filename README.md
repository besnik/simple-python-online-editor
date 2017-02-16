# Online Editor

Python Online Editor implemented using Django and Docker

![alt tag](https://raw.githubusercontent.com/besnik/online-editor/master/web/static/web/images/online-editor-screenshot.png)

Goal of this project is to create online editor for any technology you can run in docker container.

Current proof of concept is focusing on python online editor however concept is generic and works
with anything that runs inside docker container.

# Installation

You might want to create or activate python virtual environment.

1. Get source codes:

   ```
   git clone git@github.com:besnik/online-editor.git
   cd online-editor
   ```

2. Install dependencies
 
   Install python libraries to run application. On some distros you need to use `pip3`.

   `pip install django`

   Install docker. You can type `docker ps` to see if you have docker installed.
   See https://docs.docker.com/engine/installation/ for steps for your OS.

   You might want to pull docker image to avoid automatic pull with first execution
   `docker pull python:3.5.2-alpine`


3. Run

   Start django dev server by typing:
   
   `python manage.py runserver 8080`

   For Python 3 on some linux distros use `python3` instead of `python`.


4. Open your browser

   and type url `http://localhost:8080`

# Architecture

We use container virtualization to isolate code execution from the host. Our platform of choice
is docker but concept should very well run with rocket as well.

Entry point to the editor is simple django frontend app with single responsive page that acts
as presenaton layer between user and commands executed in container.

By clicking submit button there is ajax post request to the server where the code is executed in
docker container. The container is run with every request and stopped after exection of code 
is finished.

# Data flow

```
browser -> (ajax post req) -> django page -> (stores file in /tmp/code.py) -> 
docker run -> (execute code) -> (store result in /tmp/code.out) -> 
(response to browser) -> browser callback (update UI)
```

Currently the python execution is based on `Python Alpine Linux` docker images.
See `run_in_docker.sh` for details which docker image is used.
 
# Implementation

Current implementation is pretty naive and needs improvements on all fronts.
Compared to other online (and paid) solution the execution even on localhost is ~2-3 times slower (1s-1.5s vs 3s).
There are many improvements that could be done. I am listing some ideas I'd like to implement next:

- pool of containers (similar concept to pool of connections to db. currently we are loosing time with starting and stopping containers.)
- limit execution time of command in container
- cut off container from internet communication (disallow connecting from container to third parties).
- limit currently executing commands by implementing queue (with Rabbit MQ or Redis).
- current impl is heavily based on files. Leverage stdin and stdout to optimize input/output
- configure container and exec command (basically allow any code to be executed using online editor framework).
- provide pre-configured configurations for most popular languages like Node.js, Go, Python, C++, Java, C#, Linux shell and others.

# Feedback

I would love to hear feedback on this work. Do not hesitate and reach out to me with any questions or comments.
