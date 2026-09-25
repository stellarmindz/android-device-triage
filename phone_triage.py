import subprocess

raw_output = subprocess.check_output(["adb", "shell", "getprop", "ro.product.model"])
clean_model = raw_output.decode("utf-8").strip()
print(clean_model)

