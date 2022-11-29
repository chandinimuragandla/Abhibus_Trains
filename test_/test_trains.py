import time

from POM.train_module import Trains1
import pytest


class Test_Trains:
     @pytest.mark.parametrize("forsource_,fordestination_,mobile_number,irctc_id",[("pune","bangalore",9390444316,"sravanivadithya")])
      #@pytest.mark.parametrize("forsource_,fordestination_,mobile_number,irctc_id",data)
     def test_trains(self,_driver,forsource_,fordestination_,mobile_number,irctc_id):
        result=Trains1(_driver)
        time.sleep(2)
        result.openTrainspage()
        time.sleep(2)

        result.forSource(forsource_)
        time.sleep(2)
        result.forDestination(fordestination_)
        time.sleep(2)
        result.forSearch()
        time.sleep(2)
        result.forCalendar()
        time.sleep(2)
        result.Trainindex()
        time.sleep(2)
        result.Mobilenumber(mobile_number)
        time.sleep(2)
        result.Generateotp()
        time.sleep(2)
        result.Submitotp()
        time.sleep(2)
        result.bookingtrain()
        time.sleep(2)
        result.Irctcuserid(irctc_id)
        time.sleep(2)
        result.Proceed()
        time.sleep(2)