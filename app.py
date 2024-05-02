# # from flask import Flask, request, jsonify
# # from tensorflow.keras.models import load_model
# # from tensorflow.keras.preprocessing.image import img_to_array, load_img
# # import numpy as np
# # import os
# # from flask_cors import CORS  # Import the CORS class from flask-cors

# # app = Flask(__name__)
# # CORS(app)  # Enable CORS for your Flask app

# # # Load the trained model
# # model = load_model('image_classifier_model.h5')  # Replace with your model file path

# # # Define the class labels
# # class_labels = os.listdir('content')  # Replace with your data folder path

# # @app.route('/classify', methods=['POST'])
# # def classify_image():


# #     if 'image' not in request.files:
# #         return jsonify({"error": "No image provided in the request"})

# #     image_file = request.files['image']
# #     if image_file.filename == '':
# #         return jsonify({"error": "No selected image file"})

# #     # Save the uploaded image to a temporary file
# #     temp_image_path = 'temp_image.jpg'  # Path to a temporary file
# #     image_file.save(temp_image_path)

# #     # Load and preprocess the image
# #     img = load_img(temp_image_path, target_size=(150, 150))
# #     img_array = img_to_array(img)
# #     img_array = np.expand_dims(img_array, axis=0)
# #     img_array = img_array / 255.0

# #     # Make predictions
# #     predictions = model.predict(img_array)
# #     class_index = np.argmax(predictions)
# #     class_name = class_labels[class_index]
    
# #     print("Class name="+class_name)

# #     # Additional information based on class prediction
# #     additional_info = [];
# #     if class_name == 'Arive-Dantu':
# #         additional_info = "Also known as Amarnath, this plant can be used as a food to eat when on a diet or looking for weight loss as it is rich in fiber, extremely low in calories, has traces of fats and absolutely no cholesterol. It is used to help cure ulcers, diarrhea, swelling of the mouth or throat, and high cholesterol. It also has chemicals that act as antioxidants."
# #     if class_name == 'aloevera':
# #         additional_info = "Basale has anti-inflammatory activity and wound healing ability. It can be helpful as a first aid, and the leaves of this plant can be crushed and applied to burns, scalds, and wounds to help in healing of the wounds."
# #     if class_name == 'amla':
# #         additional_info = "Amla, also known as Indian gooseberry, is a fruit that has been used in traditional Ayurvedic medicine for centuries. It is highly valued for its nutritional content and potential health benefits. "
# #     if class_name == 'Avacado':
# #         additional_info = "Avocado is a nutritious fruit that is not only delicious but also offers various health benefits. While it may not be considered a traditional medicinal plant, avocados contain several nutrients that contribute to overall health. "
# #     if class_name == 'Arive-Dantu':
# #         additional_info = "Also known as Amarnath, this plant can be used as a food to eat when on a diet or looking for weight loss as it is rich in fiber, extremely low in calories, has traces of fats and absolutely no cholesterol. It is used to help cure ulcers, diarrhea, swelling of the mouth or throat, and high cholesterol. It also has chemicals that act as antioxidants."
# #     if class_name == 'aloevera':
# #         additional_info = "Basale has anti-inflammatory activity and wound healing ability. It can be helpful as a first aid, and the leaves of this plant can be crushed and applied to burns, scalds, and wounds to help in healing of the wounds."
# #     if class_name == 'Arali':
# #         additional_info = "Nerium oleander, most commonly known as oleander or nerium, is a shrub or small tree cultivated worldwide in temperate and subtropical areas as an ornamental and landscaping plant. It is the only species currently classified in the genus Nerium, belonging to subfamily Apocynoideae of the dogbane family Apocynaceae. It is so widely cultivated that no precise region of origin has been identified, though it is usually associated with the Mediterranean Basin."
# #     if class_name == 'Ashoka':
# #         additional_info = "Saraca asoca, commonly known as the ashoka tree, is a plant belonging to the Detarioideae subfamily of the legume family. It is an important tree in the cultural traditions of the Indian subcontinent and adjacent areas. It is sometimes incorrectly known as Saraca indica. The flower of Ashoka tree is the state flower of Indian state of Odisha."
# #     if class_name == 'Ashwagandha':
# #         additional_info = "Ashwagandha, scientifically known as Withania somnifera, is an herb that is commonly used in traditional Ayurvedic medicine, which is an ancient system of medicine that originated in India. It is also known by several other names, including Indian ginseng and winter cherry."
# #     if class_name == 'Avacado':
# #         additional_info = "The avocado (Persea americana) is a medium-sized, evergreen tree in the laurel family (Lauraceae). It is native to the Americas and was first domesticated in Mesoamerica more than 5,000 years ago. Then as now it was prized for its large and unusually oily fruit. The tree likely originated in the highlands bridging south-central Mexico and Guatemala."
# #     if class_name == 'Bamboo':
# #         additional_info = "Bamboos are a diverse group of mostly evergreen perennial flowering plants making up the subfamily Bambusoideae of the grass family Poaceae. Giant bamboos are the largest members of the grass family, in the case of Dendrocalamus sinicus individual culms reaching a length of 46 meters, up to 36 centimeters in thickness and a weight of up to 450 kilograms."
# #     if class_name == 'Basale':
# #         additional_info = "Basella alba is an edible perennial vine in the family Basellaceae. It is found in tropical Asia and Africa where it is widely used as a leaf vegetable. It is native to the Indian subcontinent, Southeast Asia and New Guinea. It is naturalized in China, tropical Africa, Brazil, Belize, Colombia, the West Indies, Fiji and French Polynesia"
# #     if class_name == 'Betel':
# #         additional_info = "The betel, Piper betle, is a species of flowering plant in the pepper family Piperaceae, native to Southeast Asia. It is an evergreen, dioecious vine, with glossy heart-shaped leaves and white catkins. Betel plants are cultivated for their leaves which are most commonly used as flavoring in chewing areca nut (betel nut chewing)."
# #     if class_name == 'Betel_Nut':
# #         additional_info = "The areca nut is the fruit of the areca palm (Areca catechu), which grows in much of the tropical Pacific (Melanesia and Micronesia), South Asia, Southeast Asia, and parts of east Africa. It is commonly referred to as betel nut, not to be confused with betel (Piper betle) leaves that are often used to wrap it."
# #     if class_name == 'Brahmi':
# #         additional_info = "Bacopa monnieri is a perennial, creeping herb native to the wetlands of southern and Eastern India, Australia, Europe, Africa, Asia, and North and South America. It is known by the common names water hyssop, waterhyssop, brahmi, thyme-leafed gratiola, herb of grace, and Indian pennywort."
# #     if class_name == 'Castor':
# #         additional_info = "Ricinus communis, the castor bean or castor oil plant, is a species of perennial flowering plant in the spurge family, Euphorbiaceae. It is the sole species in the monotypic genus, Ricinus, and subtribe, Ricininae. The evolution of castor and its relation to other species are currently being studied using modern genetic tools."
# #     if class_name == 'Curry_Leaf':
# #         additional_info = "The curry tree or Bergera koenigii (syn.Murraya koenigii), is a tropical and sub-tropical tree in the family Rutaceae (the rue family, which includes rue, citrus, and satinwood), native to Asia. The plant is also sometimes called sweet neem."
# #     if class_name == 'Doddapatre':
# #         additional_info = "Coleus amboinicus, synonym Plectranthus amboinicus, is a semi-succulent perennial plant in the family Lamiaceae with a pungent oregano-like flavor and odor. Coleus amboinicus is considered to be native to parts of Africa, the Arabian Peninsula, and India."
# #     if class_name == 'Ekka':
# #         additional_info = "Calotropis gigantea, the crown flower, is a species of Calotropis native to Cambodia, Vietnam, Bangladesh, Indonesia, Malaysia, Thailand, Sri Lanka, India, China, Pakistan, and Nepal. It is a large shrub growing to 4 m (13 ft) tall. It has clusters of waxy flowers that are either white or lavender in colour."
# #     if class_name == 'Ganike':
# #         additional_info = "Solanum nigrum, the European black nightshade or simply black nightshade or blackberry nightshade,[1] is a species of flowering plant in the family Solanaceae, native to Eurasia and introduced in the Americas, Australasia, and South Africa."
# #     if class_name == 'Geranium':
# #         additional_info = "Geranium is a genus of 422 species of annual, biennial, and perennial plants that are commonly known as geraniums or cranesbills. They are found throughout the temperate regions of the world and the mountains of the tropics, with the greatest diversity in the eastern part of the Mediterranean region."
# #     if class_name == 'Guava':
# #         additional_info = "Guava is a common tropical fruit cultivated in many tropical and subtropical regions. The common guava Psidium guajava (lemon guava, apple guava) is a small tree in the myrtle family (Myrtaceae), native to Mexico, Central America, the Caribbean and northern South America."
# #     if class_name == 'Henna':
# #         additional_info = "Henna is a dye prepared from the plant Lawsonia inermis, also known as the henna tree, the mignonette tree, and the Egyptian privet,[1] and one of the only two species of the genus Lawsonia, with the other being Lawsonia odorata."
# #     if class_name == 'Hibiscus':
# #         additional_info = "Hibiscus is a genus of flowering plants in the mallow family, Malvaceae. The genus is quite large, comprising several hundred species that are native to warm temperate, subtropical and tropical regions throughout the world."
# #     if class_name == 'Honge':
# #         additional_info = "Pongamia pinnata is a species of tree in the pea family, Fabaceae, native to eastern and tropical Asia, Australia, and the Pacific islands. It is the sole species in genus Pongamia."
# #     if class_name == 'Insulin':
# #         additional_info = "Chamaecostus cuspidatus, common name fiery costus or spiral flag, is a species of herbaceous plant in the family Costaceae native to eastern Brazil (States of Bahia and Espirito Santo). In India, it is known as insulin plant for its purported anti-diabetic properties."
# #     if class_name == 'Jasmine':
# #         additional_info = "Jasmine is a genus of shrubs and vines in the olive family of Oleaceae. It contains around 200 species native to tropical and warm temperate regions of Eurasia, Africa, and Oceania."
# #     if class_name == 'Lemon':
# #         additional_info = "The lemon (Citrus limon) is a species of small evergreen tree in the flowering plant family Rutaceae, native to Asia, primarily Northeast India (Assam), Northern Myanmar, or China."
# #     if class_name == 'Lemon_grass':
# #         additional_info = "Cymbopogon, also known as lemongrass, barbed wire grass, silky heads, oily heads, Cochin grass, Malabar grass, citronella grass or fever grass, is a genus of Asian, African, Australian, and tropical island plants in the grass family."
# #     if class_name == 'Mango':
# #         additional_info = "A mango is an edible stone fruit produced by the tropical tree Mangifera indica. It is believed to have originated in southern Asia, particularly in eastern India, Bangladesh, and the Andaman Islands."
# #     if class_name == 'Mint':
# #         additional_info = "Mentha (also known as mint). It is a genus of plants in the family Lamiaceae (mint family). The exact distinction between species is unclear; it is estimated that 13 to 24 species exist."
# #     if class_name == 'Nagadali':
# #         additional_info = "Ruta graveolens, commonly known as rue, common rue or herb-of-grace, is a species of the genus Ruta grown as an ornamental plant and herb. It is native to the Balkan Peninsula. It is grown throughout the world in gardens, especially for its bluish leaves, and sometimes for its tolerance of hot and dry soil conditions."
# #     if class_name == 'Neem':
# #         additional_info = "Azadirachta indica, commonly known as neem, margosa, nimtree or Indian lilac, is a tree in the mahogany family Meliaceae. It is one of two species in the genus Azadirachta. "
# #     if class_name == 'Nithyapushpa':
# #         additional_info = "Catharanthus roseus, commonly known as bright eyes, Cape periwinkle, graveyard plant, Madagascar periwinkle, old maid, pink periwinkle, rose periwinkle, is a perennial species of flowering plant in the family Apocynaceae."
# #     if class_name == 'Nooni':
# #         additional_info = "Morinda citrifolia is a fruit-bearing tree in the coffee family, Rubiaceae, native to Southeast Asia and Australasia, and was spread across the Pacific by Polynesian sailors. The species is now cultivated throughout the tropics and widely naturalized."
# #     if class_name == 'Pappaya':
# #         additional_info = "The papaya, papaw,  or pawpaw is the plant species Carica papaya, one of the 21 accepted species in the genus Carica of the family Caricaceae. It was first domesticated in Mesoamerica, within modern-day southern Mexico and Central America."
# #     if class_name == 'Pepper':
# #         additional_info = "Black pepper (Piper nigrum) is a flowering vine in the family Piperaceae, cultivated for its fruit (the peppercorn), which is usually dried and used as a spice and seasoning."
# #     if class_name == 'Pomegranate':
# #         additional_info = "The pomegranate (Punica granatum) is a fruit-bearing deciduous shrub in the family Lythraceae, subfamily Punicoideae, that grows between 5 and 10 m (16 and 33 ft) tall."
# #     if class_name == 'Raktachandini':
# #         additional_info = "Pterocarpus santalinus, with the common names red sanders, red saunders, Yerra Chandanam, Chenchandanam, red sandalwood, Rakta Chandana, and saunderswood, is a species of Pterocarpus endemic to the southern Eastern Ghats mountain range of South India."
# #     if class_name == 'Rose':
# #         additional_info = "A rose is either a woody perennial flowering plant of the genus Rosa, in the family Rosaceae, or the flower it bears. There are over three hundred species and tens of thousands of cultivars."
# #     if class_name == 'Sapota':
# #         additional_info = "Manilkara zapota, commonly known as sapodilla, sapote, chicozapote, chicoo, chicle, naseberry, or nispero, soapapple among other names, is an evergreen tree native to southern Mexico and Central America. "
# #     if class_name == 'Tulasi':
# #         additional_info = "Ocimum tenuiflorum, commonly known as holy basil or tulsi, is an aromatic perennial plant in the family Lamiaceae. It is native to tropical and subtropical regions of Australia, Malesia, Asia, and the western Pacific"
# #     if class_name == 'Wood_sorei':
# #         additional_info = "Oxalis is a large genus of flowering plants in the wood-sorrel family Oxalidaceae, comprising over 550 species."
# #     if class_name == 'Amla':
# #         additional_info = "Phyllanthus emblica, also known as emblic, emblic myrobalan, myrobalan, Indian gooseberry, Malacca tree, or amla, from the Sanskrit आमलकी (āmalakī), is a deciduous tree of the family Phyllanthaceae. Its native range is tropical and southern Asia"
    
# #     # Add more conditions for other class names

# #     # Clean up the temporary image file
# #     os.remove(temp_image_path)

# #     return jsonify({"classification": class_name, "additional_info": additional_info})

# # if __name__ == '__main__':
# #     app.run(debug=True,use_reloader=False)
# from flask import Flask, request, jsonify
# # from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing.image import img_to_array, load_img
# import numpy as np
# import os

# app = Flask(__name__)

# # Load your TensorFlow model
# model = load_model('your_model.h5')  # Replace with your model file path

# @app.route('/classify', methods=['POST'])
# def classify_image():
#     # Check if an image file is uploaded
#     if 'image' not in request.files:
#         return jsonify({"error": "No image provided in the request"})

#     image_file = request.files['image']

#     # Save the uploaded image to a temporary file
#     temp_image_path = 'temp_image.jpg'
#     image_file.save(temp_image_path)

#     # Load and preprocess the image
#     img = load_img(temp_image_path, target_size=(224, 224))  # Adjust target size as needed
#     img_array = img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)

#     # Make predictions
#     predictions = model.predict(img_array)
#     # Assuming your model outputs class probabilities, you can return the class with highest probability
#     class_index = np.argmax(predictions)
#     class_name = str(class_index)  # Convert class index to class name (or use a dictionary)

#     # Clean up the temporary image file
#     os.remove(temp_image_path)

#     return jsonify({"classification": class_name})

# if __name__ == '__main__':
#     app.run(debug=True)
