
import unittest


class TestSlimtaCore(unittest.TestCase):

    def test_import_slimta(self):
        import slimta

    def test_import_slimta_core_version(self):
        from slimta.core import VERSION
        self.assert_(isinstance(VERSION, basestring))

    def test_import_slimta_core_slimtaerror(self):
        from slimta.core import SlimtaError
        self.assert_(issubclass(SlimtaError, Exception))


# vim:et:fdm=marker:sts=4:sw=4:ts=4