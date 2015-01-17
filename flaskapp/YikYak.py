#! /usr/bin/env python3
import API as pk
import pygeocoder
import requests
from plugin import process

def dostuff():
    # Title text
    print("\nYik Yak Command Line Edition : Created by djtech42\n\n")
	
    # Initialize Google Geocoder API
    geocoder = pygeocoder.Geocoder("AIzaSyAGeW6l17ATMZiNTRExwvfa2iuPA1DvJqM")
	
    try:
        # If location already set in past, read file
        f = open("locationsetting", "r")
        fileinput = f.read()
        f.close()
		
        # Extract location coordinates and name from file
        coords = fileinput.split('\n')
		
        currentlatitude = coords[0]
        currentlongitude = coords[1]
        print("Location is set to: ", coords[2])
		
        # Set up coordinate object
        coordlocation = pk.Location(currentlatitude, currentlongitude)
		
    except FileNotFoundError:
        # If first time using app, ask for preferred location
        coordlocation = newLocation(geocoder)
		
        # If location retrieval fails, ask user for coordinates
        if coordlocation == 0:
            print("Please enter coordinates manually: ")
			
            currentlatitude = input("Latitude: ")
            currentlongitude = input("Longitude: ")
            coordlocation = pk.Location(currentlatitude, currentlongitude)
	
    print()
	
    try:
        # If user already has ID, read file
        f = open("userID", "r")
        userID = f.read()
        f.close()
		
        # start API with saved user ID
        remoteyakker = pk.Yakker(userID, coordlocation, False)
		
    except FileNotFoundError:
        # start API and create new user ID
        remoteyakker = pk.Yakker(None, coordlocation, True)
		
    try:
            # Create file if it does not exist and write user ID
            f = open("userID", 'w+')
            f.write(remoteyakker.id)
            f.close()
			
    except:
        pass
			
    # Print User Info Text
    print("User ID: ", remoteyakker.id, "\n")
    print("Connecting to Yik Yak server...\n")
    connection = True
    try:
        print("Yakarma Level:",remoteyakker.get_yakarma(), "\n")
    except:
        print("Error: Not connected to the Internet\n")
        connection = False

    if connection:
        currentlist = []
        choice = 'R'
        currentlist = remoteyakker.get_yaks()
        return read(currentlist)
    
			
def newLocation(geocoder, address=""):
	# figure out location latitude and longitude based on address
	if len(address) == 0:
		address = input("Enter college name or address: ")
	try:
		currentlocation = geocoder.geocode(address)
	except:
		print("\nGoogle Geocoding API is offline or has reached the limit of queries.\n")
		return 0
		
	coordlocation = 0
	try:
		coordlocation = pk.Location(currentlocation.latitude, currentlocation.longitude)
		
		# Create file if it does not exist and write
		f = open("locationsetting", 'w+')
		coordoutput = str(currentlocation.latitude) + '\n' + str(currentlocation.longitude)
		f.write(coordoutput)
		f.write("\n")
		f.write(address)
		f.close()
	except:
		print("Unable to get location.")
		
	return coordlocation
	
def setUserID(location, userID=""):
	if userID == "":
		userID = input("Enter userID or leave blank to generate random ID: ")
		
	if userID == "":
		# Create new userID
		remoteyakker = pk.Yakker(None, location, True)
	else:
		# Use existing userID
		remoteyakker = pk.Yakker(userID, location, False)
	try:
		# Create file if it does not exist and write user ID
		f = open("userID", 'w+')
		f.write(remoteyakker.id)
		f.close()
		
	except:
		pass
	
	return remoteyakker
	
def changeLocation(geocoder, address=""):
	coordlocation = newLocation(geocoder, address)
	
	# If location retrieval fails, ask user for coordinates
	if coordlocation == 0:
		print("\nPlease enter coordinates manually: ")
		currentlatitude = input("Latitude: ")
		currentlongitude = input("Longitude: ")
		coordlocation = pk.Location(currentlatitude, currentlongitude)
		
	return coordlocation
	
def read(yaklist):
    list_o_yaks = list()
    for yak in yaklist:
        #process(yak) 
        list_o_yaks.append(yak.message)
    return list_o_yaks
            
