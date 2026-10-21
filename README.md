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
Since I am building a *Music Recommender Simulation*, my system will prioritize using Content-Based Filtering. I can create a User Profile that will store what the user likes. I can use the User Profile to recommend songs to the user. If possible we can also add a Collaborative-Filtering approach. I believe that will require gathering more user data. So for now my version will prioritize a CBF approach. Will see how much it changes.

AI - Answer; Need to evaluate
Real-world platforms like Spotify and TikTok blend collaborative filtering (learning from what many users do, such as plays, skips, and shares) with content-based filtering (learning from song attributes). My simulation will prioritize content-based filtering. It needs no data from other users, and it is easy to explain why a song was recommended. A `UserProfile` stores what the user likes, and each song is scored by how closely its features match that profile. I may add collaborative filtering later, but it would require data from many users.


### List the specific features your Song and UserProfile objects will use in your simulation.
**Song:** `genre`, `mood`, `energy`, `tempo_bpm`, `valence`, `danceability`, `acousticness` (plus `id`, `title`, and `artist` for identification).

**UserProfile:** `favorite_genre`, `favorite_mood`, `target_energy`, and `likes_acoustic`.

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

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
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



