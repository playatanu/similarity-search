from similarity_search.sqlite_db import SqliteDB
from similarity_search.faiss_db import FaissDB
from similarity_search.resnet50 import embedding

import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

faissDB = FaissDB(embedding_dim=2048)
sqliteDB = SqliteDB()

if os.path.exists("faiss_index.ivf"):
    faissDB.load("faiss_index.ivf")


def save_image(image_path):
    image = [(image_path)]
    id, loc = sqliteDB.store(image)[0]
    print(f"id:{id} image stored at location: {loc}")

    embedds = embedding(image_path)
    faissDB.store(id, embedds)
    print(f"embeding stored at vectordb at {id}")


def load_image():
    images = sqliteDB.load()
    return images


def get_similar_images(image_path, k=1):
    embedds = embedding(image_path)
    inf, idx = faissDB.search(embedds, k=k)
    return sqliteDB.search(idx.tolist()[0])


if __name__ == "__main__":
    """
    STORE IMAGE
    """
    # images = os.listdir("images")
    # for image_path in images:
    #     img_path = f"images/{image_path}"
    #     save_image(img_path)

    """
    GET SIMILAR IMAGES
    """
    # sm_img = get_similar_images("images/cat_03.jpg", 2)
    # print(sm_img)

    """
    GET ALL IMAGES
    """
    # all_images = load_image()
    # print(all_images)
