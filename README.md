## Introduction
\[WARNING\] This is more of a journal of this project. It doesn't assume any prior machine learning/technology experience.

### It's a wonderful day, life just misses the right song playing in the background.

The inspiration of this project is for myself to find new songs, not just based on artist or music genre but lyrics.
People ask themselves if the music is more important or are the lyrics. I can't tell for sure - for some, I'm drawn by the music, for example, songs in other languages which I don't understand but I'm also often paying close attention to the lyrics.
Intent of this project is to discover more songs that I haven't listened to which semantically "discuss" the plight of human condition, like Bitter Sweet Symphony. Another idea is to find "motivating" songs which can be my ring/alarm tone(s).
Intended approach is:
- Get a dataset of lyrics
- Process lyrics into semantic [embeddings](https://cloud.google.com/blog/topics/developers-practitioners/meet-ais-multitool-vector-embeddings) In over-simplified words, an embedding is a representation of text into a series of numbers which a machine can do "something" with.
- Process these embeddings to find how similar two songs are and store this information (ahem, efficiently/sensibly)
- Create a UI where I can explore the songs and find which songs are similar in terms of gravitas of the lyrics, and try them out

Easy-peasy, fellas! Stay with me! ;)

### Prerequisites

- A general overview of what large language models/transformer models can do, but we can live happily without it too.
- A bit of patience since the current state of the project is unfortunately really just a collection of Jupyter Notebooks + Data Dump, although I promise you, I'm working on improving it. I also hope that since I tried to keep the notebooks succinct, they should not be difficult to follow.
- Hope that we'll find what we're looking for and/or something interesting, because why bother otherwise?! :)

### Initial Approach

- I plan to do some *sanity checks* first, for example:
    - Can I get lyrics dataset readily or do I need to scrape azlyrics or a similar website?
    - Does the lyrics data actually contain sensible lyrics, etc.?
    - Are there pre-trained language models available to convert lyrics to [embeddings](https://cloud.google.com/blog/topics/developers-practitioners/meet-ais-multitool-vector-embeddings)?
    - Are these embeddings actually translating similar lyrics into "similar" embeddings?
    - ...
- Now I want to have a feeling of how much I need to build on what's already available and what needs to be done there. The first step is to patch something together then try to diagnose issues and improve from there. I spent quite some time here, basically processing my thoughts.

## Let's go!
### Hunt for a dataset
- Lyrics dataset - I found something: [Kaggle Song Lyrics Dataset](https://www.kaggle.com/datasets/deepshah16/song-lyrics-dataset)
- Yayy, let's download and have a deeper look. You can find the downloaded data at the directory `data/raw/lyrics`
#### Findings/Observations
- There are songs in many languages, so I'd need to know all possible languages present and ensure that those languages are handled by one or more language models.
- Some songs don't have lyrics, or some standard text as lyrics like "unreleased".
- Unfortunately for me, the artists present are too mainstream for my taste, but I like songs from almost all of these artists. I can still rely on this dataset for now to get to basic setup
- For the whole analysis, please refer to `01_LyricsDataset.ipynb` notebook. The results should already be present as output.

## Resources found that seems to be promising
### Model for Language Detection:
[Hugging Face XLM-RoBERTa transformer model fine-tuned for Language Identification](https://huggingface.co/papluca/xlm-roberta-base-language-detection)

### Model for deriving embeddings for the lyrics of the songs:
[Hugging Face all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)

### Dataset:
[Kaggle Song Lyrics Dataset](https://www.kaggle.com/datasets/deepshah16/song-lyrics-dataset)
