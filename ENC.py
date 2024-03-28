import os, sys
try:
    __import__("ENC").main()
except Exception as e:
    exit(str(e))
