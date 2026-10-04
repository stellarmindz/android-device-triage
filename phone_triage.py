import subprocess

raw_output = subprocess.check_output(["adb", "shell", "getprop", "ro.product.model"])
clean_model = raw_output.decode("utf-8").strip()
print(clean_model)

# Prints the model of the phone connected to the computer via adb
def get_property(prop_name):
    raw_output = subprocess.check_output(["adb", "shell", "getprop", prop_name])
    clean_property = raw_output.decode("utf-8").strip()
    return clean_property

# Test the function for these properties
brand = get_property("ro.product.brand")
model = get_property("ro.product.model")
version = get_property("ro.build.release.version")
serial = get_property("ro.serialno")
print(f"Brand: {brand}, Model: {model}, Version: {version}, Serial: {serial}")



