from decouple import config

url = "mongodb+srv://freddypinto:{}@cluster0.woyzvx9.mongodb.net/?retryWrites=true&w=majority".format(
    config('MONGODB_PASSWORD', default='password')
)
