##########################################################################
# Author:               ValeruS
# Date:                 September 2017
# Revised:
#
# xupsBatteryMap modeler plugin
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__ = """xupsBatteryMap

Gather table information from BatteryMap based on XUPS-MIB (.1.3.6.1.4.1.534).
"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap

class xupsBatteryMap(SnmpPlugin):

    maptype = "xupsBatteryMap"
    modname = "ZenPacks.community.xUPS.xupsBattery"
    relname = "xupsBattery"


    snmpGetMap = GetMap({
                       '.1.3.6.1.4.1.534.1.2.1.0': 'xupsBatTimeRemaining',
                       '.1.3.6.1.4.1.534.1.2.2.0': 'xupsBatVoltage',
                       '.1.3.6.1.4.1.534.1.2.3.0': 'xupsBatCurrent',
                       '.1.3.6.1.4.1.534.1.2.4.0': 'xupsBatCapacity',
                       '.1.3.6.1.4.1.534.1.2.5.0': 'xupsBatteryAbmStatus',
                       '.1.3.6.1.4.1.534.1.2.6.0': 'xupsBatteryLastReplacedDate',
                       '.1.3.6.1.4.1.534.1.8.2.0': 'xupsTestBatteryStatus',
                       '.1.3.6.1.2.1.33.1.2.1.0' : 'upsBatteryStatus',
                    })


    BatteryAbmStatus  = {1:'batteryCharging',
                         2:'batteryDischarging',
                         3:'batteryFloating',
                         4:'batteryResting',
                         5:'unknown',
                        }

    BatteryStatus     = {1: ( 2, 'Unknown'),
                         2: ( 0, 'batteryNormal'),
                         3: ( 4, 'batteryLow'),
                         4: ( 3, 'batteryDepleted'),
                        }

    TestBatteryStatus = {1:'unknown',
                         2:'passed',
                         3:'failed',
                         4:'inProgress',
                         5:'notSupported',
                         6:'inhibited',
                         7:'scheduled',
                        }


    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
#        log.info( "Data= %s", getdata )
        rm = self.relMap()

# If no data supplied then simply return
        if not getdata:
            log.warn( 'No SNMP response from %s for the %s plugin', device.id, self.name() )
            log.warn( "Data= %s", getdata )
            return

        om = self.objectMap(getdata)
        try:
                om.xupsBatTimeRemaining = om.xupsBatTimeRemaining / 60
                om.xupsBatteryAbmStatusText = self.BatteryAbmStatus.get(int(om.xupsBatteryAbmStatus), 'unknown')
                om.xupsTestBatteryStatusText = self.TestBatteryStatus.get(int(om.xupsTestBatteryStatus), 'unknown')
                index = om.upsBatteryStatus
                om.upsBatteryStatus = self.BatteryStatus[index][0]
                om.upsBatteryStatusText = self.BatteryStatus[index][1]
                om.id = "Baterry"
                om.id = self.prepId(om.id)
                om.snmpindex = '0'
                rm.append(om)
        except (KeyError, IndexError, AttributeError, TypeError), errorInfo:
                log.warn( ' Error in xupsBatteryMap modeler plugin %s', errorInfo)
        return rm
