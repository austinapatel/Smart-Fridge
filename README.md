# Smart-Fridge

Won 3rd place at Base Hacks 3 hackathon (basehacks.org)

Every year, about 25% to 40% of food in households is wasted. Much of the time it is because food goes bad in the fridge without people knowing about it. This hardware/software solution helps tell which items are in the fridge to better inform people about when their food will expire to decrease food loss. The Smart Fridge that uses an image recognition system to detect which items are in the fridge automatically and provide useful information about expiration dates (work in progress), nutrition, and other analytics. It supports Alexa commands for making queries about the fridge. A raspberry pi camera was used to take the photos of the food in the fridge and provide a live feed via a 5" display on the front of the refrigerator, while Arduino-compatible LEDs were used to light the fridge for a real-time video feed and photo lighting. This lighting setup mimics that of an actual fridge, proving that our model accurately represents the future of the Smart Fridge product. Also, Google Cloud Platform Vision API detects the type of food inside using its own neural network and image recognition software in the Cloud Platform API (Application Programming Interface). We then pass on the value of the food to the NLP-integrated Edamam API, which we use to obtain the values of the analytics. There is an automated door that is powered by an Arduino. You can say "Alexa, ask smart fridge what's inside" or "Alexa, ask smart fridge for the nutrition information for apple."
