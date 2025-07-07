# mosamatic-cli
Command-line tool for running processing tasks on medical images

# To-do
- NumPy to NIFTI conversion

- Create PNG images from DICOM files

- Slice selection using either Total Segmentator or MOOSE

  What you can do is first create spinal segmentations of a CT scan. Then
  you can use that data to pick a segmentation, e.g., the L3 vertebra and
  select the middle slice. In terms of commands/tasks, this would mean a
  command/task:
  - SegmentAnatomyTS: with option to output a specific segmentation object
  - SegmentAnatomyMOOSE: with option to output a specific segmentation 
    object
  - SelectSlice: Given a CT scan and a segmentation object, select the 
    middle or other slice

- CT/MRI registration using ANTsPy

- Total Segmentator liver segmentation CT + MRI (Dixon H2O)

- IMAT analysis

  Discuss with Leroy how to detect fat inside muscle (either as SAT or 
  black pixels). If pixels inside muscle are black, what does that mean?
  Can I overlay the mask on top of the image and check the pixel gray
  values and then determine (using the Alberta threshold range) whether
  these pixels are fat or not?

- Calculate muscle PDFF maps from Dixon MRI after registering with CT

# Commands
- numpy2nifti
- createpngsfromdicomfiles
- selectvertebralslice --engine=ts,moose --vertebra=l3,t4 --position=all,top,middle,bottom
- registerl3 --modalities=ct/dixon,ct/t1,ct/t2
- segmentanatomy --engine=ts,moose --masks=all,spine,l3,t4,liver,vessels
- segmentmusclefatl3[tensorflow] --imat=true,false
- calculatepdffmap2d --inphase=/path/to/image --outphase=/path/to/image --water=/path/to/image --mask=/path/to/mask (muscle and fat)
- calculatepdffmap3d --inphase=/path/to/series --outphase=/path/to/series --water=/path/to/series --mask=/path/to/mask (liver)

# Next action
- Implement slice selection with Total Segmentator