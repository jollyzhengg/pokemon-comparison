import pandas as pd

# Load the dataset
df = pd.read_csv("pre-process-data/pokemon.csv")

#limiting to just generation 1 pokemons
df = df[df["generation"] == 1]



#removing columns
df = df.drop(columns=['abilities', 'base_egg_steps','base_total', 'capture_rate',
                       'japanese_name', 'percentage_male', 'experience_growth', 
                       'generation'])


#all columns with types
type_columns = df.columns[:18]

def categorize_effectiveness(row):

    super_effective = [t.replace("against_", "") for t in type_columns if row[t] == 4]
    effective = [t.replace("against_", "") for t in type_columns if row[t] == 2]
    
    resistant_to = [t.replace("against_", "") for t in type_columns if row[t] == 0.25]
    not_effective = [t.replace("against_", "") for t in type_columns if row[t] == 0.5]

    effective_sorted = ", ".join(super_effective + effective)
    not_effective_sorted = ", ".join(resistant_to + not_effective)

    return pd.Series([effective_sorted, not_effective_sorted])


# dataframe now with effective and not effective
df[["effective", "not_effective"]] = df.apply(categorize_effectiveness, axis=1)

df = df.drop(df.columns[:18], axis=1)

df= df[['name', 'pokedex_number', 'classfication', 'type1', 'type2', 'is_legendary',
         'height_m', 'weight_kg', 'base_happiness', 'hp', 'attack', 'defense',
           'sp_attack', 'sp_defense', 'speed',
             'effective','not_effective' ]]

# Save the updated dataset
df.to_csv("post-process-data/pokemon_dataset.csv", index=False)

