### Model for Language Detection:
[Hugging Face XLM-RoBERTa transformer model fine-tuned for Language Identification](https://huggingface.co/papluca/xlm-roberta-base-language-detection)

### Dataset:
[Kaggle Song Lyrics Dataset](https://www.kaggle.com/datasets/deepshah16/song-lyrics-dataset)



### Introduction
#### 2022-08-31: It's a wonderful day, life just misses the right song playing in the background.
The inspiration of this project is for myself to find new songs, not just based on artist or music genre but lyrics.
People ask themselves if the music is more important or are the lyrics. I can't tell for sure - for some, I'm drawn by the music, for example, songs in other languages which I don't understand but I'm also often paying close attention to the lyrics.
Intent of this project is to discover more songs that I haven't listened to which semantically "discuss" the plight of human condition, like Bitter Sweet Symphony.
Intended approach is:
- Get a dataset of lyrics
- Process lyrics into semantic vectors
- Process vectors to find similarity and store the similarity matrix (ahem, efficiently/sensibly)
- Create a UI where I can explore the songs and find which songs are similar in terms of gravitas of the lyrics, and try them out


#### 2022-09-01: Sanity checks:
* Can I get lyrics dataset readily or do I need to scrape azlyrics or a similar website?:
    - df 