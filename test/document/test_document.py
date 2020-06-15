#!/usr/bin/env python
import os
import io
import tempfile

from rtfng.utils import RTFTestCase
from rtfng.Elements import Document
from rtfng.document.section import Section


class DocumentTestCase(RTFTestCase):

    def test_documentWrite(self):
        doc, section, styles = RTFTestCase.initializeDoc()

        fd, filename = tempfile.mkstemp(prefix='test-pyrtf', suffix='.rtf')
        os.close(fd)
        doc.write(filename)

        result = io.StringIO()
        doc.write(result)

        assert open(filename, 'r').read() == result.getvalue()
        os.remove(filename)
