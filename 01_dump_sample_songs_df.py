import os
import pandas as pd

source_relative_path = "data/raw/sample_songs"
destination_relative_path = "data/intermediate"
output_file_name = "sample_songs_df.tsv"

if not os.path.exists(destination_relative_path):
    os.makedirs(destination_relative_path)

cwd = os.getcwd()

df = pd.DataFrame(columns=["Song", "Lyrics"])
for file in os.listdir("./" + source_relative_path):
    with open(os.path.join(cwd, source_relative_path, file), 'r') as f:
        lines = f.readlines()
        lyrics = " ".join(lines)
        song = file[:-4]
        song_df = pd.DataFrame({"Song":[song], "Lyrics": [lyrics]})
        df = pd.concat([df, song_df])
        del song_df, lines, lyrics, song

print(df.head())
df.to_csv(os.path.join(cwd, destination_relative_path, output_file_name), sep="\t", index=False)
