import subprocess
import time
import glob
import sys

#show_jude_status
arg = {"show_jude_status": False}
def get_arg():
    if len(sys.argv) != 1:
        args = sys.argv[1:]
        for a in args:
            arg[str(a)] = True

def print_error(error):
    print(f"\033[31m{error}\033[0m")

def compile_ans():
    files = glob.glob("../answer/*.cpp")
    for file in files:
        f_name = file.replace(".cpp", "")
        subprocess.run(f"g++ -o {f_name} {file} -std=c++17", shell=True)#要変更

def check_status(code, status):
    if "AC" in code:
        if status["WA"] != 0:
            print_error(f"WA in {code}")
        if status["TLE"] != 0:
            print_error(f"TLE in {code}")
    if "WA" in code:
        if status["WA"] == 0:
            print_error(f"no WA in {code}")
    if "TLE" in code:
        if status["TLE"] == 0:
            print_error(f"no TLE in {code}")

def execute_code(code, output_ans = False, TLE = 2):
    if len(glob.glob("./temp_out")) != 0:
        subprocess.run(f"rm -r temp_out", shell=True)
    subprocess.run(f"mkdir temp_out", shell=True)
    files = glob.glob("../in/*")
    status = {"AC": 0, "TLE":0, "WA":0}
    max_time = 0
    #cpp
    if ".cpp" in code:
        exec_code = code.replace(".cpp", "")
        for file in files:
            start = time.time()
            name = file
            name = name.replace("../in/", "")
            now_status = "AC"
            try:
                if output_ans:
                    subprocess.run(f"cat ../in/{name} | {exec_code} > ../out/{name}", shell=True, timeout=TLE)
                else:
                    subprocess.run(f"cat ../in/{name} | {exec_code} > temp_out/{name}", shell=True, timeout=TLE)
                    a = subprocess.check_output(f"cat temp_out/{name}", shell=True).decode('utf-8')
                    b = subprocess.check_output(f"cat ../out/{name}", shell=True).decode('utf-8')
                    if a == b:
                        status["AC"] += 1
                    else:
                        status["WA"] += 1
                        now_status = "WA"
            except subprocess.TimeoutExpired as e:
                status["TLE"] += 1
                now_status = "TLE"
            end = time.time()
            if arg["show_jude_status"]:
                print(f"{name}: {int((end - start) * 1000)}ms status: {now_status}")
            max_time = max(max_time, int((end - start) * 1000))
    #python
    if ".py" in code:
        for file in files:
            start = time.time()
            name = file
            name = name.replace("../in/", "")
            now_status = "AC"
            try:
                if output_ans:
                    subprocess.run(f"cat ../in/{name} | python3 {code} > ../out/{name}", shell=True, timeout=TLE)
                else:
                    subprocess.run(f"cat ../in/{name} | python3 {code} > temp_out/{name}", shell=True, timeout=TLE)
                    a = subprocess.check_output(f"cat temp_out/{name}", shell=True).decode('utf-8')
                    b = subprocess.check_output(f"cat ../out/{name}", shell=True).decode('utf-8')
                    if a == b:
                        status["AC"] += 1
                    else:
                        status["WA"] += 1
                        now_status = "WA"
            except subprocess.TimeoutExpired as e:
                print(e)
                status["TLE"] += 1
                now_status = "TLE"
            end = time.time()
            if arg["show_jude_status"]:
                print(f"{name}: {int((end - start) * 1000)}ms status: {now_status}")
            max_time = max(max_time, int((end - start) * 1000))
    if not output_ans:
        print(f"code: {code}\n  結果: {status}\n  実行時間: {max_time}ms")
    check_status(code, status)
    subprocess.run(f"rm -r temp_out", shell=True)

def make_correct_ans():
    subprocess.run(f"rm ../out/*", shell=True)
    codes = glob.glob("../answer/*.cpp")
    for code in codes:
        if "AC" not in code:
            continue
        execute_code(code, True)

def execute_ans():
    codes = glob.glob("../answer/*")
    codes = [code for code in codes if "." in code.replace("..", "")]
    for code in codes:
        execute_code(code)

def validate_input():
    subprocess.run(f"g++ -o validate_in validate_in.cpp -std=c++17", shell=True)#要変更
    files = glob.glob("../in/*")
    for file in files:
        a = subprocess.check_output(f"cat {file} | ./validate_in", shell=True).decode('utf-8')
        if "WA" in a:
            print(f"bad input: {file}")

def validate_output():
    subprocess.run(f"g++ -o validate_out validate_out.cpp -std=c++17", shell=True)
    files = glob.glob("../out/*")
    for file in files:
        a = subprocess.check_output(f"cat {file} | ./validate_out", shell=True).decode('utf-8')#要変更
        if "WA" in a:
            print(f"bad output: {file}")

if __name__ == '__main__':
    get_arg()
    compile_ans()
    validate_input()
    make_correct_ans()
    validate_output()
    execute_ans()
