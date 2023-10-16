from decouple import config

url = "mongodb+srv://freddypinto:{MONGODB_PASSWORD}@cluster0.woyzvx9.mongodb.net/?retryWrites=true&w=majority".format(
    config('MONGODB_PASSWORD', default='password')
)
