import subprocess
import sys

def pythonwinbash(source_file, output_file=None, flags=None):
    if not output_file:
        output_file = source_file.rsplit('.', 1)[0]
    command = ["gcc", source_file, "-o", output_file]
    
    if flags:
       command.append(flags)
    
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    
    if error:
       return 0, "Ошибка!"
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
print(iters_cur) # // 1024 // 1024 // 1024 // 1024 // 1024 // 8
