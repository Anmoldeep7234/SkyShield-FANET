import os

print("=" * 60)
print("SkyShield FANET Security System")
print("=" * 60)

print("\n1. Running Network Simulation")
os.system("python main.py")

print("\n2. Generating Dataset")
os.system("python src/dataset_generator.py")

print("\n3. Running Security Engine")
os.system("python src/security_engine.py")

print("\n4. Generating Benchmarks")
os.system("python src/benchmark_generator.py")

print("\n5. Calculating Metrics")
os.system("python src/network_metrics.py")

print("\nSystem Execution Completed")