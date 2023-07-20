import pandas as pd
import numpy as np

class SyntheticTabularGenerator:
    def __init__(self, schema: dict):
        self.schema = schema

    def generate(self, n_samples: int = 1000) -> pd.DataFrame:
        data = {}
        for col, dtype in self.schema.items():
            if dtype == 'int':
                data[col] = np.random.randint(0, 100, n_samples)
            elif dtype == 'float':
                data[col] = np.random.randn(n_samples)
        return pd.DataFrame(data)
