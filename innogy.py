#!/usr/bin/env python2.7
# coding: utf8

from datetime import date, time, datetime, timedelta
from time import mktime

from Discovergy import Discovergy

#d = date(2017, 1, 12)
#t = time(10, 00, 0)
#dt = datetime.combine(d, t)
dt = datetime.now() - timedelta(hours=1) + timedelta(seconds=10)
unixTimeStampFrom = mktime(dt.timetuple())
unixTimeStampFrom = int(round(unixTimeStampFrom * 1000))

discovergy = Discovergy()
#meterId = discovergy.buildMeterId('EASYMETER', '1024000034')
#meterId = discovergy.buildMeterId('EASYMETER', '60327495')
#meterId = discovergy.buildMeterId('EASYMETER', '60327462')
meterId = discovergy.buildMeterId('EASYMETER', '60668728')

#print(discovergy.getMeters())
#print(discovergy.getFieldNamesForMeter(meterId))
#print(discovergy.getMeasurementsForMeterInTimeInterval(meterId, None, unixTimeStampFrom, None, "raw", False))
print(discovergy.getLastMeasurementForMeter(meterId, None, False))
#print(discovergy.getRawLoadProfileFileForRlmMeterOnDate(meterId, 1, 1, 2016))
#print (discovergy.getStatistics(meterId, unixTimeStampFrom))

