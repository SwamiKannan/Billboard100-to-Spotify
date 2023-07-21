# Billboard100 to Spotify
<p align='center'>
 <img src="https://github.com/SwamiKannan/Billboard100-to-Spotify/blob/main/cover.png">
</p>
<br>
This repo creates a Spotify playlist based on the Hot 100 playlist on any specific date.
You will need the following details about your Spotify account
<ul>
 <li>Your Spotify username </li>
 <li>A Spotify developer account</li>
 <li>Your client id (from Spotify)</li>
 <li>Your client secret key (from Spotify) </li>
</ul>
You can get the client id and client secret as follows:
<ol> 
<li>Go to developers.spotify.com and click "Log in"</li><br />
 <img src="https://github.com/SwamiKannan/Billboard100-to-Spotify/blob/main/spotify_creds/1.png"><br /><br />  

 <li>Once you are logged in, go to the account name, drop down and click on "Dashboard"</li><br>    
 <img src="https://github.com/SwamiKannan/Billboard100-to-Spotify/blob/main/spotify_creds/2.png"><br /><br />

 This will show you the list of apps you may have created in the past. If the first time, you are accessing the developers page, the list will be empty. For this repo, I created the Billboard Top 100 app so it displays the app here.Your list might be empty.<br />  
<li>  Click on Create App</li>
 <img src="https://github.com/SwamiKannan/Billboard100-to-Spotify/blob/main/spotify_creds/3.png"><br /><br />
<li> Fill in the app name, the app description and the website as per your preferences. A sample is shown in the screenshot below. However, fill the Redirect URI <b>exactly</b> as shown.<br />
CLick on the checkbox that says "I understand and agree with Spotify's Developer Terms of Service and Design Guidelines after reading them and click "Save"</li><br />
<img src="https://github.com/SwamiKannan/Billboard100-to-Spotify/blob/main/spotify_creds/4.png"><br /><br />
<li>Your app's homepage is now displayed. This page shows you all the statistics of your app. Click on "Settings" on the top right hand side of the page</li><br />
<img src="https://github.com/SwamiKannan/Billboard100-to-Spotify/blob/main/spotify_creds/5.png"><br /><br />
<li>In the Settings page, you will finally get your Client Id and Client Secret.<br />
Click on the icon next to your client id. This will copy your Client Id.</li><br />
<img src="https://github.com/SwamiKannan/Billboard100-to-Spotify/blob/main/spotify_creds/6.png"><br /><br />
<li>To use the client id and client secret on this app, there are three ways to incorporate these details into the app:
<ul><li>Saving the client id and client secret in the environment variables: Save the client id in the key: 'spotify_client_id' and the secret in the key: 'spotify_secret_id' </li></li><br />
<img src="https://github.com/SwamiKannan/Billboard100-to-Spotify/blob/main/spotify_creds/6.png"><br /><br />
</ol>

