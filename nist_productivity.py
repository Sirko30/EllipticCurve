import time
import matplotlib.pyplot as plt
import pandas as pd
from ecdsa import SigningKey, NIST256p, NIST384p, NIST521p


def measure_performance(curve, curve_name):
    start_time = time.time()
    private_key = SigningKey.generate(curve=curve)
    key_gen_time = time.time() - start_time

    start_time = time.time()
    signature = private_key.sign(b"Hello, world!")
    sign_time = time.time() - start_time

    public_key = private_key.verifying_key
    start_time = time.time()
    is_valid = public_key.verify(signature, b"Hello, world!")
    verify_time = time.time() - start_time

    security_bits = curve.baselen * 8 // 2

    return {
        "curve": curve_name,
        "key_size_bits": curve.baselen * 8,
        "security_bits": security_bits,
        "key_gen_time_sec": key_gen_time,
        "sign_time_sec": sign_time,
        "verify_time_sec": verify_time,
    }


curves = {
    "NIST256p": NIST256p,
    "NIST384p": NIST384p,
    "NIST521p": NIST521p,
}

results = []
for curve_name, curve in curves.items():
    result = measure_performance(curve, curve_name)
    results.append(result)

df = pd.DataFrame(results)

df["key_gen_change"] = df["key_gen_time_sec"] / df["key_gen_time_sec"].iloc[0]
df["sign_change"] = df["sign_time_sec"] / df["sign_time_sec"].iloc[0]
df["verify_change"] = df["verify_time_sec"] / df["verify_time_sec"].iloc[0]

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

print("Порівняння продуктивності:")
print(df)

plt.figure(figsize=(12, 6))
plt.plot(df["key_size_bits"], df["key_gen_time_sec"], label="Генерація ключів", marker="o")
plt.plot(df["key_size_bits"], df["sign_time_sec"], label="Створення підпису", marker="o")
plt.plot(df["key_size_bits"], df["verify_time_sec"], label="Перевірка підпису", marker="o")
plt.title("Порівняння продуктивності для різних кривих")
plt.xlabel("Розмір ключа (біт)")
plt.ylabel("Час (с)")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(df["curve"], df["security_bits"], color=["blue", "orange", "green"])
plt.title("Стійкість кривих")
plt.xlabel("Крива")
plt.ylabel("Стійкість (біт)")
plt.show()
