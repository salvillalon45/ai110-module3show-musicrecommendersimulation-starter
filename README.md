# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

### How Real World Recommendations System Work?
Platforms like Spotify, Youtube, and TikTok use a combination of filtering methods. The filtering methods are Collaborative Filtering (CF) and Content-Based Filtering (CBF).

#### Collaborative Filtering (CF)
It focuses on **people like you, lke this**. To accomplish this,  it ignores a song and only looks at user behavior. The user behavior is uses is actions such as plays, skips, like, saves, playlist adds, repeat listens, .etc. 

It can do a **User-Based** filtering where it finds users with similar histories to yours, then recommend what they liked and you haven't heard.

Also an **Item-Based** filtering where it find songs that tend to be liked by the same people, then recommend songs "near" the ones you already like.

##### Strengths and Weakness of Collaborative Filtering
Strenghts:
- is that it does not need knowledge of the music itself since it focuses on looking at behavior and other songs that people like as well.
Weakness:
- is that there is a popularity bias where more popular songs will be recommended more 
- It has a Cold Start where a brand new song or brand new user has no behavior data so it might not be recommended 

#### Content-based Filtering (CBF)
It focuses on **more like what you liked**. To accomplish this, it looks at the attributes of songs and matches them to your taste profile. Attributes include genre, tempo (BPM), energy, danceability, valence (mood), acousticness, key, artist, lyrics, and audio-derived features. 

With all those attributes **it creates a profile** from the features of songs you liked, then ranks other songs by similarity to it.

##### Strengths and Weakness of Content-based Filtering (CBF)
Strengths:
- It needs no other user data. This is great since it protect user privacy
- Its transparent and explainable because you like high-energy, upbeat tracks then it will recommend those type of songs
Weakness:
- It has a filter bubble since it will only recommend thingssimilar to what you already liked

### How Do Real World Platforms Use Them?
**Spotify** uses a combination of CBF and CF to create the Discover Weekly and Release Radar playlists. Spotify does a audio analysis of the track and Natural Language Processing on text such as blogs, playlists, titles, and metadata. The audio and text help new songs with little listening data get discovered.

**TikTok and Youtube** lean heavily on behavioral signals suchs as watch time, replays, shares, and skips in Collaborative Filtering approach. They use content understanding (video, audio, captions, hashtags) so new videos can be tested on small audiences. TikTok's For You feature is very behavior driven. This is why it updates and adapts very fast.

### What My Version Will Prioritize
Real-world platforms like Spotify and TikTok blend *Collaborative Filtering* (learning from what many users do, such as plays, skips, and shares) with *Content-Based Filtering* (learning from song attributes).

For this project, I want to prioritize *Content-Based Filtering*. This is because it needs no data from other users, and it is easy to explain why a song was recommended. This benefits me since currently I do not have a lot of data from other users, but I do have data from songs in the CSV.

A `UserProfile` stores what the user likes, and each song is scored by how closely its features match that profile. I may add Collaborative Filtering later, but it would require data from many users.

### List the specific features your Song and UserProfile objects will use in your simulation.
**Song:** `genre`, `mood`, `energy`, `tempo_bpm`, `valence`, `danceability`, `acousticness` (plus `id`, `title`, and `artist` for identification).

**UserProfile:** `favorite_genre`, `favorite_mood`, `target_energy`, and `likes_acoustic`.

### The Algorithm Recipe
This is the scoring weights that will be used against comparing songs:
```json
"weights": {
    "genre": 2.0,
    "mood": 1.0,
    "energy": 2.0,
    "tempo": 1.0,
    "acousticness": 1.0,
    "valence": 0.5,
    "danceability": 0.5,
}
```

**Calculating Score Notes**

- Categorical (genre, mood): 1 for a match, 0 otherwise.
- Numeric: `1 - abs(song - target)`. For tempo, divide the difference by about 100 first so that it can be a number between `0 - 1`.
- Score: `sum(weight × feature_score) / sum(weights)`. This gives a 0–1 score.
- Output: Rank all songs by score and return the top N, with a short explanation of the top features.


**Potential Biases Notes**

- The system may over prioritize genre so a song that matches the user's mood and numeric taste can rank below a weaker song in the right genre.

- Exact match moods ignore related moods (for example "focused" vs "chill").

- Mood overlaps with energy, tempo, and acousticness so it can be counted twice.

- Currently the profile only holds on favorite genre and mood so it cannot capture mixed taste (going to see if this can be change to support mixed taste).

- The system will be use *Content-Based Filtering* so it will look onl at song attributes to determine what the user likes.

- This is a small dataset which might favor some profile over others.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output
The output below is based on a User Profile of:

```python
user_prefs = {
  "genre": "pop",
  "mood": "happy", 
  "energy": 0.8
}
```

```bash
Loaded 20 songs from data/songs.csv

==================================================
  TOP RECOMMENDATIONS
==================================================

#1  Sunrise City by Neon Echo
    Score: 0.99 / 1.00
    Reasons:
      - genre match (+2.0)
      - mood match (+1.0)
      - energy closeness (+1.96 of 2.0)

#2  Gym Hero by Max Pulse
    Score: 0.75 / 1.00
    Reasons:
      - genre match (+2.0)
      - energy closeness (+1.74 of 2.0)

#3  Rooftop Lights by Indigo Parade
    Score: 0.58 / 1.00
    Reasons:
      - mood match (+1.0)
      - energy closeness (+1.92 of 2.0)

#4  Concrete Crown by Verse Alley
    Score: 0.39 / 1.00
    Reasons:
      - energy closeness (+1.96 of 2.0)

#5  Night Drive Loop by Neon Echo
    Score: 0.38 / 1.00
    Reasons:
      - energy closeness (+1.90 of 2.0)

==================================================
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



