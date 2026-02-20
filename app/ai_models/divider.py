import os
import random
import shutil

#common paths
test_root = "Dataset/TTest"
val_root = "Dataset/Validate"

classes = os.listdir(test_root)

for cls in classes:
    test_cls_path = os.path.join(test_root, cls)
    val_cls_path = os.path.join(val_root, cls)

    #all images from the Test folder
    images = [
        img for img in os.listdir(test_cls_path)
        if os.path.isfile(os.path.join(test_cls_path, img))
    ]

    random.shuffle(images)

    total = len(images)
    val_count = total // 2

    #dividing the data
    for img in images[:val_count]:
        src = os.path.join(test_cls_path,img)
        out = os.path.join(val_cls_path,img)
        shutil.move(src,out)

    print(f"Process completed! {val_count} pictures moved")