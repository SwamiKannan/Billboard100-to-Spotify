#How to get your Spotify Client id and Client Secret

You can get the client id and client secret as follows:
<ol> 
<li>Go to developers.spotify.com and click "Log in"</li><br />
 <img src="https://github.com/SwamiKannan/Billboard100-to-Spotify/blob/main/get_spotify_creds/screenshots/1.png"><br /><br />  

 <li>Once you are logged in, go to the account name, drop down and click on "Dashboard"</li><br>    
 <img src="https://github.com/SwamiKannan/Billboard100-to-Spotify/blob/main/get_spotify_creds/screenshots/2.png"><br /><br />

 This will show you the list of apps you may have created in the past. If the first time, you are accessing the developers page, the list will be empty. For this repo, I created the Billboard Top 100 app so it displays the app here.Your list might be empty.<br />  
<li>  Click on Create App</li>
 <img src="https://github.com/SwamiKannan/Billboard100-to-Spotify/blob/main/get_spotify_creds/screenshots/3.png"><br /><br />
<li> Fill in the app name, the app description and the website as per your preferences. A sample is shown in the screenshot below. However, fill the Redirect URI <b>exactly</b> as shown.<br />
CLick on the checkbox that says "I understand and agree with Spotify's Developer Terms of Service and Design Guidelines after reading them and click "Save"</li><br />
<img src="https://github.com/SwamiKannan/Billboard100-to-Spotify/blob/main/get_spotify_creds/screenshots/4.png"><br /><br />

<li>Your app's homepage is now displayed. This page shows you all the statistics of your app. Click on "Settings" on the top right hand side of the page</li><br />
<img src="https://github.com/SwamiKannan/Billboard100-to-Spotify/blob/main/get_spotify_creds/screenshots/5.png"><br /><br />

<li>In the Settings page, you will finally get your Client Id and Client Secret.<br />
To use the client id and client secret on this app, there are three ways to incorporate these details into the app:
<ul><li>Saving the client id and client secret in the environment variables: Save the client id in the key: 'spotify_client_id' and the secret in the key: 'spotify_secret_id' </li>
<li>Open the keys_spotify.json file in this repo. Add the client id between the quotes next to the text "client_id". Add the client secret between the quotes next to the text "client_secret". <br />
<b>NOTE: Anyone who can access this JSON will be able to see your client id and client secret and hence, will be able to access and make changes to your app. Hence, please ensure that this file is stored in a safe location</b></li>
<li>Save the client id and the client secret separately in a safe location. If the app cannot find your client id / client secret either in the environment variables or in the json file, it will ask for the client id and client secret. While this may be the safest way to store the details, you will have to fill them in everytime you use the app</li></ul></li><br />
<li>Click on the icon next to your client id. This will copy your Client Id.<br /> Save this as explained in step 6.</li><br />
<img src="https://github.com/SwamiKannan/Billboard100-to-Spotify/blob/main/get_spotify_creds/screenshots/6.png"><br /><br />

<li>Click on "View Client Secret"<br />
The page then displays the Client Secret code as well. Copy this by clicking on the icon displayed on the right of the text box.<br /> Save this as explained in step 6.</li><br />
<img src="https://github.com/SwamiKannan/Billboard100-to-Spotify/blob/main/spotify_creds/7.png"><br /><br />
</ol>

