# mosamatic-cli
Command-line tool for running processing tasks on medical images

# To-do
- NumPy to NIFTI conversion

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

# Next action
- Implement slice selection with Total Segmentator