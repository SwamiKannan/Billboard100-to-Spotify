# Billboard100 to Spotify
<p align='center'>
 <img src="https://github.com/SwamiKannan/Billboard100-to-Spotify/blob/main/cover.png">
</p>
<br>
This repo creates a Spotify playlist based on the Hot 100 playlist on any specific date.

## Requirements
<ul><li>You will need the following details about your Spotify account
<ul>
 <li>Your Spotify username </li>
 <li>A Spotify developer account</li>
 <li>Your client id (from Spotify)</li>
 <li>Your client secret key (from Spotify) </li>
</ul></li>
</ul>
 
If you do not know how to get your Client Id and Client Secret keys from Spotify, you can follow the instructions <a href="https://github.com/SwamiKannan/Billboard100-to-Spotify/blob/main/get_spotify_creds/README.md"> here </a><br>

## Installation:

  1. Download this git repo using:<br>
 `git clone https://github.com/SwamiKannan/Billboard100-to-Spotify.git`<br><br>
  2. Install the requirement libraries <br>
 `pip install -e requirements.txt`


## Usage:
1. Run the code in the command prompt<br>
`python main.py`<br><br>
2. The code will ask you for the date for which you want to Billboard top 100 playlist. Enter the date in <b>dd/mmy/yyyy format</b><br><br>
3. If the Spotify client id and client secret are not stored either in the environment variables or in the provided json format, the prompt will then ask for the appropriate keys. Please provide the same.<br><br>
4. Finally, the app will ask you for your Spotify username. Please provide the same.<br><br>
5. On completion, you will be able to see the playlist on your Spotify account named <b>"Billboard Hot 100 for < date > "</b><br><br>
6. ENJOY !

