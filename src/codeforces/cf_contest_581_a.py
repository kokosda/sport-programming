a, b = map(int, input().split())
stereo, mono = 0, 0

stereo = min(a, b)
mono = (max(a, b) - stereo) // 2

print(stereo, mono)