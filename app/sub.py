import subprocess

output_str = subprocess.run(["ping", "-c", "5", "0.0.0.0"], capture_output=True, text=True).stdout

print(output_str)
