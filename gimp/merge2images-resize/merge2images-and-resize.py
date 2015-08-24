#!/usr/bin/python

from gimpfu import *

def merge_and_resize(timg, tdrawable):

    #
    
    nameArray = tdrawable.name.split('.jpg')
    
    newFileName = nameArray[0] + "H" + ".jpg"

    pdb.gimp_image_resize(timg,tdrawable.width+75,tdrawable.height+75,37,37)

    # To work with this filter, images and maps must have the same size. All images to be selected must be present on screen.
    #pdb.plug_in_depth_merge (run_mode,image,result,source1,source2,depthMap1,depthMap2,overlap,offset,scale1,
    pdb.file_jpeg_save(timg, tdrawable, newFileName , newFileName, 
                           0.9, 0, 0, 0, "", 0, 0, 0, 0)

register(
        "python_fu_merge_and_resize", 
        "Merge two images, resizing to the biggest dimension",
        "Merge two images, resizing to the biggest dimension",
        "Angel del Blanco Aguado",
        "Angel del Blanco Aguado",
        "2015",
        "<Image>/Image/Merge and Resize...", # menu PATH
        "*", # The image types supported
        [		# Script input (Type, Name, Description, default, extra)	
             #   (PF_INT, "max_width", "Maximum Width", 500),
             #   (PF_INT, "max_height", "Maximum Height", 500),
             #   (PF_BOOL, "copy", "Make a JPEG copy", TRUE),	 
        ],
        [],	# Script output
        merge_and_resize)

main()



