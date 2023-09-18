# Scenario Refin_er_: Grounding subjects in images at the morphological level.

The code is under Creative Common License: https://creativecommons.org/licenses/by/4.0/

**Data Instructions**

Please find the data in the **data**  folder. The dataset is in **json** format and contains the following:

- A reference to the image in the original dataset: **dataset**
    - Visual Genome dataset is licensed under the _Creative Commons Attribution 4.0 International License_ : https://creativecommons.org/licenses/by/4.0/
    - MS COCO dataset is licensed under the _Creative Commons Attribution 4.0 International License_: https://creativecommons.org/licenses/by/4.0/
    - Geograph dataset is licensed under the _Creative Commons Attribution-ShareAlike 2.0 Generic License_: https://creativecommons.org/licenses/by-sa/2.0/
    - Wikimedia dataset is licensed under the _Creative Commons Attribution 2.0 Generic License_: https://creativecommons.org/licenses/by-sa/2.0/
      
- A reference to the numeric image id or link: **image_file**.
  
- The two annotations containing the different morphological words paired to the image: **annot1** and **annot2**

For the images, please refer to the **dataset** and to the id in **image_file**

Please find the code for computing image-text pairs with different Vision and Language models:

- To test the dataset with CLIP: **Scenario_refiner_CLIP**
- To test the dataset with ViLT: **Scenario_refiner_ViLT**
- To test the dataset with LXMERT: **Scenario_refiner_LXMERT**


# Reference
Please cite our paper if you are using this dataset:
