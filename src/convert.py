# https://github.com/2Obe/BSData

import os

import supervisely as sly
from supervisely.io.fs import get_file_name_with_ext
from supervisely.io.json import load_json_file

# from tqdm import tqdm


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    dataset_path = "APP_DATA/BSData-main"
    batch_size = 30
    ds_names = ["train", "test"]

    images_folder = "data"
    annotations_folder = "label"
    image_data = "image_data.json"

    def create_ann(image_path):
        labels = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        image_name = get_file_name_with_ext(image_path)
        image_data = name_to_data[image_name]
        ann_name = image_data[3]
        if ann_name is not None:
            ann_path = os.path.join(annotations_path, ann_name)

            ann_data = load_json_file(ann_path)
            poly_data = ann_data["shapes"]
            for curr_poly in poly_data:
                polygons_coords = curr_poly["points"]
                exterior = []
                for coords in polygons_coords:
                    for i in range(0, len(coords), 2):
                        exterior.append([int(coords[i + 1]), int(coords[i])])
                poligon = sly.Polygon(exterior)
                label_poly = sly.Label(poligon, obj_class)
                labels.append(label_poly)

            # type_tag = sly.Tag(type_tag_meta, value=image_data[1])

            if image_data[1] == 1:
                tags = [sly.Tag(type_1_tag)]
            elif image_data[1] == 2:
                tags = [sly.Tag(type_2_tag)]

            # tag_name = getitfrom(ann_file) # for example
            # tags = [sly.Tag(tag_meta) for tag_meta in tag_metas if tag_meta.name == tag_name]

            # return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=tags)

            wear_dev = image_data[2]
            for curr_wear_dev in wear_dev:
                tag_wear_dev = sly.Tag(wear_dev_tag, value=curr_wear_dev)
                tags.append(tag_wear_dev)

            # train_test_meta = tag_name_to_meta.get(image_data[0])
            # if train_test_meta is not None:
            #     tag_train_test = sly.Tag(train_test_meta)
            #     tags.append(tag_train_test)

            return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=tags)

    obj_class = sly.ObjClass("pitting", sly.Polygon)
    # train_tag = sly.TagMeta("train", sly.TagValueType.NONE)
    # test_tag = sly.TagMeta("test", sly.TagValueType.NONE)
    type_1_tag = sly.TagMeta("type_1", sly.TagValueType.NONE)
    type_2_tag = sly.TagMeta("type_2", sly.TagValueType.NONE)
    wear_dev_tag = sly.TagMeta("wear_dev", sly.TagValueType.ANY_STRING)

    tag_name_to_meta = {"type_1": type_1_tag, "type_2": type_2_tag}

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(
        obj_classes=[obj_class], tag_metas=[type_1_tag, type_2_tag, wear_dev_tag]
    )
    api.project.update_meta(project.id, meta.to_json())

    # images_path = os.path.join(dataset_path, images_folder)
    annotations_path = os.path.join(dataset_path, annotations_folder)
    train_test_split = os.path.join(dataset_path, image_data)

    all_data = load_json_file(train_test_split)["images"]

    name_to_data = {}

    for curr_data in all_data:
        name_to_data[curr_data["filename"]] = (
            curr_data["train_test_split"],
            curr_data["type"],
            curr_data["wear_dev"],
            curr_data["annotations"],
        )

    progress = sly.Progress("Add data to {}".format(project_name), len(name_to_data))

    for ds_name in ds_names:
        curr_name_to_data = {name: tpl for name, tpl in name_to_data.items() if tpl[0] == ds_name}
        images_names = list(curr_name_to_data.keys())

        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        for img_names_batch in sly.batched(images_names, batch_size=batch_size):
            images_pathes_batch = [
                os.path.join(dataset_path, images_folder, image_name)
                for image_name in img_names_batch
            ]

            img_infos = api.image.upload_paths(dataset.id, img_names_batch, images_pathes_batch)
            img_ids = [im_info.id for im_info in img_infos]

            anns_batch = [create_ann(image_path) for image_path in images_pathes_batch]

            try:
                api.annotation.upload_anns(img_ids, anns_batch)
            except Exception:
                pass

            progress.iters_done_report(len(img_names_batch))

    return project
