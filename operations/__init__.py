from . import asset
from .asset import MarkAsFinished, ClearCustomNormals_Selection, PrepForExport, CleanUp, SimpleExport, SimplifyPipes, RenameToSelected, GroupForExport
from . import test
from .test import TestingCode, TestCode2, BmeshTest


Register_Unregister_Classes = [
    PrepForExport,
    CleanUp,
    SimpleExport,
    SimplifyPipes,
    RenameToSelected,
    MarkAsFinished,
    ClearCustomNormals_Selection,
    TestingCode,
    TestCode2,
    BmeshTest,
    GroupForExport
]
