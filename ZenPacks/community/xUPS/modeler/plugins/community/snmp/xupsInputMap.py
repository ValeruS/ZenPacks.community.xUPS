##########################################################################
# Author:               ValeruS
# Date:                 September 2017
# Revised:
#
# xupsInputMap modeler plugin
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__ = """xupsInputMap

Gather table information from InputMap based on XUPS-MIB (.1.3.6.1.4.1.534).
"""

import Globals
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap

class xupsInputMap(SnmpPlugin):

    maptype = "xupsInputMap"
    modname = "ZenPacks.community.xUPS.xupsInput"
    relname = "xupsInput"


    snmpGetTableMaps = (
        GetTableMap('xupsInputEntry',
                    '.1.3.6.1.4.1.534.1.3.4.1',
                    {
                       '.2': 'xupsInputVoltage',
                       '.3': 'xupsInputCurrent',
                    }
        ),
    )

    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
#        log.info( "Data1 = %s", tabledata )
        rm = self.relMap()

        xupsentry = tabledata.get('xupsInputEntry')

# If no data supplied then simply return
        if not xupsentry:
            log.warn( 'No SNMP response from %s for the %s plugin', device.id, self.name() )
            log.warn( "Data= %s", tabledata )
            return

        for oid, data in xupsentry.iteritems():
            try:
                om = self.objectMap(data)
                om.snmpindex = oid.strip('.')
                om.xupsInputPhaseText = "InputPhase" + oid.strip('.')
                om.id = self.prepId(om.xupsInputPhaseText)
            except (KeyError, IndexError, AttributeError, TypeError), errorInfo:
                log.warn( ' Error in xupsInputMap modeler plugin %s', errorInfo)
                continue
            rm.append(om)
        return rm
