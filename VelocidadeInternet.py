import speedtest


test = speedtest.Speedtest()
down = test.download()
up = test.upload()


print(f"Download speed: {down}")
print(f"Uoload speed: {up}")