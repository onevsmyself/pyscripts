import subprocess
import sys

def pythonwinbash(source_file, output_file, flags):
    command = ["gcc", source_file, "-o", output_file]
    
    if flags:
       command.extend(flags)
    
    compile_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error1 = compile_process.communicate()

    command = f"./{out}.exe"
    #print(command)
    run_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error2 = run_process.communicate()
    
    if error1:
       return 0, f"{error1.decode('utf-8')}"
    elif error2:
       return 0, f"{error2.decode('utf-8')}"
    else: 
       return 1, "Окей"


src = sys.argv[1]
out = "app"

find = 1
rc = 1

iters_min = 1
iters_max = 1000000000000000000000000
iters_cur = (iters_min + iters_max) // 2

while find:
    flags = ["-std=c99" ,"-Wall", "-Werror"]
    flags.append(str(f"-DN={iters_cur}"))
    print(flags, iters_max, iters_cur, iters_min)
    rc, result = pythonwinbash(src, out, flags)

    if iters_min >= iters_max or iters_max - iters_min < 1024 * 8:
      find = 0
    elif rc == 1:
      iters_min = iters_cur
      iters_cur = (iters_min + iters_max) // 2
    else:
      iters_max = iters_cur
      iters_cur = (iters_min + iters_max) // 2

print(result)
print(iters_cur)
