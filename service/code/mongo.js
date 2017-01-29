use property
db.property.insert(
	{
		"overview" : {
			"Type": "Condominium",
			"MLS": 1059799,
			"Address:" : { 
				"street" : "16322 NE 12th Place Unit A-1",
				"city": "Bellevue",
				"zip": "98008",
				"coord": [47.620201, -122.121837]
			},
			"Sq Feet": 2059,
			"Price": 849900,
			"Beds": 4,
			"Baths": 2.5,
			"Description": "These stunningly modern town home condos are now under construction & ready for move in Sept. 2017. Be one of the first to take advantage of this central location just minutes from Crossroads Park, Mall, 520, & Microsoft. Featuring ceilings soaring up to 10 ft, designer finishes, open railing, bed & bath on 1st level, & tons of natural light from over sized windows. Don't forget the convenience of a 2 car garage, private street, & all landscaping maintained. Renderings are representative.",
			"Photo": 
				["https://ssl.cdn-redfin.com/photo/1/mbpaddedwide/799/genMid.1059799_2.jpg", 
				"https://ssl.cdn-redfin.com/photo/1/mbpaddedwide/799/genMid.1059799_1_2.jpg",
				"https://ssl.cdn-redfin.com/photo/1/mbpaddedwide/799/genMid.1059799_2_2.jpg",
				"https://ssl.cdn-redfin.com/photo/1/mbpaddedwide/799/genMid.1059799_3_2.jpg",
				"https://ssl.cdn-redfin.com/photo/1/mbpaddedwide/799/genMid.1059799_4_2.jpg"
				],
			"HOA Dues": "300/month",
			"Status": ["active", "new construction"],
			"Built": 2016,
			"Lot": ""
		},
		"detail": {
			"Virtual Tour, Parking / Garage, Exterior Features, Multi-Unit Information": {
				"Virtual Tour": "",
				"Parking Information":
				[
					"Parking Space Number: 2",
					"Individual Guarage"
				],
				"Building Information":
				["Under construction", "Standard Frame", "# of Units: 4", "Cement Planked Exterior, Metal/Vinyl Exterior", "Build-Up Roof", "Storage Location: Garage"],
				"Community Information":
				["# of Units in Complex: 18"]
			},
			"Interior Features":{

			},
			"Homeowner Association, School":{

			},
			"Property / Lot Details":{

			},
			"Location Details, Listing Information":
			{

			}
		},
		"Tour Insights" : [],
		"History":
		[
			{"Date": "Dec 22, 2016", "Event": "Listed (Active)", "Price": 849000}
		],
		"Activities":{
			"Views": 0,
			"Favorites": 0,
			"X-Outs": 0,
			"Tour": 0
		}
	}
)

db.user.insert(
	{
		"email":"sample@example.com",
		"password encrypted":"",
		"mobile":"+1 206-572-3937",
		"Favorites":[],
		"X-Outs":[],
		"Tours":[]
	}
)