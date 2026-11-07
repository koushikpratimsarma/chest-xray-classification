
import random
import shutil
from pathlib import Path

# Reproducible random selection
random.seed(42)

RAW_DIR = Path("dataset/raw")
OUTPUT_DIR = Path("dataset/processed")

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}

# Collect images from source folders
normal_images = [
    p for p in (RAW_DIR / "Normal").rglob("*")
    if p.suffix.lower() in IMAGE_EXTENSIONS
]

abnormal_images = []

for folder in ["Lung_Opacity", "Viral Pneumonia"]:
    abnormal_images.extend([
        p for p in (RAW_DIR / folder).rglob("*")
        if p.suffix.lower() in IMAGE_EXTENSIONS
    ])

print("Available Normal images:", len(normal_images))
print("Available Abnormal images:", len(abnormal_images))

# Check sufficient images
if len(normal_images) < 500 or len(abnormal_images) < 500:
    raise ValueError("Not enough images to create the balanced dataset.")

# Select 500 images from each class
normal_images = random.sample(normal_images, 500)
abnormal_images = random.sample(abnormal_images, 500)

# Split: 70% train, 15% validation, 15% test
def split_images(images):
    random.shuffle(images)
    return {
        "train": images[:350],
        "val": images[350:425],
        "test": images[425:]
    }

normal_split = split_images(normal_images)
abnormal_split = split_images(abnormal_images)

# Copy images into output folders
for split in ["train", "val", "test"]:
    for class_name, image_list in [
        ("Normal", normal_split[split]),
        ("Abnormal", abnormal_split[split])
    ]:
        destination = OUTPUT_DIR / split / class_name
        destination.mkdir(parents=True, exist_ok=True)

        for index, image_path in enumerate(image_list):
            new_name = f"{class_name.lower()}_{index:04d}{image_path.suffix.lower()}"
            shutil.copy2(image_path, destination / new_name)

        print(f"{split}/{class_name}: {len(image_list)} images")

print("\nDataset preparation completed!")
