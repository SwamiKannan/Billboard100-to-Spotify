import spotipy
from scrape_billboard import Billboard
import calendar
import json
import os



def process_names(track_name: str):
    track_name = track_name.replace(' & ', ',') if ' & ' in track_name else track_name
    track_name = track_name.replace(' (', '(') if ' (' in track_name else track_name
    track_name = track_name.replace('The', '') if 'The' in track_name else track_name

    return track_name


class SpotifyPlaylist:
    def __init__(self):
        self.USERID = None
        self.playlist = None
        self.tracks = None
        self.spotifyObject = None
        self.billboard = Billboard()
        self.billboard.get_ratings()
        self.initialize()
        self.errors = []

    def initialize(self):
        print('Initializing')
        self.USERID=input('Please enter your user id\n')
        try:
            client_id = os.environ['spotify_client_id']
            client_secret = os.environ['spotify_secret_id']
        except KeyError as e:
            try:
                with open('keys_spotify.json', 'r') as f:
                    API_keys = json.load(f)
                    client_id = API_keys['Spotify']['client_id']
                    client_secret = API_keys['Spotify']['client_secret']
            except FileNotFoundError as e:
                print('Exception 2', e)
                client_id = input('Enter your client id')
                client_secret = input('Enter your client secret key')
        oauth_object = spotipy.SpotifyOAuth(client_id, client_secret,
                                            "http://localhost:8888/callback", scope='playlist-modify-private')
        token = oauth_object.get_access_token(as_dict=False)
        self.spotifyObject = spotipy.Spotify(token)

    def get_track_id(self, track, artist):
        #### Get track id
        results = self.spotifyObject.search(q="artist:" + artist + " track:" + track, type="track")
        if len(results['tracks']['items']) > 0:
            return results['tracks']['items'][0]['id']
        else:
            track_name = track.replace(' & ', ',') if ' & ' in track else track
            artist_name = artist.replace(' & ', ',') if ' & ' in artist else artist
            results = self.spotifyObject.search(q="artist:" + artist_name + " track:" + track_name, type="track")
            if len(results['tracks']['items']) > 0:
                return results['tracks']['items'][0]['id']
            else:
                track_name = track.replace(' (', '(') if ' (' in track else track
                artist_name = artist.replace(' (', '(') if ' (' in artist else artist
                results = self.spotifyObject.search(q="artist:" + artist_name + " track:" + track_name, type="track")
                if len(results['tracks']['items']) > 0:
                    return results['tracks']['items'][0]['id']
                else:
                    track_name = track.replace('The', '') if 'The' in track else track
                    artist_name = artist.replace('The', '') if 'The' in artist else artist
                    results = self.spotifyObject.search(q="artist:" + artist_name + " track:" + track_name,
                                                        type="track")
                    if len(results['tracks']['items']) > 0:
                        return results['tracks']['items'][0]['id']
                    else:
                        track_name = track.replace('/', ' / ') if 'The' in track else track
                        artist_name = artist.replace('/', ' / ') if 'The' in artist else artist
                        results = self.spotifyObject.search(q="artist:" + artist_name + " track:" + track_name,
                                                            type="track")
                        if len(results['tracks']['items']) > 0:
                            return results['tracks']['items'][0]['id']
                        else:
                            track_name = process_names(track)
                            artist_name = process_names(artist)
                            results = self.spotifyObject.search(q="artist:" + artist_name + " track:" + track_name,
                                                                type="track")
                            if len(results['tracks']['items']) > 0:
                                return results['tracks']['items'][0]['id']
                            else:
                                self.errors.append((track, artist))
                                return None

    def get_all_track_ids(self):
        print('\nGetting track ids.....')
        self.tracks = []
        for songs in self.billboard.ranks.values():
            track = songs[0]
            artist = songs[1]
            if self.get_track_id(track, artist):
                self.tracks.append(self.get_track_id(track, artist))
        print('Track ids received\n')
        if len(self.errors) > 0:
            print('A few tracks could not be found:')
            for track in self.errors:
                print(track[0] + ' by ' + track[1])
        print('\n')
        # print('Results')
        # print(results.keys())
        # print(results['tracks'].keys())

        # for key in results['tracks'].keys():5.
        #     print(key, '\t', results['tracks'][key])

    def create_playlist(self):
        #### Create a fresh playlist
        print('Creating your playlist :) .....')
        name = 'Billboard Hot 100 for ' + calendar.month_name[
            int(self.billboard.month)] + ' ' + self.billboard.date + ", " + self.billboard.year + "."
        self.playlist = self.spotifyObject.user_playlist_create(self.USERID, name, public=False, collaborative=False,
                                                                description='')
        print('Playlist created\n')

    def add_song_to_playlist(self):
        ##### Add song to playlist
        print('Adding your songs to the playlist!')
        self.spotifyObject.playlist_add_items(playlist_id=self.playlist['id'],
                                              items=['spotify:track:' + t_id for t_id in self.tracks])
        print('Songs added !\n')

    def create_final_playlist(self):
        self.get_all_track_ids()
        self.create_playlist()
        self.add_song_to_playlist()
        print('Go ahead ! Check out your new playlist!')


playlist_spotify = SpotifyPlaylist()
playlist_spotify.create_final_playlist()
