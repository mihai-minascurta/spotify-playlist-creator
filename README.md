<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=26&pause=1000&color=39FF14&center=true&vCenter=true&width=600&lines=%F0%9F%8E%B5+Spotify+Playlist+Creator;%E2%8F%AA+Musical+Time+Machine;%F0%9F%90%8D+Python+%2B+OAuth2" alt="Animated Header" />
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
  <span style="color: #39FF14;">🚀 Project Overview</span><br>
  <img src="https://placehold.co/1000x2/39FF14/39FF14.png" width="100%" height="2" alt="Green Divider"/>
</h3>

An automated pipeline that bridges historical music charts with modern streaming. The application scrapes the Billboard Hot 100 for a user-specified date, authenticates via Spotify's OAuth 2.0 protocol, and programmatically compiles a private playlist of those specific tracks.

**Technical Logic (Verified):**
* **🕷️ Precise Web Scraping:** Uses `BeautifulSoup` to target specific HTML tags (`h3` and `span`) within the Billboard structure to extract track names and artists accurately.
* **🔐 Secure Authentication:** Implements `spotipy.SpotifyOAuth` with a local redirect URI to handle secure token exchange and scope management (`playlist-modify-private`).
* **⚙️ Robust Track Matching:** Features a search loop with error handling to manage cases where Billboard titles might not have an exact match in the Spotify catalog.
* **📂 Data Transformation:** Converts raw scraped data into a list of Spotify URIs before executing a single-batch playlist creation command.

<br>

<h3>
  <span style="color: #00E5FF;">📁 Project Structure</span><br>
  <img src="https://placehold.co/1000x2/00E5FF/00E5FF.png" width="100%" height="2" alt="Cyan Divider"/>
</h3>

```text
spotify-playlist-creator/
├── main.py                     # Main execution logic & Spotify integration
├── .env                        # Environment variables (Client ID/Secret)
└── token.txt                   # Local cache for OAuth access tokens
```
<h3>
  <span style="color: #BC13FE;">🧠 Code Review & Complexity</span><br>
  <img src="https://placehold.co/1000x2/BC13FE/BC13FE.png" width="100%" height="2" alt="Purple Divider"/>
</h3>

<div align="center">
  <img src="https://img.shields.io/badge/OVERALL_DIFFICULTY-INTERMEDIATE-FE428E?style=for-the-badge&logoColor=white" height="35">
</div>

<br>

> <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=18&pause=1000&color=39FF14&vCenter=true&width=400&lines=>_ANALYZING_SYSTEM_COMPLEXITY..." alt="Animated Loading" />
> 
> <table>
>   <tr>
>     <td width="260"><b><span style="color: #39FF14;">OAuth 2.0 Auth Flow</span></b></td>
>     <td width="200"><img src="https://placehold.co/180x10/39FF14/39FF14.png"/><img src="https://placehold.co/20x10/2F2F2F/2F2F2F.png"/></td>
>     <td width="50"><b><span style="color: #39FF14;">90%</span></b></td>
>   </tr>
>   <tr>
>     <td width="260"><b><span style="color: #00E5FF;">Web Scraping (BS4)</span></b></td>
>     <td width="200"><img src="https://placehold.co/140x10/00E5FF/00E5FF.png"/><img src="https://placehold.co/60x10/2F2F2F/2F2F2F.png"/></td>
>     <td width="50"><b><span style="color: #00E5FF;">70%</span></b></td>
>   </tr>
>   <tr>
>     <td width="260"><b><span style="color: #BC13FE;">Search & Matching Logic</span></b></td>
>     <td width="200"><img src="https://placehold.co/160x10/BC13FE/BC13FE.png"/><img src="https://placehold.co/40x10/2F2F2F/2F2F2F.png"/></td>
>     <td width="50"><b><span style="color: #BC13FE;">80%</span></b></td>
>   </tr>
>   <tr>
>     <td width="260"><b><span style="color: #39FF14;">List Comprehension & Parsing</span></b></td>
>     <td width="200"><img src="https://placehold.co/100x10/39FF14/39FF14.png"/><img src="https://placehold.co/100x10/2F2F2F/2F2F2F.png"/></td>
>     <td width="50"><b><span style="color: #39FF14;">50%</span></b></td>
>   </tr>
> </table>

<br>

**🟢 High-Impact Wins:**
* **API Proficiency:** Demonstrates strong knowledge of the Spotipy library and its authorization flows.
* **Data Cleansing:** Efficiently stripping whitespace and formatting scraped strings to improve API search accuracy.

**🔧 Technical Debt:**
* **Error Resilience:** In your current code, if the user enters an invalid date format, the script might crash. Adding a `datetime` validation check would make it production-ready.
* **Search Optimization:** You could further refine the search by adding the artist name to the Spotify query to avoid matching "covers" or different songs with the same title.

<br>

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=500&size=16&duration=3000&pause=1000&color=00E5FF&center=true&vCenter=true&width=500&lines=[SYSTEM_SCAN_COMPLETE]----------------------------" alt="Animated Scan Divider" />
</div>
