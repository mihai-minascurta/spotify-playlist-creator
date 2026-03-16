<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=26&pause=1000&color=1DB954&center=true&vCenter=true&width=600&lines=%F0%9F%8E%B5+Spotify+Playlist+Creator;%E2%8F%AA+Musical+Time+Machine;%F0%9F%90%8D+Python+%2B+OAuth2" alt="Animated Header" />
</div>

<br>

<div align="center">
  <img src="https://img.shields.io/badge/Python-FE428E?style=for-the-badge&logo=python&logoColor=white" height="35">
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Spotify_API-1DB954?style=for-the-badge&logo=spotify&logoColor=white" height="35">
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/BeautifulSoup-A9FEF7?style=for-the-badge&logo=python&logoColor=black" height="35">
</div>

<br>

<h3>
  🚀 Project Overview<br>
  <img src="https://placehold.co/1000x2/C3B550/C3B550.png" width="100%" height="2" alt="Yellow Divider"/>
</h3>

A "Musical Time Machine" script that completely automates playlist creation. By inputting a specific date, the application scrapes the Billboard Hot 100 chart for that week, connects to your Spotify account via OAuth 2.0, searches for the tracks, and generates a private custom playlist for you to enjoy.

**Key Features:**
* **🕷️ Web Scraping:** Extracts the top 100 songs for any historical date using `BeautifulSoup`.
* **🔐 OAuth 2.0 Authentication:** Securely connects to the Spotify Web API using `spotipy`.
* **⚙️ Automated Search & Build:** Queries Spotify's database for each scraped track and compiles them into a new playlist programmatically.

<br>

<h3>
  📁 Project Structure<br>
  <img src="https://placehold.co/1000x2/C3B550/C3B550.png" width="100%" height="2" alt="Yellow Divider"/>
</h3>

```text
spotify-playlist-creator/
├── main.py                     # Main execution script & API Logic
├── .env                        # Hidden environment variables (ID/Secret)
└── token.txt                   # Auto-generated Spotify OAuth token
```

<h3>
  🧠 Code Review & Complexity<br>
  <img src="https://placehold.co/1000x2/C3B550/C3B550.png" width="100%" height="2" alt="Yellow Divider"/>
</h3>

<div align="center">
  <img src="https://img.shields.io/badge/OVERALL_DIFFICULTY-INTERMEDIATE-FE428E?style=for-the-badge&logoColor=white" height="35">
</div>

<br>

> **📊 SYSTEM COMPLEXITY RADAR**
>
> 🟩🟩🟩🟩🟩🟩🟩🟩⬛⬛ **80%** | **OAuth 2.0 Authentication**<br>
> 🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛ **70%** | **Web Scraping (BeautifulSoup)**<br>
> 🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛ **80%** | **API Search & Playlist Build**<br>
> 🟪🟪🟪🟪🟪⬛⬛⬛⬛⬛ **50%** | **Error Handling (Missing Songs)**

<br>

**🟢 High-Impact Wins:**
* **Authentication Mastery:** Successfully navigating Spotify's OAuth 2.0 flow is a major milestone for intermediate developers.
* **Data Extraction:** Efficiently scraping and parsing the complex HTML structure of the Billboard Hot 100.

**🔧 Key Recommendations (Refactoring):**
* **Security:** Ensure credentials (`CLIENT_ID` / `CLIENT_SECRET`) are strictly hidden using a `.env` file (`python-dotenv`) and ignored via `.gitignore`.
* **Resilience:** Add specific `try/except` blocks (like `IndexError`) for when a scraped song doesn't exist on Spotify, to prevent the loop from breaking.

<br>

<div align="center">
  <img src="https://placehold.co/1000x3/FE428E/FE428E.png" width="100%" height="3" alt="Pink Divider"/>
</div>
