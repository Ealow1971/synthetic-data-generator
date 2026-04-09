import pandas as pd
import numpy as np

class TabularGenerator:
    def generate_noise(self, rows, cols):
        return np.random.normal(0, 1, (rows, cols))

    def generate_data(self, n_samples=1000):
        data = {
            "age": np.random.randint(18, 80, n_samples),
            "income": np.random.normal(50000, 15000, n_samples),
            "active": np.random.choice([0, 1], n_samples)
        }
        return pd.DataFrame(data)

if __name__ == "__main__":
    gen = TabularGenerator()
    df = gen.generate_data()
    print(df.head())
# SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS









