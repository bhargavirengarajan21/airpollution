from flask_frozen import Freezer
from app import application

application.config['FREEZER_RELATIVE_URLS'] = True
application.debug = False
freezer = Freezer(application)

@freezer.register_generator
def predict():
	yield '/predict'

if __name__ == '__main__':
    freezer.freeze()
