# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

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

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider 
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

One weakness I found is that the exact genre and mood matches can override the energy a user actually asked for. Together they are worth 3.0 of the 7.0 total weight, so a song that matches both labels can outrank a song with a much better energy fit. For example, a pop/happy user who asks for energy 0.3 still gets Sunrise City (energy 0.82) at #1 with a score of 0.79, and Gym Hero (energy 0.93) at #2, while the low-energy songs rank lower. The problem is made worse by a small dataset where 15 of the 17 genres have only one song, so a user whose genre or mood appears once gets a single guaranteed match and everything else is ranked on the numbers alone. Labels also only match exactly, so "relaxed" earns no credit for similar songs tagged "chill" or "peaceful", and "indie pop" earns none for a pop fan.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

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

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
