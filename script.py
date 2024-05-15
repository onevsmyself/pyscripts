import subprocess
import sys

def python_win_bash(source_file, output_file, flags):
   command = ["gcc"]
    
   if flags:
      command.extend(flags)
   command.extend(["-o", output_file, source_file])

   compile_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   output, error1 = compile_process.communicate()

   if compile_process.returncode != 0:
      return 0, f"{error1.decode('utf-8')}"

   command = [f"./{out}"]

   run_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   output, error2 = run_process.communicate()
    
   #  if error1:
   #     return 0, f"{error1.decode('utf-8')}"
   if run_process.returncode != 0:
      return 0, f"{error2.decode('utf-8')}"
   else: 
      return 1, "Окей"


src = sys.argv[1]
out = "app.exe"

find = 1
rc = 1

iters_min = 1
iters_max = 1000000000000000000000000
iters_cur = (iters_min + iters_max) // 2

while find:
    flags = ["-std=c99" ,"-Wall", "-Werror"]
    flags.append(str(f"-DN={iters_cur}"))
    print(iters_min, iters_cur, iters_max)
    rc, result = python_win_bash(src, out, flags)

    if iters_min >= iters_max or iters_max - iters_min < 2:
      find = 0
    elif rc == 1:
      iters_min = iters_cur + 1
      iters_cur = (iters_min + iters_max) // 2
    else:
      iters_max = iters_cur - 1
      iters_cur = (iters_min + iters_max) // 2

print(result)
print(iters_cur)
