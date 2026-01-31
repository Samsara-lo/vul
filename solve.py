#!/usr/bin/env python3
"""
readflag solver - 作为 payload 在服务器上运行
"""
import subprocess
import sys

def solve():
    try:
        # 启动 readflag
        p = subprocess.Popen(
            ['/readflag'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # 读取输出直到看到表达式
        output = ""
        while True:
            char = p.stdout.read(1)
            if not char:
                break
            output += char
            if "input your answer:" in output:
                break
        
        print(f"[DEBUG] Output: {output}", file=sys.stderr)
        
        # 找到表达式 ((((...)))
        lines = output.split('\n')
        expr = None
        for line in lines:
            if line.strip().startswith('('):
                expr = line.strip()
                break
        
        if not expr:
            print("[ERROR] No expression found", file=sys.stderr)
            return
        
        print(f"[*] Expression: {expr}", file=sys.stderr)
        
        # 计算结果
        result = eval(expr)
        print(f"[*] Result: {result}", file=sys.stderr)
        
        # 发送答案
        p.stdin.write(str(result) + "\n")
        p.stdin.flush()
        
        # 读取 flag
        remaining = p.stdout.read()
        print(remaining)
        
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)

if __name__ == '__main__':
    solve()
