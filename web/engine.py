import subprocess

# saves content to file with given name
def save_as_file(file_name, content):
    with open(file_name, 'w') as f:
        f.write(content)

def read_output(file_name):
    with open(file_name, 'r') as f:
        return f.read()

# execute file in docker container and return output as string
def call_docker(command):
    process = subprocess.run(command, shell=True, stderr=subprocess.STDOUT, timeout=5, check=False)
    pass

# executes given code in a docker container
def run_in_docker(input_file, content, run_in_docker_sh_path, output_file):
    save_as_file(input_file, content)
    call_docker(run_in_docker_sh_path)
    return read_output(output_file)