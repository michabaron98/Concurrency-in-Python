from dataclasses import dataclass

# More info at: https://dinosaur-facts-api.shultzlab.com/
API_URL='https://dinosaur-facts-api.shultzlab.com/'

@dataclass
class Endpoints:
	DINOSAURS: str = "dinosaurs"
	DINOSAURS_RANDOM: str = "dinosaurs/random"
	DINOSAURS_RANDOM_NAME: str = "/dinosaurs/random/name"
	DINOSAURS_RANDOM_DESCRIPTION: str = "/dinosaurs/random/description"
