import pytest
from get_logs import GetLogs

class TestExample(GetLogs):
    
    def test_00(self):
        print("My first")
        
    def test_01(self):
        log = self.getLogger()
        log.info("Info from test execution")


    @pytest.mark.smoke  
    @pytest.mark.skip
    def test_03(self):
        assert 1 == 3, "One is not equal to three"