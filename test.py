import spotify
import json

creds = json.load(open('creds.json'))

config = spotify.Config()

config.user_agent = 'test'

session = spotify.Session(config)

session.login(creds["username"], creds["passwd"])

while session.connection.state != 1:
	session.process_events()
	#print session.connection.state

print len(session.playlist_container)
print session.connection.state
ct = session.playlist_container
pl = ct[3]

pl.load()

print pl.name
