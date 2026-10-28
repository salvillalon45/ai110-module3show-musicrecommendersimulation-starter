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

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

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
