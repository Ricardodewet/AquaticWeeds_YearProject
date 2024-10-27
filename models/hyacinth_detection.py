# Import necessary libraries
import os
import tensorflow as tf
from object_detection.utils import label_map_util


# Step 2: Define paths to the directories containing the TFRecord files and label map
BASE_DIR = "C:\Users\rober\OneDrive\Desktop\Year 3 BC\Year Project\water_hyacinth_project\Trained Model"

TRAIN_DIR = os.path.join(BASE_DIR, "Hyacinth Detection Model.v1i.tfrecord", "train")
VALID_DIR = os.path.join(BASE_DIR, "Hyacinth Detection Model.v1i.tfrecord", "valid")
TEST_DIR = os.path.join(BASE_DIR, "Hyacinth Detection Model.v1i.tfrecord", "test")

TRAIN_TFRECORD_PATH = os.path.join(TRAIN_DIR, "Hyacinth.tfrecord")
VALID_TFRECORD_PATH = os.path.join(VALID_DIR, "Hyacinth.tfrecord")
TEST_TFRECORD_PATH = os.path.join(TEST_DIR, "Hyacinth.tfrecord")

TRAIN_LABEL_MAP_PATH = os.path.join(TRAIN_DIR, "Hyacinth_label_map.pbtxt")
VALID_LABEL_MAP_PATH = os.path.join(VALID_DIR, "Hyacinth_label_map.pbtxt")
TEST_LABEL_MAP_PATH = os.path.join(TEST_DIR, "Hyacinth_label_map.pbtxt")

# Step 3: Load the label map
label_map_path = TRAIN_LABEL_MAP_PATH  # Using the label map from the training folder
category_index = label_map_util.create_category_index_from_labelmap(label_map_path, use_display_name=True)

# Step 4: Load the TFRecord files
def parse_tfrecord(example_proto):
    features = {
        'image/encoded': tf.io.FixedLenFeature([], tf.string),
        'image/object/class/label': tf.io.VarLenFeature(tf.int64),
        # Add other features based on your specific TFRecord schema
    }
    parsed_features = tf.io.parse_single_example(example_proto, features)
    image = tf.image.decode_jpeg(parsed_features['image/encoded'])
    labels = tf.sparse.to_dense(parsed_features['image/object/class/label'])
    return image, labels

def load_dataset(tfrecord_path):
    raw_dataset = tf.data.TFRecordDataset(tfrecord_path)
    parsed_dataset = raw_dataset.map(parse_tfrecord)
    return parsed_dataset

# Load train, validation, and test datasets
train_dataset = load_dataset(TRAIN_TFRECORD_PATH)
valid_dataset = load_dataset(VALID_TFRECORD_PATH)
test_dataset = load_dataset(TEST_TFRECORD_PATH)

# Step 5: Load the trained TensorFlow model
model_dir = "C:\Users\rober\OneDrive\Desktop\Year 3 BC\Year Project\water_hyacinth_project\Trained Model"  # Replace with the actual path to your saved model
model = tf.saved_model.load(model_dir)

# Step 6: Run inference on one sample from the train dataset
for data in train_dataset.take(1):  # Get one example from the dataset
    image_data = data['image/encoded'].numpy()
    image_tensor = tf.io.decode_jpeg(image_data)
    input_tensor = tf.expand_dims(image_tensor, 0)  # Add batch dimension
    detections = model(input_tensor)
    print(detections)
