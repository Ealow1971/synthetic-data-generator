from generator.tabular import SyntheticTabularGenerator

gen = SyntheticTabularGenerator({'age': 'int', 'income': 'float'})
df = gen.generate(500)
print(df.head())
