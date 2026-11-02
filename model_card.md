# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

MusicSearch 1.0

---

## 2. Intended Use  

MusicSearch tries to suggest songs a listener will like. 
It does not predict a rating or a play count. It ranks every song in a small catalog by how well it fits a taste profile. 

The listener gives a profile, such as a favorite genre, a mood, and a target energy level. The system returns the top 5 songs, each with a short reason, such as "genre match" or "energy closeness."

**Intended use.** MusicSearch is for classroom exploration. It is a small project to learn how a recommender scores and ranks items. It assumes the listener can describe their taste in a few simple labels, like a genre, a mood, and an energy level. It is meant to be run by students who want to test profiles and see why each song was picked.

**Non-intended use.** It should not be used as a real music app or for real listeners. The catalog has only 20 made-up songs, so it can't serve real tastes. It should not be used to make decisions about people, such as what music to play in a store or what to promote to an artist. It also should not be treated as a fair or complete picture of music taste, since it favors genres and moods that have more songs and matches labels only exactly.

---

## 3. How the Model Works  

The recommender gives every song a score from 0 to 1 that shows how well it matches what a listener likes. A score of 1 is a perfect match and 0 is no match at all.

**What it looks at.** For each song it considers its genre, mood, energy, tempo, acousticness (how acoustic versus electronic it sounds), valence (how positive or upbeat it feels), and danceability.

**What the listener provides.** The listener gives a taste profile, such as "I like happy pop songs with fairly high energy." They don't have to fill in everything. The recommender only looks at the things they told it about.

**How a song earns points.**
- Genre and mood are all-or-nothing. If the song matches what the listener wants, it earns the points. If not, it earns none.
- For qualities like energy, tempo, and danceability, the closer the song is to what the listener wants, the more points it earns. A song that is exactly right earns full points, and one that is far off earns almost none.
- Not everything matters equally. Genre and energy count the most, mood, tempo, and acousticness count less, and valence and danceability count the least. A listener's profile can change these levels if they care about something differently.

**Putting it together.** The points from every feature are added up and compared to the most the song could have earned. That gives the final score. Every song in the collection is scored this way, the songs are ranked from highest to lowest, and the top few are recommended. Each recommendation also comes with a short list of reasons, such as "genre match" or "energy is very close," so the listener can see why it was picked.

**What changed from the starter code.** The starter version didn't score or rank anything and returned an empty result. I added the scoring rules above, the ranking of all songs, and the written reasons for each recommendation.

---

## 4. Data  

The catalog is a small file called `songs.csv` with 20 songs. Each song has a `title`, an `artist`, a `genre`, a `mood`, and five number features: `energy`, `tempo` (in beats per minute), `valence`, `danceability`, and `acousticness`. The number features run from 0 to 1, except tempo, which runs from 60 to 168.

**Genres and moods.** 

There are *17 genres*. Lofi has 3 songs and pop has 2. The other 15 genres have one song each, such as rock, jazz, metal, and country. 

There are *15 moods*. Chill has 3 songs, and happy, intense, and melancholic have 2 each. The rest have one.

**Energy is uneven.** 

Nine songs have energy of 0.4 or lower, and nine have 0.7 or higher. 

Only two songs sit between 0.5 and 0.6, and none sit between 0.

6 and 0.7. Listeners who want medium energy have very little to choose from.

**Changes to the data.** 

I added 10 more songs based on the assignment instructions.

**What is missing.** 

The catalog has no lyrics, language, release year, or artist popularity. It has no listening history, so it can't learn what a person actually plays. It also has only one or two songs for most genres, so it can't show much variety within a genre. The songs are made up for a class project, so the results say little about real music taste.

---

## 5. Strengths  

**It works well for clear, consistent tastes.** The three standard profiles (High-Energy Pop, Chill Lofi, and Deep Intense Rock) all got a sensible #1 pick. Their top scores were 0.95, 0.99, and 0.99. A listener who knows what they like, and whose genre, mood, and energy all agree, gets good results.

**It separates opposite tastes.** The pop and lofi profiles had no songs in common in their top 5. Pop got loud, danceable songs and lofi got quiet, acoustic ones. The scores react the way I would expect when the energy target changes.

**The runners-up make sense.** After the three lofi songs, Chill Lofi recommended an ambient chill song and a peaceful folk song. These are close neighbors of lofi. For Deep Intense Rock, the next picks were other loud, high-energy songs.

**It helps listeners with a rare mood.** Mood is worth points on its own. A listener who wants "nostalgic" gets Dust Road Home at the top with a score of 0.99, even though its energy is in the quiet middle of the catalog. A "melancholic" listener gets Blue Delta Nights first at 0.97. Without mood, these songs would be buried by the louder or quieter clusters.

**It explains itself.** Every recommendation lists its reasons, such as "genre match" or "energy closeness." This made it easy to find why a song ranked where it did, and it helped me spot the problems in my experiments.

**It is flexible.** A listener can give only the features they care about, and the scorer ignores the rest. The scores stay between 0 and 1 even with odd inputs, like an energy of 1.5.

---

## 6. Limitations and Bias 

One weakness I found is that the exact genre and mood matches can override the energy a user actually asked for. Together they are worth 3.0 of the 7.0 total weight, so a song that matches both labels can outrank a song with a much better energy fit. For example, a pop/happy user who asks for energy 0.3 still gets Sunrise City (energy 0.82) at #1 with a score of 0.79, and Gym Hero (energy 0.93) at #2, while the low-energy songs rank lower. The problem is made worse by a small dataset where 15 of the 17 genres have only one song, so a user whose genre or mood appears once gets a single guaranteed match and everything else is ranked on the numbers alone. Labels also only match exactly, so "relaxed" earns no credit for similar songs tagged "chill" or "peaceful", and "indie pop" earns none for a pop fan.

---

## 7. Evaluation  

### Profiles tested

I tested six profiles. Three were standard and three were adversarial, built to try to trick the scoring logic.

- **High-Energy Pop:** pop, happy, energy 0.9, tempo 128, acousticness 0.1
- **Chill Lofi:** lofi, chill, energy 0.35, tempo 75, acousticness 0.8
- **Deep Intense Rock:** rock, intense, energy 0.92, tempo 150, acousticness 0.1
- **Adversarial: Conflicting:** classical, sad, energy 0.9, valence 0.1 (a mood and a genre that pull away from the energy)
- **Adversarial: Impossible combo:** metal, peaceful, energy 0.1, tempo 60, acousticness 0.95 (a genre and mood that never occur together)
- **Adversarial: Out-of-range:** edm, euphoric, energy 1.5, tempo 400 (values outside the normal 0 to 1 range)

The three standard profiles behaved as expected. Each one ranked its own genre and mood match first, with scores of 0.95, 0.99 and 0.99.

### What surprised me

- **Gym Hero kept showing up.** It ranked #2 for both High-Energy Pop and Deep Intense Rock, and it also appeared in the top 5 of two adversarial profiles. It is a pop song with an "intense" mood and energy 0.93, so it gets credit from either the genre or the mood depending on the user.
- **The conflicting profile put a quiet song first.** A user asking for energy 0.9 got Moonlit Sonata (energy 0.22) at #1 because it was the only classical song. The genre match was worth more than a very large energy gap.
- **The "impossible" combo wasn't impossible.** The scorer treats genre and mood as separate points to collect, so the metal request was simply ignored and the peaceful mood plus the quiet numeric targets decided the result.
- **Removing mood changed a lot.** In a test with mood turned off, Gym Hero overtook Sunrise City for High-Energy Pop, and Porch Light Lullaby fell from #1 to #3 in the impossible combo. This showed me that mood was acting as the tiebreaker between songs with similar numbers.
- **Out-of-range values didn't break anything.** Scores stayed between 0 and 1, but after the exact edm match the scores dropped to 0.16 and below.

### Comparing each pair of profiles

- **High-Energy Pop vs Chill Lofi:** The top 5 lists have no songs in common. Pop wants loud, danceable songs like Sunrise City, and lofi wants quiet acoustic ones like Library Rain. This is what I'd expect from the two opposite ends of the energy scale.
- **High-Energy Pop vs Deep Intense Rock:** Four of the five songs are shared (Sunrise City, Gym Hero, Neon Pulse Drop, Storm Runner), because both users want high energy. The genre and mood decide the order: Sunrise City is #1 for pop and Storm Runner is #1 for rock. Gym Hero is #2 for both, through the pop genre for one user and the intense mood for the other.
- **High-Energy Pop vs Adversarial Conflicting:** Both ask for energy 0.9, so Gym Hero, Neon Pulse Drop and Storm Runner appear in both lists. The conflicting user's #1 is Moonlit Sonata because of the classical genre match, which is not a sensible result for a high-energy request.
- **High-Energy Pop vs Adversarial Impossible Combo:** No songs in common. The impossible profile asks for energy 0.1 and acousticness 0.95, so its list is quiet, acoustic songs. That is the correct reaction to the numeric targets.
- **High-Energy Pop vs Adversarial Out-of-range:** Three songs overlap (Neon Pulse Drop, Gym Hero, Storm Runner). Neon Pulse Drop is first for the out-of-range user because of the edm and euphoric matches, and the energy of 1.5 pushes toward the loudest songs, which makes sense.
- **Chill Lofi vs Deep Intense Rock:** No songs in common. Lofi favors energy around 0.35 and rock favors 0.92, so the outputs are completely different, which is valid.
- **Chill Lofi vs Adversarial Conflicting:** No songs in common. The conflicting profile wants high energy, so it pulls in the loud tracks that lofi users never see.
- **Chill Lofi vs Adversarial Impossible Combo:** Three shared songs (Library Rain, Spacewalk Thoughts, Porch Light Lullaby). The impossible profile's numeric targets (low energy, slow, acoustic) are close to the lofi profile, so the overlap makes sense. This shows the numeric features were driving the result and the metal genre was ignored.
- **Chill Lofi vs Adversarial Out-of-range:** No songs in common. Lofi wants quiet songs and the out-of-range profile asks for energy 1.5 and tempo 400, so they are opposites.
- **Deep Intense Rock vs Adversarial Conflicting:** Four shared songs (Storm Runner, Gym Hero, Neon Pulse Drop, Iron Requiem). Both want high energy. The difference is Moonlit Sonata at #1 for the conflicting user, which only appears because of the classical genre match.
- **Deep Intense Rock vs Adversarial Impossible Combo:** No songs in common. Rock wants energy 0.92 and the impossible combo wants 0.1.
- **Deep Intense Rock vs Adversarial Out-of-range:** Four shared songs (Storm Runner, Gym Hero, Neon Pulse Drop, Iron Requiem). Both want very high energy, but the out-of-range profile ranks Neon Pulse Drop first because of its edm and euphoric matches. It then drops to scores of 0.16 or less, while the rock user still gets reasonable scores of 0.5 to 0.7.
- **Adversarial Conflicting vs Adversarial Impossible Combo:** Only Moonlit Sonata is in both. It is first for the conflicting profile through the classical match and second for the impossible profile through its low energy and high acousticness. The overlap is a coincidence of two different features, not an agreement.
- **Adversarial Conflicting vs Adversarial Out-of-range:** Four shared songs (Iron Requiem, Storm Runner, Gym Hero, Neon Pulse Drop). Both ask for very high energy, and the difference is again the one song with a genre match (Moonlit Sonata for conflicting, Neon Pulse Drop for out-of-range).
- **Adversarial Impossible Combo vs Adversarial Out-of-range:** No songs in common. One asks for energy 0.1 and the other asks for 1.5, so the numeric targets are at opposite ends, as I'd expect.

---

## 8. Future Work  

1. **Add more songs.** The catalog has only 20 songs, and most genres have just one. More songs, especially ones with medium energy (0.5 to 0.7), would give more listeners good matches and fewer repeats like Gym Hero.

2. **Give partial credit for similar genres and moods.** Right now a label either matches or it doesn't. "Relaxed" earns nothing for a "chill" song, and "pop" earns nothing for "indie pop." Giving a smaller score for close labels would fix this and would stop genre and mood from overriding energy so easily.

3. **Make the top 5 more varied.** Nothing stops one artist from taking several slots. A simple rule, like at most one song per artist, would help. I could also add one song that is a little outside the listener's profile, so they can find new things.

4. **Handle mixed tastes.** A listener can only give one genre, one mood, and one energy target. Real people like more than one thing, such as calm songs for studying and loud ones for the gym. Letting a profile hold two or three tastes would work better.

5. **Make the explanations clearer.** The reasons show raw points, like "+1.60 of 2.0." Plain sentences, such as "Matches your energy and is also acoustic," would be easier for a normal listener to understand.

---

## 9. Personal Reflection  

I learned that Recommendation Systems use a mix of **Collaborative Filtering** and **Content Based Filtering** to recommend content such as TikToks, Reels, music, etc. It is very interesting to learn how the systems capture user behavior. For example, TikTok captures a share or a like on a TikTok video to build a user profile of you. Each of the actions are mapped to a weight dictionary (or something similar) that determines how much weight to give an action. This also opened up how Spotify creates the Discover Weekly and Release Radar playlists. 

It is interesting to learn that I created a model! This gave me an idea of how models such as Claude and OpenAI are created. `recommender.py` contains all the code to recommend songs so I am curious how Claude models are created.  

This assignment changed the way I think about music recommendation apps because now I am more concious of how systems work! I will understand what happens when I like a song. I even discovered I can use Discover Weekly and Release Radar playlists to find new music for me. 