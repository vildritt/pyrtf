import os
import sys
sys.path.append( '../' )

from rtfng import *

def MakeExample1() :
    doc     = Document()
    ss      = doc.StyleSheet
    section = Section()
    doc.Sections.append( section )

    #    text can be added directly to the section
    #    a paragraph object is create as needed
    section.append( 'Image Example 1' )

    section.append( 'You can add images in one of two ways, either converting the '
                    'image each and every time like;' )

    image = Image( 'examples/image.jpg' )
    section.append( Paragraph( image ) )

    section.append( 'Or you can use the image object to convert the image and then '
                    'save it to a raw code element that can be included later.' )

    fout = open( 'image_tmp.py', 'w' )
    print('from rtfng import RawCode', file=fout)
    print(file=fout)
    fout.write( image.ToRawCode( 'TEST_IMAGE' ) )
    fout.close()

    import image_tmp
    section.append( Paragraph( image_tmp.TEST_IMAGE ) )
    section.append( 'Have a look in image_tmp.py for the converted RawCode.' )

    section.append( 'here are some png files' )
    for f in [ 'examples/img1.png',
               'examples/img2.png',
               'examples/img3.png',
               'examples/img4.png' ] :
        section.append( Paragraph( Image( f ) ) )

    return doc

def OpenFile( name ) :
    return open( '%s.rtf' % name, 'w' )

if __name__ == '__main__' :
    DR = Renderer()

    doc1 = MakeExample1()

    DR.Write( doc1, OpenFile( 'Image1' ) )

    print("Finished")

