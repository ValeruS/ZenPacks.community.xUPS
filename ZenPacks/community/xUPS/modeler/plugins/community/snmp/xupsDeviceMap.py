##########################################################################
# Author:               ValeruS
# Date:                 September 2017
# Revised:
#
# xupsDeviceMap modeler plugin
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__ = """xUPSDeviceMap

Gather information from DeviceMap based on XUPS-MIB (.1.3.6.1.4.1.534).
"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap
from Products.DataCollector.plugins.DataMaps import MultiArgs
import re

class xupsDeviceMap(SnmpPlugin):
    maptype = "xupsDeviceMap"

    snmpGetMap = GetMap({
        '.1.3.6.1.4.1.534.1.1.1.0': '_HWManufacturer',
        '.1.3.6.1.4.1.534.1.1.2.0': 'setHWProductKey',
         })

    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        if not getdata:
            log.warn(' No SNMP response from %s for the %s plugin ' % ( device.id, self.name() ) )
            return

        om = self.objectMap(getdata)
        try:
            manufacturer = om._HWManufacturer
            om.setHWProductKey = MultiArgs(om.setHWProductKey, manufacturer)
        except (KeyError, IndexError, AttributeError, TypeError), errorInfo:
            log.warn( ' Attribute error in xupsDeviceMap modeler plugin %s', errorInfo)
        return om
