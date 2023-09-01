# Scenario Refiner: Grounding subjects in images at the morphological level.

**Data Instructions**

Please find the data in the **data** folder. The dataset is in **json** format and contains the following:

- A reference to the image in the original dataset: **dataset** and **image_file**.
- The two annotations containing the different morphological words paired to the image: **annot1** and **annot2**

For the images, please refer to the **dataset** and to the id in **image_file**

Please find the code for computing image-text pairs with different Vision and Language models:

- To test the dataset with CLIP: **Scenario_refiner_CLIP**
- To test the dataset with ViLT: **Scenario_refiner_ViLT**
- To test the dataset with LXMERT: **Scenario_refiner_LXMERT**


# Reference
Please cite our paper if you are using this dataset:
