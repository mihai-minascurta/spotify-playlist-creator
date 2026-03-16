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

An automated pipeline that bridges historical music charts with modern streaming. The application scrapes the Billboard Hot 100 for a user-specified date, authenticates via Spotify's OAuth 2.0 protocol, and programmatically compiles a private playlist of those specific tracks.

**Technical Logic (Verified):**
* **🕷️ Precise Web Scraping:** Uses `BeautifulSoup` to target specific HTML tags (`h3` and `span`) within the Billboard structure to extract track names and artists accurately.
* **🔐 Secure Authentication:** Implements `spotipy.SpotifyOAuth` with a local redirect URI to handle secure token exchange and scope management (`playlist-modify-private`).
* **⚙️ Robust Track Matching:** Features a search loop with error handling to manage cases where Billboard titles might not have an exact match in the Spotify catalog.
* **📂 Data Transformation:** Converts raw scraped data into a list of Spotify URIs before executing a single-batch playlist creation command.

<br>

<h3>
  📁 Project Structure<br>
  <img src="https://placehold.co/1000x2/C3B550/C3B550.png" width="100%" height="2" alt="Yellow Divider"/>
</h3>

```text
spotify-playlist-creator/
├── main.py                     # Main execution logic & Spotify integration
├── .env                        # Environment variables (Client ID/Secret)
└── token.txt                   # Local cache for OAuth access tokens
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
> 🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛ **90%** | **OAuth 2.0 Auth Flow**<br>
> 🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛ **70%** | **Web Scraping (BS4)**<br>
> 🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛ **80%** | **Search & Matching Logic**<br>
> 🟪🟪🟪🟪🟪⬛⬛⬛⬛⬛ **50%** | **List Comprehension & Parsing**

<br>

**🟢 High-Impact Wins:**
* **API Proficiency:** Demonstrates strong knowledge of the Spotipy library and its authorization flows.
* **Data Cleansing:** Efficiently stripping whitespace and formatting scraped strings to improve API search accuracy.

**🔧 Technical Debt (For Interview Awareness):**
* **Error Resilience:** In your current code, if the user enters an invalid date format, the script might crash. Adding a `datetime` validation check would make it production-ready.
* **Search Optimization:** You could further refine the search by adding the artist name to the Spotify query to avoid matching "covers" or different songs with the same title.


<div align="center">
  <img src="https://placehold.co/1000x3/FE428E/FE428E.png" width="100%" height="3" alt="Pink Divider"/>
</div>
